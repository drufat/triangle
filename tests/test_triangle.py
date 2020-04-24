import numpy as np

from triangle import triangulate, convex_hull, voronoi, delaunay


def test_triangulate():
    v = [[0, 0], [0, 1], [1, 1], [1, 0]]
    t = triangulate({"vertices": v}, "a0.2")
    assert np.allclose(
        t["vertices"],
        [
            [0.0, 0.0],
            [0.0, 1.0],
            [1.0, 1.0],
            [1.0, 0.0],
            [0.5, 0.5],
            [0.0, 0.5],
            [0.5, 0.0],
            [1.0, 0.5],
            [0.5, 1.0],
        ],
    )
    assert np.allclose(
        t["vertex_markers"],
        [[1], [1], [1], [1], [0], [1], [1], [1], [1]],
    )
    assert np.allclose(
        t["triangles"],
        [
            [7, 2, 4],
            [5, 0, 4],
            [4, 8, 1],
            [4, 1, 5],
            [4, 0, 6],
            [6, 3, 4],
            [4, 3, 7],
            [4, 2, 8],
        ],
    )


def test_delaunay():
    pts = [[0, 0], [0, 1], [0.5, 0.5], [1, 1], [1, 0]]
    tri = delaunay(pts)
    assert np.allclose(
        tri,
        [
            [1, 0, 2],
            [2, 4, 3],
            [4, 2, 0],
            [2, 3, 1],
        ],
    )


def test_hull():
    pts = [[0, 0], [0, 1], [1, 1], [1, 0]]
    segments = convex_hull(pts)
    assert np.allclose(segments, [[3, 0], [2, 3], [1, 2], [0, 1]])


def test_voronoi():
    pts = [[0, 0], [0, 1], [0.5, 0.5], [1, 1], [1, 0]]
    points, edges, ray_origin, ray_direct = voronoi(pts)
    assert np.allclose(
        points,
        [[0.0, 0.5], [1.0, 0.5], [0.5, 0.0], [0.5, 1.0]],
    )
    assert np.allclose(edges, [[0, 2], [0, 3], [1, 2], [1, 3]])

    assert np.allclose(ray_origin, [0, 1, 2, 3])
    assert np.allclose(
        ray_direct,
        [[-1.0, 0.0], [1.0, 0.0], [0.0, -1.0], [0.0, 1.0]],
    )
