# Pengenalan Tuples, Set, dan Dictionary

from pickle import APPEND



print("tuples".center(20,"-"))
'''
penggunaakn tuples seperti list akan tetapi menggunakan kurang buka tutup
tuples tidak dapat dirubah nilai di dalam nya
tetapi dapat melihat nilai dalam tuples

tupples digunakan untuk nilai yang tidak dapat dirubah
'''
angka = (1,2,3,4,5)
print(f"angka = {angka}")
print(f"ambil angka index 3 = {angka[3]}")

# angka[2] = "dans"
# print(f"angka baru = {angka}") # akan eror dikarenakan tupples tidak support assigment

# angka.append(3)
# print(f"angka baru = {angka}") # akan eror juga

print("set".center(20,"-"))
'''
penggunaakn set seperti list akan tetapi menggunakan kurang kurawa
set tidak memiliki index oleh karena itu nilai dalam set tidak dapat diambil
akan tetapi dapat menghapus nilai dalam set
'''
number = {1,2,3,4,5}
print(f"number = {number}")

# print(f"ambil number index 3 = {number[3]}") # akan eror dikarenakan set tidak memiliki index
number.remove(4)
print("number baru remove = ",number)
number.pop()
print("number baru pop = ",number)

print("dictionary".center(20,"-"))
'''
penggunaakn dictionary seperti list akan tetapi menggunakan kurang kurawa
index dalam list dirubah menjadi key oleh karena itu apabila ingin mencari spesifik dalam list
tidak perlu menggunakan index tetapi menggunakan key

dictionary lebih powerfull dari pada list
dictionary dapat diisi dengan str,number,bool,list,dictionary juga
'''
nama = {
    'ds' : 'Daniel Saputra',
    'bc' : 'Bili Candra',
    'dc' : 'Denny Caknan',
    'phd' : 'Pizza Hut Delivery',
    'nmbr' : [1,2,3,4,4],
    'mtn' : {
        'ans' : 'Anisa',
        'sls' : 'Salsa'
    }
}
print(f"penggunaan dictionary")
print(f"{nama['ds']} dan {nama['bc']} melihat {nama['dc']} di {nama['phd']}")