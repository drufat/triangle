import matplotlib.pyplot as plt

import triangle as tr

plt.figure(figsize=(8, 7))

la = tr.get_data('la')
ax1 = plt.subplot(311)
tr.plot(ax1, **la)

t = tr.triangulate(la, 'pq')
ax2 = plt.subplot(312, sharex=ax1, sharey=ax1)
tr.plot(ax2, **t)

t = tr.triangulate(la, 'pqa')
ax2 = plt.subplot(313, sharex=ax1, sharey=ax1)
tr.plot(ax2, **t)

plt.show()
