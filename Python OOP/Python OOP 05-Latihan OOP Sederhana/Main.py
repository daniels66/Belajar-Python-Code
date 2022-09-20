class Hero:
    # inisialisasi class
    def __init__(self, name, health, attackPower, armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang(self, com):
        print(self.name + " menyerang " + com.name)
        com.diserang(self, self.attackPower)
        """
        self menunjuk pada sniper variable
        self.attackPower menunjuk pada sniper.attackPower
        """

    def diserang(self, player, attackPower_lawan):
        """
        self menunjuk pada rikimaru variable
        player menunjuk pada sniper variable
        (self, self.attackPower) -> (player, attackPower_lawan)
        """
        print(self.name + " diserang " + player.name)
        attack_diterima = attackPower_lawan / self.armorNumber
        print("serangan terasa : " + str(attack_diterima))
        self.health -= attack_diterima
        print("darah " + self.name + " tersisa " + str(self.health))


sniper = Hero("sniper", 100, 10, 5)
rikimaru = Hero("rikimaru", 100, 20, 10)

sniper.serang(rikimaru)
print("\n")
sniper.serang(rikimaru)
print("\n")
