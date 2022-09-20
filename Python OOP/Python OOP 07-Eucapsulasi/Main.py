# eucapsulasi adalah membuat semua data pada class menjadi private
# apabila ingin mengambil private variabel menggunakan getter
# apabila ingin merubah/setting private variable menggunakan setter


from socket import herror


class Hero:
    __jumlah = 0

    def __init__(self, name, health, attackPower):
        self.__name = name
        self.__health = health
        self.__attPower = attackPower
        Hero.__jumlah += 1
        print("nama dari hero" + str(Hero.__jumlah) + " = ", self.getName())
        print("hero memiliki health =", self.getHealth())
        print("hero memiliki attack power =", self.getattPower(), "\n")

    # getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    def getattPower(self):
        return self.__attPower

    # setter
    def menyerang(self, lawan):
        print("hero " + self.getName() + " menyerang " + "hero " + lawan.getName())
        print(
            "menyerang dengan attack power",
            self.getattPower(),
        )
        lawan.diserang(self, self.getattPower())

    def diserang(self, lawan, serangPower):
        print(f"hero {self.getName()} diserang oleh hero {lawan.getName()}")
        self.__health -= serangPower
        print(f"sisa health hero {self.getName()} adalah = {self.getHealth()}\n")


# inisialisasi variable
hero1 = Hero("daniel", 100, 5)
hero2 = Hero("bili", 50, 10)
print(30 * "-")

# print(hero1.__name)
# print(hero2.__name)
"""
apabila ingin mengambil dengan cara diatas akan eror dikarenakan variable private,
harus membuat method terlebih dahulu dengan adanya return yang diinginkan,
baru dapat dipanggil nilai dalam variable private
"""

hero1.menyerang(hero2)
"""
apabila ingin merubah nilai private variable health dapat menggunakan setter,
harus membuat method terlebih dahulu (lihat method diserang())
"""
hero2.menyerang(hero1)
hero1.menyerang(hero2)
hero2.menyerang(hero1)
