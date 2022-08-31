# lopping dictionary
nama = {
    'ds' : 'Daniel Saputra',
    'bc' : 'Bili Candra',
    'dc' : 'Denny Caknan',
    'phd' : 'Pizza Hut Delivery',
    'nmbr' : [1,2,3,4,4],
    'mtn' : {
        'ans' : 'Anisa',
        'sls' : 'Salsa'
    }
}
print(f"mengambil key".center(20,"-"))
keys = nama.keys()
print(f"type key = {type(keys)}")
print(keys,"\n")

print(f"mengambil nilai".center(20,"-"))
values = nama.values()
print(f"type key = {type(values)}")
print(values,"\n")

print(f"mengambil item".center(20,"-"))
items = nama.items()
print(f"type key = {type(items)}")
print(items,"\n")

print(f"looping key".center(20,"-"))
for key in nama.keys():
    print(key)
print(f"type key = {type(key)}")
print("\n")

print(f"looping nilai".center(20,"-"))
for nilai in nama.values():
    print(nilai)
print(f"type nilai = {type(nilai)}")
print("\n")

print(f"looping items".center(20,"-"))
for items in nama.items():
    print(items)
print(f"type items = {type(items)}")
print("\n")

print(f"looping key didalam key".center(35,"-"))
for key in nama.keys():
    print(key)
    if key == 'mtn':
        for mtn in nama["mtn"].keys():
            print("-",mtn)
print("\n")

print(f"looping nilai didalam nilai".center(35,"-"))
for nilai in nama.values():
    print(nilai)
    if nilai == nama["nmbr"]:
        for nmbr in nama["nmbr"]:
            print("-",nmbr)
    if nilai == nama["mtn"]:
        for mtn in nama["mtn"].values():
            print("-",mtn)
print("\n")