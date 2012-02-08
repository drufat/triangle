import numpy.testing
import triangle.core

test = numpy.testing.Tester().test

def triangulate(pts, maxarea=0.0, minangle=0.0):
    '''
    Triangulate the area inside the set of points pts.
    '''

    opts = 'Qzq'
    if minangle > 0.0:
        opts += ('%.2f' % minangle)
    if maxarea > 0.0:
        opts += ('a%.16f' % maxarea)

    return triangle.core.triangulate(pts, opts)

__all__ = ['test', 'triangulate']
