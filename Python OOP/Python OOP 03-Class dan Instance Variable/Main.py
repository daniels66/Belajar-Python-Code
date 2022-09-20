class Hero:  # template
    # class variabel adalah variable yang berada pada class utama
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variabel adalah variable yang berada pada suatu fungsi
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        """
        self mengacu pada inisialisasi class
        self.name = hero1.name , dll
        """
        Hero.jumlah += 1
        print("membuat Hero dengan nama " + inputName)


hero1 = Hero("daniels", 100, 10, 4)
print(Hero.jumlah)
hero2 = Hero("bili", 100, 15, 1)
print(Hero.jumlah)
hero3 = Hero("okti", 1000, 100, 0)
print(Hero.jumlah)
