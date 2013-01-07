import triangle
import triangle.plot
import matplotlib.pyplot as plt

la = triangle.get_data('la')

ax1 = plt.subplot(311, aspect='equal')
triangle.plot.plot(ax1, **la)

t = triangle.triangulate(la, 'pq')
ax2 = plt.subplot(312, sharex=ax1, sharey=ax1)
triangle.plot.plot(ax2, **t)

t = triangle.triangulate(la, 'pqa')
ax2 = plt.subplot(313, sharex=ax1, sharey=ax1)
triangle.plot.plot(ax2, **t)

plt.show()
