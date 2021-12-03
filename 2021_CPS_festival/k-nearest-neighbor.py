import numpy as numpy
import matplotlib.pyplot as plt

plt.scatter(1.2, 1.1)   # group A
plt.scatter(1.0, 1.0)

plt.scatter(1.8, 0.8)   # group B
plt.scatter(2, 0.9)

plt.scatter(1.6, 0.85, color='r')   # target 
plt.show()

# DATA creation, function def
p1 = [1.2, 1.1]
p2 = [1.0, 1.0]
p3 = [1.8, 0.8]
p4 = [2, 0.9]
category = ['A', 'A', 'B', 'B']