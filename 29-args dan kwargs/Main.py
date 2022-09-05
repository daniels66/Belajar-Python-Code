# args dan kwargs

print("args".center(20,"-"))
'''
args digunakan untuk fungsi yang membutuhkan banyak input
dan tidak mengerti berapa banyak input yang dibutuhkan
args bertype tupple oleh karena itu 
data tidak dapat dirubah tetapi dapat diambil datanya
'''
# contoh
def tambah1(a,b,c,d,e,f,g,h,i,j):
    hasil = a + b + c + d + e + f + g + h + i + j
    return hasil # sangat tidak praktis

print(tambah1(1,2,3,4,5,6,7,8,9,10)) 

# dengan args
def tambah2(*args): # penamaan tidak harus args akan tetapi harus memakai bintang 1
    output = 0
    print(args) # args bertype tupple
    for angka in args:
        output = output + angka
    return output

print(tambah2(1,2,3,4,5,6,7,8,9,10))
print(tambah2(1,3,5,7,9)) # input sesuai yang diinginkan

print("kwargs".center(20,"-"))
'''
kwargs digunakan untuk fungsi yang membutuhkan key dan value seperti dictionary
oleh karena itu kwargs bertype dictionary
'''

def personal(**kwargs): # penamaan tidak harus kwargs akan tetapi harus memakai bintang 2
    print(kwargs) # kwargs bertype dictionary yang memiliki key dan value
    # mengambil value dengan key
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"nama saya {nama}, tinggi saya {tinggi} dan memiliki berat {berat}")

personal(nama="daniel",tinggi=166,berat=86)

# latihan args dan kwargs
print("latihan args kwargs".center(30,"-"))
def operasi(*args,**kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output = output + angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output = output * angka
    else:
        print("operasi salah")
    return output


hasil = operasi(1,3,5,option="tambah")
print(hasil)
hasil = operasi(1,3,5,option="kali")
print(hasil)

