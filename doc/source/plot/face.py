import matplotlib.pyplot as plt

import triangle as tr

face = tr.get_data('face.1')
tr.plot(plt.axes(), **face)
plt.show()
