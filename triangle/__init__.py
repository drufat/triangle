import os

import numpy as np
import triangle.core as core
from .version import  __version__

def triangulate(tri, opts=''):
    '''
    Perform triangulation on the input data `tri`. `tri` must be a dictionary
    that contains the following keys:

        * `vertices` - 2-D array that stores the xy position of each vertex
        * `segments` - optional 2-D array that stores segments. Segments are edges whose presence in the triangulation is enforced (although each segment may be subdivided into smaller edges). Each segment is specified by listing the indices of its two endpoints.
        * `holes` - optional 2-D array that stores holes. Holes are specified by identifying a point inside each hole. After the triangulation is formed, Triangle creates holes by eating triangles, spreading out from each hole point until its progress is blocked by PSLG segments; you must be careful to enclose each hole in segments, or your whole triangulation might be eaten away. If the two triangles abutting a segment are eaten, the segment itself is also eaten. Do not place a hole directly on a segment; if you do, Triangle will choose one side of the segment arbitrarily.
        * `regions` - optional 2-D array that stores region attributes and areas.

    The second (optional) arguments lists the options that should be passed to triangle.

        * `p` - Triangulates a Planar Straight Line Graph.
        * `r` - Refines a previously generated mesh.
        * `q` - Quality mesh generation with no angles smaller than 20 degrees. An alternate minimum angle may be specified after the `q`.
        * `a` - Imposes a maximum triangle area constraint. A fixed area constraint (that applies to every triangle) may be specified after the `a`, or varying areas may be read from the input dictionary.
        * `c` - Encloses the convex hull with segments.
        * `D` - Conforming Delaunay: use this switch if you want all triangles in the mesh to be Delaunay, and not just constrained Delaunay; or if you want to ensure that all Voronoi vertices lie within the triangulation.
        * `X` - Suppresses exact arithmetic.
        * `S` - Specifies the maximum number of added Steiner points.
        * `i` - Uses the incremental algorithm for Delaunay triangulation, rather than the divide-and-conquer algorithm.
        * `F` - Uses Steven Fortune's sweepline algorithm for Delaunay triangulation, rather than the divide-and-conquer algorithm.
        * `l` - Uses only vertical cuts in the divide-and-conquer algorithm. By default, Triangle uses alternating vertical and horizontal cuts, which usually improve the speed except with vertex sets that are small or short and wide. This switch is primarily of theoretical interest.
        * `s` - Specifies that segments should be forced into the triangulation by recursively splitting them at their midpoints, rather than by generating a constrained Delaunay triangulation. Segment splitting is true to Ruppert's original algorithm, but can create needlessly small triangles. This switch is primarily of theoretical interest.
        * `C` - Check the consistency of the final mesh. Uses exact arithmetic for checking, even if the -X switch is used. Useful if you suspect Triangle is buggy.
    '''

    fields = (('pointlist', 'vertices', 'double', 2),
              ('segmentlist', 'segments', 'int32', 2),
              ('holelist', 'holes', 'double', 2),
              ('regionlist', 'regions', 'double', 4),
              ('trianglelist', 'triangles', 'int32', 3),
              ('trianglearealist', 'triangle_max_area', 'double', 1),
              ('pointmarkerlist', 'vertex_markers', 'int32', 1),
              ('segmentmarkerlist', 'segment_markers', 'int32', 1),)

    if ('vertices' not in tri) or (len(tri['vertices'])<3) :
        raise ValueError('Input must have at least three input vertices.')

    a = core.TriangulateIO()
    for n0, n1, t, _ in fields:
        if n1 not in tri:
            continue
        value = np.array(tri[n1], dtype=t).flatten()
        setattr(a, n0, value)

    r = {}

    b = core.TriangulateIO()
    core.triang('Qz'+opts, a, b)
    for n0, n1, _, d in fields:
        try:
            value = np.array(getattr(b, n0))
        except ValueError:
            continue
        r[n1] = value.reshape((-1,d))

    return r

def delaunay(pts):
    """
    Computes the delaunay triangulation of points `pts`.

    >>> pts = [[0, 0], [0, 1], [0.5, 0.5], [1, 1], [1, 0]]
    >>> tri = delaunay(pts)

    .. plot..

        import triangle
        import triangle.plot
        import matplotlib.pyplot as plt
        import numpy as np
        pts = np.array([[0, 0], [0, 1], [.5, .5], [1, 1], [1, 0]])
        tri = triangle.delaunay(pts)
        triangle.plot.plot(plt.axes(), vertices=pts, triangles=tri)
        plt.show()

    """

    pts = np.array(pts, dtype='double')
    opts = 'Qz'

    _in = core.TriangulateIO()
    _in.pointlist = pts.flatten()
    _in.pointmarkerlist = np.zeros(pts.shape[0], dtype='int32')

    _out = core.TriangulateIO()

    core.triang(opts, _in, _out)

    return np.array(_out.trianglelist).reshape((-1, 3))


