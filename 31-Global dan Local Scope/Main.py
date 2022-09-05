# global dan local scope

'''
scope global dan lokal hanya terdapat dalam fungsi
perkondisian dan perulangan tidak terdapat scope global dan lokal
'''

print("global local scope dalam pengkondisian")
angka1 = 0
angka2 = 10

print(f"angka1 sebelum pengkondisian = {angka1}")
print(f"angka2 sebelum pengkondisian = {angka2}")

if True:
    angka1 = 11 # dapat mengubah angka global
    angka2 = 111

print(f"angka1 sesudah pengkondisian = {angka1}")
print(f"angka2 sesudah pengkondisian = {angka2}")

print("global local scope dalam perulangan")
angka1 = 0
angka2 = 10

print(f"angka1 sebelum perulangan = {angka1}")
print(f"angka2 sebelum perulangan = {angka2}")

for i in range(0,4):
    angka1 += i # dapat mengubah angka global
    angka2 = 0

print(f"angka1 sebelum perulangan = {angka1}")
print(f"angka2 sebelum perulangan = {angka2}")

print("global local scope dalam fungsi")
angka1 = 0
angka2 = 10

def ubah_angka(angka3):
    angka1 = angka3

ubah_angka(10)
print(angka1)  # angka global tidak dapat diubah dalam lokal

def ubah_angka(angka3):
    '''
    apabila ingin mengubah global dalam lokal 
    gunakan keyword global pada awal variable global
    '''
    global angka1
    angka1 = angka3

ubah_angka(100)
print(angka1)  # angka global dapat diubah dalam lokal

