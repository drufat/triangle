import numpy as np
import triangle.core as core

def _opts(kw):
    opts = 'Qz'
    if 'constrained' in kw:
        opts += 'p'
    if 'quality' in kw:
        opts += 'q'
        if 'minangle' in kw:
            opts += ('%.2f' % kw['minangle'])
    if 'maxarea' in kw:
        opts += ('a%.16f' % kw['maxarea'])
    if 'conforming' in kw:
        opts += 'L'
    return opts

def triangulate(pts, **kw):
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
    _in = dict(vertices=pts)
    _out = triangulate2(_in, **kw)
    return (_out['vertices'],
            _out['triangles'])

def triangulate1(vertices=None, vertex_markers=None,
                segments=None, segment_markers=None,
                holes=None, **kw):
    _in = dict(vertices=vertices, 
               segments=segments, 
               holes=holes)    
    if vertex_markers is not None:
        _in['vertex_markers']=vertex_markers
    if segment_markers is not None:
        _in['segment_markers']=segment_markers
    _out = triangulate2(_in, **kw)
    return (_out['vertices'],
            _out['triangles'])

def triangulate2(tri, **kw):

    mp = (('pointlist', 'vertices', 'double', 2),
          ('segmentlist', 'segments', 'int32', 2),
          ('holelist', 'holes', 'double', 2),
          ('trianglelist', 'triangles', 'int32', 3),
          ('pointmarkerlist', 'vertex_markers', 'int32', 1),
          ('segmentmarkerlist', 'segment_markers', 'int32', 1),)
    
    a = core.TriangulateIO()    
    for n0, n1, t, _ in mp:
        if n1 not in tri: continue
        value = np.array(tri[n1], dtype=t).flatten()
        setattr(a, n0, value)

    r = {}
    
    b = core.TriangulateIO()
    core.triang(_opts(kw), a, b)
    for n0, n1, _, d in mp:
        try:
            value = np.array(getattr(b, n0))
        except ValueError:
            continue
        r[n1] = value.reshape((-1,d))
    
    return r

def convex_hull(pts):
    """
    >>> pts = [[0, 0], [0, 1], [1, 1], [1, 0]]
    >>> convex_hull(pts)
    array([[3, 0],
           [2, 3],
           [1, 2],
           [0, 1]], dtype=int32)
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
    >>> pts = [[0, 0], [0, 1], [1, 1], [1, 0]]
    (array([[ 0.5,  0.5],
           [ 0.5,  0.5]]),
     array([[0, 1]], dtype=int32),
     array([0, 0, 1, 1], dtype=int32),
     array([[-1.,  0.],
           [ 0., -1.],
           [ 1.,  0.],
           [ 0.,  1.]]))
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
    filter = (e[:,1]!=-1)
    edges = e[filter]
    ray_origin = e[-filter][:,0]
    ray_direct = n[-filter]
    
    return p, edges, ray_origin, ray_direct

