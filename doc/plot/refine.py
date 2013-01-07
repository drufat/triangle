import triangle
import triangle.plot as plot
import matplotlib.pyplot as plt

box1 = triangle.get_data('bbox.1')
box2 = triangle.triangulate(box1, 'rpa0.2')
box3 = triangle.triangulate(box2, 'rpa0.05')
box4 = triangle.triangulate(box3, 'rpa0.0125')

plt.figure(figsize=(15, 5))

ax1 = plt.subplot(131, aspect='equal')
plot.plot(ax1, **box2)

ax2 = plt.subplot(132, sharex=ax1, sharey=ax1)
triangle.plot.plot(ax2, **box3)

ax2 = plt.subplot(133, sharex=ax1, sharey=ax1)
triangle.plot.plot(ax2, **box4)

plt.show()