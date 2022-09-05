# lambda function dan anonymous function

print("lambda function".center(30,"-"))

'''
digunakan untuk menyederhanakan fungsi yang sedikit penjadi 1 baris
'''

# fungsi biasa
def f_kuadrat(angka):
    return angka**2

print(f"hasil kuadrat dengan fungsi = {f_kuadrat(3)}")

# fungsi dengan lambda
'''
output = lambda arguments:expresi
'''
l_kuadrat1 = lambda angka:angka**2 # lebih singkat
print(f"hasil kuadrat dengan lambda = {l_kuadrat1(6)}")

l_kuadrat2 = lambda angka,pangkat:angka**pangkat
print(f"hasil kuadrat dengan lambda = {l_kuadrat2(2,5)}")

# filter list biasa
list_angka = [1,2,3,4,5,6,7,8,9]
def f_filter(angka):
    return angka > 5

list_filter = list(filter(f_filter,list_angka))
print(f"filter list angka dengan fungsi biasa = \n {list_filter}")

# filter list dengan lambda
list_filter = list(filter(lambda angka:angka>4,list_angka))
print(f"filter list angka dengan lambda = \n {list_filter}")

# filter list genap dengan lambda
list_genap = list(filter(lambda angka:(angka % 2 == 0),list_angka))
print(f"filter list angka genap dengan lambda = \n {list_genap}")

# filter list ganjil dengan lambda
list_genap = list(filter(lambda angka:(angka % 2 != 0),list_angka))
print(f"filter list angka ganjil dengan lambda = \n {list_genap}")

print("anonymous function".center(30,"-"))
'''
currying adalah salah satu dari anonymous function
'''

# fungsi biasa
def f_kuadrat(angka):
    return angka**2

print(f"hasil kuadrat dengan fungsi = {f_kuadrat(3)}")

l_kuadrat1 = lambda angka:angka**2 # lebih singkat
print(f"hasil kuadrat dengan lambda = {l_kuadrat1(6)}")

# dengan currying
def c_kuadrat(pangkat):
    return lambda angka:angka**pangkat

pangkat2 = c_kuadrat(2)
print(f"hasil kuadrat dengan currying = {pangkat2(7)}")
pangkat3 = c_kuadrat(3)
print(f"hasil kuadrat dengan currying = {pangkat3(5)}")

print(f"pangkat bebas = {c_kuadrat(3)(8)}") # delapan pangkat tiga bukan tiga pangkat 8



