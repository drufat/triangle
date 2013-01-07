import triangle
import triangle.plot as plot
import matplotlib.pyplot as plt

spiral = triangle.get_data('spiral')

ax1 = plt.subplot(221, aspect='equal')
triangle.plot.plot(ax1, vertices=spiral['vertices'])

a = triangle.triangulate(spiral)
ax2 = plt.subplot(222, sharex=ax1, sharey=ax1)
plot.plot(ax2, **a)

b = triangle.triangulate(spiral, 'q')
ax3 = plt.subplot(223, sharex=ax1, sharey=ax1)
plot.plot(ax3, **b)

c = triangle.triangulate(spiral, 'q32.5')
ax4 = plt.subplot(224, sharex=ax1, sharey=ax1)
plot.plot(ax4, **c)

plt.show()
