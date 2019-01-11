import matplotlib.pyplot as plt
import numpy as np

import triangle as tr

A = dict(vertices=np.array(((0, 0), (1, 0), (1, 1), (0, 1))))
B = tr.triangulate(A, 'qa0.01')
tr.compare(plt, A, B)
plt.show()
