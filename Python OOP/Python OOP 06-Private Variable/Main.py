class Hero:

    # class variabel
    jumlah = 0
    __privateJumlah = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

        # variabel instance private
        self.__private = "private"
        """
        variable instance private menggunakan __<nama> untuk pemakaiannya
        untuk variable private tidak dapat diambil nilainya
        """
        # variabel instance protected
        """
        variable instance protected menggunakan _<nama> untuk pemakaiannya
        perlakuan protected sama seperti variable biasa
        """
        self._protected = "protected"


lina = Hero("lina", 100)

print(lina.__dict__)
# print(lina.__private) # akan eror karena private tidak dapat diambil nilainya
print(lina._protected)
print(Hero.__dict__)
# print(Hero.__privateJumlah) # akan eror karena private tidak dapat diambil nilainya
