# getter dan setter dalam pyhton


class Hero:
    def __init__(self, nama, health) -> None:
        self.nama = nama
        self.__health = health
        # self.__info = (
        #     f"nama hero adalah = {self.nama} \nhero memili health = {self.__health}"
        # )

    @property
    def info(self):
        return f"nama hero adalah = {self.nama} \nhero memili health = {self.__health}"

    # membuat getter dan setter python
    @property
    def health(self):
        pass

    @health.getter
    def health(self):
        return self.__health

    @health.setter
    def health(self, input):
        self.__health = input

    @health.deleter
    def health(self):
        print("health di delate")
        self.__health = None


hero1 = Hero("daniel", 100)
print("@property".center(25, "-"))
print(hero1.info)
"""
client dapat merubah info dengan mudah padahal info dibuat agar tidak dapat dirubah,
apabila membuatnya menjadi private maka akan tidak bisa diakses, apabila mengakses dengan
getter dan setter maka akan membuat method juga, oleh karena itu lebih baik membuat
decorator property(@property) yang berguna untuk merubah method menjadi variable
"""
# hero1.info = "ayoo"
# print(hero1.info)
print(
    hero1.__dict__
)  # tidak terdapat variable info akan tetapi dapat mengambil info sebagai method
"""
keunggulan @property adalah apabila merubah variable dalam class akan langsung update
"""
hero1.nama = "bili"
print(hero1.info)
print(hero1.__dict__)

print("getter & setter".center(25, "-"))
print("health hero ", hero1.nama, "adalah =", str(hero1.health))
# merubah health hero
print(hero1.__dict__)
hero1.health = 40  # setter atau merubah nilai health
print("health hero ", hero1.nama, "adalah = ", str(hero1.health))
print(hero1.__dict__)

print("deleter".center(25, "-"))
"""
deleter digunakan untuk mendelete variable dalam class
"""
del hero1.health
print(hero1.__dict__)
