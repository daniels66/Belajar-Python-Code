# operasi dalam list

from pickle import TRUE


angka = [1,2,3,4,5,6] 

# mengambil data dalam list
print(f"ambil data angka awal = {angka[0]}") # indek awal list dimulai dari angka 0
print(f"ambil data angka akhir = {angka[-1]}") # indek belakang list dimulai dari -1
print(f"ambil data angka akhir = {angka[-3]}") # mengambil nilai ke 3 dari belakang

# mengambil panjang dari list
panjang_list = len(angka)
print(f"panjang dari list = {panjang_list}")

# menambahkan nilai terbaru di dalam list (insert)
angka.insert(1,3) # pada index 1 tambahkan angka 3, index 1 sebelumya bergeser
print("angka tambah = ", angka)

# menambahkan nilai dari belakang (append)
angka.append("kamu")
print("angka tambah belakang = ", angka)

# tambah data list dengan list (extend)
tambah_list = [True,True,False,True]
angka.extend(tambah_list)
print(f"angka tambah list = {angka}")

# ubah data dalam list
angka[7] = 7
print(f"ubah angka index 7 = {angka}")

# menghitung jumlah data (count)
jumlah_angka_3 = angka.count(3) # menghitung jumlah angka 3 dalam angka
print(f"jumlah angka 3 = {jumlah_angka_3}")

# remove data dalam list (remove)
angka.remove(3)
print(f"angka remove 3 = {angka}") # remove hasil awal dalam list

# remove data dari belakang (pop)
angka.pop()
print(f"angka pop = {angka}")

# mengambil index data
index_angka_3 = angka.index(3)
print(f"angka 3 berada pada index = {index_angka_3}")

# melakukan urutan list (sort)
angka.sort()
print(f"angka sesudah urut = {angka}")

# reverse sort list
angka.reverse()
print(f"angka sesudah reverse = {angka}")
