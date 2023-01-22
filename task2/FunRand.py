import random
import numpy as np

class FunRand:

    def Exp( timeMean):
        a = 0
        while(a == 0):
            a = random.random()
        a = -timeMean*np.log(a)
        return a

    def Unif(timeMean, timeMax):
        a = 0
        while( a == 0):
            a = random.random()
        a = timeMean + a * (timeMax - timeMean)
        return a

    def Norm(timeMean, timeDeviation):
        r = random.random
        a = timeMean + timeDeviation * random.gauss(0.0, 1.0)
        return a
