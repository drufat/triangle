import matplotlib.pyplot as plt

import triangle as tr

spiral = tr.get_data('spiral')

t = tr.triangulate(spiral, 'a.2')
ax1 = plt.subplot(111)
tr.plot(ax1, **t)

plt.show()
