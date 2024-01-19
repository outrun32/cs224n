import numpy as np

a = np.ones((10, 3))
b = np.ones((3, ))

c = np.dot(a, b)
print(c, c.shape)