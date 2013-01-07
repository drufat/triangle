import triangle
import triangle.plot as plot
import matplotlib.pyplot as plt

box = triangle.get_data('box')

ax1 = plt.subplot(121, aspect='equal')
triangle.plot.plot(ax1, **box)

t = triangle.triangulate(box, 'pc')

ax2 = plt.subplot(122, sharex=ax1, sharey=ax1)
plot.plot(ax2, **t)

plt.show()
