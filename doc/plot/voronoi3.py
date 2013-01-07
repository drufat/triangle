import triangle
import triangle.plot
import matplotlib.pyplot as plt

pts = [[0, 0], [0, 1], [0.5, 0.5], [1, 1], [1, 0]]
import numpy as np
pts = np.array(pts)

vertices, edges, ray_origins, ray_directions = triangle.voronoi(pts)
ax = plt.axes()
triangle.plot.plot(ax, vertices=pts)
lim = ax.axis()
triangle.plot.plot(ax, vertices=vertices, edges=edges, 
                   ray_origins=ray_origins, ray_directions=ray_directions)
ax.axis(lim)

plt.show()
