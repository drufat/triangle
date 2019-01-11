import matplotlib.pyplot as plt

import triangle as tr

spiral = tr.get_data('spiral')
a = tr.triangulate(spiral)
b = tr.triangulate(spiral, 'q')
c = tr.triangulate(spiral, 'q32.5')

plt.figure(figsize=(5, 6))
ax1 = plt.subplot(221)
tr.plot(ax1, **spiral)

ax2 = plt.subplot(222)
tr.plot(ax2, **a)

ax3 = plt.subplot(223)
tr.plot(ax3, **b)

ax4 = plt.subplot(224)
tr.plot(ax4, **c)

plt.tight_layout()
plt.show()
