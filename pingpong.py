import pygame
import random

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Palli ja aluse mäng")

BACKGROUND = (200, 200, 255)
TEXT_COLOR = (0, 0, 0)
font = pygame.font.SysFont(None, 36)

ball_img = pygame.image.load("ball.png")
paddle_img = pygame.image.load("pad.png")

BALL_WIDTH, BALL_HEIGHT = ball_img.get_size()
PADDLE_WIDTH, PADDLE_HEIGHT = paddle_img.get_size()

paddle_x = (WIDTH - PADDLE_WIDTH) // 2
paddle_y = int(HEIGHT / 1.5)
paddle_speed = 4
paddle_direction = 1

ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 3
ball_speed_y = 3

score = 0

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BACKGROUND)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    paddle_x += paddle_speed * paddle_direction
    if paddle_x <= 0 or paddle_x + PADDLE_WIDTH >= WIDTH:
        paddle_direction *= -1

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x <= 0 or ball_x + BALL_WIDTH >= WIDTH:
        ball_speed_x *= -1
    if ball_y <= 0:
        ball_speed_y *= -1
    if ball_y + BALL_HEIGHT >= HEIGHT:
        ball_speed_y *= -1
        score -= 1

    if (paddle_y < ball_y + BALL_HEIGHT < paddle_y + PADDLE_HEIGHT and
        paddle_x < ball_x + BALL_WIDTH and
        ball_x < paddle_x + PADDLE_WIDTH and
        ball_speed_y > 0):
        ball_speed_y *= -1
        score += 1

    screen.blit(paddle_img, (paddle_x, paddle_y))
    screen.blit(ball_img, (ball_x, ball_y))

    score_text = font.render(f"Punktid: {score}", True, TEXT_COLOR)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
