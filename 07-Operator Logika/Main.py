'''
Operator Logika dalam Python
AND (&)
OR (|)
XOR (^)
NOT
'''
from operator import not_


a = True
b = not a

print(5*'=','NOT',5*'=') # Kebalikan
print('nilai a =',a)
print('nilai b =',b, 'not', a)

print(5*'=','AND (&)',5*'=') # Harus True dan True
hasil = a & a
print(a,'&',a, '=',hasil)
hasil = a & b
print(a,'&',b, '=',hasil)
hasil = b & a
print(b,'&',a, '=',hasil)
hasil = b & b
print(b,'&',b, '=',hasil)

print(5*'=','OR (|)',5*'=') # Cukup satu True
hasil = a | a
print(a,'|',a, '=',hasil)
hasil = a | b
print(a,'|',b, '=',hasil)
hasil = b | a
print(b,'|',a, '=',hasil)
hasil = b | b
print(b,'|',b, '=',hasil)

print(5*'=','XOR (^)',5*'=') # Harus True dan False
hasil = a ^ a
print(a,'^',a, '=',hasil)
hasil = a ^ b
print(a,'^',b, '=',hasil)
hasil = b ^ a
print(b,'^',a, '=',hasil)
hasil = b ^ b
print(b,'^',b, '=',hasil)

