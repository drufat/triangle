import triangle
import triangle.data
import matplotlib.pyplot as plt

pts = triangle.data.dot['vertices']

points, edges, ray_origin, ray_direct = triangle.voronoi(pts)

ax1 = plt.subplot(121, aspect='equal')
ax1.scatter(*pts.T, color='k')
lim = ax1.axis()
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)

ax2 = plt.subplot(122, sharex=ax1, sharey=ax1)
ax2.axis(lim)
ax2.scatter(*pts.T, color='k')
#plot regular edges
for beg, end in edges:
    x0, y0 = points[beg, :]
    x1, y1 = points[end, :]
    ax2.fill([x0, x1], [y0, y1], facecolor='none', edgecolor='k', linewidth=.5)
#plot rays for edges whose one endpoint is at infinity
for (beg, (vx, vy)) in zip(ray_origin, ray_direct):
    x0, y0 = points[beg, :]
    scale = 1000
    x1, y1 = x0 + scale*vx, y0 + scale*vy
    ax2.fill([x0, x1], [y0, y1], facecolor='none', edgecolor='k', linewidth=.5)
    ax2.get_xaxis().set_visible(False)
    ax2.get_yaxis().set_visible(False)

plt.show()
