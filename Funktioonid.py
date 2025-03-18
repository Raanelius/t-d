import pygame
import sys
import random

pygame.init()

# Värvid
red = [255, 0, 0]
lGreen = [153, 255, 153]

# Ekraani seaded
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Harjutamine")
screen.fill(lGreen)

# Funktsioonid
def drawHouse(x, y, width, height, screen, color):
    points = [
        (x, y - ((3 / 4.0) * height)), (x, y), (x + width, y),
        (x + width, y - (3 / 4.0) * height), (x, y - ((3 / 4.0) * height)),
        (x + width / 2.0, y - height), (x + width, y - (3 / 4.0) * height)
    ]
    lineThickness = 2
    pygame.draw.lines(screen, color, False, points, lineThickness)

# Joonistame maja
drawHouse(100, 400, 300, 200, screen, red)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
