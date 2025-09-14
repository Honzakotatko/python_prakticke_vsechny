import pygame

# Inicializace pygame
pygame.init()

# Nastavení okna
SIRKA, VYSKA = 400, 300
OKNO = pygame.display.set_mode((SIRKA, VYSKA))
pygame.display.set_caption("Maturita")

# Nastavení hráče
HRAC_VELIKOST = 25
hrac_x, hrac_y = SIRKA // 2, VYSKA // 2
rychlost = 5  # Rychlost pohybu
BARVA_HRACE = (0, 255, 0)  # Zelená

# Nastavení FPS
FPS = 165
hodiny = pygame.time.Clock()

# Herní smyčka
bezi = True
while bezi:
    hodiny.tick(FPS)  # Limit FPS

    # Zpracování událostí
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            bezi = False

    # Pohyb hráče
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:  # Nahoru
        hrac_y -= rychlost
    if keys[pygame.K_s]:  # Dolů
        hrac_y += rychlost
    if keys[pygame.K_a]:  # Doleva
        hrac_x -= rychlost
    if keys[pygame.K_d]:  # Doprava
        hrac_x += rychlost

    # Aktualizace okna
    OKNO.fill((0, 0, 0))  # Černé pozadí
    pygame.draw.rect(OKNO, BARVA_HRACE, (hrac_x, hrac_y, HRAC_VELIKOST, HRAC_VELIKOST))  # Hráč
    pygame.display.update()

# Ukončení pygame
pygame.quit()
