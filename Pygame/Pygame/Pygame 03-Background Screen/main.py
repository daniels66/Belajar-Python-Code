import pygame

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

# set background dengan gambar
background = pygame.image.load("gambar/background.png")

# looping game
while True:
    # set background dengan warna tertentu (R,G,B)
    screen.fill((255, 0, 0))
    # set background dengan gambar
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            """
            game tidak akan tutup secara otomatis dan dapat di close
            """

    pygame.display.update()
    """
    update selalu terletak pada akhir loop game yang digunakan untuk update
    setiap perubahan yang terjadi pada loop game
    """
