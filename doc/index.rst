.. triangle documentation master file, created by
   sphinx-quickstart on Wed Jul  4 10:04:04 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Python Triangle
===============

*Python Triangle* is a python wrapper around Jonathan Richard Shewchuk's
two-dimensional quality mesh generator and delaunay triangulator library,
available `here <http://www.cs.cmu.edu/~quake/triangle.html>`_ . The
documentation and examples in the aforementioned site have been modified to
make them applicable to python, and working source code is also provided. 

.. toctree::
   :maxdepth: 2

   installing.rst
   definitions.rst
   quality.rst
   convex.rst
   delaunay.rst
   examples.rst
   refine.rst
   
API
===

.. autofunction:: triangle.triangulate

.. autofunction:: triangle.triangulate1

.. autofunction:: triangle.convex_hull

.. autofunction:: triangle.voronoi
    		
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

