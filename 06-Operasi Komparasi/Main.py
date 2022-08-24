'''
Operasi Komparasi dalam python untuk membandingkan 2 buah variabel

- lebih besar (>), lebih kecil (<)
- lebih besar sama dengan (>=), lebih kecil sama dengan (<=)
- sama dengan (==), tidak sama dengan (!=)
- is, is not (harus object, tidak dapat assigment dan pengecekan terhadap addres memory)

nilai dari operasi komparasi adalah boolean (True/False)
'''
a = 4
b = 3
c = 4

print('====== Lebih Besar (>)')
hasil = a > b
print(a,'>',b,'=',hasil)
hasil = b > a
print(b,'>',a,'=',hasil)

print('====== Lebih Kecil (<)')
hasil = a < b
print(a,'<',b,'=',hasil)
hasil = b < a
print(b,'<',a,'=',hasil)

print('====== Lebih Besar sama dengan (>=)')
hasil = a >= b
print(a,'>=',b,'=',hasil)
hasil = b >= a
print(b,'>=',a,'=',hasil)
hasil = a >= a
print(a,'>=',a,'=',hasil)
hasil = b >= b
print(b,'>=',b,'=',hasil)

print('====== Lebih Kecil sama dengan (<=)')
hasil = a <= b
print(a,'<=',b,'=',hasil)
hasil = b <= a
print(b,'<=',a,'=',hasil)
hasil = a <= a
print(a,'<=',a,'=',hasil)
hasil = b <= b
print(b,'<=',b,'=',hasil)

print('====== Sama Dengan (==)')
hasil = a == b
print(a,'==',b,'=',hasil)
hasil = a == c
print(a,'==',c,'=',hasil)

print('====== Tidak Sama Dengan (!=)')
hasil = a != b
print(a,'!=',b,'=',hasil)
hasil = a != c
print(a,'!=',c,'=',hasil)

print('====== Object Identity (is)')
alamat_a = hex(id(a))
alamat_b = hex(id(b))
alamat_c = hex(id(c))
hasil = a is b
print("addres a =", alamat_a)
print("addres b =", alamat_b)
print(a,'is',b,'=',hasil)
hasil = a is c
print("addres a =", alamat_a)
print("addres c =", alamat_c)
print(a,'is',c,'=',hasil)

print('====== Object Identity (is not)')
alamat_a = hex(id(a))
alamat_b = hex(id(b))
alamat_c = hex(id(c))
hasil = a is not b
print("addres a =", alamat_a)
print("addres b =", alamat_b)
print(a,'is not',b,'=',hasil)
hasil = a is not c
print("addres a =", alamat_a)
print("addres c =", alamat_c)
print(a,'is not',c,'=',hasil)