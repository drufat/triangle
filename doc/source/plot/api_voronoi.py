import matplotlib.pyplot as plt
import numpy as np

import triangle as tr

pts = np.array([[0, 0], [0, 1], [0.5, 0.5], [1, 1], [1, 0]])

vertices, edges, ray_origins, ray_directions = tr.voronoi(pts)

A = dict(vertices=pts)
B = dict(vertices=vertices, edges=edges,
         ray_origins=ray_origins, ray_directions=ray_directions)
tr.compare(plt, A, B)
plt.show()
