from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np
from numpy import concatenate, nbytes, zeros,array,dot,linspace, linalg, hstack
import matplotlib.pyplot as plt

def interpolationSplines2(x, y, nb):

    # x: array of x values
    # y: array of y values
    # n: number of points in the spline

    n = len(x)-1
    T = zeros((n-2, n-2))
    h = zeros(n-1)
    f = zeros(n-2)
    m = zeros(n-2)
    a = zeros(n-1)
    b = zeros(n-1)
    xp = array([])
    yp = array([])

    ## Construction du vecteur h ##
    for l in range(0, n-1):
        h[l] = x[l+1] - x[l]
    
    print(h)

    ## Construction de la matrice T ##
    for i in range(1, n-2):
        T[i][i] = 2 * (h[i] + h[i-1])

    T[0][0] = 2 * (h[0] + h[1])
    
    for p in range(1, n-3):
        T[p][p+1] = h[p]
    T[0][1] = h[1]

    for q in range(1, n-2):
        T[q][q-1] = h[q-1]

    ## Construction du vecteur f
    for j in range(1, n-2):
        f[j-1] = 6 * (y[j+1] - y[j]) / h[j] - 6 * (y[j] - y[j-1]) / h[j-1]
    f[n-3] = 6 * (y[n-4] - y[n-3]) / h[n-4] - 6 * (y[n-3] - y[n-4]) / h[n-4]

    print('T = \n', T)
    print('f = ', f)

    ## Construction du vecteur m ##
    m = dot(linalg.inv(T), f)

    m = np.append(m, 0)
    m = np.insert(m, 0, 0)
    print('m = ', m)
    print(len(m))

    ## Construction des coefficients a et b ##
    for t in range(0, n-1):
        a[t] = (y[t+1] - y[t])/h[t] - h[t]*(m[t+1] - m[t])/6
        b[t] = y[t] - (m[t]*h[t]**2)/6
    
    print('a = ', a)
    print('b = ', b)

    ## Construction de la spline ##
    for k in range(0, n-1):
        
        Xp = linspace(x[k], x[k+1], nb)
        # xp = np.append(xp, Xp)
        Yp = (m[k+1]*(((Xp - x[k])**3)/(6*h[k])) + m[k]*(((x[k+1] - Xp)**3)/(6*h[k])) + (a[k]*(Xp - x[k]))) + b[k]
        print('k = ', k)
        print('Xp = ', Xp)
        print('Yp = ', Yp)
        # if(k != 0):
        #     Xp = np.delete(Xp, 0)
        #     Yp = np.delete(Yp, 0)
        xp = np.append(xp, Xp)
        yp = np.append(yp, Yp)

    print('xp = ', xp)
    print('yp = ', yp)

    return xp, yp

x1 = array([1, 2, 5, 6, 7, 8, 10, 13, 17])
x1 = np.delete(x1, -1)
print(x1)