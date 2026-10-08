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

hits = 0

start = False
pause = False
over = False 

font = pygame.font.Font(None, 40)

sw = 80
sh = 50

sponges = [
    [random.randint(0, width - sw), 750],
    [random.randint(0, width - sw), 1000],
    [random.randint(0, width - sw), 1250]
]

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                if start == False:
                    start = True

                elif over == True:
                    lx = 200
                    ly = 180
                    ty = 60
                    hits = 0

                    over = False
                    pause = False

                    sponges = [
                        [random.randint(0, width - sw), 750],
                        [random.randint(0, width - sw), 1000],
                        [random.randint(0, width - sw), 1250]
                    ]

                else:

                    if pause == False:
                        pause = True
                    else:
                        pause = False

    if start == True and pause == False and over == False:

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            lx -= move

        if keys[pygame.K_RIGHT]:
            lx += move

        if lx < 0:
            lx = 0

        if lx > 400:
            lx = 400

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

    if hits == 0:
        leaf_color = (60, 180, 70)

    elif hits == 1:
        leaf_color = (90, 165, 60)

    elif hits == 2:
        leaf_color = (120, 145, 50)

    elif hits == 3:
        leaf_color = (160, 110, 45)

    elif hits == 4:
        leaf_color = (180, 90, 40)

    else:
        leaf_color = (120, 65, 30)

    pygame.draw.rect(
        screen,
        leaf_color,
        (lx, ly, 100, 50)
    )

    if start == True and pause == False and over == False:

        if ly < 400:
            ly += up

        else:
            ty -= up

            for s in sponges:

                s[1] -= up

                pygame.draw.rect(
                    screen,
                    (220, 190, 70),
                    (s[0], s[1], sw, sh)
                )

                leaf = pygame.Rect(
                    lx,
                    ly,
                    100, 
                    50
                )

                sponge = pygame.Rect(
                    s[0],
                    s[1],
                    sw,
                    sh
                )

                if leaf.colliderect(sponge):
                    hits +=1

                    far = max(
                        sponges[0][1],
                        sponges[1][1],
                        sponges[2][1]
                    )

                    s[1] = far + random.randint(220, 300)
                    s[0] = random.randint(0, width - sw)

                    if hits >= 5:
                        hits = 5
                        over = True

                if s[1] < -sh:

                    far = max(
                        sponges[0][1],
                        sponges[1][1],
                        sponges[2][1]
                    )

                    s[1] = far + random.randint(220, 300)
                    s[0] = random.randint(0, width - sw)

    if pause == True or over == True:

        if ly >= 400:

            for s in sponges:

                pygame.draw.rect(
                    screen,
                    (220, 190, 70),
                    (s[0], s[1], sw, sh)
                )

                pygame.draw.circle(
                    screen,
                    (180, 150, 50),
                    (s[0] + 20, s[1] + 15),
                    6
                )

                pygame.draw.circle(
                    screen,
                    (180, 150, 50),
                    (s[0] + 55, s[1] + 30),
                    7
                )

                pygame.draw.circle(
                    screen,
                    (180, 150, 50),
                    (s[0] + 35, s[1] + 38),
                    5
                )

    hit_text = font.render(
        "Hits: " + str(hits) + "/5",
        True,
        (0, 0, 0)
    )

    screen.blit(hit_text, (15, 15))

    if start == False:

        start_text = font.render(
            "PESS SPACE TO START",
            True,
            (0, 0, 0)
        )

        screen.blit(start_text, (85, 330))

    if pause == True:

        pause_text = font.render(
            "PAUSED",
            True,
            (0, 0, 0)
        )

        screen.blit(pause_text, (190, 300))

        space_text = font.render(
                "SPACE TO CONTINUE",
                True,
                (0, 0, 0)
            )

        screen.blit(space_text, (105, 350))

    if over == True:
        game_text = font.render(
            "GAME OVER",
            True,
            [0, 0, 0]
        )

        screen.blit(game_text, (165, 300))

        restart_text = font.render(
            "SPACE TO RESTART",
            True,
            (0, 0, 0)
        )

        screen.blit(restart_text, (115, 350))

    pygame.display.update()

    clock.tick(60)

pygame.quit()