# duplikat list
# dalam melakukan duplikat list di python sangat triky

a = [1,2,3,4,5]
b = a

print(f"list a = {a}")
print(f"list b = {b}")
print(f"alamat dari a = {hex(id(a))}")
print(f"alamat dari b = {hex(id(b))}")

'''
apabila duplikat memakai cara seperti diatas
maka akan menyamakan addresnya oleh karena itu apabila
nilai dalam addres dirubah maka nilai memngikut dalam addres
'''

b[0] = 0
print(f"list a = {a}")
print(f"list b = {b}")
print(f"alamat dari a = {hex(id(a))}")
print(f"alamat dari b = {hex(id(b))}")

# apabila menginginkan nilai sama tetapi berbeda address memakai (copy)
print("copy()".center(24,"-"))
c = a.copy()
print(f"list a = {a}")
print(f"list b = {b}")
print(f"list c = {c}")
print(f"alamat dari a = {hex(id(a))}")
print(f"alamat dari b = {hex(id(b))}")
print(f"alamat dari c = {hex(id(c))}") 

'''
menggunakan copy() menduplikat nilai sama addres berbeda
oleh karena itu apabila ingin mengubah nilai 
maka tidak akan berpengaruh pada nilai sebelumnya
'''
c[0] = 2
print(f"list a = {a}")
print(f"list b = {b}")
print(f"list c = {c}")
print(f"alamat dari a = {hex(id(a))}")
print(f"alamat dari b = {hex(id(b))}")
print(f"alamat dari c = {hex(id(c))}") 

# nested list (list dalam list)
print("list bersarang".center(24,"-"))
peserta0 = ["Daniel",20,"Laki-Laki"]
peserta1 = ["Amar",19,"Laki-Laki"]
peserta2 = ["Wulan",18,"Perempuan"]

list_peserta = [peserta0,peserta1,peserta2]
print(f"list peserta = {list_peserta}")


for peserta in list_peserta:
#     list = f"""Nama   = {peserta[0]}
# Umur   = {peserta[1]}
# Gender = {peserta[2]}
# """
    print(f"Nama = {peserta[0]}")
    print(f"Umur = {peserta[1]}")
    print(f"Gender = {peserta[2]}\n")
    # print(list)

list_peserta_copy = list_peserta.copy()
print(f"alamat dari list_peserta = {hex(id(list_peserta))}")
print(f"alamat dari list_peserta_copy = {hex(id(list_peserta_copy))}")
# apabila copy() digunakan pada list bersarang hanya akan membuat
# beda addres pada permukaan / awalnya saja untuk turunanya akan 
# direfrensikan pada alamat yang sama, seperti contoh dibawah
print(f"alamat dari list_peserta index0 = {hex(id(list_peserta[0]))}")
print(f"alamat dari list_peserta_copy index0 = {hex(id(list_peserta_copy[0]))}")
print(f"alamat dari list_peserta index1 = {hex(id(list_peserta[1]))}")
print(f"alamat dari list_peserta_copy index1 = {hex(id(list_peserta_copy[1]))}")

# apabila menginginkan adress berbeda untuk list bersarang menggunakan deepcopy

from copy import deepcopy
print("deepcopy".center(24,"-"))
list_peserta_deepcopy = deepcopy(list_peserta)
print(f"alamat dari list_peserta = {hex(id(list_peserta))}")
print(f"alamat dari list_peserta_deepcopy = {hex(id(list_peserta_deepcopy))}")
print(f"alamat dari list_peserta index0 = {hex(id(list_peserta[0]))}")
print(f"alamat dari list_peserta_deepcopy index0 = {hex(id(list_peserta_deepcopy[0]))}")
print(f"alamat dari list_peserta index1 = {hex(id(list_peserta[1]))}")
print(f"alamat dari list_peserta_deepcopy index1 = {hex(id(list_peserta_deepcopy[1]))}")
