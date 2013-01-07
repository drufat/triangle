import triangle
import triangle.plot as plot
import matplotlib.pyplot as plt

face = triangle.get_data('face')
t = triangle.triangulate(face, 'pq0D')
plot.plot(plt.axes(), **t)

plt.show()
