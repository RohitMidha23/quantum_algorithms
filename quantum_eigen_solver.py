iimport pennylane as qml
from pennylane import numpy as np
from pennylane.optimize import GradientDescentOptimizer

dev = qml.device('default.qubit', wires=2)


def GetAnsatz():

    qml.Rot(0.3, 1.8, 5.4, wires=1)
    qml.RX(-0.5, wires=0)
    qml.RY( 0.5, wires=1)
    qml.CNOT(wires=[0, 1])


@qml.qnode(dev)
def getCircuitX():

    GetAnsatz()
    return qml.expval.PauliX(1)


@qml.qnode(dev)
def getCircuitY():

    GetAnsatz()
    return qml.expval.PauliY(1)


def getCost(var):
iimport pennylane as qml
from pennylane import numpy as np
from pennylane.optimize import GradientDescentOptimizer

dev = qml.device('default.qubit', wires=2)


def GetAnsatz():

    qml.Rot(0.3, 1.8, 5.4, wires=1)
    qml.RX(-0.5, wires=0)
    qml.RY( 0.5, wires=1)
    qml.CNOT(wires=[0, 1])


@qml.qnode(dev)
def getCircuitX():

    GetAnsatz()
    return qml.expval.PauliX(1)


@qml.qnode(dev)
def getCircuitY():

    GetAnsatz()
    return qml.expval.PauliY(1)


def getCost(var):


    expX = getCircuitX()
    expY = getCircuitY()

    return (var[0] * expX + var[1] * expY) ** 2


optimizer = GradientDescentOptimizer(0.5)


variables = [0.3, 2.5]
variables_gd = [variables]
for i in range(20):
    variables = optimizer.step(getCost, variables)
    variables_gd.append(variables)

    print('Cost - step {:5d}: {: .7f} | Variable values: [{: .5f},{: .5f}]'
          .format(i+1, getCost(variables), variables[0], variables[1]) )
