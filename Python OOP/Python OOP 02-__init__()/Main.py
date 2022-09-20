class Hero:  # template class
    """
    __init__ akan dijalankan pertama kali pada saat dilakukan inisialisasi class
    """

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


hero1 = Hero("daniel", 100, 10, 4)
hero2 = Hero("bili", 100, 15, 1)
hero3 = Hero("okti", 1000, 100, 0)

print(hero1.__dict__)  # mengambil semua variable dalam hero1
print(hero2.__dict__)
print(hero3.__dict__)
print("Hero1 nama =", hero1.name)  # mengambil variable teretentu dalam hero1
print("Hero2 nama =", hero2.name)
print("Hero3 nama =", hero3.name)
