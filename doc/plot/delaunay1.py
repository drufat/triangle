import triangle
import triangle.data
import triangle.plot
import matplotlib.pyplot as plt

pts = triangle.data.spiral['vertices']

ax1 = plt.subplot(121, aspect='equal')
triangle.plot.plot(ax1, vertices=pts)

pnts, triangles = triangle.triangulate(pts)

ax2 = plt.subplot(122, sharex=ax1, sharey=ax1)
triangle.plot.plot(ax2, vertices=pnts, triangles=triangles)

plt.show()
