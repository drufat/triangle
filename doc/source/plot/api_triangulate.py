import matplotlib.pyplot as plt
import numpy as np

import triangle as tr

A = {'vertices': np.array([[0, 0], [0, 1], [1, 1], [1, 0]])}
B = tr.triangulate(A, 'a0.2')

tr.compare(plt, A, B)
plt.show()
