import triangle
import triangle.plot
import matplotlib.pyplot as plt

box1 = triangle.get_data('bbox.1')
box2 = triangle.triangulate(box1, 'rpaa.5')
triangle.plot.plot(plt.axes(), **box2)
plt.show()
