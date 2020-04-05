import matplotlib.pyplot as plt

import triangle as tr

A = tr.get_data('A')
ax = plt.axes()
tr.plot(ax, **A)
plt.show()
