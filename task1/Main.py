import random
import sys
import Create as Create
import Model as Model
import Process as Process
import pandas as pd

def Task1_Probability():

    delay = [2,1,1,1,1]
    maxQueue = [5,5,5,5,5]
    simulateTime = 1000
    methodOfSelection =  "probability"
    probabilityParam =  [0.1, 0.5, 0.2, 0.2]

    SimModelForTask1(delay, simulateTime, maxQueue, methodOfSelection, probability = probabilityParam)


def Task1_Priority():
    delay = [2,1,1,1,1]
    maxQueue = [5,5,5,5,5]
    simulateTime = 1000
    methodOfSelection =  "priority"
    priorityParam = [2, 4, 1, 3]

    SimModelForTask1(delay, simulateTime, maxQueue, methodOfSelection, priority = priorityParam)
   


def SimModelForTask1(delay, simulateTime, maxQueue, methodOfSelection, probability = [], priority=[] ):

    c = Create.Create(delay[0])
    p1 = Process.Process(delay[1])
    p2 = Process.Process(delay[2])
    p3 = Process.Process(delay[3])
    p4 = Process.Process(delay[4])

    c.name = 'Creator'
    p1.name = 'Processor1'
    p2.name = 'Processor2'
    p3.name = 'Processor3'
    p4.name = 'Processor4'

    p1.maxQueue = maxQueue[0]
    p2.maxQueue = maxQueue[1]
    p3.maxQueue = maxQueue[2]
    p4.maxQueue = maxQueue[3]

    c.nextElement = [p1, p2, p3, p4]
    

    if(methodOfSelection == "probability"):
        c.probability = probability
        c.methodOfSelection = methodOfSelection
    elif(methodOfSelection == "priority"):
        c.priority = priority
        c.methodOfSelection = methodOfSelection

    modelList = [c, p1, p2, p3, p4]

    model = Model.Model(modelList)
    model.simulate(simulateTime)

# Task1_Probability()    
Task1_Priority()