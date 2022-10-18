from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
from numpy import nbytes, zeros,array,dot,linspace, linalg, hstack
import matplotlib.pyplot as plt


def interpolationSplines(x, y, nb):

    # x: array of x values
    # y: array of y values
    # n: number of points in the spline

    n = len(x)
    T = zeros((n-1, n-1))
    h = zeros(n-1)
    f = zeros(n-1)
    m = zeros(n-1)
    a = zeros(n-1)
    b = zeros(n-1)
    Yp = zeros(nb*n)
    xp = [0]
    yp = [0]

    h[0] = x[1] - x[0]
    f[0] = (y[1] - y[0]) / h[0]
    T[0][0] = 2 * h[0]
    
    ## Construction de la matrice T ##
    for i in range(1, n-1):
        h[i] = x[i+1] - x[i]
        T[i][i] = 2 * (h[i] + h[i-1])
        T[i][i-1] = h[i-1]
        T[i-1][i] = h[i-1]
        f[i] = 6*((y[i+1] - y[i])/h[i] - (y[i] - y[i-1])/h[i-1])

    print(T)
    print(f)
    ## Construction du vecteur m ##
    m = dot(linalg.inv(T), f)
    print(m)

    ## Construction des coefficients a et b ##
    for j in range(0, n-2):
        a[j] = (y[j+1] - y[j])/h[j] - h[j]*(2*m[j] + m[j+1])/6
        b[j] = y[j] - m[j]*h[j]**2/6
    
    print(a)
    print(b)

    ## Construction de la spline ##
    for k in range(n-1):
        Xp = linspace(x[k], x[k+1], nb)
        for l in range(nb):
            Yp[k] = m[k+1]*((Xp[l] - x[k])**3)/6*h[k] + m[k]*((Xp[l] - x[k])**3)/6*h[k] + a[k]*(Xp[l] - x[k]) + b[k]

        xp = hstack((xp, Xp))
        yp = hstack((yp, Yp))

    return xp, yp


x = array([1, 2, 5, 6, 7, 8, 10, 13, 17])
y = array([3, 3.7, 3.9, 4.2, 5.7, 6.6, 7.1, 6.7, 4.5])
nb = 100
[xp, yp] = interpolationSplines(x, y, 100)
plt.plot(xp, yp)
# for i in range(len(xp)):
#     plt.plot(xp[i], yp[i])
