import triangle
import triangle.plot
import matplotlib.pyplot as plt

def bndry(dict):
    d = {}
    for k in ('vertices', 'segments'): d[k] = dict[k]
    return d

face = triangle.get_data('face.1')

ax1 = plt.subplot(121, aspect='equal')
rslt = triangle.triangulate(face, 'rc')
triangle.plot.plot(ax1, **bndry(rslt))

ax2 = plt.subplot(122, sharex=ax1, sharey=ax1, aspect='equal')
rslt = triangle.triangulate(face, 'rpc')
triangle.plot.plot(ax2, **bndry(rslt))

plt.show()
