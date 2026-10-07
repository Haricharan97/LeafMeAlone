import pygame
import random

pygame.init()

width = 500
height = 700

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

lx = 200
ly = 180

up = 2
move = 5
ty = 60

sponges = [
    [random.randint(0, 430), 750],
    [random.randint(0, 430), 1000],
    [random.randint(0, 430), 1250]
]

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        lx -= move

    if keys[pygame.K_RIGHT]:
        lx += move

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

        for s in sponges:

            s[1] -= up

            pygame.draw.rect(
                screen,
                (220, 190, 70),
                (s[0], s[1], 70, 50)
            )

            if s[1] < -50:

                s[1] = 750
                s[0] = random.randint(0, width - 70)

    pygame.display.update()

    clock.tick(60)

pygame.quit()