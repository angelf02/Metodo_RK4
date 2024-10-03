#Método numérico Runge-Kutta de orden 4

En análisis numérico, los métodos de Runge-Kutta son un conjunto de métodos genéricos iterativos, explícitos e implícitos, de resolución numérica de ecuaciones diferenciales ordinarias, concretamente, del problema de valor inicial. Este conjunto de métodos fue inicialmente desarrollado alrededor del año 1900 por los matemáticos alemanes Carl David Tolmé Runge y Martin Wilhelm Kutta.

Restringimos nuestro estudio al método Runge-Kutta de orden 4 (RK4). Habiendo definido el problema: \(\frac{dy}{dt} = f(t, y)\) sujeto a \(y(t_0) = y_0\), se procede a ir perturbando el estado "presente" \(y_{n}(t_{n})\) de forma iterativa, con el objetivo de encontrar el estado siguiente (\(y_{n+1}\)):

\(y_{n+1}=y_{n}+\frac{1}{6}(k_{1}+2k_{2}+2k_{3}+k_{4})\)

donde:

\begin{equation}
\left\{ \begin{array}{lr}
k_{1} := h \cdot f(t_{n},y_{n}) \\
k_{2} := h \cdot f \left( t_{n} + \frac{h}{2} , y_{n} + \frac{k_{1}}{2} \right) \\
k_{3} := h \cdot f \left( t_{n} + \frac{h}{2} , y_{n} + \frac{k_{2}}{2} \right) \\
k_{4} := h \cdot f \left( t_{n} + h , y_{n} + k_{3} \right)
\end{array} \right.
\end{equation}

Acá, \(h\) es el paso por iteración, o lo que es lo mismo, el incremento \(\Delta t_{n}\) entre los sucesivos puntos \(t_{n}\) y \(t_{n+1}\).

