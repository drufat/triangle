import triangle.data as data
from triangle.plot import plot
import matplotlib.pyplot as plt
import triangle as t
from triangle import triangulate1

ax = plt.axes()
pnt, tri = triangulate1(constrained=True, **data.A)
plot(ax, vertices=pnt, triangles=tri)
plt.show()
