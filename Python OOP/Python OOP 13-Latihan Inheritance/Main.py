from Hero import HeroIntelligent, HeroStrength


lina = HeroIntelligent("lina")
slardar = HeroStrength("slardar")

lina.show_info()
slardar.show_info()
print(30 * "-")

lina.gainExp = 50
slardar.gainExp = 75
lina.show_info()
slardar.show_info()
print(30 * "-")

lina.gainExp = 100
slardar.gainExp = 75
lina.show_info()
slardar.show_info()
print(30 * "-")

lina.gainExp = 50
slardar.gainExp = 75
lina.show_info()
slardar.show_info()
print(30 * "-")
