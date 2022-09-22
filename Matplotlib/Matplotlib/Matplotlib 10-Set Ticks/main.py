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

# 4. Menganti nilai min dan max pada ticks
plt.yticks([-1, 0, 1])
plt.xticks([0, 1, 2, 3, 4])

# 5. Menampilkan plot
plt.show()
