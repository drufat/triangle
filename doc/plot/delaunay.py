import triangle
import triangle.plot
import matplotlib.pyplot as plt

d0 = triangle.get_data('dots')
d1 = triangle.triangulate(d0)
triangle.plot.compare(plt, d0, d1)
plt.show()
