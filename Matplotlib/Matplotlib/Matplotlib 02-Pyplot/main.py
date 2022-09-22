import numpy as np
import matplotlib.pyplot as plt

# mengenal lebih dalam cara membuat plot
"""
untuk membuat plot diperlukan
1. membuat data terlebih dahulu
2. membuat plot
3. menampilkan plot
"""

# 1. membuat data
x = np.array([1, 2, 3, 4, 5])
y1 = np.array(x**2)
y2 = np.array(y1**2)

# 2. membuat plot
plt.plot(x, y1)
plt.plot(x, y2)

# 3. menampilkan plot
plt.show()
