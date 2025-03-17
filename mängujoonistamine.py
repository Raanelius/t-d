import pygame
pygame.init()

#värvid
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine")
screen.fill(lGreen)

gameover = False

while not gameover:

    #Lisame pildid
    youWin = pygame.image.load("img/youwin.png")
    youWin = pygame.transform.scale(youWin, [300, 120])
    screen.blit(youWin,[180,100])

    pygame.display.flip()

pygame.quit()
