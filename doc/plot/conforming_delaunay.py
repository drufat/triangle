import triangle.data as data
from triangle.plot import plot
import matplotlib.pyplot as plt
import triangle as t

ax = plt.axes()
pnt, tri = t.triangulate1(constrained=True, conforming=True, quality=True, **data.A)
plot(ax, vertices=pnt, triangles=tri)
plt.show()
