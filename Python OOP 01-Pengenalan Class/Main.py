"""
topik class sebenarnya masuk dalam materi
object oriented programing (OOP)
class merupakan blueprint dalam membuat object
class harus ditaruh pada bagian atas dikarenankan 
python adalah interpreter yang mengeksekusi kode secara berurutan
"""

# class
class Person:
    # x  adalah class variable
    x = 0

    # fungsi dalam class disebut methode
    def __init__(self):
        print(f"selamat datang di class dari init")
        """
        fungsi __init__() adalah fungsi yang dijalankan pertama kali ketika kelas sedang dinisialisasi.
        """

    def personal(self, inputname, inputage):
        # self.name,self.age adalah instance Variable
        self.name = inputname
        self.age = inputage
        """
        self adalah referensi ke kelas yang dibuat untuk digunakan
        dalam mengakses argument kelas.
        tidak harus bernama self dapat diganti apa pun
        tetapi harus ada dalam pembuatan fungsi/methode dalam class
        """


# print(x)
"""
kita tidak dapat mengabil nilai dari suatu class secara langsung
apabila ingin mengambil suatu nilai atau fungsi dalam class
lakukan inisialisasi terlebih dahulu, seperti contoh dibawah
"""

p1 = Person()
"""
saat dilakukan inisialisasi class fungsi/method init langsung dijalanakan
"""
p1.personal("daniel", 20)

p2 = Person()
p2.personal("bili", 30)

print(p1.x)  # mengambil variable dari attribut class

# mengambil variable dari method/fungsi dalam class
print(p1.name)
print(p1.age)

print(p2.name)
print(p2.age)

print(p1.__dict__)
print(p2.__dict__)
"""
nilai dalam class bertype dictionary
"""
