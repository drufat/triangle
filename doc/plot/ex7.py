import matplotlib.pyplot as plt
import numpy as np

import triangle as tr

# arrays to fill in with input
vertices = []
segments = []
regions = []


# make a box with given dims and place given attribute at its center
def make_box(x, y, w, h, attribute):

    i = len(vertices)

    vertices.extend([
        [x, y],
        [x + w, y],
        [x + w, y + h],
        [x, y + h],
    ])

    segments.extend([
        (i + 0, i + 1),
        (i + 1, i + 2),
        (i + 2, i + 3),
        (i + 3, i + 0),
    ])

    regions.append([x + 0.5 * w, y + 0.5 * h, attribute, 0])


# generate some input
make_box(0, 0, 5, 5, 1)
make_box(1, 1, 3, 1, 2)
make_box(1, 3, 1, 1, 3)
make_box(3, 3, 1, 1, 4)

A = dict(vertices=vertices, segments=segments, regions=regions)
B = tr.triangulate(A, 'pA')

tr.compare(plt, A, B)
plt.show()
