# membuat ufunc pribadi
"""
Untuk membuat ufunc pribadi, harus mendefinisikan suatu fungsi seperti fungsi normal di Python, 
lalu menambahkan fungsi ke ufunc NumPy dengan metode frompyfunc().
frompyfunc(fungsi yang dibuat, input array, output array)
"""
import numpy as np


def myadd(x, y):
    return np.add(x, y)
    # return x + y # ini juga bisa


print(type(myadd))  # akan bertipe <class 'function'>
myadd = np.frompyfunc(myadd, 2, 1)  # jumlah array input 2, jumlah array hasil akan 1
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

print(type(myadd))  # akan berubah tipe menjadi <class 'numpy.ufunc'>
print(type(np.add))  # akan bertipe <class 'numpy.ufunc'>
print(
    type(np.concatenate)
)  # akan bertipe <class 'function'> dikarenakn buka termasuk ufunc
