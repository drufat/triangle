from numpy.testing import *
from triangle import triangulate

def test_ident():

    pts = [[0, 0], [0, 1], [1, 1], [1, 0]]
    (verts, _) = triangulate(pts)

    for p1, p2 in zip(pts, verts):
        assert_approx_equal(p1[0], p2[0])
        assert_approx_equal(p1[1], p2[1])

if __name__ == '__main__':
    run_module_suite()
