import random
import FunRand as fr
import numpy as np

class Element:
    nextId = 0

    def __init__(self, delay=None, distribution='exp'):
        self.id =  Element.nextId
        self.name = 'Element' + str(self.id)
        self.tnext = [0]  # момент часу наступноїї події
        self.delayMean = delay  # середнє значення часової затримки
        self.delayDev = None # середнє квадратичне відхилення часової затримки
        self.distribution = distribution # розподіл
        self.quantity = 0 #кількість
        self.tcurr = self.tnext  #поточний момент часу
        self.state = [0]  # стан
        self.nextElement = []  #вказує на наступний елемент моделі
        Element.nextId += 1
        self.probability = [1] #ймовірність
        self.priority = [1] # пріоретність
        self.methodOfSelection = "probability"


    def getDelayMean(self):
        return self.delayMean

    def getDelayDev(self):
        return self.delayDev    

    def setDelayDev(self, delay):
        self.delayDev = delay

    def getDistribution(self):
        return self.distribution

    def getDelay(self): #розрахунок часової затримками
        funRand = fr.FunRand
        delay = self.getDelayMean()
        if(self.distribution == 'exp'):
            delay = funRand.Exp(self.getDelayMean())
        elif(self.distribution == 'norm'):
            delay = funRand.Norm(self.delayMean, self.delayDev)  
        elif(self.distribution == 'unif'):
            delay = funRand.Unif(self.delayMean, self.delayDev)
        else:
            delay = self.getDelayMean()  
        return delay

    def goToNextElement(self):
        if self.methodOfSelection == "priority":
            return self.selectionByPriority()
        elif self.methodOfSelection == "probability":
            return self.selectionByProbabaility()
        else :
            raise Exception('unknown method for selecting the next element')

    
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
        print('')
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