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

# 3. Membuat label dan title
judul = "Grafik Sinusoidal"
plt.title(judul)

# membuat xlabel dan y label
plt.xlabel("waktu(detik)")
plt.ylabel("magnituda(cm)")

# menambahkan text didalam plot
"""
untuk menambahkan text didalam plot menggunakan
plt.text(xposisi, yposisi, text yang diinginkan)
"""

plt.text(1.75, 0.5, r"$ y = \mathcal{A}.sin(2 \omega t)$")
plt.text(1.65, 0.4, r"$ \mathcal{A} = 1 cm, \omega = 1 Hz$")

# 4. Menampilkan plot
plt.show()
