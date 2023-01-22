import numpy as np
import Element as element

class Process(element.Element):

    def __init__(self, delay, channels = 1):
        super().__init__(delay)

        self.queue = 0
        self.maxQueue = float('inf')
        self.meanQueue = 0.0
        self.failure = 0
        self.meanLoad = 0
        self.numOfChannels = channels
        self.tnext = [np.inf]*self.numOfChannels
        self.state = [0]*self.numOfChannels
        self.timeBetweenClients = 0
        self.timeInBank = 0
        self.timeEnterToBank = 0
        self.timePreviousLeftBank = 0
        self.meanQueueLength = 0
        self.failureProbability = 0
        self.averageLoad = 0
    
    def inAct(self):
        freeChanel = []
        for i in range(self.numOfChannels):
            if self.state[i] == 0:
                freeChanel.append(i)

        if len(freeChanel) > 0:            
            for i in freeChanel:
                self.state[i] = 1
                self.tnext[i] = self.tcurr + super().getDelay()
        else:
            if self.queue < self.maxQueue:
                self.queue += 1
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

            self.timeBetweenClients += self.tcurr - self.timePreviousLeftBank
            self.timePreviousLeftBank = self.tcurr
            self.timeInBank += self.tcurr - self.timeEnterToBank

            if self.queue > 0:
                self.setQueue(self.queue - 1)
                self.state[i] = 1
                self.tnext[i] = self.tcurr + super().getDelay()

    def printInfo(self):
        super().printInfo()
        print('failure = '+str(self.failure))

    def doStatistics(self, delta):
        self.meanQueue += self.queue * delta

        for i in range(self.numOfChannels):
            print(self.state)
            self.meanLoad += self.state[i] * delta

        self.meanLoad = self.meanLoad / self.numOfChannels

    def setQueue(self, queue):
        self.queue = queue
