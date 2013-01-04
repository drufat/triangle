import matplotlib.pyplot as plt
import triangle
import triangle.data
import triangle.plot

d = triangle.data.spiral

ax1 = plt.subplot(221, aspect='equal')
triangle.plot.plot(ax1, vertices=d['vertices'])

pnts, triangles = triangle.triangulate(d['vertices'])
ax2 = plt.subplot(222, sharex=ax1, sharey=ax1)
triangle.plot.plot(ax2, vertices=pnts, triangles=triangles)

pnts, triangles = triangle.triangulate(d['vertices'], quality=True)
ax3 = plt.subplot(223, sharex=ax1, sharey=ax1)
triangle.plot.plot(ax3, vertices=pnts, triangles=triangles)

pnts, triangles = triangle.triangulate(d['vertices'], quality=True, minangle=32.5)
ax4 = plt.subplot(224, sharex=ax1, sharey=ax1)
triangle.plot.plot(ax4, vertices=pnts, triangles=triangles)

plt.show()
