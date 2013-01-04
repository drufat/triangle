import triangle
import triangle.data
import triangle.plot
import matplotlib.pyplot as plt

import numpy as np

d = triangle.data.face

ax1 = plt.subplot(121, aspect='equal')
triangle.plot.plot(ax1, **d)

pts, tri = triangle.triangulate1(constrained=True, quality=True, minagle=1.0, conforming=True, **d)

ax2 = plt.subplot(122, sharex=ax1, sharey=ax1)
triangle.plot.plot(ax2, vertices=pts, triangles=tri)

plt.show()
