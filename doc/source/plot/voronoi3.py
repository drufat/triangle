import matplotlib.pyplot as plt
import numpy as np

import triangle as tr

pts = [[0, 0], [0, 1], [0.5, 0.5], [1, 1], [1, 0]]
pts = np.array(pts)

vertices, edges, ray_origins, ray_directions = tr.voronoi(pts)
ax = plt.axes()
tr.plot(ax, vertices=pts)
lim = ax.axis()
tr.plot(ax, vertices=vertices, edges=edges,
        ray_origins=ray_origins, ray_directions=ray_directions)
ax.axis(lim)

plt.show()
