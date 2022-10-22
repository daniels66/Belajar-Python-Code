# file handling digunakan untuk creat, read, update, delete (CRUD)
# dengan menggunakan fungsi
"""
open(path,mode)
path = lokasi file
mode r = read (digunakan untuk membaca file, jika file tidak ada akan eror)
mode a = append (digunakan untuk menambahkan file yang ada, jika file tidak ada akan dibuatkan)
mode w = write (digunakan untuk menulis, jika file tidak ada akan dibuatkan)
mode x = create (digunakan untuk membuat file spesifik, eror jika file tidak ada)

selain mode diatas ada tambahan yaitu
mode rt = read text
mode rb = read binary
mode at = append text
mode ab = append binary
mode wt = write text
mode wb = write binary
mode xt = create text
mode xb = create binary
"""

path1 = "read/read.txt"
path2 = "read/read2.txt"

print("membaca file".center(30, "-"))
r_file = open(path1, mode="r")

print(
    "file dapat dibaca ?? ", r_file.readable()
)  # untuk mengecek apakah file dapat dibaca atau tidak
print(
    "file dapat diwrite ?? ", r_file.writable()
)  # untuk mengecek apakah file dapat ditulis atau tidak
"""
untuk file dengan mode r akan dapat dibaca tetapi tidak dapat ditulis
"""
# print(r_file.read())  # untuk membaca semua text dalam read.txt
# print(r_file.read(5))  # untuk membaca 5 character pertama dalam read.txt
# print(r_file.readline())  # untuk membaca line pertama pertama dalam read.txt
# print(
#     r_file.readlines(), end=""
# )  # untuk membaca line perbaris dan dimasukkan ke dalam list

# membaca file dengan loop
# for char in r_file:
#     print(char)

r_file.close()  # biasakan setelah open file ditutup dengan close

print("write file".center(30, "-"))

w_file = open(path2, mode="w")
print(
    "file dapat dibaca ?? ", w_file.readable()
)  # untuk mengecek apakah file dapat dibaca atau tidak
print(
    "file dapat diwrite ?? ", w_file.writable()
)  # untuk mengecek apakah file dapat ditulis atau tidak
# w_file.write("hallo ini dari read 2")
w_file.close()
# # apabila ingin menulis text lakukan seperti diatas

# w_file = open(path2, mode="r")
# print(w_file.read())
# w_file.close()

"""
untuk file dengan mode w akan dapat ditulis tetapi tidak dapat dibaca sebelum ditutup terlebih dahulu
"""

print("append file".center(30, "-"))

a_file = open(path2, mode="a")  # ganti mode menjadi append
print(
    "file dapat dibaca ?? ", a_file.readable()
)  # untuk mengecek apakah file dapat dibaca atau tidak
print(
    "file dapat diwrite ?? ", a_file.writable()
)  # untuk mengecek apakah file dapat ditulis atau tidak
# a_file.write("\ntext ini ditambahkan dari append")
a_file.close()
# # apabila ingin append text lakukan seperti diatas

# a_file = open(path2, mode="r")
# print(a_file.read())
# a_file.close()
# # apabila ingin membaca setelah di tambahkan
"""
untuk file dengan mode a akan dapat ditulis tetapi tidak dapat dibaca sebelum ditutup terlebih dahulu
"""

print("create file".center(30, "-"))
# c_file = open("create.txt", mode="w")
# c_file2 = open("create2.txt", mode="a")
# """
# mode w dan mode a akan membuat file apabila file tersebut tidak ada
# dan tidak eror jika file ada
# mode x akan membuat file apabila file tersebut tidak ada, jika ada akan eror
# c_file = open("create.txt", mode="x") # akan eror dikarenakan file sudah dibuat
# """

print("delete file".center(30, "-"))
# # delete file terdapat dalam module os oleh karena itu harus diimport
# import os

# os.remove("create2.txt")

# # remove jika file ada
# # if os.path.exists("create.txt"):
# #     os.remove("create.txt")
# # else:
# #     print("The file does not exist")

"""
perbedaan write dan append
write:
- apabila tidak ada file txt akan dibuatkan
- apabila ada file txt, isi dalam file txt akan dikosongkan
dan ditambahkan dengan text dalam write

append:
- apabila tidak ada file txt akan dibuatkan
- apabila ada file txt, isi dalam file tidak akan dikosongkan
dan ditambahkan text baru pada bagian bawah text lama
"""
