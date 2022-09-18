# operasi set
import numpy as np

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

print("array =\n", arr)
print("array 1 =\n", arr1)
print("array 2 =\n", arr2)

print("unique()".center(30, "-"))
"""
unique() digunakan untuk menemukan elemen unik dari array 
dan array hanya boleh berupa array 1-D.
"""
x = np.unique(arr)
print("array tidak duplikat =\n", x)

print("union1d()".center(30, "-"))
"""
union1d() digunakan untuk menemukan elemen unik dari beberapa array
"""
newarr = np.union1d(arr1, arr2)
print("stacking kedua array lalu nilai duplikat disisakan satu =\n", newarr)

print("intersect1d()".center(30, "-"))
"""
intersect1d() digunakan untuk menemukan nilai array yang duplikat
"""
newarr = np.intersect1d(arr1, arr2, assume_unique=True)
print("nilai array duplikat dari array 1 dan array 2 =\n", newarr)
"""
assume_unique=True diperlukan agar nilai dapat tampil
"""

print("setdiff1d()".center(30, "-"))
"""
setdiff1d() digunakan untuk 
"""
newarr = np.setdiff1d(arr1, arr2, assume_unique=True)
print("nilai dalam array 1 yang tidak duplikat dalam array 2 =\n", newarr)
"""
assume_unique=True diperlukan agar nilai dapat tampil
"""

print("setxorld()".center(30, "-"))
"""
setxorld() digunakan untuk menghapus duplikat nilai dari beberapa array
"""
newarr = np.setxor1d(arr1, arr2, assume_unique=True)
print("nilai tidak duplikat pada kedua array =\n", newarr)
