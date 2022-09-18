# visualisasi distribusi data array
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""
untuk visualisasi distribusi data array perlu tambahan package,
yaitu seaborn (pip install seaborn) dan 
matplotlib (pip install matplotlib)
"""

a = np.array([1, 2, 3, 4, 5])
plt.figure(1)
sns.distplot(a)
"""
distplot adalah distribusi plot yang dibutuhkan sebagai input array 
dan plot kurva yang sesuai dengan distribusi titik dalam array.
"""
plt.show()

plt.figure(2)
sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()

"""
apabila terjadi eror
UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, 
so cannot show the figure.
pada terminal ketik pip install pyqt5
"""
