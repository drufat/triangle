import triangle
import triangle.plot
import matplotlib.pyplot as plt

box1 = triangle.get_data('bbox.1')
box2 = triangle.triangulate(box1, 'rpa')
triangle.plot.plot(plt.axes(), **box2)
plt.show()
