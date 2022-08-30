# looping dalam list

angka = [3,5,2,4,1]
print(f"alamat dari angka = {hex(id(angka))}")

# for loop
print(f"for loop".center(30,"-"))
for i in angka:
    print(f"nilai dalam angka = {i}")

# for loop in range
print(f"for loop in range".center(30,"-"))
for i in range(len(angka)):
    print(f"nilai dalam index angka {i} = {angka[i]}")

# while loop
print(f"while loop".center(30,"-"))
panjang_angka = len(angka)
i = 0
while i < panjang_angka:
    print(f"nilai dalam angka = {angka[i]}")
    print(f"alamat dari nilai {angka[i]} = {hex(id(angka[i]))}")
    i += 1

# list comperhension
print(f"list comperhension".center(30,"-"))
[print(f"angka = {i}") for i in angka]
kuadrat = [i**2 for i in angka]
print(f"kuadrat angka = {kuadrat}")
[print(f"kuadrat = {i}") for i in kuadrat]

# enumerate
print(f"enumerate".center(30,"-"))
for index,nilai in enumerate(angka):
	print(f"index = {index}, data = {nilai}")