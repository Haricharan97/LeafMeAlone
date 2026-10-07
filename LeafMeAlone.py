import pygame

pygame.init()

width = 500
height = 700

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

lx = 200
ly = 180

up = 2
ty = 60

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill((180, 220, 250))

    pygame.draw.rect(
        screen,
        (120, 75, 40),
        (150, ty + 220, 200, height - (ty + 220))
    )

    pygame.draw.rect(
        screen,
        (40, 150, 60),
        (50, ty, 400, 180)
    )

    pygame.draw.rect(
        screen,
        (40, 150, 60),
        (0, ty + 60, 500, 180)
    )

    pygame.draw.rect(
        screen,
        (60, 180, 70),
        (lx, ly, 100, 50)
    )

    if ly < 400:
        ly += up

    else:
        ty -= up

    pygame.display.update()

    clock.tick(60)

pygame.quit()