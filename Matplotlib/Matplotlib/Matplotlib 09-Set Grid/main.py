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

# 4. Membuat Grid pada plot
#  plt.grid()
# plt.grid(axis="x") # akan membuat grid sumbu vertikal saja
# plt.grid(axis="y") # akan membuat grid sumbu horizontal saja
"""
selain hal diatas kita dapat set property dari grid
grid(color = 'color', linestyle = 'linestyle', linewidth = number).
"""
plt.grid(color="green", linestyle="--", linewidth=0.5)

# 5. Menampilkan plot
plt.show()
