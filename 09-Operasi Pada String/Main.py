# Operasi dan Memanipulasi String

# 1. Menyambung String (concatenate)
print( "1. Menyambung String (concatenate) (+)")
nama_pertama = "Daniel"
nama_tengah = "D"
nama_akhir = "Putra"

print(nama_pertama)
print(nama_tengah)
print(nama_akhir)
nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)
print(15*'=')

# 2. Menghitung panjang string
print( "2. Menghitung panjang string (len)")
panjang = len(nama_lengkap)
print("panjang " + nama_lengkap + " adalah " + str(panjang))
print(15*'=')

# 3. operator untuk string
print( "3. operator untuk string")

# cek apakah ada komponen pada sebuah string
print( "3a. cek apakah ada komponen pada sebuah string (in dan not in)")
d = "d"
status = d in nama_lengkap
print("apakah " + d + " ada di " + nama_lengkap + ", =" + str(status))

D = "D"
status = D in nama_lengkap
print("apakah " + D + " ada di " + nama_lengkap + ", =" + str(status))

x = "x"
status = x not in nama_lengkap
print("apakah " + x + " tidak ada di " + nama_lengkap + ", =" + str(status))
print(15*'-')

# mengulang string
print( "3b. mengulang string")
print("wk"*20)
print(20*"wk")
print(15*'-')

# indexing
print( "3c. indexing")
print("index ke-0 : " + nama_lengkap[0]) # dimulai dari 0
print("index ke-3 : " + nama_lengkap[3]) # index bebas
print("index ke-(-1) : " + nama_lengkap[-1]) # indexing dari dibelakang
print("index ke-[6,8) : " + nama_lengkap[6:8]) # dimulai dari index 6 sampai sebelum 8
print("index ke-[0,2,4,6,8] : " + nama_lengkap[0:10:2]) # diambil index 0,2,4,6,8
print(15*'-')

print( "3d. nilai item terbesar atau terkecil berdasarkan ascii (min dan max)")
# item paling kecil
print("nilai terkecil : " + min(nama_lengkap))
# item paling besar
print("nilai terbesar : " + max(nama_lengkap))

ascii_code = ord(" ") # urutan nilai space berdasarkan ascii
print("ASCII number dari spasi : " + str(ascii_code))
data = 117 # urutan nilai 117 berdasarkan ascii
print("Character dari ascii code 117 : " + chr(data))
print(15*'=')

# 4. operator dalam bentuk method
print( "4. operator dalam bentuk method")
print( "4a. menghitung jumlah suatu char dan string")
data = "sasa sara masa marisa"
cari_char = "s"
jumlah = data.count(cari_char)
print("jumlah "+ cari_char+ " di " + data + " : " + str(jumlah)) 
cari_string = "asa"
jumlah = data.count(cari_string)
print("jumlah "+ cari_string+ " di " + data + " : " + str(jumlah))
print(15*'-')

## merubah case pada string
print( "4b. merubah case pada string (upper() atau lower())")

# merubah semua ke upper case
salam = "bro!"
print("normal " + salam)
salam = salam.upper()
print("upper " + salam)

# merubah semua ke lower case
alay = "aKu KeCe AbieeZZZ"
print("normal " + alay)
alay = alay.lower()
print("lower " + alay)
print(15*'-')

# startwith() dan endwith()
print( "4c. melakukan pengecekan awal dan akhir character atau string dalam string (startwith() dan endwith())")
judul = "ada apa dengan cinta"
print("judul = " + judul)
string_awal="ada"
string_akhir="cinta"
cek_start = judul.startswith(string_awal)
print("string "+ string_awal +" berada di start ?" + str(cek_start))
cek_end = judul.endswith(string_akhir)
print("string "+ string_akhir +" berada di end ?" + str(cek_end))
print(15*'-')

# join() dan split()
print( "4d. menggabungkan dan memisah string join() dan split())")

pisah = ['aku','sayang','kamu']
gabungan = '-'.join(pisah) # merubah list menjadi string
print(pisah)
print(gabungan)

gabungan = "naik vespa keliling kota"
pisah = gabungan.split() # membuat perkata menjadi list
print(gabungan)
print(pisah)

