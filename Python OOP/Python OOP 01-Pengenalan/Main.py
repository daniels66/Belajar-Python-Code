class Hero:  # template classs
    pass


hero1 = Hero()  # inisialisasi class menjadi objeck
hero2 = Hero()
hero3 = Hero()

hero1.name = "sniper"  # menambahkan variable dalam class
hero1.health = 100

hero2.name = "sven"
hero2.health = 200

hero3.name = "ucup"
hero3.health = 1000

print(hero1)
print(hero1.__dict__)  # memanggil semua variable dalam class bentuk dictionary
print(hero1.name)  # mengambil variable tertentu dalam class
