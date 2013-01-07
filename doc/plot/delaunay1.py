import triangle
import triangle.plot as plot
import matplotlib.pyplot as plt

spiral = triangle.get_data('spiral')
ax1 = plt.subplot(121, aspect='equal')
plot.plot(ax1, **spiral)

t = triangle.triangulate(spiral)

ax2 = plt.subplot(122, sharex=ax1, sharey=ax1)
plot.plot(ax2, **t)

plt.show()
