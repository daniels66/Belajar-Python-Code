import pygame, sys

# inisialisasi pygame
pygame.init()

# untuk mengatur lebar layar pygame
lebar = 400
tinggi = 500
screen = pygame.display.set_mode(
    (lebar, tinggi)
)  # akan flash (buka dan tutup game dalam satu waktu)

# looping game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            """
            game tidak akan tutup secara otomatis dan dapat di close
            """
