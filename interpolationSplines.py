from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
from numpy import concatenate, nbytes, zeros,array,dot,linspace, linalg, hstack
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
    Yp = zeros(nb)

    h[0] = x[1] - x[0]
    f[0] = 6*(y[1] - y[0]) / h[0]
    T[0][0] = 2 * h[0]
    
    ## Construction de la matrice T ##
    for i in range(1, n-1):
        h[i] = x[i+1] - x[i]
        T[i][i] = 2 * (h[i] + h[i-1])
        T[i][i-1] = h[i-1]
        T[i-1][i] = h[i]
        f[i] = 6 * (y[i+1] - y[i]) / h[i] - 6 * (y[i] - y[i-1]) / h[i-1]

    print('T = \n', T)
    print('f = ', f)
    ## Construction du vecteur m ##
    m = dot(linalg.inv(T), f)
    print('m = ', m)

    ## Construction des coefficients a et b ##
    for j in range(0, n-2):
        a[j] = (y[j+1] - y[j])/h[j] - h[j]*(m[j+1] - m[i])/6
        b[j] = y[j] - (m[j]*h[j]**2)/6
    a[n-2] = (y[n-1] - y[n-2])/h[n-2] + h[n-2]*(m[n-2])/6
    b[n-2] = y[n-2] - m[n-2]*h[n-2]**2/6
    
    print('a = ', a)
    print('b = ', b)

    ## Construction de la spline ##
    for k in range(0, n-2):
        Xp = linspace(x[k], x[k+1], nb)
        Yp = m[k+1]*((Xp - x[k])**3)/6*h[k] + m[k]*((x[k+1] - Xp)**3)/6*h[k] + a[k]*(Xp - x[k]) + b[k]


        # for l in range(nb):
        #     if(k != n-2):
        #         Yp[l] = m[k+1]*((Xp[l] - x[k])**3)/6*h[k] + m[k]*((x[k+1] - Xp[l])**3)/6*h[k] + a[k]*(Xp[l] - x[k]) + b[k]
        #     else:
        #         Yp[l] = m[k]*((x[k+1] - Xp[l])**3)/6*h[k] + a[k]*(Xp[l] - x[k]) + b[k]
        
        if (k == 0):
            yp = Yp
            xp = linspace(x[0], x[1], nb)
        else:
            xp = concatenate((xp, Xp))
            yp = concatenate((yp, Yp))
    print('xp = ', xp)
    print('yp = ', yp)

    return xp, yp


x = array([1, 2, 5, 6, 7, 8, 10, 13, 17])
y = array([3, 3.7, 3.9, 4.2, 5.7, 6.6, 7.1, 6.7, 4.5])
nb = 3

[xp, yp] = interpolationSplines(x, y, nb)
plt.plot(xp, yp)
plt.show()
# for i in range(len(xp)):
#     plt.plot(xp[i], yp[i])
