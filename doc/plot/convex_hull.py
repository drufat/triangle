import triangle
import triangle.plot as plot
import matplotlib.pyplot as plt

dots = triangle.get_data('dots')
pts = dots['vertices']
segs = triangle.convex_hull(pts)

plot.plot(plt.axes(), vertices=pts, segments=segs)

plt.show()
