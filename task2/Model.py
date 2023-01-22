import Process as Process
import numpy as np


class Model:
    def __init__(self, elements):
        self.list = elements
        self.tnext = 0.0
        self.event = 0
        self.tcurr = self.tnext
        self.workloadOfCashiers = 0
        self.changeQueue = 0

    def simulate(self, time):
        while self.tcurr < time:
            self.tnext = float('inf')

            for elem in self.list:
                tnext_val = np.min(elem.tnext)
                if tnext_val < self.tnext:
                    self.tnext = tnext_val
                    self.event = elem.id      

            def findElem():
                for item in self.list:
                    if item.id == self.event:
                        return item  

            print(" ")
            print("It's time for event in "+ str(findElem().name) + ", time = " + str(self.tnext))

            for elem in self.list:
                elem.doStatistics(self.tnext - self.tcurr)

            self.tcurr = self.tnext
            for elem in self.list:
                elem.tcurr = self.tcurr

            if len(self.list) > self.event:
                self.list[self.event].outAct()

            for elem in self.list:
                if self.tcurr == elem.tnext:
                        elem.outAct()        

            self.printInfo()
            self.queueChange()

        return self.printResult()

    def queueChange(self):
        queueList = []
        for element in self.list:
            if isinstance(element, Process.Process):
                queueList.append(element.queue)

        if queueList[1] - queueList[0] >= 2:
            self.list[2].queue -= 1 
            self.list[1].queue += 1
            self.changeQueue += 1
            print("The car changed queue 2 to queue 1")
        elif queueList[0] - queueList[1] >= 2:
            self.list[1].queue -= 1 
            self.list[2].queue += 1
            self.changeQueue += 1
            print("The car changed queue 1 to queue 2")


    def printInfo(self):
        for elem in self.list:
            elem.printInfo()

    def printResult(self):
        print(" ")
        print('--------RESULTS--------')

        numOfProcessors = 0
        averageTimeInBank = 0
        averageTimeBetweenClients = 0
        quantity = 0
        failure = 0

        for elem in self.list:
            elem.printResult()
            if isinstance(elem, Process.Process):
                numOfProcessors += 1
                quantity += elem.quantity
                failure +=elem.failure

                averageTimeInBank += elem.timeInBank / elem.quantity
                averageTimeBetweenClients += elem.timeBetweenClients / elem.quantity
                
                elem.meanQueueLength = elem.meanQueue / self.tcurr
                failureProbability = elem.failure / (elem.quantity + elem.failure) if (elem.quantity + elem.failure) != 0 else 0
                elem.averageLoad = elem.meanLoad / self.tcurr

                print("Mean length of queue: " + str(elem.meanQueueLength))
                print("Failure probability: " + str(failureProbability))
                print("Avarage load: " + str(elem.averageLoad))

    
    
        print(" ")
        print(f"Average number of customers:  {quantity/self.tcurr}")
        print(f"Failure probability:  {failure/(quantity+failure)}")
        print(f"Average time between customer departure: {averageTimeBetweenClients / numOfProcessors}")
        print(f"Average time time in bank: {averageTimeInBank / numOfProcessors}")
        print(f"Average time lines: {self.changeQueue}")
        print(f"The queue changed {self.changeQueue} times")
