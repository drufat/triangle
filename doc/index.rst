.. triangle documentation master file, created by
   sphinx-quickstart on Wed Jul  4 10:04:04 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to triangle's documentation!
====================================

.. toctree::
   :maxdepth: 2

**Triangle** is a wrapper around Jonathan Richard Shewchuk's two-dimensional quality mesh generator 
and delaunay triangulator, that is available `here <http://www.cs.cmu.edu/~quake/triangle.html>`_ .

Installation
=============

To install simply run::

	easy_install triangle

or build from source::

	git clone https://github.com/drufat/triangle.git
	cd triangle
	python setup.py install


API
====
So far the module only consists of a single function

.. autofunction:: triangle.triangulate

Examples
=========

Let us triangulate a simple square ::

	pts = array(((0,0), (1,0), (1, 1), (0, 1)))
	triangulate(pts)


.. plot:: 

	from triangle.plot import plot
	from numpy import *
	import matplotlib.pyplot as plt

	pts = array(((0,0), (1,0), (1, 1), (0, 1)))
	plot(plt, pts)
	plt.show()


In order to set maximum area of the triangles, we set the *maxarea* keyword ::

	triangulate(pts, maxarea=0.1)
		
.. plot:: 

	from triangle.plot import plot
	from numpy import *
	import matplotlib.pyplot as plt

	pts = array(((0,0), (1,0), (1, 1), (0, 1)))
	plot(plt, pts, maxarea=0.1)
	plt.show()

If we want to  decrease the area even further ::

	triangualte(pts, maxarea=0.01)
	
.. plot:: 

	from triangle.plot import plot
	from numpy import *
	import matplotlib.pyplot as plt

	pts = array(((0,0), (1,0), (1, 1), (0, 1)))
	plot(plt, pts, maxarea=0.01)
	plt.show()

To do the same with a circle ::

	from numpy import *

	theta = linspace(0, 2*pi, 33)[:-1]
	pts = vstack((cos(theta), sin(theta))).T
	triangulate(pts)
	

.. plot:: 

	from triangle.plot import plot
	from numpy import *
	import matplotlib.pyplot as plt

	theta = linspace(0, 2*pi, 33)[:-1]
	pts = vstack((cos(theta), sin(theta))).T
	plot(plt, pts)
	plt.show()


::

	triangulate(pts, maxarea=0.05)

.. plot:: 

	from triangle.plot import plot
	from numpy import *
	import matplotlib.pyplot as plt

	theta = linspace(0, 2*pi, 33)[:-1]
	pts = vstack((cos(theta), sin(theta))).T
	plot(plt, pts, maxarea=0.05)
	plt.show()
		

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

