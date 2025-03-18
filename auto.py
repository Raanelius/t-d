import pygame
import random

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Auto Mäng")

background = pygame.image.load("bg_rally.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

red_car = pygame.image.load("f1_red.png")
red_car = pygame.transform.scale(red_car, (50, 100))
red_car_x = WIDTH // 2 - 25
red_car_y = HEIGHT - 120

blue_car = pygame.image.load("f1_blue.png")
blue_car = pygame.transform.scale(blue_car, (50, 100))

blue_cars = []
for _ in range(3):
    x_pos = random.randint(100, WIDTH - 100)
    y_pos = random.randint(-400, -50)
    speed = random.randint(2, 5)
    blue_cars.append([x_pos, y_pos, speed])

score = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    screen.blit(background, (0, 0))
    screen.blit(red_car, (red_car_x, red_car_y))
    
    for car in blue_cars:
        car[1] += car[2]
        if car[1] > HEIGHT:
            car[1] = random.randint(-400, -50)
            car[0] = random.randint(100, WIDTH - 100)
            car[2] = random.randint(2, 5)
            score += 1
        screen.blit(blue_car, (car[0], car[1]))
    
    score_text = font.render("Skoor: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.time.delay(30)

pygame.quit()
