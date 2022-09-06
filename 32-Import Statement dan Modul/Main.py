'''
import steatment digunakan untuk meringkas kode agar 
kode tidak terlalu panjang sehingga dapat mudah dibaca
dengan cara memisahkan suatu kode atau fungsi dalam file .py terpisah
'''

import nama 
'''
akan mencari nama.py dalam satu folder dan menjalankan semua kode dalam nama.py
'''

# mengambil suatu data dalam file nama.py
data1 = nama.data # tulis nama file terlebih dahulu baru data dalam file tersebut

print(f"data dalam nama.py = {data1}")

angka_tambah = 100 + nama.angka
print(f"angka tambah = {angka_tambah}")

# mengambil fungsi dalam fungsi.py
import fungsi

nama = nama.data
fungsi.menghitung_panjang_string(nama) # tulis nama file terlebih dahulu baru fungsi dalam file tersebut

# mengambil fungsi tertentu dalam fungsi.py
from fungsi import menghitung_panjang_list,copy_list

list = [1,2,3,4,5,6,7,8,9]
menghitung_panjang_list(list)
listcopy = copy_list(list)
print(f"alamat list sebelum di copy = {hex(id(list))}")
print(f"alamat list setelah di copy = {hex(id(listcopy))}")

# mempersingkat penulisan fungsi yang diambil dengan as
from fungsi import menghitung_panjang_list as htg_p_ls
from fungsi import copy_list as cpy_ls

list = [1,2,3,4,5,6,7,8,9]
htg_p_ls(list)
listcopy = cpy_ls(list)
print(f"alamat list sebelum di copy = {hex(id(list))}")
print(f"alamat list setelah di copy = {hex(id(listcopy))}")




