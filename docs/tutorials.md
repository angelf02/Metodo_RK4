#Ejemplo de uso

En el presente documento se mostrará un ejemplo de uso del código de implementación del método RK4, este se encuentra en Referencia.

Se tiene que la dinámica del problema depende intrínsecamente del operador \(\mathbf{O}\). De forma que se escoge el siguiente:
\begin{equation}
\mathbf{O}=\begin{pmatrix}
0 & 1 \\
1 & 0 \\
\end{pmatrix}
\end{equation}

Dicho operador puede tener distintos significados físicos dependiendo del problema dinámico en cuestión. Y su implementación en python se vería de la siguiente manera: `oOper = np.array([[0, 1], [1, 0]])` (tómese en cuenta que` np` representa un acrónimo para invocar la funcionalidad módulo `numpy`).

Además, para el estado inicial se utilizará:
\begin{equation}
\mathbf{y}(t_0)=\begin{pmatrix}
1 & 0 \\
0 & 0 \\
\end{pmatrix}
\end{equation}

Equivalentemente, en python: `yInit = np.array([[1, 0], [0, 0]])`.


Ahora, se procede a inicializar un arreglo de valores temporales y definir \(h\), que como  se mencionó anteriormente, es el paso por iteración:

```
times = np.linspace(0.0,10.0, num=50)     
h=times[1]-times[0]
```

Una buena práctica es realizar un "deep copy" de un objeto sobre el que vamos a sobreescribir más adelante, este es el caso de `yInit`, por lo tanto, se usará `copy()`, también del módulo `numpy`:

`yCopy = yInit.copy()`

Con esto hecho, se llamará de manera iterativa la rutina `rk4()`. Calculando así el operador que genera la dinámica del sistema, u operador del estado del sistema

\begin{equation}
f(t,\mathbf{y}) = -i[\mathbf{O}, \mathbf{y}(t)] 
\end{equation}

a través del tiempo. Es importante notar que \(f\) no depende explícitamente de \(t\), sino, del operador y el estado; siendo en realidad este último el que cuenta con una dependencia temporal explícita.

Para visualizar su cambio de una forma clara, se va a guardar la entrada \((0, 0)\) y \((1, 1)\) de la matriz \(\mathbf{y}(t)\) para posteriormente graficarlas.

De manera que, se inicializará dos arreglos destinados a contener dichas entradas con valores iniciales de cero. Se utilizará el mismo tamaño del arreglo que contiene la variable independiente temporal:

```
stateQuant00 = np.zeros(times.size)      
stateQuant11 = np.zeros(times.size)
```

Y además, se crea una rutina que almacena los valores deseados, y realiza la evolución temporal:

```
for tt in range(times.size):
    stateQuant00[tt]=yInit[0,0].real
    stateQuant11[tt]=yInit[1,1].real

    yInit=rk4(dyn_generator,oOper,yInit,h)
```

Finalmente, con ayuda de `matplotlib` (`import matplotlib.pyplot as plt`) se grafican la entrada \((0, 0)\) y \((1, 1)\) de la matriz \(\mathbf{y}(t)\) con respecto al arreglo de valores temporales `times`:

```
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
```

El gráfico resultante se muestra a continuación:

<div>
<img src="Evolucion de las entradas.png" width="600"/>
</div>

