import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 3, 0.3)
y1 = x
y2 = x**2
y3 = x**3

plt.plot(y1, color='red', linestyle='-')
plt.plot(y2, color='blue', linestyle=':')
plt.plot(y3, color='black', marker='o')
plt.show()