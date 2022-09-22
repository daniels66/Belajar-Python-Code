import numpy as np
import matplotlib.pyplot as plt

# membuat lingkaran
PI = np.pi
sudut = np.linspace(0, 2 * PI, 100)
radius = 5

x = radius * np.cos(sudut)
y = radius * np.sin(sudut)

# inisialisasi plot
plt.plot(x, y)

# menampilkan plot
plt.show()
