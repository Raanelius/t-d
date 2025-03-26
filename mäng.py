import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mäng")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

Mänja_suurus = 20
Mängja_x = WIDTH // 2
Mängja_y = HEIGHT // 2
Mängja_kiirus = 5
Mängja_värv = BLUE

palju_takistusi = 10
takisutste_suurus = 30
takistused = []
for _ in range(palju_takistusi):
    takistuse_x = random.randint(0, WIDTH - takisutste_suurus)
    takistused_y = random.randint(0, HEIGHT - takisutste_suurus)
    takistused.append(pygame.Rect(takistuse_x, takistused_y, takisutste_suurus, takisutste_suurus))

running = True
while running:
    pygame.time.delay(30)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        Mängja_x -= Mängja_kiirus
    if keys[pygame.K_RIGHT]:
        Mängja_x += Mängja_kiirus
    if keys[pygame.K_UP]:
        Mängja_y -= Mängja_kiirus
    if keys[pygame.K_DOWN]:
        Mängja_y += Mängja_kiirus

    Mänja_reageerib = pygame.Rect(Mängja_x, Mängja_y, Mänja_suurus, Mänja_suurus)
    
    for obs in takistused:
        if Mänja_reageerib.colliderect(obs):
            Mängja_värv = RED
            running = False
            break

    for obs in takistused:
        pygame.draw.rect(screen, BLACK, obs)
    
    pygame.draw.rect(screen, Mängja_värv, Mänja_reageerib)
    
    pygame.display.update()

pygame.quit()