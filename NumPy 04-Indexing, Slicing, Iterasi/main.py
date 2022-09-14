# indexing, slicing, iterasi
import numpy as np

a = np.arange(10) ** 2
print(a)

# indexing array numpy
print("nilai ke 1 dari array a = ", a[0])
print("nilai ke 6 dari array a = ", a[5])

# slicing array numpy
print("ambil nilai 2 hingga nilai 6 = ", a[1:6])  # (start:end)
print("ambil nilai awal hingga nilai 6 = ", a[:6])
print("ambil nilai dari 4 hingga akhir = ", a[4:])

# iterasi atau looping array
number = 0
for e in a:
    print(f"element ke {number} dari array a = {e}")
    number += 1
