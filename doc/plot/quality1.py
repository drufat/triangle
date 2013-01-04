import matplotlib.pyplot as plt
import triangle
import triangle.data
import triangle.plot

d = triangle.data.spiral

pnts, triangles = triangle.triangulate(d['vertices'], maxarea=.2)
ax1 = plt.subplot(111, aspect='equal')
triangle.plot.plot(ax1, vertices=pnts, triangles=triangles)
