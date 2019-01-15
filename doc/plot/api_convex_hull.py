import matplotlib.pyplot as plt
import numpy as np

import triangle as tr

pts = np.array([[0, 0], [0, 1], [1, 1], [1, 0]])
segments = tr.convex_hull(pts)

A = dict(vertices=pts)
B = dict(vertices=pts, segments=segments)
tr.compare(plt, A, B)
plt.show()
