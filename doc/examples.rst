Additional Examples
====================

Let us triangulate a simple square::

	pts = array(((0,0), (1,0), (1, 1), (0, 1)))
	triangulate(pts)

.. plot:: plot/ex1.py

In order to set maximum area of the triangles, we set the *maxarea* keyword::

	triangulate(pts, maxarea=0.1)
		
.. plot:: plot/ex2.py

If we want to  decrease the area even further::

	triangulate(pts, maxarea=0.01)
	
.. plot:: plot/ex3.py

To do the same with a circle::

	from numpy import *

	theta = linspace(0, 2*pi, 33)[:-1]
	pts = vstack((cos(theta), sin(theta))).T
	triangulate(pts, quality=True)
	
.. plot:: plot/ex4.py

::

	triangulate(pts, quality=True, maxarea=0.05)

.. plot:: plot/ex5.py
