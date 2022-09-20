# static dan class method dalam sebuah class
class Hero:
    __jumlah = 0

    def __init__(self, name):
        self.__name = name
        Hero.__jumlah += 1
        print("hero" + str(Hero.__jumlah) + " adalah =", self.__name)

    # hanya berlaku untuk objek
    def getHero1(self):
        return Hero.__jumlah

    # tidak berlaku untuk objek, berlaku untuk class
    def getHero2():
        return Hero.__jumlah

    # static method (decorator)
    # berlaku untuk objek dan class
    @staticmethod
    def getHero():
        return Hero.__jumlah

    @classmethod
    def getHero3(cls):
        return cls.__jumlah


hero1 = Hero("daniel")
# print(Hero.__jumlah) # akan eror apabila ingin mengambil variable private diluar class
# apabila menggunakan getter
# print(Hero.getHero1()) # akan eror dikarenakan hanya berlaku untuk objek
print(hero1.getHero1())  # getHero1() berlaku untuk objek
print(Hero.getHero2())  # getHero2() berlaku untuk class
# print(hero1.getHero2())  # akan eror dikarenakan hanya berlaku untuk class
"""
dapatkah mengambil getHero() yang berlaku untuk objek dan class??
bisa dengan menggunakan static method
"""
print(hero1.getHero())  # tidak akan eror dikarenakan static method
print(Hero.getHero())  # tidak akan eror dikarenakan static method
"""
selain static method ada juga class method yang berguna pada saat merubah nama class
    @staticmethod
    def getHero():
        return Hero.__jumlah
di static method apabila ingin merubah nama class maka nama class sebelumnya (Hero)
harus ikut dirubah, apabila tidak banyak tidak apa-apa, kalau banyak??
oleh karena itu menggunakan class method
    @classmethod
    def getHero(cls):
        return cls.__jumlah
    *cls dapat ditulis terserah
"""
hero2 = Hero("bili")
print(hero1.getHero3())
hero3 = Hero("okti")
print(Hero.getHero3())
