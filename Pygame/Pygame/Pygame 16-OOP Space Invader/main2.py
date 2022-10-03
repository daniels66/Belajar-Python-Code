import pygame, sys, random, math
from pygame import mixer

# inisialisasi pygame
pygame.init()

# untuk mengatur lebar layar pygame
lebar_x = 800
tinggi_y = 600
screen = pygame.display.set_mode((lebar_x, tinggi_y))

# mengatur judul dan icon pygame
pygame.display.set_caption("Space Invader")  # judul game
icon = pygame.image.load("gambar/ufo.png")  # letak icon
pygame.display.set_icon(icon)  # tampilkan icon
# set musik dalam background
mixer.music.load("sound/background.wav")
mixer.music.play(-1)  # -1 digunakan agar suara berulang terus menerus

# set background dengan gambar
background = pygame.image.load("gambar/background.png")

# membuat class player
class Player:
    def __init__(self, gambar, posisix, posisiy, ubahx, ubahy):
        self.gambar = gambar
        self.posisix = posisix
        self.posisiy = posisiy
        self.ubahx = ubahx
        self.ubahy = ubahy

    # fungsi menambahkan gambar player
    def pict_player(self):
        screen.blit(self.gambar, (self.posisix, self.posisiy))

    # fungsi movement keyboard
    def keyboard_move(self):
        # setting agar keyboard dapat digerakkan
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.ubahx = -3
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.ubahx = 3
            elif event.key == pygame.K_SPACE:
                if bullet.status_peluru == "ready":
                    # set musik ketika space diteken
                    bullet_sound = mixer.Sound("sound/laser.wav")
                    bullet_sound.play()
                    bullet.posisix = pemain.posisix
                    bullet.bullet_fire(bullet.posisix, bullet.posisiy)
        elif event.type == pygame.KEYUP:
            if (
                event.key == pygame.K_LEFT
                or event.key == pygame.K_RIGHT
                or event.key == pygame.K_a
                or event.key == pygame.K_d
            ):
                self.ubahx = 0

    # fungsi membatasi pergerakan player dalam screen
    def player_max(self):
        if self.posisix <= 0:
            self.posisix += 3  # ditambahakan 3 angka supaya tidak terjadi eror saat melintasi pojokan
        elif self.posisix >= (lebar_x - 64):
            self.posisix = lebar_x - 67


# membuat class enemy
class Enemy:
    def __init__(self, gambar, posisix, posisiy, ubahx, ubahy):
        self.gambar = gambar
        self.posisix = posisix
        self.posisiy = posisiy
        self.lawan_ubahx = ubahx
        self.lawan_ubahy = ubahy

    # fungsi menambahkan gambar enemy
    def pict_enemy(self):
        screen.blit(self.gambar, (self.posisix, self.posisiy))

    # fungsi enemy movemnt
    def enemy_movement(self):
        if self.posisix <= 0:
            self.lawan_ubahx = 2
            self.posisiy += self.lawan_ubahy
        elif self.posisix >= (lebar_x - 64):
            self.lawan_ubahx = -2
            self.posisiy += self.lawan_ubahy


# membuat class peluru
class Peluru:
    def __init__(self, gambar, posisix, posisiy, ubahy, status):
        self.gambar = gambar
        self.posisix = posisix
        self.posisiy = posisiy
        self.peluru_ubahy = ubahy
        self.status_peluru = status

    # fungsi menambahkan gambar bullet
    def bullet_fire(self, x, y):
        self.status_peluru = "fire"
        screen.blit(self.gambar, (x + 16, y + 10))

    # fungsi bullet movement
    def bullet_movement(self):
        """
        ready -> tidak menampilkan bullet pada screen
        fire -> bullet sedang bergerak
        """
        if self.posisiy <= -30:
            self.posisiy = 470
            self.status_peluru = "ready"
        elif self.status_peluru == "fire":
            self.bullet_fire(self.posisix, self.posisiy)
            self.posisiy -= self.peluru_ubahy


# fungsi apabila terjadi tabrakan antara dua buah benda
def tabrakan(x1, y1, x2, y2):
    tabrakan = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
    if tabrakan < 27:
        return True
    else:
        return False


# fungsi setelah terjadi tabrakan
def tabrak(tabrak):
    if tabrak:
        bullet.posisiy = 470
        bullet.status_peluru = "ready"
        tabrak_sound = mixer.Sound("sound/explosion.wav")
        tabrak_sound.play()
        lawan.posisix = random.randint(0, 735)
        lawan.posisiy = random.randint(30, 120)


# gambar pemain
pict = pygame.image.load("gambar/player.png")
pemain = Player(pict, 375, 470, 0, 0)

# gambar enemy
lawan = pygame.image.load("gambar/enemy.png")
lawanx = random.randint(0, 735)
lawany = random.randint(30, 120)
# membuat variable perubahan player x dan y
if lawanx > 400:
    lawan_ubahx = -2
elif lawanx < 400:
    lawan_ubahx = 2
lawan_ubahy = 30
lawan = Enemy(lawan, lawanx, lawany, lawan_ubahx, lawan_ubahy)

# gambar peluru
bullet = pygame.image.load("gambar/bullet.png")
bullet = Peluru(bullet, 0, 470, 4, "ready")

# looping game
while True:
    # set background dengan gambar
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            False
            sys.exit()
        pemain.keyboard_move()

    bullet.bullet_movement()

    pemain.pict_player()
    pemain.posisix += pemain.ubahx
    pemain.player_max()

    lawan.enemy_movement()
    lawan.posisix += lawan.lawan_ubahx
    lawan.pict_enemy()

    duar = tabrakan(lawan.posisix, lawan.posisiy, bullet.posisix, bullet.posisiy)
    tabrak(duar)

    pygame.display.update()
