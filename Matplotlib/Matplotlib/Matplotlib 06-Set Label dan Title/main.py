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

# set font properti untuk title dan label
font1 = {"family": "serif", "color": "blue", "size": 15}
font2 = {"family": "serif", "color": "purple", "size": 12}

judul = "Grafik Sinusoidal"
plt.title(judul, fontdict=font1, loc="left")  # untuk membuat judul dari plot

# membuat xlabel dan y label
plt.xlabel("waktu(detik)", fontdict=font2)
plt.ylabel("magnituda(cm)", fontdict=font2)

# 4. Menampilkan plot
plt.show()

"""
apabila ingin menuliskan judul dengan adanya simbol matematika, 
lihat dokumetasinya di 
https://matplotlib.org/stable/tutorials/text/mathtext.html
"""
