import numpy as np
import matplotlib.pyplot as plt

"""
	1. Membuat data
	2. Membuat plot
	3. Menampilkan plot
"""

# 1. Membuat data (sin(2wt + theta))
def sinusGenerator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0, tAkhir, 0.1)
    y = amplitudo * np.sin(2 * frekuensi * t + np.deg2rad(theta))
    return t, y


# 2. Membuat plot
t1, y1 = sinusGenerator(1, 1, 4, 0)
plt.plot(t1, y1)

t2, y2 = sinusGenerator(1, 1, 4, 30)
plt.plot(t2, y2, "r")

t3, y3 = sinusGenerator(1, 1, 4, 60)
plt.plot(t3, y3, "b--")

t4, y4 = sinusGenerator(1, 1, 4, 90)
plt.plot(t4, y4, "o:r")

"""
format untuk plot yaitu
marker|line|colour
"""
# 3. Menampilkan plot
plt.show()

"""
untuk mengetahui market, line, colour apa saja yang dapat dimasukkan,
kunjungi : https://www.w3schools.com/python/matplotlib_markers.asp
"""
