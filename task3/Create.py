import Element as element
import numpy as np

class Create(element.Element):

    def __init__(self, delay):
        print(self, delay)
        super().__init__(delay)

    def outAct(self):
        super().outAct()
        tnext = super().getDelay() + self.tcurr
        self.tnext[0] = tnext
        self.next_type_element = np.random.choice([1, 2, 3], p=[0.5, 0.1, 0.4])
        next_element = self.goToNextElement()
        next_element.inAct(self.next_type_element, self.tcurr)
