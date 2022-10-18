from numpy import zeros,array,dot,linspace
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt


def interpolationSplines(x, y, n):

    # x: array of x values
    # y: array of y values
    # n: number of points in the spline

    # returns: array of n points in the spline
    T = zeros((n, n))
    h = zeros(n-1)
    f = zeros(n-1)
    m = zeros(n-1)
    a = zeros(n-1)
    b = zeros(n-1)
    for i in range(n-1):
        h[i] = x[i+1] - x[i]
        T[i][i] = 2(h[i-1] + h[i])
        T[i][i-1] = h[i-1]
        T[i-1][i] = h[i-1]
        f[i] = 6*((y[i+1] - y[i])/h[i] - (y[i] - y[i-1])/h[i-1])
    m = dot(linalg.inv(T), f)

    for j in range(n-1):
        a[j] = (y[j+1] - y[j])/h[j] - h[j]*(2*m[j] + m[j+1])/6
        b[j] = y[j] - m[j]*h[j]**2/6




    # Cubic spline interpolation
    # cs = CubicSpline(x, y)
    # xnew = np.linspace(x[0], x[-1], n)
    # ynew = cs(xnew)

    return xnew, ynew