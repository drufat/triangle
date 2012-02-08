/*
 *  triangle_ext.c
 *  
 *
 *  Created by Dzhelil Rufat on Dec 26, 2009.
 *  Copyright 2009. All rights reserved.
 *
 */

#include <Python.h>
#include <numpy/arrayobject.h>

#define VOID void
#define REAL double
#define ANSI_DECLARATORS
#include "triangle.h"

static PyObject *
triangle_triangulate(PyObject *self, PyObject *args)
{
    PyObject *pts;
    char *opts;
    PyObject *R;

    if (!PyArg_ParseTuple(args, "Os", &pts, &opts))
        return NULL;

    pts = PyArray_ContiguousFromObject(pts, PyArray_DOUBLE, 2, 2);
    if (pts == NULL)
        return NULL;
    if (((PyArrayObject *)pts)->dimensions[1] != 2)
        return NULL;

    PyObject *PTS, *TR;

    {
        // call the triangle library
        struct triangulateio in, out;
        in.numberofpoints = ((PyArrayObject *)pts)->dimensions[0];
        in.numberofpointattributes = 0;
        in.pointlist = PyMem_New(REAL, 2*in.numberofpoints);
        memcpy(in.pointlist,
               ((PyArrayObject *)pts)->data,
               2*in.numberofpoints*sizeof(REAL));
        Py_DECREF(pts);

        in.pointmarkerlist = PyMem_New(int, in.numberofpoints);
        {
            int i;
            for (i=0; i<in.numberofpoints; ++i)
                in.pointmarkerlist[i] = 0;
        }

        in.numberofsegments = 0;
        in.numberofholes = 0;
        in.numberofregions = 0;

        out.pointlist = (REAL *) NULL;
        out.pointmarkerlist = (int *) NULL;
        out.trianglelist = (int *) NULL;

        triangulate(opts, &in, &out, NULL);

        {
            npy_intp dims[2] = { out.numberofpoints, 2 };
            PTS = PyArray_SimpleNew(2, dims, NPY_DOUBLE);
            memcpy(((PyArrayObject *)PTS)->data,
                   out.pointlist,
                   dims[0]*dims[1]*sizeof(REAL));
        }

        {
            npy_intp dims[2] = {out.numberoftriangles, 3};
            TR = PyArray_SimpleNew(2, dims, NPY_INT);
            memcpy(((PyArrayObject *)TR)->data,
                   out.trianglelist,
                   dims[0]*dims[1]*sizeof(NPY_INT));
        }

        PyMem_Free(in.pointlist);
        PyMem_Free(in.pointmarkerlist);
        free(out.pointlist);
        free(out.pointmarkerlist);
        free(out.trianglelist);
    }

    return Py_BuildValue("NN", PTS, TR);
};

static PyMethodDef triangleMethods[] = {
    {"triangulate", triangle_triangulate, METH_VARARGS, ""},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC
initcore(void)
{
    PyObject *m;
    Py_InitModule((char*)"core", triangleMethods);

    // REQUIRED FOR NUMPY TO WORK CORRECTLY
    import_array();
}
