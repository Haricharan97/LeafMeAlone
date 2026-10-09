import pygame
import random
import math

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

landed = False
ground = 650
fall = 0

clear = False

hit_time = 0
end_speed = 10

dry = 0
swing = 0

fallo = lx
falle = 0

font = pygame.font.Font(None, 40)

sw = 80
sh = 50

score = 0
coins = 0

level = 1

coin_x = random.randint(20, width - 20)
coin_y = 900

coin_type = 1

sponges = [
    [random.randint(0, width - sw), 750],
    [random.randint(0, width - sw), 950],
    [random.randint(0, width - sw), 1150],
    [random.randint(0, width - sw), 1350],
    [random.randint(0, width - sw), 1550]
]

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                if over == True:

                    if landed == True:
                        lx = 200
                        ly = 180
                        ty = 60

                        hits = 0
                        score = 0
                        coins = 0

                        level = 1
                        up = 2

                        coin_x = random.randint(25, width - 25)
                        coin_y = 900
                        coin_type = 1

                        over = False
                        pause = False

                        landed = False
                        fall = 0
                        clear = False
                        hit_time = 0
                        dry = 0
                        swing = 0
                        fallo = lx
                        falle = 0

                        sponges = [
                            [random.randint(0, width - sw), 750],
                            [random.randint(0, width - sw), 950],
                            [random.randint(0, width - sw), 1150],
                            [random.randint(0, width - sw), 1350],
                            [random.randint(0, width - sw), 1550]
                        ]

                elif start == False:
                    
                    start = True
                    pause = False

                else:
                    pause = not pause

    if score < 30:

        level = 1
        up = 2

    elif score < 70:

        level = 2
        up = 3

    elif score < 120:

        level = 3
        up = 4

    else:

        level = 4
        up = 5

    if hit_time > 0 and pause == False and over == False:

        hit_time -= 1

    if dry > 0 and pause == False and over == False:
        dry -= 1

    if start == True and pause == False and over == False:

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            lx -= move

        if keys[pygame.K_RIGHT]:
            lx += move

        if lx < 0:
            lx = 0

        if lx > width - 100:
            lx = width - 100

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

    if over == True:

        clear = True

        for s in sponges:

            s[1] -= end_speed

            if s[1] + sh > 0 and s[1] < height:
                clear = False

                s[1] -= end_speed

                if s[1] + sh > 0 and s[1] < height:
                    clear = False

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

        if coin_y > -30 and coin_y <= height:

            clear = False

            coin_y -= end_speed

            if coin_type == 1:
                pygame.draw.circle(
                    screen,
                    (255, 220, 40),
                    (coin_x, int(coin_y)),
                    15
                )

            else:

                pygame.draw.circle(
                    screen,
                    (255, 140, 30),
                    (coin_x, int(coin_y)),
                    22
                )

        if landed == False:

            falle += 1
            swing += 0.115

            fall += 0.045

            if fall > 4.5:
                fall = 4.5

            ly += fall

            rem = max(0, (ground - 50 - ly) / 200)
            amp = 12 + 28 * min(1, rem)

            lx = (
                fallo + math.sin(swing) * amp
                + math.sin(swing * 0.43) * 12
            )

            lx = max(0, min(width - 100, lx))

            if ly >= ground - 50:

                ly = ground - 50
                landed = True
                fall = 0

        if clear == True:

            pygame.draw.rect(
                screen,
                (70, 140, 60),
                (0, ground, width, 50)
            )

    draw_x = lx
    draw_color = leaf_color

    if over == True:

        draw_x = lx

    if dry > 0 and over == False and pause == False:

        shake = math.sin(dry * 0.5) * 5

        draw_x = lx + shake

        fade = abs(math.sin(dry * 0.12))

        draw_color = (
            int(leaf_color[0] + (190 - leaf_color[0]) * fade),
            int(leaf_color[1] + (110 - leaf_color[1]) * fade),
            int(leaf_color[2] + (40 - leaf_color[2]) * fade)
        )



    if dry > 0 and over == False and pause == False:

        if hits >= 4:

            dry_text = font.render(
                "ONE MORE HIT!",
                True,
                (0, 0, 0)
            )

            screen.blit(
                dry_text,
                (140, 330)
            )

        else:

            dry_text = font.render(
                "GETTING DRY!",
                True,
                (0, 0, 0)
            )

            screen.blit(
                dry_text,
                (145, 330)
            )

    if start == True and pause == False and over == False:

        if ly < 400:

            ly = min(400, ly + up)

        else:
            
            ty -= up

            for s in sponges:

                s[1] -= up

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

                if leaf.colliderect(sponge) and hit_time == 0:
                    hits +=1
                    hit_time = 45

                    if hits < 5:
                        dry = 75

                    if hits >= 5:

                        hits = 5
                        over = True

                        fall = 0
                        swing = 0
                        falle = 0
                        fallo = lx

                        dry = 0
                        clear = False

                        break

                    far = height

                    for other in sponges:

                        if other[1] > far:
                            far = other[1]

                    s[1] = far + random.randint(170, 230)
                    s[0] = random.randint(0, width - sw)

                    while abs(s[0] - coin_x) < 100 and abs(s[1] - coin_y) < 100:

                        s[0] = random.randint(
                            0, 
                            width - sw
                        )

                if s[1] < -sh:

                    score += 1

                    far = height

                    for other in sponges:

                        if other[1] > far:
                            far = other[1]

                    s[1] = far + random.randint(170, 230)
                    s[0] = random.randint(0, width - sw)

                    while abs(s[0] - coin_x) < 100 and abs(s[1] - coin_y) < 100:

                        s[0] = random.randint(
                            0, 
                            width - sw
                        )

            if over == False:
            
                coin_y -= up

                if coin_type == 1:

                    coin_size = 15

                else:
                    coin_size = 22

                coin_box = pygame.Rect(
                    coin_x - coin_size,
                    coin_y - coin_size,
                    coin_size * 2,
                    coin_size * 2
                )

                leaf = pygame.Rect(
                    lx,
                    ly,
                    100,
                    50
                )

                if leaf.colliderect(coin_box):

                        if coin_type == 1:

                            coins += 1
                            score += 5

                        else:

                            coins += 5
                            score += 25

                        coin_x = random.randint(
                            25,
                            width - 25
                        )

                        coin_y = random.randint(
                            800,
                            1100
                        )

                        safe = False

                        while safe == False:

                            safe = True

                            for s in sponges:

                                if abs(coin_x - s[0]) < 100 and abs(coin_y - s[1]) < 100:

                                    coin_x = random.randint(
                                        25,
                                        width - 25
                                    )

                                    coin_y = random.randint(
                                        800,
                                        1100
                                    )

                                    safe = False
                                    break

                        if random.randint(1,5) == 1:
                            coin_type = 2

                        else:
                            coin_type = 1

                if coin_y < -30:

                        coin_x = random.randint(
                            25,
                            width - 25
                        )

                        coin_y = random.randint(
                            800,
                            1100
                        )

                        safe = False

                        while safe == False:

                            safe = True

                            for s in sponges:

                                if abs(coin_x - s[0]) < 100 and abs(coin_y - s[1]) < 100:
                                    coin_x = random.randint(25, width - 25)

                                    coin_y = random.randint(800, 1100)

                                    safe = False
                                    break

                        if random.randint(1, 5) == 1:
                            coin_type = 2

                        else:
                            coin_type = 1

                if coin_type == 1:

                    pygame.draw.circle(
                        screen,
                        (255, 220, 40),
                        (coin_x, coin_y),
                        15
                    )

                else:

                    pygame.draw.circle(
                        screen,
                        (255, 140, 30),
                        (coin_x, coin_y),
                        22
                    )

    if over == True:
        draw_x = lx

    elif dry > 0 and pause == False:
        draw_x = lx + math.sin(dry * 0.5) * 5

    else:
        draw_x = lx

    pygame.draw.rect(
        screen, draw_color, (int(draw_x), int(ly), 100, 50)
    )

    if pause == True and over == False:

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

                if coin_type == 1:

                    pygame.draw.circle(
                        screen,
                        (255, 220, 40),
                        (coin_x, int(coin_y)),
                        15
                    )

                else:

                    pygame.draw.circle(
                        screen,
                        (255, 140, 30),
                        (coin_x, int(coin_y)),
                        22
                    )
            
    hit_text = font.render(
        "Hits: " + str(hits) + "/5",
        True,
        (0, 0, 0)
    )

    screen.blit(hit_text, (15, 15))

    score_text = font.render(
        "Score: " + str(score),
        True,
        (0, 0, 0)
    )

    screen.blit(score_text, (170, 15))

    coin_text = font.render(
        "Coins: " + str(coins),
        True,
        (0, 0, 0)
    )

    screen.blit(coin_text, (350, 15))

    if start == False:

        start_text = font.render(
            "PRESS SPACE TO START",
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

    if over == True and landed == True:
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