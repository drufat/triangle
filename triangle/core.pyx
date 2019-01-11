from libc.stdlib cimport malloc, free
from libc.string cimport memcpy
import numpy as np

cdef extern from "triangle.h":

    cdef struct triangulateio:

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

cdef array_i(int N, int* p):
    if p and N:
        return <int[:N]> p

cdef array_d(int N, double* p):
    if p and N:
        return <double[:N]> p

cdef replace_i(int** pA, int[:] B):
    if pA[0]:
        free(pA[0])
    pA[0] = <int*>malloc(sizeof(int)*B.size)
    memcpy(pA[0], &(B[0]), sizeof(int)*B.size)

cdef replace_d(double** pA, double[:] B):
    # Free memory before overwriting pointer
    if pA[0]:
        free(pA[0])
    # Allocate new memory
    pA[0] = <double*>malloc(sizeof(double)*B.size)
    # Copy array in B to pA
    memcpy(pA[0], &(B[0]), sizeof(double)*B.size)

cdef copy_d(double** pA, int N):
    # Allocate new memory
    cdef double* t = pA[0]
    pA[0] = <double*>malloc(sizeof(double)*N)
    # Copy array
    memcpy(pA[0], t, sizeof(double)*N)

cdef cleanup(void** pp):
    if pp[0]:
        free(pp[0])
    pp[0] = NULL

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

cdef dealloc(triangulateio *c):
    cleanup(<void**>&c.pointlist)
    cleanup(<void**>&c.pointattributelist)
    cleanup(<void**>&c.pointmarkerlist)

    cleanup(<void**>&c.trianglelist)
    cleanup(<void**>&c.triangleattributelist)
    cleanup(<void**>&c.trianglearealist)
    cleanup(<void**>&c.neighborlist)

    cleanup(<void**>&c.segmentlist)
    cleanup(<void**>&c.segmentmarkerlist)

    cleanup(<void**>&c.holelist)
    cleanup(<void**>&c.regionlist)

    cleanup(<void**>&c.edgelist)
    cleanup(<void**>&c.edgemarkerlist)
    cleanup(<void**>&c.normlist)

_fields = (

    ('pointlist', 'double', 2),
    ('pointattributelist', 'double', 1),
    ('pointmarkerlist', 'intc', 1),

    ('trianglelist', 'intc', 3),
    # ('triangleattributelist', 'double', numberoftriangleattributes),
    ('trianglearealist', 'double', 1),
    ('neighborlist', 'double', 1),

    ('segmentlist', 'intc', 2),
    ('segmentmarkerlist', 'intc', 1),

    ('holelist', 'double', 2),

    ('regionlist', 'double', 4),

    ('edgelist', 'intc', 2),
    ('edgemarkerlist', 'intc', 1),
    ('normlist', 'double', 2),

)

fields = {_0: (_1, _2) for _0, _1, _2 in _fields}

