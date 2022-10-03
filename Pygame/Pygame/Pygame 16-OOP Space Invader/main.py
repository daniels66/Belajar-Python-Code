import pygame, sys
import random
import math
from pygame import mixer

# inisialisasi pygame
pygame.init()

# untuk mengatur lebar layar pygame
lebar_x = 800
tinggi_y = 600
screen = pygame.display.set_mode(
    (lebar_x, tinggi_y)
)  # akan flash (buka dan tutup game dalam satu waktu)

# mengatur judul dan icon pygame
pygame.display.set_caption("Space Invader")  # judul game
icon = pygame.image.load("gambar/ufo.png")  # letak icon
pygame.display.set_icon(icon)  # tampilkan icon

# set musik dalam background
mixer.music.load("sound/background.wav")
mixer.music.play(-1)  # -1 digunakan agar suara berulang terus menerus


# set background dengan gambar
background = pygame.image.load("gambar/background.png")

# set gambar dalam screen
player = pygame.image.load("gambar/player.png")
player_x = 375
player_y = 470
# membuat variable perubahan player x dan y
playerx_change = 0
playery_change = 0

# set enemy dalam screen
enemy = []
enemy_x = []
enemy_y = []
enemyy_change = []
enemyx_change = []
banyak_enemy = 6


for i in range(banyak_enemy):
    enemy.append(pygame.image.load("gambar/enemy.png"))
    enemy_x.append(random.randint(0, 735))
    enemy_y.append(random.randint(30, 120))
    # membuat variable perubahan player x dan y
    if enemy_x[i] > 400:
        enemyx_change.append(-2)
    elif enemy_x[i] < 400:
        enemyx_change.append(2)
    enemyy_change.append(30)

# set bullet dalam screen
bullet = pygame.image.load("gambar/bullet.png")
bullet_x = 0
bullet_y = 470
bullety_change = 4
bullet_state = "ready"
"""
ready -> tidak menampilkan bullet pada screen
fire -> bullet sedang bergerak
"""
# set score dalam screen
score_value = 0
set_font = pygame.font.Font("freesansbold.ttf", 25)
set_font_x = 0
set_font_y = 10

# game over font
over_font = pygame.font.Font("freesansbold.ttf", 64)

# fungsi menambahkan gambar player
def player_img(x, y):
    screen.blit(player, (x, y))


# fungsi menambahkan gambar enemy
def enemy_img(x, y, i):
    screen.blit(enemy[i], (x, y))


# fungsi menambahkan gambar bullet
def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 16, y + 10))


# fungsi menampilkan score
def tampil_score(x, y):
    score = set_font.render("Score = " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


# fungsi menampilkan game over
def game_over():
    over = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over, (200, 250))


# fungsi movement keyboard
def movement_key():
    # setting agar keyboard dapat digerakkan
    if event.type == pygame.KEYDOWN:
        global playerx_change, playery_change, bullet_x
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            playerx_change = -3
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            playerx_change = 3
        elif event.key == pygame.K_SPACE:
            if bullet_state == "ready":
                # set musik ketika space diteken
                bullet_sound = mixer.Sound("sound/laser.wav")
                bullet_sound.play()
                bullet_x = player_x
                bullet_fire(bullet_x, bullet_y)
    elif event.type == pygame.KEYUP:
        if (
            event.key == pygame.K_LEFT
            or event.key == pygame.K_RIGHT
            or event.key == pygame.K_a
            or event.key == pygame.K_d
        ):
            playerx_change = 0
            playery_change = 0


# fungsi membatasi pergerakan gambar dalam screen
def move_pic_max():
    global player_x, player_y
    if player_x <= 0:
        player_x += (
            3  # ditambahakan 3 angka supaya tidak terjadi eror saat melintasi pojokan
        )
    elif player_x >= (lebar_x - 64):
        player_x = lebar_x - 67
    elif player_y <= 0:
        player_y += 3
    elif player_y >= (tinggi_y - 64):
        player_y = tinggi_y - 67


# fungsi bullet movement
def bullet_movement():
    global bullet_y, bullet_state
    if bullet_y <= -30:
        bullet_y = 470
        bullet_state = "ready"
    elif bullet_state == "fire":
        bullet_fire(bullet_x, bullet_y)
        bullet_y -= bullety_change


# fungsi apabila terjadi tabrakan antara dua buah benda
def tabrakan(enemy_x, enemy_y, bullet_x, bullet_y):
    tabrakan = math.sqrt(
        (math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2))
    )
    if tabrakan < 27:
        return True
    else:
        return False


# fungsi setelah terjadi tabrakan
def tabrak(tabrak):
    global bullet_y, bullet_state, enemy_x, enemy_y, score_value
    if tabrak:
        bullet_y = 470
        bullet_state = "ready"
        score_value += 1
        tabrak_sound = mixer.Sound("sound/explosion.wav")
        tabrak_sound.play()
        enemy_x[i] = random.randint(0, 735)
        enemy_y[i] = random.randint(30, 120)


# looping game
while True:
    # set background dengan warna tertentu (R,G,B)
    screen.fill((255, 0, 0))
    # set background dengan gambar
    screen.blit(background, (0, 0))

    # setting game supaya tidak flash dan dapat di quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            False
            sys.exit()
        movement_key()

    player_img(player_x, player_y)

    player_x += playerx_change
    player_y += playery_change
    move_pic_max()

    # enemy movement
    for i in range(banyak_enemy):

        # Game Over
        if enemy_y[i] > 440:
            for j in range(banyak_enemy):
                enemy_y[j] = 2000
            game_over()
            break

        enemy_x[i] += enemyx_change[i]
        if enemy_x[i] <= 0:
            enemyx_change[i] = 2
            enemy_y[i] += enemyy_change[i]
        elif enemy_x[i] >= (lebar_x - 64):
            enemyx_change[i] = -2
            enemy_y[i] += enemyy_change[i]

        duar = tabrakan(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        tabrak(duar)

        enemy_img(enemy_x[i], enemy_y[i], i)

    bullet_movement()
    tampil_score(set_font_x, set_font_y)
    pygame.display.update()
