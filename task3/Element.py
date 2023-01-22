import random
import FunRand as fr
import numpy as np

class Element:
    nextId = 0

    def __init__(self, delayDev = 0, delayMean = 1, channel = 1):
        self.id =  Element.nextId
        self.name = 'Element' + str(self.id)
        self.tnext = [0] * channel # момент часу наступноїї події
        self.delayMean = delayMean  # середнє значення часової затримки
        self.delayDev = delayDev    
        self.distribution = 'exp' # розподіл
        self.quantity = 0 #кількість
        self.tcurr = self.tnext  #поточний момент часу
        self.state = [0] * channel # стан
        self.nextElement = None  #вказує на наступний елемент моделі
        Element.nextId += 1
        self.probability = [1]  #ймовірність
        self.priority = [1] # пріоретність
        self.methodOfSelection = "priority"
        self.typeElement = None
        self.numOfChannels = channel
        self.maxQueue = float('inf')
        self.failure = 0
        self.meanQueue = 0
        self.queue = 0
        self.meanLoad = 0
        self.timeFinished1 = 0
        self.timeFinished2 = 0
        self.timeFinished3 = 0
        self.type1 = 0
        self.type2 = 0
        self.type3 = 0



    def getDelayMean(self):
        return self.delayMean

    def getDelayDev(self):
        return self.delayDev    

    def setDelayDev(self, delay):
        self.delayDev = delay

    def getDistribution(self):
        return self.distribution

    def getDelay(self): #розрахунок часової затримками
        if self.name == 'Reception':
            match self.typeElement:
                case 1:           
                    self.delayMean = 15
                case 2:
                    self.delayMean = 40
                case 3:
                    self.delayMean = 30
       
        funRand = fr.FunRand
        delay = self.getDelayMean()
        if(self.distribution == 'exp'):
            delay = funRand.Exp(self.getDelayMean())
        elif(self.distribution == 'norm'):
            delay = funRand.Norm(self.delayMean, self.delayDev)  
        elif(self.distribution == 'uniform'):
            delay = funRand.Unif(self.delayMean, self.delayDev)
        else:
            delay = self.getDelayMean()  
        return delay

    def goToNextElement(self):
        if self.probability != [1]:
            nextElement = np.random.choice(a=self.nextElement, p=self.probability)
            return nextElement
        elif self.priority != [1]:
            nextElement = self.selectionByPriority()
            return nextElement
        elif self.probability == [1] and self.priority == [1]:
            return self.nextElement[0]
        elif self.probability != [1] and self.priority != [1]:
            raise Exception('We cannot choose a route. Please specify probability OR priority value (not both)')


    
    
    def selectionByProbabaility(self):
        nextElement = np.random.choice(a = self.nextElement, p = self.probability)
        return nextElement

    def selectionByPriority(self):
        maxPriority = 0
        nextElement = -1

        for i in range(len(self.priority)):
            if self.priority[i] > maxPriority:
                if 0 in self.nextElement[i].state:
                    nextElement = self.nextElement[i]
                    maxPriority = self.priority[i]

        if nextElement == -1:
            return None
        else:
            return nextElement


    def setDisctribution(self, distribution):
        self.distribution = distribution

    def outAct(self):  #вихід з елементу
        self.quantity += 1    

    def printResult(self):
        print(self.name + ' quantity = ' + str(self.quantity) + ' state = ' + str(self.state))

    def printInfo(self):
        print(self.name +' state = '+str(self.state)+' quantity = '+str(self.quantity)+' tnext = '+str(self.tnext))
    
    def setTnext(self, tnext):
        self.tnext = tnext
    
    def getTcurr(self):
        return self.tcurr

    def inAct(self): #вхід в елемент
        pass

    def doStatistics(self, delta):
        pass

    def getTcurr(self):
        return self.tcurr

    def getNextElement(self):
        return self.nextElement

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def setTcurr(self, tcurr):
        self.tcurr = tcurr