cdef class TriangulateIO:

    cdef triangulateio c

    def __cinit__(self):
        cinit(&self.c)

    def __dealloc__(self):
        dealloc(&self.c)

    property pointlist:
        def __get__(self):
            return array_d(self.c.numberofpoints*2, self.c.pointlist)
        def __set__(self, double[:] value):
            replace_d(&self.c.pointlist, value)
            self.c.numberofpoints = value.size / 2

    property pointattributelist:
        def __get__(self):
            return array_d(self.c.numberofpoints*self.c.numberofpointattributes, self.c.pointattributelist)
        def __set__(self, double[:] value):
            assert value.size == self.c.numberofpoints
            replace_d(&self.c.pointattributelist, value)

    property pointmarkerlist:
        def __get__(self):
            return array_i(self.c.numberofpoints, self.c.pointmarkerlist)
        def __set__(self, int[:] value):
            assert value.size == self.c.numberofpoints
            replace_i(&self.c.pointmarkerlist, value)

    property trianglelist:
        def __get__(self):
            return array_i(self.c.numberoftriangles*self.c.numberofcorners, self.c.trianglelist)
        def __set__(self, int[:] value):
            replace_i(&self.c.trianglelist, value)
            self.c.numberofcorners = 3
            self.c.numberoftriangles = value.size/self.c.numberofcorners

    property triangleattributelist:
        def __get__(self):
            return array_d(self.numberoftriangles*self.c.numberoftriangleattributes, self.c.triangleattributelist)
        def __set__(self, double[:] value):
            assert value.size == self.c.numberoftriangles*self.c.numberoftriangleattributes
            replace_d(&self.c.triangleattributelist, value)

    property trianglearealist:
        def __get__(self):
            return array_d(self.c.numberoftriangles, self.c.trianglearealist)
        def __set__(self, double[:] value):
            assert value.size == self.c.numberoftriangles
            replace_d(&self.c.trianglearealist, value)

    property neighborlist:
        def __get__(self):
            return array_i(self.c.numberoftriangles*3, self.c.neighborlist)
        def __set__(self, int[:] value):
            assert value.size == self.c.numberoftriangles*3
            replace_i(&self.c.neighborlist, value)

    property numberoftriangles:
        def __get__(self):
            return self.c.numberoftriangles
        def __set__(self, int value):
            self.c.numberoftriangles = value

    property numberofcorners:
        def __get__(self):
            return self.c.numberofcorners
        def __set__(self, int value):
            self.c.numberofcorners = value

    property numberoftriangleattributes:
        def __get__(self):
            return self.c.numberoftriangleattributes
        def __set__(self, int value):
            self.c.numberoftriangleattributes = value

    property segmentlist:
        def __get__(self):
            return array_i(self.c.numberofsegments*2, self.c.segmentlist)
        def __set__(self, int[:] value):
            replace_i(&self.c.segmentlist, value)
            self.c.numberofsegments = value.size/2

    property segmentmarkerlist:
        def __get__(self):
            return array_i(self.c.numberofsegments, self.c.segmentmarkerlist)
        def __set__(self, int[:]  value):
            assert value.size == self.c.numberofsegments
            replace_i(&self.c.segmentmarkerlist, value)

    property holelist:
        def __get__(self):
            return array_d(self.c.numberofholes*2, self.c.holelist)
        def __set__(self, double[:]  value):
            replace_d(&self.c.holelist, value)
            self.c.numberofholes = value.size/2

    property regionlist:
        def __get__(self):
            return array_d(self.c.numberofregions*4, self.c.regionlist)
        def __set__(self, double[:]  value):
            replace_d(&self.c.regionlist, value)
            self.c.numberofregions = value.size/4

    property edgelist:
        def __get__(self):
            return array_i(self.c.numberofedges*2, self.c.edgelist)
        def __set__(self, int[:] value):
            replace_i(&self.c.edgelist, value)
            self.c.numberofedges = value.size/2

    property edgemarkerlist:
        def __get__(self):
            return array_i(self.c.numberofedges, self.c.edgemarkerlist)
        def __set__(self, int[:] value):
            assert self.c.numberofedges == value.size
            replace_i(&self.c.edgelist, value)

    property normlist:
        def __get__(self):
            return array_d(self.c.numberofedges*2, self.c.normlist)
        def __set__(self, double[:] value):
            assert self.c.numberofedges == value.size
            replace_d(&self.c.normlist, value)/2


def fin(tri):
    rslt = TriangulateIO()
    for name in tri:
        t, d = fields[name]
        value = np.array(tri[name], dtype=t)
        assert value.shape[1] == d
        value = value.flatten()
        setattr(rslt, name, value)
    return rslt


def fout(tri):
    rslt = {}
    for name in fields:
        t, d = fields[name]
        arr = getattr(tri, name)
        if arr:
            arr = np.array(arr)
            assert arr.dtype == t
            rslt[name] = arr.reshape((-1, d))
    return rslt


def triang(_in, opts):

    if ('pointlist' not in _in) or (len(_in['pointlist']) < 3):
        raise ValueError('Input must have at least three input vertices.')

    opts = opts.encode('utf-8')

    cdef TriangulateIO in_ = fin(_in)
    cdef TriangulateIO out_ = TriangulateIO()
    cdef TriangulateIO vorout_ = TriangulateIO()

    triangulate(opts, &in_.c, &out_.c, &vorout_.c)
    # Copy whole array to avoid freeing of non-allocated pointers
    copy_d(&(out_.c.holelist), out_.c.numberofholes * 2)
    copy_d(&(out_.c.regionlist), out_.c.numberofregions * 4)

    _out = fout(out_)
    _vorout = fout(vorout_)

    return _out, _vorout
