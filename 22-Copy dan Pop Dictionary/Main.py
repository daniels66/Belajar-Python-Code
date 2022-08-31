# copy dictionary
nama = {
    'ds' : 'Daniel Saputra',
    'bc' : 'Bili Candra',
    'dc' : 'Denny Caknan',
    'mtn' : {
        'ans' : 'Anisa',
        'sls' : 'Salsa'
    },
    'nmbr' : [1,2,3,4,4],
    'phd' : 'Pizza Hut Delivery',
}

print(f"copy()".center(20,"-"))
# copy_nama = nama
copy_nama = nama.copy()
'''
copy() menduplikat dictionary dengan alamat yang berbeda
oleh karena itu apabila ingin merubah nilai tidak akan merubah nilai sebelum copy
'''

print("nama = ", nama)
print(f"addres = {hex(id(nama))} \n")
print("copy dictionary biasa = ", copy_nama)
print(f"addres = {hex(id(copy_nama))} \n")

copy_nama['bc'] = "bali coy"
print("nama = ", nama)
print(f"addres = {hex(id(nama))} \n")
print("copy dictionary biasa = ", copy_nama)
print(f"addres = {hex(id(copy_nama))} \n")

print(f"pop() dan popitem()".center(30,"-"))
'''
pop() digunakan untuk mengambil satu buah nilai dengan memasukkan key didalamnya
'''
ambil_key = nama.pop("ds")
print(f"ambil nilai dengan pop = {ambil_key}")

'''
popitem() digunakan untuk menghapus dictionary pada bagian akhir
'''
print(f"dictionary sebelum dihapus = \n{nama}")
nama.popitem()
print(f"\nhapus dictionary dengan popitem() = \n{nama}")
nama['mtn'].popitem()
print(f"\nhapus dictionary dalam dictionary = \n{nama}")