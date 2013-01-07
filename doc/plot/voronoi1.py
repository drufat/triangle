import triangle
import triangle.plot
import matplotlib.pyplot as plt

pts = triangle.get_data('diamond_02_00009')['vertices']

ax1 = plt.subplot(121, aspect='equal')
triangle.plot.plot(ax1, vertices=pts)
lim = ax1.axis()

d = triangle.get_data('diamond_02_00009.1.v')
ax2 = plt.subplot(122, sharex=ax1, sharey=ax1)
triangle.plot.plot(ax2, **d)
ax2.axis(lim)

plt.show()