def convex_hull(pts):
    """
    Computes the convex hull enclosing `pts`.

    >>> pts = [[0, 0], [0, 1], [1, 1], [1, 0]]
    >>> segments = convex_hull(pts)

    .. plot::

        import triangle
        import triangle.plot
        import matplotlib.pyplot as plt
        import numpy as np
        pts = np.array([[0, 0], [0, 1], [1, 1], [1, 0]])
        segments = triangle.convex_hull(pts)
        triangle.plot.plot(plt.axes(), vertices=pts, segments=segments)
        plt.show()

    """
    pts = np.array(pts, dtype='double')
    opts = 'Qzc'

    _in = core.TriangulateIO()
    _in.pointlist = pts.flatten()
    _in.pointmarkerlist = np.zeros(pts.shape[0], dtype='int32')

    _out = core.TriangulateIO()

    core.triang(opts, _in, _out)

    return np.array(_out.segmentlist).reshape((-1, 2))

def voronoi(pts):
    """
    Computes the voronoi diagram `pts`.

    >>> pts = [[0, 0], [0, 1], [0.5, 0.5], [1, 1], [1, 0]]
    >>> points, edges, ray_origin, ray_direct = voronoi(pts)

    .. plot::

        import triangle
        import triangle.plot
        import matplotlib.pyplot as plt

        pts = [[0, 0], [0, 1], [0.5, 0.5], [1, 1], [1, 0]]
        import numpy as np
        pts = np.array(pts)

        vertices, edges, ray_origins, ray_directions = triangle.voronoi(pts)
        ax = plt.axes()
        triangle.plot.plot(ax, vertices=pts)
        lim = ax.axis()
        triangle.plot.plot(ax, vertices=vertices, edges=edges,
                           ray_origins=ray_origins, ray_directions=ray_directions)
        ax.axis(lim)

        plt.show()

    """
    pts = np.array(pts, dtype='double')
    opts = 'Qzv'

    _in = core.TriangulateIO()
    _in.pointlist = pts.flatten()
    _in.pointmarkerlist = np.zeros(pts.shape[0], dtype='int32')

    _out = core.TriangulateIO()
    _vorout = core.TriangulateIO()

    core.triang(opts, _in, _out, _vorout)

    p = np.array(_vorout.pointlist).reshape((-1,2))
    e = np.array(_vorout.edgelist).reshape((-1,2))
    n = np.array(_vorout.normlist).reshape((-1,2))
    fltr = (e[:,1]!=-1)
    edges = e[fltr]
    ray_origin = e[-fltr][:,0]
    ray_direct = n[-fltr]

    return p, edges, ray_origin, ray_direct

