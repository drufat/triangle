from triangle.plot import demo
from numpy import *
import matplotlib.pyplot as plt

theta = linspace(0, 2*pi, 33)[:-1]
pts = vstack((cos(theta), sin(theta))).T
demo(plt, pts, quality=True)
plt.show()