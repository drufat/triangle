import matplotlib.pyplot as plt

import triangle as tr

d0 = tr.get_data('dots')
d1 = tr.triangulate(d0)
tr.compare(plt, d0, d1)
plt.show()
