import random
import sys
import Create as Create
import Model as Model
import Process as Process
import pandas as pd
import FunRand as fr

def Task2():
    funRand = fr.FunRand

    daleyCreate = 0.5
    delayProcess1 = 0.3
    delayProcess2 = 0.3

    maxQueueP1 = 3
    maxQueueP2 = 3

    stateP1 = [1]
    stateP2 = [1]

    tnextC = 0.1
    tnextP1 = [funRand.Norm(1, 0.3)]
    tnextP2 = [funRand.Norm(1, 0.3)]

    queueP1 = 2
    queueP2 = 2

    simulateTime = 1000

    delay = [daleyCreate, delayProcess1, delayProcess2]
    maxQueue = [maxQueueP1, maxQueueP2]
    state = [stateP1, stateP2]
    tnext = [tnextC, tnextP1, tnextP2]
    queue = [queueP1, queueP2]

    SimModelForTask2(delay, simulateTime, maxQueue, tnext, state, queue)

   

def SimModelForTask2(delay, simulateTime, maxQueue, tnext, state, queue):

    c = Create.Create(delay[0])
    p1 = Process.Process(delay[1])
    p2 = Process.Process(delay[2])

    c.name = 'Creator'
    p1.name = 'Queue1'
    p2.name = 'Queue2'

    p1.maxQueue = maxQueue[0]
    p2.maxQueue = maxQueue[1]

    c.tnext = tnext[0]
    p1.tnext = tnext[1]
    p2.tnext = tnext[2]

    p1.state = state[0]
    p2.state = state[1]

    p1.queue = queue[0]
    p2.queue = queue[1]

    c.nextElement = [p1, p2]
    
    modelList = [c, p1, p2]

    model = Model.Model(modelList)
    model.simulate(simulateTime)




Task2()