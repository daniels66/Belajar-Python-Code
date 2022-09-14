# array pada package numpy
import numpy as np

# list python
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

# array numpy
anp = np.array([1, 2, 3, 4, 5])
bnp = np.array([6, 7, 8, 9, 10])

# operasi aritmatika pada array (+ - * / **)
# penjumlahan
hasil_jumlah = a + b  # akan menambahkan dibelakang list pertama
hasil_jumlah_np = anp + bnp  # akan ditambah setiap element

# pengurangan
# hasil_kurang = a - b  # akan eror
hasil_kurang_np = anp - bnp  # akan dikurangi setiap element

# perkalian
# hasil_kali = a * b  # akan eror
hasil_kali_np = anp * bnp  # akan dikali setiap element

# pembagian
# hasil_bagi = a / b  # akan eror
hasil_bagi_np = anp / bnp  # akan dibagi setiap element

# pembagian
# hasil_pangkat = a**2  # akan eror
hasil_pangkat_np = anp**2  # akan dipangkat setiap element

# menampilkan hasil
print(hasil_jumlah)
print(hasil_jumlah_np)
print(hasil_kurang_np)
print(hasil_kali_np)
print(hasil_bagi_np)
print(hasil_pangkat_np)

# array multi dimensi
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[7, 8, 9], [-1, -2, -3]])

hasil_matrix = c + d
print(hasil_matrix)
hasil_matrix = c * d
print(
    hasil_matrix
)  # hanya dilakukan perkalian setiap element, buka perkalian matrix yang sebenarnya
