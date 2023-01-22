import Process as Process
import numpy as np


class Model:
    def __init__(self, elements):
        self.list = elements
        self.tnext = 0.0
        self.event = 0
        self.tcurr = self.tnext

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
                if isinstance(elem.tnext, list):
                    if self.tcurr in elem.tnext:
                        elem.outAct()
                else:
                    if self.tcurr == elem.tnext:
                        elem.outAct()        

            self.printInfo()

        return self.printResult()

    def printInfo(self):
        for elem in self.list:
            elem.printInfo()

    def printResult(self):
        print(" ")
        print('--------RESULTS--------')

        numOfProcessors = 0

        for elem in self.list:
            elem.printResult()
            if isinstance(elem, Process.Process):
                numOfProcessors += 1

                elem.meanQueueLength = elem.meanQueue / self.tcurr
                elem.failureProbability = elem.failure / (elem.quantity + elem.failure) if (elem.quantity + elem.failure) != 0 else 0
                elem.averageLoad = elem.meanLoad / self.tcurr

                print("Mean length of queue: " + str(elem.meanQueueLength))
                print("Failure probability: " + str(elem.failureProbability))
                print("Avarage load: " + str(elem.averageLoad))
