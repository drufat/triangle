import matplotlib.pyplot as plt

import triangle as tr

pts = tr.get_data('diamond_02_00009')['vertices']
t = dict(vertices=pts)
d = tr.get_data('diamond_02_00009.1.v')

tr.compare(plt, t, d)
plt.show()
