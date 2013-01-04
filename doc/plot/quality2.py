import triangle
import triangle.data
import triangle.plot
import matplotlib.pyplot as plt

import numpy as np

d = triangle.data.la

ax1 = plt.subplot(211, aspect='equal')
triangle.plot.plot(ax1, **d)


pts, tri = triangle.triangulate1(constrained=True, quality=True, **d)

ax2 = plt.subplot(212, sharex=ax1, sharey=ax1)
triangle.plot.plot(ax2, vertices=pts, triangles=tri)

plt.show()
