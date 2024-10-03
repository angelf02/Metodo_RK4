#!/usr/bin/env python

import numpy as np

oOper = np.array([[0, 1], [1, 0]])
yInit = np.array([[1, 0], [0, 0]])

def dyn_generator(oper, state):
    """Se refiere a la función que genera la dinámica del problema.

    Examples:
        >>> import numpy as np
        >>> oOper = np.array([[0, 1], [1, 0]])
        >>> yInit = np.array([[1, 0], [0, 0]])
        >>> dyn_generator(oOper,yInit)
        [[0.-0.j 0.+1.j]
         [0.-1.j 0.-0.j]]

    Args:
        oper (array_object): Primer argumento, especifica al operador deseado
        state (array_object): Segundo argumento, especifica un estado

    Returns:
        out (array_object): Devuelve el valor de la función evaluada en oper y state.

    """
    return -1.0j*(np.dot(oper,state)-np.dot(state,oper))

def rk4(func, oper, state, h):
    """Se refiere a la función que realiza la operación dinámica (implementación de RK4).

    Examples:
        >>> rk4(dyn_generator,oOper,yInit,0.1)
        [[0.99003333+0.j         0.        +0.09933333j]
         [0.        -0.09933333j 0.00996667+0.j        ]]

    Args:
        func (function): Primer argumento, especifica la función que genera la dinámica
        oper (array_object): Segundo argumento, especifica al operador deseado
        state (array_object): Tercer argumento, especifica un estado
        h (float): Cuarto argumento, se refiere al paso temporal deseado

    Returns:
        out (array_object): Devuelve el estado siguiente.

    """
    k1=h*func(oper,state)
    k2=h*func(oper,state+k1/2)
    k3=h*func(oper,state+k2/2)
    k4=h*func(oper,state+k3)
    return state+(1/6)*(k1+2*k2+2*k3+k4)

times = np.linspace(0.0,10.0, num=50)
h=times[1]-times[0]

yCopy = yInit.copy()

stateQuant00 = np.zeros(times.size)
stateQuant11 = np.zeros(times.size)

for tt in range(times.size):
    stateQuant00[tt]=yInit[0,0].real
    stateQuant11[tt]=yInit[1,1].real

    yInit=rk4(dyn_generator,oOper,yInit,h)

import matplotlib.pyplot as plt

plt.style.use('_mpl-gallery')

x = times
y = stateQuant00
y2 = stateQuant11

plt.plot(x, y, 'g.-',linewidth=1.5)
plt.plot(x, y2 , '.-', linewidth=1.5)

plt.title("Evolucion temporal de las entradas (0,0) y (1,1) del estado estudiado.")
plt.xlabel("Tiempo")
plt.ylabel("Entradas del estado")
plt.legend(["Entrada (0,0)", "Entrada (1,1)"], loc="upper left",bbox_to_anchor=(1.05, 0.75), ncol=1)

plt.savefig('Evolucion de las entradas.png')

