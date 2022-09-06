# import sebuah kode dalam suatu package (folder)
import matematika
'''
akan menuju ke dalam folder matematika,
setelah itu menuju ke file __init__.py terlebih dahulu
dari pada file python lainnya
'''

# import file dalam folder matematika/basic/...py
from matematika.basic import kali,tambah

print(f"hasil kali = {kali.kali(7,5)}")
print(f"hasil tambah = {tambah.tambah(20,5)}")

# import file dalam folder matematika/scient/...py
from matematika.scient import pangkat
print(f"hasil pangkat2 = {pangkat.pangkat(2)(8)}")


