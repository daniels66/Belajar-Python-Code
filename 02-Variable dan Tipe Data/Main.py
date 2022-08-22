# membuat variabel dalam bahasa python
# dalam python tidak memerlukan penulisan type data (python otomatis mengetahui)
# serta tidak perlu untuk mendeklarasikan variable | int a = 10
nilai_a = 1
print("nilai a adalah =", nilai_a,"\n")

# type data dalam python
# - integer (bilangan bulat)
type_int = 12
print("nilai variable adalah", type_int)
print("type variable adalah",type(type_int),"\n")

# - float (bilangan desimal / bilangan koma)
type_float = 3.14
print("nilai variable adalah", type_float)
print("type variable adalah",type(type_float),"\n")

# - string (kata)
type_string = "daniels"
print("nilai variable adalah", type_string)
print("type variable adalah",type(type_string),"\n")

# - boolean (True / False)
type_bool = True
print("nilai variable adalah", type_bool)
print("type variable adalah",type(type_bool),"\n")

# selain tipe data diatas python dapat mengambil tipe data dalam bahasa c
# dikarenakan python dibuat berdasarkan bahasa c

from ctypes import c_char, c_ushort, c_double
data_c = c_double(123.56)
print("nilai variable adalah", data_c)
print("type variable adalah",type(data_c),"\n")