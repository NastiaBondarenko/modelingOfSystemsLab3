import Element as element

class Create(element.Element):

    def __init__(self, delay):
        print(self, delay)
        super().__init__(delay)
        super().setTnext(0.0)

    def outAct(self):
        super().outAct()
        super().setTnext(super().getTcurr() + super().getDelay())
        nextElement = super().goToNextElement()
        nextElement.inAct()

