import triangle
import triangle.plot as plot
import matplotlib.pyplot as plt

face = triangle.get_data('face')

ax1 = plt.subplot(121, aspect='equal')
plot.plot(ax1, **face)

t = triangle.triangulate(face, 'p')

ax2 = plt.subplot(122, sharex=ax1, sharey=ax1)
triangle.plot.plot(ax2, **t)

plt.show()
