import matplotlib.pyplot as plt

import triangle as tr

box = tr.get_data('box')
t = tr.triangulate(box, 'pc')

tr.compare(plt, box, t)
plt.show()
