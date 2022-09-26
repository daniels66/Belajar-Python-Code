import pygame, sys
import random

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
enemy = pygame.image.load("gambar/enemy.png")
enemy_x = random.randint(0, 800)
enemy_y = random.randint(30, 120)
# membuat variable perubahan player x dan y
if enemy_x > 400:
    enemyx_change = -2
elif enemy_x < 400:
    enemyx_change = 2
enemyy_change = 30

# fungsi menambahkan gambar player
def player_img(x, y):
    screen.blit(player, (x, y))


# fungsi menambahkan gambar enemy
def enemy_img(x, y):
    screen.blit(enemy, (x, y))


# fungsi movement keyboard
def movement_key():
    # setting agar keyboard dapat digerakkan
    if event.type == pygame.KEYDOWN:
        global playerx_change, playery_change
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            playerx_change = -3
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            playerx_change = 3
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            playery_change = -3
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            playery_change = 3
    elif event.type == pygame.KEYUP:
        if (
            event.key == pygame.K_LEFT
            or event.key == pygame.K_RIGHT
            or event.key == pygame.K_UP
            or event.key == pygame.K_DOWN
            or event.key == pygame.K_a
            or event.key == pygame.K_d
            or event.key == pygame.K_w
            or event.key == pygame.K_s
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


# fungsi enemy movemnt
def enemy_movement():
    global enemy_x, enemyx_change, enemy_y, enemyy_change
    if enemy_x <= 0:
        enemyx_change = 2
        enemy_y += enemyy_change
    elif enemy_x >= (lebar_x - 64):
        enemyx_change = -2
        enemy_y += enemyy_change


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

    player_x += playerx_change
    player_y += playery_change
    move_pic_max()

    enemy_x += enemyx_change
    enemy_movement()

    player_img(player_x, player_y)
    enemy_img(enemy_x, enemy_y)
    pygame.display.update()
