import matplotlib.pyplot as plt
import triangle
import triangle.plot

spiral = triangle.get_data('spiral')

t = triangle.triangulate(spiral, 'a.2')
ax1 = plt.subplot(111, aspect='equal')
triangle.plot.plot(ax1, **t)

plt.show()