# multiple inheritance
class A:
    def method_A(self):
        print("ini adalah method A")


class B:
    def method_B(self):
        print("ini adalah method B")


class C(A, B):  # akan copy semua isi dalam class a dan b
    pass


class D:
    def method(self):
        print("ini adalah method D")


class E:
    def method(self):
        print("ini adalah method E")


class F(D, E):
    """
    apabila nama method sama maka akan memanggil, method F terlebih dahulu,
    lalu method D, lalu method E (sesuai urutan)
    """

    # def method(self):
    # print("ini adalah method E")
    pass


# diamond problem
# (sebenarnya tidak terlalu disarankan karena sangat bergantung pada class)
"""
    G
   / \
  H   I
   \ /
    J

apabila nama method sama, mana yang akan didulukan??
apbila memanggil method J,  maka akan menjalankan method J dahulu, apabila method J tidak ada,
maka akan menjalankan method H, apabila method H tidak ada, maka akan menjalankan method I,
apabila method I tidak ada, maka akan menjalankan method G
"""


class H:
    # def show(self):
    #     print("ini adalah show H")
    pass


class I:
    def show(self):
        print("ini adalah show I")


class G(H, I):
    def show(self):
        print("ini adalah show G")


class J(H, I):
    # def show(self):
    #     print("ini adalah show J")
    pass


print("Multiple Inheritance".center(30, "-"))
objek1 = C()
objek1.method_A()  # akan memanggil method dalam kelas a
objek1.method_B()  # akan memanggil method dalam kelas b

print("Method Resolution Order".center(30, "-"))
objek2 = F()
objek2.method()

print("Diamond Problem".center(30, "-"))
objek3 = J()
objek3.show()
