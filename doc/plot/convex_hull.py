import triangle
import triangle.data
import triangle.plot
import matplotlib.pyplot as plt

import numpy as np

pts = triangle.data.dot['vertices']

ax1 = plt.subplot(111, aspect='equal')

segs = triangle.convex_hull(pts)

triangle.plot.plot(ax1, vertices=pts, segments=segs)

plt.show()
