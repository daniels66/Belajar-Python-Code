# subplot adalah menampilkan beberapa plot dalam satu figure
import matplotlib.pyplot as plt
import numpy as np

# 1. Membuat data (sin(2wt + theta)) plot 1
def sinusGenerator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0, tAkhir, 0.1)
    y = amplitudo * np.sin(2 * frekuensi * t + np.deg2rad(theta))
    return t, y


# 2. Membuat plot 1
t, y1 = sinusGenerator(1, 1, 4, 0)

plt.subplot(2, 1, 1)
dataPlot = plt.plot(t, y1)
"""
plt.subplot diletakkan plot (plt.plot)
plt.subplot meminta 3 parameter yaitu
plt.subplot(1, 2, 1)
gambar memiliki 1 baris, 2 kolom, dan subplot terletak pada nomor 1 dari kiri.
"""
plt.setp(
    dataPlot,
    marker=".",
    linestyle="-",
    color="r",
)

ax = plt.gca()  # gca = get current axis
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")

# 3. Membuat label
# membuat xlabel dan y label 1
plt.xlabel("waktu(detik)")
plt.ylabel("magnituda(cm)")

# 4. Menganti nilai min dan max pada ticks 1
plt.yticks([-1, 0, 1])
plt.xticks([0, 1, 2, 3, 4])


# 1. membuat data plot 2
sudut = np.arange(0, 360, 1)
y2 = np.sin(np.deg2rad(sudut))


# 2. membuat plot 2
plt.subplot(2, 1, 2)
plt.plot(sudut, y2)
plt.text(190, 1, "magnituda")
plt.text(360, 0.1, "sudut")
plt.yticks([-1, -0.5, 0, 0.5, 1])
plt.xticks(
    [0, 90, 180, 270, 360],
    [r"${0}^o$", r"${90}^o$", r"${180}^o$", r"${270}^o$", r"${360}^o$"],
)


ax = plt.gca()  # gca = get current axis
ax.spines["left"].set_position(("data", 180))
ax.spines["bottom"].set_position(("data", 0))
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")


# tampilkan plot 1 dan plot 2
"""
super title (plt.suptitle) yaitu title utama dalam supplot
"""
plt.suptitle("Grafik Sinusoidal")
"""
plt.tight_layout digunakan agar setiap plot memiliki jarak yang sesuai
"""
plt.tight_layout()
plt.show()
