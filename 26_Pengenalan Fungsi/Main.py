# pengenalan fungsi

'''
def say_hi(argument):
    body fungsi

dalam penulisan fungsi dilakukan sebelum fungsi tersebut dipanggil
singkatnya fungsi ditulis pada bagian atas tidak seperti bahasa c
yang dapat ditulis pada bagian awal atau akhir
'''

# fungsi biasa
print(f"fungsi biasa".center(50,"-"))
def say_hi():
    print(f"Hallo Kamu, Apa Kabar?")

say_hi()
say_hi()

# fungsi dengan argument
print(f"fungsi dengan argument".center(50,"-"))
def move_on(nama): # argument dapat lebih dari 1 dan dapat diisi type apapun
    print(f"Hai {nama}, sudah move on belum??")

def patah_hati(nama1,nama2): # argument dapat lebih dari 1 dan dapat diisi type apapun
    print(f"Hai {nama1}, {nama2} sudah punya pacar baru loh !!!")

move_on("niel")
patah_hati("niel","arum")

# fungsi dengan return
print(f"fungsi dengan return".center(50,"-"))
def tambah(angka1,angka2):
    tambah = angka1 + angka2
    return tambah # return dapat bernilai apapun (str,bool,number,dll)

hasil = tambah(50,14)
print(f"hasil fungsi tambah = {hasil}")

# fungsi dengan default argument
print(f"fungsi dengan default arguments".center(50,"-"))
def patah_hati(nama1,nama2 = "dia"):
    print(f"Hai {nama1}, {nama2} sudah punya pacar baru loh !!!")

patah_hati("niel") 
# apabila sebuah argument tidak memiliki nilai maka akan eror
# apabila tidak terdapat default argument
patah_hati("niel","arum")

