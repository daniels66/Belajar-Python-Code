# magic method

"""
magic method adalah method spesial yang namanya diawali dan diakhiri dengan dobel underscore.
contoh :
__init__
__dict__
dll
untuk lihat lebih lengkap magic method cek dokumentasinya
https://docs.python.org/3/reference/datamodel.html#special-method-names

"""


class Mobil:

    # magic method
    def __init__(
        self, nama, tahun
    ):  # digunakan untuk menjalakan awal program saat inisialisasi class
        self.nama = nama
        self.tahun = tahun

    def __repr__(
        self,
    ):  # digunakaan pada saat debug program, akan tetapi lebih baik menggunakan __str__
        return "Debug - Mobil: {} dengan tahun: {}".format(self.nama, self.tahun)

    def __str__(self):
        return "Mobil: {} dengan tahun: {}".format(self.nama, self.tahun)

    @property
    def __dict__(self):
        return "objek ini mempunyai nama dan tahun"


mobil1 = Mobil("Fortuner", 2020)
mobil2 = Mobil("Xpander", 2021)
print(mobil1)
print(mobil2)
""" 
kegunaan magic method __str__ dan __repr__
pada saat print inisialisai class yang biasanya akan begini
<__main__.Mobil object at 0x7f5b7fe88310>
dapat dirubah menjadi yang diinginkan
dan dapat mengakses nilai dalam __init__
"""
print(mobil1.__dict__)
""" 
kegunaan magic method __dict__
dapat merubah dictionary menjadi yang diinginkan 
"""
