import pandas as pd
from numpy import random

data = pd.DataFrame(random.randint(1, 10, size=(2, 2)))

"""
menampilkan tipe data frame
"""
print("data = \n", data, "\n")

print("tipe data = \n", data.dtypes)  # menampilkan tipe data pada setiap kolom
print(
    "tipe data pada kolom 1 = ", data.dtypes[1], "\n"
)  # menampilkan tipe data pada kolom 1

"""
mengubah tipe data beberapa kolom dari int ke string
"""
ubah_data = data.astype(
    {1: "string"}
)  # apabila ingin merubah tipe data harus dimasukkan dalam variable baru
print("tipe ubah_data = \n", ubah_data.dtypes)
print("tipe ubah_data pada kolom 1 = ", ubah_data.dtypes[1], "\n")

"""
mengubah tipe data semua kolom dari int ke string
"""
data = data.applymap(str)
print("data = \n", data, "\n")
print("tipe data = \n", data.dtypes)  # menampilkan tipe data pada setiap kolom
