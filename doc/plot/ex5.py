import triangle
import triangle.plot
from numpy import *
import matplotlib.pyplot as plt

theta = linspace(0, 2*pi, 33)[:-1]
pts = vstack((cos(theta), sin(theta))).T
A = dict(vertices=pts)
B = triangle.triangulate(A, 'qa0.05')
triangle.plot.compare(plt, A, B)
plt.show()
