import matplotlib.pyplot as plt
import numpy as np

import triangle as tr

N = 32
theta = np.linspace(0, 2 * np.pi, N, endpoint=False)
pts = np.stack([np.cos(theta), np.sin(theta)], axis=1)
A = dict(vertices=pts)
B = tr.triangulate(A, 'qa0.05')
tr.compare(plt, A, B)
plt.show()
