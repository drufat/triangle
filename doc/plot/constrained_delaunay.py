import matplotlib.pyplot as plt

import triangle as tr

ax = plt.axes()
A = tr.get_data('A')
t = tr.triangulate(A, 'p')
tr.plot(ax, **t)
plt.show()
