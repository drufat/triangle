import triangle
from triangle.plot import plot
import matplotlib.pyplot as plt

A = triangle.get_data('A')
ax = plt.axes()
plot(ax, **A)
plt.show()
