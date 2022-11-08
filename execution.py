from interpolationSplines import interpolationSplines
import matplotlib.pyplot as plt
import numpy as np
from numpy import nbytes, zeros,array,dot,linspace, linalg


nb = 1000

## Courbe 1 ##
x1 = array([1, 2, 5, 6, 7, 8, 10, 13, 17])
y1 = array([3, 3.7, 3.9, 4.2, 5.7, 6.6, 7.1, 6.7, 4.5])
[X1, Y1] = interpolationSplines(x1, y1, nb)

## Courbe 2 ##
x2 = array([17, 20, 23, 24, 25, 27, 27.7])
y2 = array([4.5, 7, 6.1, 5.6, 5.8, 5.2, 4.1])
[X2, Y2] = interpolationSplines(x2, y2, nb)

## Courbe 3 ##
x3 = array([27.7, 28, 29, 30])
y3 = array([4.1, 4.3, 4.1, 3])
[X3, Y3] = interpolationSplines(x3, y3, nb)


## tracer ##
plt.plot(X1, Y1, X2, Y2, X3, Y3)
plt.title("Mon Chien Numérique")
plt.show()