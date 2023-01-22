import Element as element

class Create(element.Element):

    def __init__(self, delay):
        print(self, delay)
        super().__init__(delay)
        super().setTnext(0.0)

    def outAct(self):
        super().outAct()
        super().setTnext(super().getTcurr() + super().getDelay())
        p1 = self.nextElement[0]
        p2 = self.nextElement[1]
        if p1.queue <= p2.queue :
            p1.inAct()
        else :
            p2.inAct()

