from libc.stdlib cimport malloc, free
from libc.string cimport memcpy
cimport c_triangle as ct

cdef replace_d(double** pA, double[:] B):
    # Free memory before overwriting pointer
    if pA[0]: free(pA[0])
    # Allocate new memory
    pA[0] = <double*>malloc(sizeof(double)*B.size)
    # Copy array in B to pA
    memcpy(pA[0], &(B[0]), sizeof(double)*B.size)

cdef replace_i(int** pA, int[:] B):
    if pA[0]: free(pA[0])
    pA[0] = <int*>malloc(sizeof(int)*B.size)
    memcpy(pA[0], &(B[0]), sizeof(int)*B.size)

cdef copy_d(double** pA, int N):
    # Allocate new memory
    cdef double* t = pA[0]
    pA[0] = <double*>malloc(sizeof(double)*N)
    # Copy array
    memcpy(pA[0], t, sizeof(double)*N)

cdef cleanup(void** pA):
    if pA[0]: free(pA[0])
    pA[0] = NULL

cdef class TriangulateIO:

    cdef ct.triangulateio c

    property pointlist:
        def __get__(self):
            return <double[:self.c.numberofpoints*2]> self.c.pointlist
        def __set__(self, double[:] value):
            replace_d(&(self.c.pointlist), value)
            self.c.numberofpoints = value.size / 2

    property pointattributelist:
        def __get__(self):
            return <double[:self.c.numberofpointattributes]> self.c.pointattributelist
        def __set__(self, double[:] value):
            assert value.size == self.c.numberofpoints
            replace_d(&(self.c.pointattributelist), value)

    property pointmarkerlist:
        def __get__(self):
            return <int[:self.c.numberofpoints]> self.c.pointmarkerlist
        def __set__(self, int[:] value):
            assert value.size == self.c.numberofpoints
            replace_i(&(self.c.pointmarkerlist), value)

    property trianglelist:
        def __get__(self):
            return <int[:self.c.numberoftriangles*self.c.numberofcorners]> self.c.trianglelist
        def __set__(self, int[:] value):
            replace_i(&(self.c.trianglelist), value)
            self.c.numberofcorners = 3
            self.c.numberoftriangles = value.size/self.c.numberofcorners

    property triangleattributelist:
        def __get__(self):
            return <double[:self.numberoftriangles*self.c.numberoftriangleattributes]> self.c.triangleattributelist
        def __set__(self, double[:] value):
            assert value.size == self.c.numberoftriangles*self.c.numberoftriangleattributes
            replace_d(&(self.c.triangleattributelist), value)

    property trianglearealist:
        def __get__(self):
            return <double[:self.c.numberoftriangleattributes]> self.c.trianglearealist
        def __set__(self, double[:] value):
            assert value.size == self.c.numberoftriangles
            replace_d(&(self.c.trianglearealist), value)

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

    property neighborlist:
        def __get__(self):
            return <double[:self.c.numberoftriangleattributes]> self.c.triangleattributelist
        def __set__(self, double[:] value):
            assert value.size == self.c.numberoftriangles
            replace_d(&(self.c.triangleattributelist), value)

    property segmentlist:
        def __get__(self):
            return <int[:self.c.numberofsegments*2]> self.c.segmentlist
        def __set__(self, int[:] value):
            replace_i(&(self.c.segmentlist), value)
            self.c.numberofsegments = value.size/2

    property segmentmarkerlist:
        def __get__(self):
            return <int[:self.c.numberofsegments]> self.c.segmentmarkerlist
        def __set__(self, int[:]  value):
            assert value.size == self.c.numberofsegments
            replace_i(&(self.c.segmentmarkerlist), value)

    property holelist:
        def __get__(self):
            return <double[:self.c.numberofholes*2]> self.c.holelist
        def __set__(self, double[:]  value):
            replace_d(&(self.c.holelist), value)
            self.c.numberofholes = value.size/2

    property regionlist:
        def __get__(self):
            return <double[:self.c.numberofregions*4]> self.c.regionlist
        def __set__(self, double[:]  value):
            replace_d(&(self.c.regionlist), value)
            self.c.numberofregions = value.size/4

    property edgelist:
        def __get__(self):
            return <int[:self.c.numberofedges*2]> self.c.edgelist
        def __set__(self, int[:] value):
            replace_i(&(self.c.edgelist), value)
            self.c.numberofedges = value.size/2

    property edgemarkerlist:
        def __get__(self):
            return <int[:self.c.numberofedges]> self.c.edgemarkerlist
        def __set__(self, int[:] value):
            assert self.c.numberofedges == value.size
            replace_i(&(self.c.edgelist), value)

    property normlist:
        def __get__(self):
            return <double[:self.c.numberofedges*2]> self.c.normlist
        def __set__(self, double[:] value):
            assert self.c.numberofedges == value.size
            replace_d(&(self.c.normlist), value)/2

    def __cinit__(self):
        self.c.pointlist = NULL
        self.c.pointattributelist = NULL
        self.c.pointmarkerlist = NULL
        self.c.numberofpoints = 0
        self.c.numberofpointattributes = 0

        self.c.trianglelist = NULL
        self.c.triangleattributelist = NULL
        self.c.trianglearealist = NULL
        self.c.neighborlist = NULL
        self.c.numberoftriangles = 0
        self.c.numberofcorners = 0
        self.c.numberoftriangleattributes = 0

        self.c.segmentlist = NULL
        self.c.segmentmarkerlist = NULL
        self.c.numberofsegments = 0

        self.c.holelist = NULL
        self.c.numberofholes = 0

        self.c.regionlist = NULL
        self.c.numberofregions = 0

        self.c.edgelist = NULL
        self.c.edgemarkerlist = NULL
        self.c.normlist = NULL
        self.c.numberofedges = 0

    def __dealloc__(self):
        cleanup(<void**>&(self.c.pointlist))
        cleanup(<void**>&(self.c.pointattributelist))
        cleanup(<void**>&(self.c.pointmarkerlist))

        cleanup(<void**>&(self.c.trianglelist))
        cleanup(<void**>&(self.c.triangleattributelist))
        cleanup(<void**>&(self.c.trianglearealist))
        cleanup(<void**>&(self.c.neighborlist))

        cleanup(<void**>&(self.c.segmentlist))
        cleanup(<void**>&(self.c.segmentmarkerlist))

        cleanup(<void**>&(self.c.holelist))
        cleanup(<void**>&(self.c.regionlist))

        cleanup(<void**>&(self.c.edgelist))
        cleanup(<void**>&(self.c.edgemarkerlist))
        cleanup(<void**>&(self.c.normlist))

def triang(switch, in_, out_, vorout=None):
    __triang(switch.encode('utf-8'), in_, out_, vorout)

def __triang(char* switch, TriangulateIO in_, TriangulateIO out_, vorout=None):
    cdef TriangulateIO vorout_
    if vorout:
        vorout_ = vorout
        ct.triangulate(switch, &in_.c, &out_.c, &(vorout_.c))
    else:
        ct.triangulate(switch, &in_.c, &out_.c, NULL)
    # Copy whole array to avoid freeing of non-allocated pointers
    copy_d(&(out_.c.holelist), out_.c.numberofholes*2)
    copy_d(&(out_.c.regionlist), out_.c.numberofregions*4)
