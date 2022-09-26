import pygame

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

# fungsi nenambahkan gambar player
def player_img():
    screen.blit(player, (player_x, player_y))


# fungsi movement keyboard
def movement_key():
    # setting agar keyboard dapat digerakkan
    if event.type == pygame.KEYDOWN:
        print("keyboard ditekan")
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            print("keyboard arrow left ditekan")
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            print("keyboard arrow right ditekan")
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            print("keyboard arrow up ditekan")
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            print("keyboard arrow down ditekan")
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
            print("keyboard dilepas")


# looping game
while True:
    # set background dengan warna tertentu (R,G,B)
    screen.fill((255, 0, 0))
    # set background dengan gambar
    screen.blit(background, (0, 0))

    # setting game supaya tidak flash dan dapat di quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        movement_key()

    player_img()
    pygame.display.update()
