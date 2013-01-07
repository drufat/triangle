import triangle
import triangle.plot
from numpy import *
import matplotlib.pyplot as plt

A = dict(vertices=array(((0,0), (1,0), (1, 1), (0, 1))))
B = triangle.triangulate(A, 'qa0.01')
triangle.plot.compare(plt, A, B)
plt.show()
