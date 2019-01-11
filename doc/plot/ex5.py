import matplotlib.pyplot as plt
import numpy as np

import triangle as tr

theta = np.linspace(0, 2 * np.pi, 33)[:-1]
pts = np.vstack((np.cos(theta), np.sin(theta))).T
A = dict(vertices=pts)
B = tr.triangulate(A, 'qa0.05')
tr.compare(plt, A, B)
plt.show()
