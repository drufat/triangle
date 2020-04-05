import matplotlib.pyplot as plt

import triangle as tr

spiral = tr.get_data('spiral')
t = tr.triangulate(spiral)

tr.compare(plt, spiral, t)

plt.show()
