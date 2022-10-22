# penggunaan with sebagai pengganti file handling biasa

path1 = "read.txt"
path2 = "read2.txt"

print("membuat file".center(30, "-"))
open(path1, mode="w")

print("append file".center(30, "-"))
a_file = open(path1, mode="a")
a_file.write("hallo cantik")

print(
    "file sudah ditutup ?? ", a_file.closed
)  # untuk mengecek apakah file sudah ditutup
a_file.close()
print("file sudah ditutup ?? ", a_file.closed)

print("membaca file".center(30, "-"))
r_file = open(path1, mode="r")
print(r_file.read())
r_file.close()

"""
akan sangat repot apabila harus menutup file satu persatu oleh karena itu 
terdapat cara lain yang lebih baik dalam file handling yaitu menggunakan with
"""

print("membuat file".center(30, "-"))
open(path1, mode="w")

print("append file".center(30, "-"))

# a_file2 = open(path2, mode="a") # sama seperti dibawah dengan with
with open(path2, mode="a") as a_file2:
    a_file2.write("hallo kamu yang ada disana")
    print("file sudah ditutup ?? ", a_file2.closed)
print("file sudah ditutup ?? ", a_file2.closed)

"""
saat memakai with tidak perlu menulis close secara manual
dikarenakan with sudah otomatis close jika berada di lain indentasi
"""
