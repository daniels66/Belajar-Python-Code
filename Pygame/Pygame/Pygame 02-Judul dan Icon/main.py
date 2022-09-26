import pygame, sys

# inisialisasi pygame
pygame.init()

# untuk mengatur lebar layar pygame
lebar = 800
tinggi = 600
screen = pygame.display.set_mode(
    (lebar, tinggi)
)  # akan flash (buka dan tutup game dalam satu waktu)

# mengatur judul dan icon pygame
pygame.display.set_caption("Space Invader")  # judul game
icon = pygame.image.load("gambar/ufo.png")  # letak icon
pygame.display.set_icon(icon)  # tampilkan icon

# looping game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            """
            game tidak akan tutup secara otomatis dan dapat di close
            """
