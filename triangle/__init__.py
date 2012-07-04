import numpy.testing
import triangle.core

#test = numpy.testing.Tester().test

def triangulate(pts, maxarea=None, minangle=None):
    """
    >>> pts = [[0, 0], [0, 1], [1, 1], [1, 0]]
    >>> triangulate(pts) 
    (array([[ 0.,  0.],
           [ 0.,  1.],
           [ 1.,  1.],
           [ 1.,  0.]]),
     array([[1, 0, 3],
           [3, 2, 1]], dtype=int32))
    """
    opts = 'Qzq'
    if minangle != None:
        opts += ('%.2f' % minangle)
    if maxarea != None:
        opts += ('a%.16f' % maxarea)
    return triangle.core.triangulate(pts, opts)

__all__ = ['triangulate']
