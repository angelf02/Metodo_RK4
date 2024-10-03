#Bienvenido a `RK4`

Esta documentación se refiere al módulo `RK4`, una implementación del método Runge-Kutta de orden 4.

El módulo se encuentra en: [github.com](https://github.com/angelf02/Metodo_RK4).

##Sistemas dinámicos

Un sistema dinámico es un sistema cuyo estado evoluciona con el tiempo, son modelos de suma importancia en las ciencias. En física, un sistema dinámico se describe como una partícula o conjunto de partículas cuyo estado varía con el tiempo y, por lo tanto, obedece a ecuaciones diferenciales que implican derivadas temporales.

En general, un modelo dinámico intenta resolver la trayectoria temporal de alguna cantidad física como función de algún generador dinámico; este último usualmente representado de forma funcional.

En algunos casos, podemos modelar la dinámica de un estado genérico \(y\) mediante la ecuación dinámica
\begin{equation}
\frac{dy}{dt} = f(t, y),
\end{equation}
sujeta a la condición inicial
\begin{equation}
y(t_0) = y_0.
\end{equation}

Donde, \(t\) corresponde a la variable temporal; y \(y\) a un estado del sistema. Este estado puede ser representado mediante diferentes objetos matemáticos: desde cantidades escalares hasta matrices que representan cierto operador lineal.

El problema dinámico descrito anteriormente es usualmente conocido en el campo de las matemáticas aplicadas como **problema de condición inicial**.

