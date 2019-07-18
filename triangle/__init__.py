__version__ = __import__('pkg_resources').get_distribution('triangle').version

from triangle.data import (
    loads, load, get_data, show_data,
)
from triangle.plot import (
    plot, comparev, compare,
)
from triangle.tri import (
    triangulate,
    convex_hull, delaunay, voronoi,
)
