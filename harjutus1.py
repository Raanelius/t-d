import pygame
pygame.init()

# Ekraani seaded
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Harjutamine")

# Lisame pildi
bg = pygame.image.load("bg.jpg")
screen.blit(bg, [0, 0])
youWin = pygame.image.load("youwin2.png")
youWin = pygame.transform.scale(youWin, [300, 120])
screen.blit(youWin,[180,100])
pygame.display.flip()

# Mängutsükkel
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
