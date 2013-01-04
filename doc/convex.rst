Convex hulls and mesh boundaries
================================
If the input is a vertex set (rather than a PSLG), Triangle produces its convex
hull as a by-product in the output .poly file if you use the -c switch. There
are faster algorithms for finding a two-dimensional convex hull than
triangulation, of course, but this one comes for free. In the example below,
the file dots.node is read, and its convex hull produced in dots.1.poly.

.. plot:: plot/convex_hull.py



