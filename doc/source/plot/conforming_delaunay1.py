import matplotlib.pyplot as plt

import triangle as tr

face = tr.get_data('face')
t = tr.triangulate(face, 'pq0D')
tr.plot(plt.axes(), **t)

plt.show()
