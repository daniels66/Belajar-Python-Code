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

    player_img()
    pygame.display.update()
