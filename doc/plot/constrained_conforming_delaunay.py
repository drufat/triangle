import triangle
import triangle.plot as plot
import matplotlib.pyplot as plt

A = triangle.get_data('A')
t = triangle.triangulate(A, 'pq0')
plot.plot(plt.axes(), **t)
plt.show()
