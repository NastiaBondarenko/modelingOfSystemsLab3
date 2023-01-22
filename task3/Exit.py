import numpy as np
from Element import Element


class Exit(Element):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tnext = [np.inf]
        self.timeFinished1 = 0
        self.timeFinished2 = 0
        self.timeFinished3 = 0
        self.type1 = 0
        self.type2 = 0
        self.type3 = 0

    def inAct(self, typeElement, timeStart):
        match typeElement:
            case 1:
                self.timeFinished1 += self.tcurr - timeStart
                self.type1 += 1
            case 2:
                self.timeFinished2 += self.tcurr - timeStart
                self.type2 += 1
            case 3:
                self.timeFinished3 += self.tcurr - timeStart
                self.type3 += 1
        super().outAct()
        


        