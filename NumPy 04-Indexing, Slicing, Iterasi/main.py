# indexing, slicing, iterasi
import numpy as np

a = np.arange(10) ** 2
print(a)

# indexing array numpy
print("indexing".center(20, "-"))
print("nilai ke 1 dari array a = ", a[0])
print("nilai ke 6 dari array a = ", a[5])


arr_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr_2d)
print("ambil nilai dari baris 2, dan index 3 = ", arr_2d[1, 3])

arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr_3d)
print("ambil 3D array ke 1, baris ke 2, index ke 2", arr_3d[0, 1, 2])

# slicing array numpy
print("slicing".center(20, "-"))
print("ambil nilai 2 hingga nilai 6 = ", a[1:6])  # (start:end)
print("ambil nilai awal hingga nilai 6 = ", a[:6])
print("ambil nilai dari 4 hingga akhir = ", a[4:])

print(arr_2d)
print("ambil array ke 2 dengan slice start index 1 dan end index 4\n", arr_2d[1, 1:4])

# iterasi atau looping array
print("iterasi".center(20, "-"))
print("iterasi range")
number = 0
for e in a:
    print(f"element ke {number} dari array a = {e}")
    number += 1

print("iterasi array 2D")
for i in arr_2d:
    print(i)

print("iterasi array 2D menjadi range")
for i in arr_2d:
    for j in i:
        print(j)

print("iterasi array 3D")
for i in arr_3d:
    print(i)

print("iterasi array 3D menjadi range")
for i in arr_3d:
    for j in i:
        for k in j:
            print(k)
