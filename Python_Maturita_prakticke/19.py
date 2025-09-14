import pygame

# Inicializace
pygame.init()
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Čtverec WSAD")

# Barvy a čtverec
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
x, y = 0, 0
size = 50
speed = 0.1

# Hlavní smyčka
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ovládání
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and y > 0:
        y -= speed
    if keys[pygame.K_s] and y < HEIGHT - size:
        y += speed
    if keys[pygame.K_a] and x > 0:
        x -= speed
    if keys[pygame.K_d] and x < WIDTH - size:
        x += speed

    # Kreslení
    window.fill(WHITE)
    pygame.draw.rect(window, BLUE, (x, y, size, size))
    pygame.display.update()

pygame.quit()