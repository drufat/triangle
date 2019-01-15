from libc.stdlib cimport free
import numpy as np


cdef extern from "triangle.h":

    struct triangulateio:

        double *pointlist
        double *pointattributelist
        int *pointmarkerlist
        int numberofpoints
        int numberofpointattributes

        int *trianglelist
        double *triangleattributelist
        double *trianglearealist
        int *neighborlist
        int numberoftriangles
        int numberofcorners
        int numberoftriangleattributes

        int *segmentlist
        int *segmentmarkerlist
        int numberofsegments

        double *holelist
        int numberofholes

        double *regionlist
        int numberofregions

        int *edgelist
        int *edgemarkerlist
        double *normlist
        int numberofedges

    void triangulate(
        char *triswitches,
        triangulateio *in_,
        triangulateio *out_,
        triangulateio *vorout
    )


cdef array_ii(int N, int M, int* p):
    if p and N and M:
        return <int[:N, :M]>p


cdef array_dd(int N, int M, double* p):
    if p and N and M:
        return <double[:N, :M]>p


cdef int* ptr_ii(int[:, ::1] arr):
    return &arr[0, 0]


cdef double* ptr_dd(double[:, ::1] arr):
    return &arr[0, 0]


cdef ii(int* _0, int* _1, int** pdata, check, free_):

    def _get():
        return array_ii(_0[0], _1[0], pdata[0])

    def _set(v):
        data = ptr_ii(v)
        pdata[0] = data
        _0[0], _1[0] = v.shape
        check()

    def _free():
        if free_:
            if pdata[0]:
                free(pdata[0])
            pdata[0] = NULL

    return _get, _set, _free


cdef dd(int* _0, int* _1, double** pdata, check, free_):

    def _get():
        return array_dd(_0[0], _1[0], pdata[0])

    def _set(v):
        data = ptr_dd(v)
        pdata[0] = data
        _0[0], _1[0] = v.shape
        check()

    def _free():
        if free_:
            if pdata[0]:
                free(pdata[0])
            pdata[0] = NULL


    return _get, _set, _free


fields = (
    ('pointlist', 'double'),
    ('pointattributelist', 'double'),
    ('pointmarkerlist', 'intc'),

    ('trianglelist', 'intc'),
    ('triangleattributelist', 'double'),
    ('trianglearealist', 'double'),
    ('neighborlist', 'double'),

    ('segmentlist', 'intc'),
    ('segmentmarkerlist', 'intc'),

    ('holelist', 'double'),
    ('regionlist', 'double'),

    ('edgelist', 'intc'),
    ('edgemarkerlist', 'intc'),
    ('normlist', 'double'),
)


cdef _wrap(triangulateio* c):

    cdef int _1 = 1
    cdef int _2 = 2
    cdef int _3 = 3
    cdef int _4 = 4

    def check():
        assert _1 == 1
        assert _2 == 2
        assert _3 == 3
        assert _4 == 4

    return (
        dd(&c.numberofpoints, &_2, &c.pointlist, check, True),
        dd(&c.numberofpoints, &c.numberofpointattributes, &c.pointattributelist, check, True),
        ii(&c.numberofpoints, &_1, &c.pointmarkerlist, check, True),

        ii(&c.numberoftriangles, &c.numberofcorners, &c.trianglelist, check, True),
        dd(&c.numberoftriangles, &c.numberoftriangleattributes, &c.triangleattributelist, check, True),
        dd(&c.numberoftriangles, &_1, &c.trianglearealist, check, True),
        ii(&c.numberoftriangles, &_3, &c.neighborlist, check, True),

        ii(&c.numberofsegments, &_2, &c.segmentlist, check, True),
        ii(&c.numberofsegments, &_1, &c.segmentmarkerlist, check, True),

        dd(&c.numberofholes, &_2, &c.holelist, check, False),

        dd(&c.numberofregions, &_4, &c.regionlist, check, False),

        ii(&c.numberofedges, &_2, &c.edgelist, check, True),
        ii(&c.numberofedges, &_1, &c.edgemarkerlist, check, True),
        dd(&c.numberofedges, &_2, &c.normlist, check, True),
    )


cdef cinit(triangulateio *c):
    c.pointlist = NULL
    c.pointattributelist = NULL
    c.pointmarkerlist = NULL
    c.numberofpoints = 0
    c.numberofpointattributes = 0

    c.trianglelist = NULL
    c.triangleattributelist = NULL
    c.trianglearealist = NULL
    c.neighborlist = NULL
    c.numberoftriangles = 0
    c.numberofcorners = 0
    c.numberoftriangleattributes = 0

    c.segmentlist = NULL
    c.segmentmarkerlist = NULL
    c.numberofsegments = 0

    c.holelist = NULL
    c.numberofholes = 0

    c.regionlist = NULL
    c.numberofregions = 0

    c.edgelist = NULL
    c.edgemarkerlist = NULL
    c.normlist = NULL
    c.numberofedges = 0


cdef wrap(triangulateio* c):
    rslt = []
    for field, accessor in zip(fields, _wrap(c)):
        name, dtype = field
        _get, _set, _free = accessor
        rslt.append((name, dtype, _get, _set, _free))
    return rslt


def contig2d(value, dtype):
    value = np.ascontiguousarray(value, dtype=dtype)
    if len(value.shape) == 1:
        value = value.reshape((value.shape[0], 1))
    return value


cdef fin_(d, triangulateio* c):
    for name, dtype, _get, _set, _free in wrap(c):
        if name not in d:
            continue
        value = contig2d(d[name], dtype)
        _set(value)


cdef fout_(triangulateio* c, d):
    for name, dtype, _get, _set, _free in wrap(c):
        arr = _get()
        if arr:
            d[name] =  np.array(arr)
            _free()


def triang(_in, opts):

    if ('pointlist' not in _in) or (len(_in['pointlist']) < 3):
        raise ValueError('Input must have at least three vertices.')

    opts = opts.encode('utf-8')

    cdef triangulateio in_
    cdef triangulateio out_
    cdef triangulateio vorout_

    cinit(&in_)
    cinit(&out_)
    cinit(&vorout_)

    fin_(_in, &in_)

    triangulate(opts, &in_, &out_, &vorout_)

    _out, _vorout = {}, {}
    fout_(&out_, _out)
    fout_(&vorout_, _vorout)

    return _out, _vorout
