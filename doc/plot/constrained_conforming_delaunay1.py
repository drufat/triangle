import matplotlib.pyplot as plt

import triangle as tr

face = tr.get_data('face')
t = tr.triangulate(face, 'pq10')

tr.compare(plt, face, t)
plt.show()
