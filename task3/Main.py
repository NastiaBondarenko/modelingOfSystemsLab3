import random
import sys
import Create as Create
import Model as Model
import Process as Process
import Exit as Exit
import pandas as pd

def Task3():  
    names= ['Creator','Reception','toRoom','toLaboratory','toRegistry',
            'toAnalyzes','toReseption', 'Exit1', 'Exit2']
    delays = [15, [0,1], [8, 3], [5, 2], [3, 4.5], [2, 4], [5,2]]
    channels = [2, 3, 5, 1, 1, 5]
    distribution = ['exp', 'uniform', 'uniform', 'erlang', 'erlang', 'uniform']
    requiredPath = [[[1], [2, 3]], None, None, None, [[3], [2]], None]
    priorTypes = [[1], [], [], [], [], []]
    simulateTime = 1000

    SimModelForTask3(delays, names, distribution, channels, requiredPath, simulateTime, priorTypes)



def SimModelForTask3(delay, name, distribution, channels, requiredPath, simulateTime, priorTypess):
    c = Create.Create(delay[0])
    p1 = Process.Process(delay[1][0], delay[1][1], channels[0])
    p2 = Process.Process(delay[2][0], delay[2][1], channels[1])
    p3 = Process.Process(delay[3][0], delay[3][1], channels[2])
    p4 = Process.Process(delay[4][0], delay[4][1], channels[3])
    p5 = Process.Process(delay[5][0], delay[5][1], channels[4])
    p6 = Process.Process(delay[6][0], delay[6][1], channels[5])
    d1 = Exit.Exit()
    d2 = Exit.Exit()

    c.name = name[0]
    p1.name = name[1]
    p2.name = name[2]
    p3.name = name[3]
    p4.name = name[4]
    p5.name = name[5]
    p6.name = name[6]
    d1.name = name[7]
    d2.name = name[8]

    p1.distribution=distribution[0]
    p2.distribution=distribution[1]
    p3.distribution=distribution[2]
    p4.distribution=distribution[3]
    p5.distribution=distribution[4]
    p6.distribution=distribution[5]

    c.nextElement = [p1]
    p1.nextElement = [p2, p3]
    p2.nextElement = [d1]
    p3.nextElement = [p4]
    p4.nextElement = [p5]
    p5.nextElement = [d2, p6]
    p6.nextElement = [p1]

    p1.priorTypes = priorTypess[0]
    p2.priorTypes = priorTypess[1]
    p3.priorTypes = priorTypess[2]
    p4.priorTypes = priorTypess[3]
    p5.priorTypes = priorTypess[4]
    p6.priorTypes = priorTypess[5]

    p1.requiredPath = requiredPath[0]
    p2.requiredPath = requiredPath[1]
    p3.requiredPath = requiredPath[2]
    p4.requiredPath = requiredPath[3]
    p5.requiredPath = requiredPath[4]
    p6.requiredPath = requiredPath[5]

    model = Model.Model([c, p1, p2, p3, p4, p5, p6, d1, d2])
    model.simulate(simulateTime)

Task3()