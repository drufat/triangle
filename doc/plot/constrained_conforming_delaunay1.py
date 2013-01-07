import triangle
import triangle.plot as plot
import matplotlib.pyplot as plt


face = triangle.get_data('face')
ax1 = plt.subplot(121, aspect='equal')
plot.plot(ax1, **face)

t = triangle.triangulate(face, 'pq10')

ax2 = plt.subplot(122, sharex=ax1, sharey=ax1)
plot.plot(ax2, **t)

plt.show()