gabungan = "naikehmvespaehmkelilingehmkota"
pisah = gabungan.split("ehm") # membuat perkata menjadi list (split berdasarkan kata dalam kurung)
print(gabungan)
print(pisah)
print(15*'-')

# alokasi karakter
print( "4e. alokasi karakter pada string, rjust(), ljust(), center()")
print("'kiri      '")
print(25*'.')

print("*rata kanan\n")
kanan = "kanan".rjust(20) # rata kanan dengan 20 karakter
print("'" + kanan + "'")
print(25*'.')

print("*rata kiri\n")
kiri = "kiri".ljust(20) # rata kiri dengan 20 karakter
print("'" + kiri + "'")
print(25*'.')

print("*rata tengah\n")
tengah ="tengah".center(20) # rata tengah dengan 20 karakter
print("'" + tengah + "'")
tengah ="tengah".center(20,'-') # rata tengah dengan 20 karakter
print("'" + tengah + "'")
print(25*'.')
print(15*'-')

# kebalikan dari alokasi karakter
print( "4f. menghapus karakter pada alokasi dengan strip()")
kanan = kanan.strip()
print("'" + kanan + "'")
kiri = kiri.strip()
print("'" + kiri + "'")
tengah = tengah.strip('-')
print("'" + tengah + "'")
print(15*'=')

# 5. operator dalam bentuk is method
print( "5. operator dalam bentuk is method (pengecekan)")
# isupper() <- untuk pengecekan apakah upper case semua
print("5a. isupper()")
salam = "KAMU"
apakah_upper = salam.isupper()
print(salam + " is upper? " + str(apakah_upper))
salam = salam.lower()
apakah_upper = salam.isupper()
print(salam + " is upper? " + str(apakah_upper))
print(15*'-')

# islower() <- untuk pengecekan apakah lower case semua
print("5b. islower()")
# contoh islower()
salam = "kamu"
apakah_lower = salam.islower()
print(salam + " is lower? " + str(apakah_lower))
salam = salam.upper()
apakah_lower = salam.islower()
print(salam + " is lower? " + str(apakah_lower))
print(15*'-')

# isalpha() <- untuk mengecek apakah huruf semua
print("5c. isalpha()")
# contoh isalpha()
salam = "kamu"
salam2 = "kamu124"
apakah_alpha = salam.isalpha()
print(salam + " is alpha? " + str(apakah_alpha))
apakah_alpha = salam2.isalpha()
print(salam2 + " is alpha? " + str(apakah_alpha))
print(15*'-')

# isalnum() <- untuk mengecek apakah huruf, angka atau keduanya
print("5d. isalnum()")
# contoh isalnum()
salam = "kamu"
salam2 = "kamu124"
apakah_isalnum = salam.isalnum()
print(salam + " is isalnum? " + str(apakah_isalnum))
apakah_isalnum = salam2.isalnum()
print(salam2 + " is isalnum? " + str(apakah_isalnum))
print(15*'-')

# isdecimal() <- untuk mengecek apakah numeric
print("5e. isdecimal()")
# contoh isdecimal()
salam = "kamu"
salam2 = "124"
apakah_isdecimal = salam.isdecimal()
print(salam + " is isdecimal? " + str(apakah_isdecimal))
apakah_isdecimal = salam2.isdecimal()
print(salam2 + " is isdecimal? " + str(apakah_isdecimal))
print(15*'-')

# isspace() <- apakah isinya hanya spasi, tab dan enter (newline \n)
print("5f. isspace()")
# contoh isspace()
salam = "kamu"
salam2 = "   \t"
apakah_isspace = salam.isspace()
print(salam + " is isspace? " + str(apakah_isspace))
apakah_isspace = salam2.isspace()
print(salam2 + " is isspace? " + str(apakah_isspace))
print(15*'-')

# istitle() <- huruf pertama setiap kata upper case
print("5g. isspace()")
# contoh isspace()
judul = "Ada Apa Dengan Cinta"
judul2 = judul.lower()
cek_judul = judul.istitle()
print(judul + " is title? " + str(cek_judul))
cek_judul2 = judul2.istitle()
print(judul2 + " is title? " + str(cek_judul2))
print(15*'=')
