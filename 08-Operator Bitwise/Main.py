'''
Operator Bitwise (Biner) dalam Python
AND (&)
OR (|)
XOR (^)
NOT
Shift Right (>>)
Shift Left (<<)
'''

a = 9
b = 7

print('\n',5*'=','AND (&)',5*'=')
c = a & b
print('Bitwise ',a,'=',format(a,'08b'))
print('Bitwise ',b,'=',format(b,'08b'))
print(21*'-')
print('Bitwise ',c,'=',format(c,'08b'))

print("\n",5*'=','OR (|)',5*'=')
c = a | b
print('Bitwise ',a,'=',format(a,'08b'))
print('Bitwise ',b,'=',format(b,'08b'))
print(21*'-')
print('Bitwise ',c,'=',format(c,'08b'))

print("\n",5*'=','XOR (^)',5*'=')
c = a ^ b
print('Bitwise ',a,'=',format(a,'08b'))
print('Bitwise ',b,'=',format(b,'08b'))
print(21*'-')
print('Bitwise ',c,'=',format(c,'08b'))

print("\n",5*'=','NOT',5*'=') # Bitwise sama akan tetapi bernilai negatif dengan tambahan 1 angka
c = ~a
d = ~b
print('Bitwise ',a,'=',format(a,'08b'))
print('Bitwise ',b,'=',format(b,'08b'))
print(21*'-')
print('Bitwise ',c,'=',format(c,'08b')) # 9 menjadi -10 (nilai biner sama)
print('Bitwise ',d,'=',format(d,'08b')) # 7 menjadi -8 (nilai biner sama)

print("\n",5*'=','Shift Right',5*'=')
c = a >> 2 # pindah kanan 2 langkah
d = b >> 2 # pindah kanan 2 langkah
print('Bitwise ',a,'=',format(a,'08b'))
print('Bitwise ',b,'=',format(b,'08b'))
print(21*'-')
print('Bitwise ',c,'=',format(c,'08b')) 
print('Bitwise ',d,'=',format(d,'08b'))

print("\n",5*'=','Shift Left',5*'=')
c = a << 2 # pindah kiri 2 langkah
d = b << 2 # pindah kiri 2 langkah
print('Bitwise ',a,'=',format(a,'08b'))
print('Bitwise ',b,'=',format(b,'08b'))
print(21*'-')
print('Bitwise ',c,'=',format(c,'08b')) 
print('Bitwise ',d,'=',format(d,'08b'))

