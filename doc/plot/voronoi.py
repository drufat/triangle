import triangle
import triangle.plot
import matplotlib.pyplot as plt

pts = triangle.get_data('dots')['vertices']

ax1 = plt.subplot(121, aspect='equal')
triangle.plot.plot(ax1, vertices=pts)
lim = ax1.axis()

points, edges, ray_origin, ray_direct = triangle.voronoi(pts)
d = dict(vertices=points, edges=edges, ray_origins=ray_origin, ray_directions=ray_direct)
ax2 = plt.subplot(122, sharex=ax1, sharey=ax1)
triangle.plot.plot(ax2, **d)
ax2.axis(lim)

plt.show()
