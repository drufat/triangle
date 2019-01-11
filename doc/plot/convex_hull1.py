import matplotlib.pyplot as plt
import numpy as np

import triangle as tr

pts = np.array([[0, 0], [0, 1], [1, 1], [1, 0]])
segments = tr.convex_hull(pts)
tr.plot(plt.axes(), vertices=pts, segments=segments)
plt.show()
