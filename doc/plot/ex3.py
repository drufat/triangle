from triangle.plot import demo
from numpy import *
import matplotlib.pyplot as plt

pts = array(((0,0), (1,0), (1, 1), (0, 1)))
demo(plt, pts, maxarea=0.01)
plt.show()
