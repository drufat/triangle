import matplotlib.pyplot as plt

import triangle as tr

dots = tr.get_data('dots')
pts = dots['vertices']
segs = tr.convex_hull(pts)

tr.plot(plt.axes(), vertices=pts, segments=segs)

plt.show()
