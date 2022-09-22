import numpy as np
import matplotlib.pyplot as plt

# 1. Membuat data (sin(2wt + theta))
def sinusGenerator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0, tAkhir, 0.1)
    y = amplitudo * np.sin(2 * frekuensi * t + np.deg2rad(theta))
    return t, y


# 2. Membuat plot
t, y = sinusGenerator(1, 1, 4, 0)

dataPlot = plt.plot(t, y)

plt.setp(
    dataPlot,
    marker=".",
    linestyle="-",
    color="r",
)

# 3. Set axis
"""
axis adalah nilai xmin, xmax, ymin, ymax dari suatu plot
plt.axis([xmin,xmax,ymin,ymax])
"""
plt.axis([0, 4, -1, 1])

# 4. Menampilkan plot
plt.show()
