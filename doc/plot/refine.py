import matplotlib.pyplot as plt

import triangle as tr

box1 = tr.get_data('bbox.1')
box2 = tr.triangulate(box1, 'rpa0.2')
box3 = tr.triangulate(box2, 'rpa0.05')
box4 = tr.triangulate(box3, 'rpa0.0125')

plt.figure(figsize=(15, 5))

ax1 = plt.subplot(131, aspect='equal')
tr.plot(ax1, **box2)

ax2 = plt.subplot(132, sharex=ax1, sharey=ax1)
tr.plot(ax2, **box3)

ax2 = plt.subplot(133, sharex=ax1, sharey=ax1)
tr.plot(ax2, **box4)

plt.show()
