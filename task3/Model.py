import Process as Process
import numpy as np
import Exit as Exit



class Model:
    def __init__(self, elements):
        self.list = elements
        self.tnext = 0.0
        self.event = elements[0]
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
                if self.tcurr in elem.tnext:
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
        averageFinishTime= 0
        numOfFinished = 0
        averageFinishTime = 0
        averageTimeBetweenClients = 0


        for elem in self.list:
            elem.printResult()
            if isinstance(elem, Process.Process):
                numOfProcessors += 1

                if elem.name == "toLaboratory":
                    averageTimeBetweenClients = elem.timeToReseption/elem.quantity

                if elem.name == "toReseption":
                    averagFinishTime = elem.timeType2Finished / elem.type2 if elem.type2 != 0 else np.inf
                    print("Average time to finish for type 2 = " +str(averagFinishTime) )
            elif isinstance(elem, Exit.Exit):
                averageFinishTime += elem.timeFinished1 + elem.timeFinished2 + elem.timeFinished3
                numOfFinished += elem.quantity

                averageFinishTime1 = elem.timeFinished1 / elem.type1 if elem.type1 != 0 else np.inf
                averageFinishTime2 = elem.timeFinished2 / elem.type2 if elem.type2 != 0 else np.inf
                averageFinishTime3 = elem.timeFinished3 / elem.type3 if elem.type3 != 0 else np.inf

                print("Average time to finish for type 1 = " + str(averageFinishTime1))
                print("Average time to finish for type 2 = " + str(averageFinishTime2))
                print("Average time to finish for type 3 = " + str(averageFinishTime3))
                print('')


        averageFinishTime_ = averageFinishTime / numOfFinished

        print("Average interval lab: "+ str(averageTimeBetweenClients))
        print("Average finishing time: "+str(averageFinishTime_))
        print('')