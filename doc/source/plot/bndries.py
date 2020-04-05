import matplotlib.pyplot as plt

import triangle as tr


def bndry(dict):
    return {k: dict[k] for k in ('vertices', 'segments')}


face = tr.get_data('face.1')
A = tr.triangulate(face, 'rc')
B = tr.triangulate(face, 'rpc')

tr.compare(plt, bndry(A), bndry(B))

plt.show()
