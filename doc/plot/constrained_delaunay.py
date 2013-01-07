import triangle
import triangle.plot as plot
import matplotlib.pyplot as plt

ax = plt.axes()
A = triangle.get_data('A')
t = triangle.triangulate(A, 'p')
plot.plot(ax, **t)
plt.show()
