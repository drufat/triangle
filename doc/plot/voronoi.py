import matplotlib.pyplot as plt

import triangle as tr

pts = tr.get_data('dots')['vertices']

A = dict(vertices=pts)

points, edges, ray_origin, ray_direct = tr.voronoi(pts)
B = dict(
    vertices=points, edges=edges,
    ray_origins=ray_origin, ray_directions=ray_direct
)
tr.compare(plt, A, B)
plt.show()
