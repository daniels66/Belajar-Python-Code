class Hero:
    # class variabel
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    # void function, method tanpa return, tanpa argumen
    def siapa(self):
        print("namaku adalah " + self.name)
        print("aku memiliki health = ", self.health)

    # method atau fungsi dengan argumen, tanpa return
    def healthUp(self, up):
        print("anda menerima health sebanyak =", up)
        self.health += up

    # method atau fungsi dengan return
    def getHealth(self):
        return self.health


hero1 = Hero("daniel", 100, 10, 5)
hero2 = Hero("bili", 90, 5, 10)

hero1.siapa()
hero1.healthUp(10)

print("health terakhir anda = ", hero1.getHealth())
