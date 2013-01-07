.. triangle documentation master file, created by
   sphinx-quickstart on Wed Jul  4 10:04:04 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Python Triangle
===============

*Python Triangle* is a python wrapper around Jonathan Richard Shewchuk's
two-dimensional quality mesh generator and delaunay triangulator library,
available `here <http://www.cs.cmu.edu/~quake/triangle.html>`_. 

.. toctree::
   :maxdepth: 2

   installing.rst
   definitions.rst
   delaunay.rst
   quality.rst
   refine.rst
   convex.rst
   voronoi.rst
   examples.rst
   data.rst
   
API
===

.. autofunction:: triangle.convex_hull

.. autofunction:: triangle.delaunay

.. autofunction:: triangle.voronoi

.. autofunction:: triangle.triangulate

.. autofunction:: triangle.loads

.. autofunction:: triangle.load

.. autofunction:: triangle.get_data
    		
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