def loads(node=None,
         ele=None,
         poly=None,
         area=None,
         edge=None,
         neigh=None):
    """
    Load a dictionary representing the triangle data from strings.
    """


    import re
    def remove_comments(s):
        return re.sub("#.*\n", '', s)

    def split(tuple, pos):
        return tuple[:pos], tuple[pos:]

    start_at_zero = [True]
    def _vertices(tokens):
        head, tokens = split(tokens, 4)
        N_vertices, dim, N_attr, N_bnd_markers = list(map(int, head))
        if N_vertices==0: return tokens

        head, tokens = split(tokens, N_vertices*(1+dim+N_attr+N_bnd_markers))
        v = np.array(head).reshape(-1,1+dim+N_attr+N_bnd_markers)
        # check if starting at zero or one
        start_at_zero[0] = (v[0,0]=='0')
        data['vertices'] = np.array(v[:,1:3], dtype=np.double)
        if N_attr > 0:
            data['vertex_attributes'] = np.array(v[:,3:3+N_attr], dtype=np.double)
        if N_bnd_markers > 0:
            data['vertex_markers'] = np.array(v[:,3+N_attr:3+N_attr+N_bnd_markers], dtype=np.int32)

        return tokens

    def _ele(tokens):
        head, tokens = split(tokens, 3)
        N_triangles, N_nodes, N_attr = list(map(int, head))
        if N_triangles==0: return tokens

        head, tokens = split(tokens, N_triangles*(1+N_nodes+N_attr))
        v = np.array(head).reshape(-1,1+N_nodes+N_attr)
        data['triangles'] = np.array(v[:,1:N_nodes+1], dtype=np.int32)
        if not start_at_zero[0]:
            data['triangles'] -= 1
        if N_attr > 0:
            data['triangle_attributes'] = np.array(v[:,N_nodes+1:N_nodes+1+N_attr], dtype=np.double)

        return tokens

    def _segments(tokens):
        head, tokens = split(tokens, 2)
        N_segments, N_bnd_markers = list(map(int, head))
        if N_segments == 0: return tokens

        head, tokens = split(tokens, N_segments*(3+N_bnd_markers))
        v = np.array(head).reshape(-1, 3+N_bnd_markers)
        data['segments'] = np.array(v[:,1:3], dtype=np.int32)
        if not start_at_zero[0]:
            data['segments'] -= 1
        if N_bnd_markers > 0:
            data['segment_markers'] = np.array(v[:,3:3+N_bnd_markers], dtype=np.int32)

        return tokens

    def _holes(tokens):
        head, tokens = split(tokens, 1)
        N_holes = int(head[0])
        if N_holes == 0: return tokens

        head, tokens = split(tokens, N_holes*3)
        v = np.array(head).reshape(-1, 3)
        data['holes'] = np.array(v[:,1:3], dtype=np.double)

        return tokens

    def _area(tokens):
        head, tokens = split(tokens, 1)
        N_areas = int(head[0])
        if N_areas == 0: return tokens

        head, tokens = split(tokens, N_areas*2)
        v = np.array(head).reshape(-1, 2)
        data['triangle_max_area'] = np.array(v[:,1:2], dtype=np.double)

    def _edge(inpt):
        tokens = inpt.split('\n')
        head, tokens = split(tokens, 1)
        N_edges, N_bnd_markers = list(map(int, head[0].split()))
        if N_edges == 0: return

        tokens = [x.split() for x in tokens]
        edges = [x for x in tokens if len(x)==(3+N_bnd_markers)]
        rays = [x for x in tokens if len(x)==(5+N_bnd_markers)]
        edges= np.array(edges)
        rays = np.array(rays)
        data['edges'] = np.array(edges[:,1:3], dtype=np.int32)
        data['ray_origins'] = np.array(rays[:,1:2], dtype=np.int32)
        data['ray_directions'] = np.array(rays[:,3:], dtype=np.double)

        if not start_at_zero[0]:
            data['edges'] -= 1
            data['ray_origins'] -= 1

    def _regions(tokens):
        head, tokens = split(tokens, 1)
        N_areas = int(head[0])
        if N_areas == 0: return tokens

        # number of fields must be equal to 4 according to spec,
        # but it is only 3 in la.poly
        head, tokens = split(tokens, N_areas*4)
        v = np.array(head).reshape(-1, 4)
        regs = np.array(v[:,1:4], dtype=np.double)
        #add an extra column to make fields equal to 4
        regs = np.hstack((regs[:,0:2], np.zeros((regs.shape[0], 1)), regs[:,2:3]))
        data['regions'] = regs

    def _neigh(tokens):
        head, tokens = split(tokens, 2)
        N_triangles, N_neighs = list(map(int, head))
        if N_triangles == 0: return tokens

        head, tokens = split(tokens, N_triangles*(1+N_neighs))
        v = np.array(head).reshape(-1, 1+N_neighs)
        data['triangle_neighbors'] = np.array(v[:,1:], dtype=np.int32)
        if not start_at_zero[0]:
            data['triangle_neighbors'] -= 1

    data = {}
    if node:
        tokens = remove_comments(node).split()
        tokens = _vertices(tokens)
    if ele:
        tokens = remove_comments(ele).split()
        _ele(tokens)
    if poly:
        tokens = remove_comments(poly).split()
        tokens = _vertices(tokens)
        tokens = _segments(tokens)
        tokens = _holes(tokens)
        if tokens:
            _regions(tokens)
    if area:
        tokens = remove_comments(area).split()
        _area(tokens)
    if edge:
        _edge(remove_comments(edge))
    if neigh:
        tokens = remove_comments(neigh).split()
        _neigh(tokens)

    return data

def load(directory, name):
    """
    Load a dictionary representing the triangle data from `directory` and `name`.
    """

    data = {}
    for ext in ('node', 'ele', 'poly', 'area', 'edge', 'neigh'):
        filename = os.path.join(directory, name+'.'+ext)
        try:
            with open(filename) as f:
                data[ext]= f.read()
        except IOError:
            pass
    return loads(**data)

def get_data_dir():
    root = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(root, 'data')

def get_data(name):
    """
    Load data samples provided with the module.
    Examples: A, dots, ell, face, ...
    """
    return load(get_data_dir(), name)

def show_data(name):
    import triangle.plot as plot
    import matplotlib.pyplot as plt
    d = get_data(name)
    plot.plot(plt.axes(), **d)
    plt.show()
