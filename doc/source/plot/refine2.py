import matplotlib.pyplot as plt

import triangle as tr

box1 = tr.get_data('bbox.1')
box2 = tr.triangulate(box1, 'rpaa.5')
tr.plot(plt.axes(), **box2)
plt.show()
