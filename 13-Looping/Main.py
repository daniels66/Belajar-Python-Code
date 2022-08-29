# pengulangan dalam python
'''
for kondisi:
    aksi

while kondisi: # untuk while dapat dilakukan seperti di bahasa c
    aksi
'''

# for loop
print("For Loop".center(12,"="))
# for dengan list
print("list".center(12,"-"))
list = [2,4,6,8,10]
for angka in list:
    print(f"list {angka}")

# for dengan range
print("range".center(12,"-"))
range1 = range(5) # dimulai dari angka 0 - 5
for angka1 in range1:
    print(f"angka ke {angka1}")
print("".center(12,"-"))
range2 = range(1,6) # dimulai dari angka 1 - 5
for angka2 in range2:
    print(f"angka ke {angka2}")

#for dengan string
print("string".center(12,"-"))
kata = "daniels"
for huruf in kata:
    print(huruf)

print("While Loop".center(12,"="))
'''
while loop seperti for dalam bahasa c
for(statment;kondisi;increment/decrement)
    aksi;
'''
angka = 0 # statement
while angka < 10: # kondisi
    angka += 1 # increment/ decrement (hasil angka 1 - 10)
    print(f"angka ke-{angka}")
    # angka += 1 # increment/ decrement (hasil angka 0 - 9)

