import matplotlib.pyplot as plt

import triangle as tr

A = tr.get_data('A')
t = tr.triangulate(A, 'pq0D')
tr.plot(plt.axes(), **t)
plt.show()
