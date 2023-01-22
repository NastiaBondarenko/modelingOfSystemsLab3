import numpy as np
import Element as element

class Process(element.Element):

    def __init__(self, delayDev = 0, delayMean = 1, channel = 1):
        super().__init__(delayDev, delayMean, channel)
        self.types = [-1] * channel
        self.queueTypes = []
        self.priorTypes = []
        self.requiredPath = None
        self.timeToReseption = 0
        self.timePreviousWasRegister = 0
        self.timeStart = [0] * channel
        self.timeStartQueue = []
        self.type2 = 0
        self.timeType2Finished = 0

    
    def inAct(self,typeElement, timeStart):
        self.typeElement = typeElement

        if self.name == "toLaboratory":
            self.timeToReseption += self.tcurr - self.timePreviousWasRegister
            self.timePreviousWasRegister = self.tcurr
        elif self.name == "toReseption" and self.typeElement ==2:
            self.timeType2Finished += self.tcurr - timeStart
            self.type2 += 1

        freeChanel = []
        for i in range(self.numOfChannels):
            if self.state[i] == 0:
                freeChanel.append(i)

        if len(freeChanel) > 0:            
            for i in freeChanel:
                self.state[i] = 1
                self.tnext[i] = self.tcurr + super().getDelay()
                self.types[i] = self.typeElement
                self.timeStart[i] = timeStart
                break
        else:
            if self.queue < self.maxQueue:
                self.queue += 1
                self.queueTypes.append(self.typeElement)
                self.timeStartQueue.append(timeStart)
            else:
                self.failure += 1

    def outAct(self):
        currentChannel = []

        for i in range(self.numOfChannels):
            if self.tnext[i] == self.tcurr:
                currentChannel.append(i)

        for i in currentChannel:
            super().outAct()
            self.tnext[i] = np.inf
            self.state[i] = 0
            typeElement = self.types[i]
            timeStart = self.timeStart[i]
            if self.queue > 0:
                self.setQueue(self.queue - 1)
                self.state[i] = 1
                self.tnext[i] = self.tcurr + super().getDelay()
                priorIndex = self.getPriorityIndex()
                self.next_type_element = self.queueTypes.pop(priorIndex)
                self.types[i] = self.typeElement
                self.timeStart[i] = self.timeStartQueue.pop(priorIndex)
            
            if self.nextElement is not None :
                self.typeElement = 1 if self.name == "toReception" else typeElement
                if self.requiredPath is None:
                    nextElement = np.random.choice(a = self.nextElement, p = self.probability)
                    nextElement.inAct(self.typeElement, timeStart)
                else:
                    for idx, path in enumerate(self.requiredPath):
                        if self.typeElement in path:
                            self.nextElement[idx].inAct(self.typeElement, timeStart)


    def getPriorityIndex(self):
        for prior_types_i in self.priorTypes:
            for type_i in np.unique(self.queueTypes):
                if type_i == prior_types_i:
                    return self.queueTypes.index(type_i)
        else:
            return 0

    def printInfo(self):
        super().printInfo()
        print('failure = '+str(self.failure))

    def doStatistics(self, delta):
        self.meanQueue += self.queue * delta

    def setQueue(self, queue):
        self.queue = queue
