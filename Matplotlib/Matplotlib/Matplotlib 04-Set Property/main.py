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
t2, y2 = sinusGenerator(1, 1, 4, 30)
t3, y3 = sinusGenerator(1, 1, 4, 60)

dataPlot1 = plt.plot(t1, y1)
dataPlot2 = plt.plot(t2, y2)
dataPlot3 = plt.plot(t3, y3)

"""
apabila ingin menentukan property plot (marker,line,colour) 
agar dapat mudah dipahami gunakan saja set property
plt.setp(plot,marker="",linesstyle="",linewidth="",color="")
"""

plt.setp(
    dataPlot1,
    marker="o",
    linestyle=":",
    color="r",
)
plt.setp(
    dataPlot2,
    marker="o",
    linestyle="-",
    color="g",
)
plt.setp(
    dataPlot3,
    marker="o",
    linestyle="-.",
    color="b",
)

# 3. Menampilkan plot
plt.show()

"""
untuk mengetahui market, line, color apa saja yang dapat dimasukkan,
kunjungi : 
https://www.w3schools.com/python/matplotlib_markers.asp,
https://www.w3schools.com/python/matplotlib_line.asp
"""
