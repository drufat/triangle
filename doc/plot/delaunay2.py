import matplotlib.pyplot as plt
import numpy as np

import triangle as tr

pts = np.array([[0, 0], [0, 1], [.5, .5], [1, 1], [1, 0]])
tri = tr.delaunay(pts)
tr.plot(plt.axes(), vertices=pts, triangles=tri)
plt.show()
