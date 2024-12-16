import numpy as np
import matplotlib.pyplot as plt

def z_func(x,y):
    return np.sin(12 * x) * np.cos(12 * y) / 12
def z_dif(x,y):
    return np.cos(12 * x) * np.cos(12 * y) , -np.sin(12 * x) * np.sin(12 * y)


x = np.arange(-1, 1, 0.05)
y = np.arange(-1, 1, 0.05)

X, Y = np.meshgrid(x, y)

Z = z_func(X, Y)

ax = plt.subplot(projection='3d')

ax.plot_surface(X, Y, Z, cmap = "viridis")

#plt.show()
