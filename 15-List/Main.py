# list dalam python

print("Pengenalan List".center(30,"-"))

# nilai dalam list dapat 1 jenis atau lebih
list_campuran = [1,"kamu",True,2,"dia",False]
print(f"nilai list = {list_campuran}")

# list dengan menggunakan range
data_range = range(0,10,2) # range(start,stop,step)
print(data_range)
data_list = list(data_range) # mengubah range menjadi list
print(data_list)

# list comprehension for
list_for = [i**2 for i in range(0,10,2)]
print(list_for)

# list comperhension for pake if
list_forif = [i for i in range(0,10) if i != 5]
print(list_forif)

list_forif = [i for i in range(0,10) if i%2 ==0]
print(list_forif)

list_forif = [i for i in range(0,10) if i%2 !=0]
print(list_forif)