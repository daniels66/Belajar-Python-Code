import numpy as np
import matplotlib.pyplot as plt

# 1. Membuat data (sin(2wt + theta))
def sinusGenerator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0, tAkhir, 0.1)
    y = amplitudo * np.sin(2 * frekuensi * t + np.deg2rad(theta))
    return t, y


# 2. Membuat plot
t1, y1 = sinusGenerator(1, 1, 4, 0)
t2, y2 = sinusGenerator(1, 1, 4, 90)

# 3. menambahkan legend dalam figure
# legend tipe pertama
# plt.plot(t1, y1, label="sin(0)")
# plt.plot(t2, y2, label="sin(90)")
# plt.legend()
"""
legend tipe pertama akan mencari secara otomatis posisi legend terbaik
"""

# legend tipe kedua
# plt.plot(t1, y1, label="sin(0)")
# plt.plot(t2, y2, label="sin(90)")
# plt.legend(loc="upper center")

# legend tipe ketiga
plt.plot(t1, y1, label="sin(0)")
plt.plot(t2, y2, label="sin(90)")
plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.02))
# plt.legend(loc="upper center", bbox_to_anchor=(0, 0))

# legend tipe keempat (advance)
# plt.figure(1)
# ax = plt.subplot(111)
# plt.plot(t1, y1, label="sin(0)")
# plt.plot(t2, y2, label="sin(90)")
# box = ax.get_position()
# ax.set_position([box.x0, box.y0, box.width * 0.7, box.height])
# plt.legend(loc="upper center", bbox_to_anchor=(1.2, 1))

# 4. Membuat label dan title
judul = "Grafik Sinusoidal"
plt.title(judul)

# membuat xlabel dan y label
plt.xlabel("waktu(detik)")
plt.ylabel("magnituda(cm)")

# 5. Menampilkan plot
plt.show()
