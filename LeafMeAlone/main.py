import asyncio
import pygame
import random
import math

async def main():
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
    groundy = height
    fall = 0

    clear = False

    hit_time = 0
    end_speed = 10

    dry = 0
    swing = 0

    fallo = lx
    falle = 0

    font = pygame.font.Font(None, 26)

    def drawc(x, y, coin_type):
        x = int(x)
        y = int(y)

        if coin_type == 1:
            size = 15
            border = (170, 115, 20)
            body = (255, 210, 35)
            highlight = (255, 240, 120)
            value = "1"

        else:
            size = 22
            border = (150, 75, 20)
            body = (255, 145, 35)
            highlight = (255, 195, 85)
            value = "5"

        pygame.draw.circle(screen, border, (x, y), size)
        pygame.draw.circle(screen, body, (x, y), size - 3)
        pygame.draw.circle(screen, border, (x, y), size - 5, 2)
        pygame.draw.rect(screen, highlight, (x - size // 2, y - size // 2, 5, 4))

        coinf = pygame.font.Font(None, 22 if coin_type == 1 else 28)
        number = coinf.render(value, True, border)
        numberr = number.get_rect(center = (x, y))
        screen.blit(number, numberr)

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

    clds = [
        [40, 90, 0.4],
        [220, 140, 0.3],
        [360, 70, 0.5]
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
                            groundy = height
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

                            clds = [
                                [40, 90, 0.4],
                                [220, 140, 0.3],
                                [360, 70, 0.5]
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

        if start == True and pause == False and over == False:
            if ly >= 400:
                ty -= up

                for c in clds:
                    c[1] -= up * c[2]

                    if c[1] < -40:
                        c[0] = random.randint(-20, width - 80)
                        c[1] = height + random.randint(40, 160)
        
        pygame.draw.rect(screen, (135, 205, 245), (0, 0, width, 180))
        pygame.draw.rect(screen, (160, 220, 250), (0, 180, width, 200))
        pygame.draw.rect(screen, (190, 235, 255), (0, 380, width, 320))

        for c in clds:
            cx = int(c[0])
            cy = int(c[1])

            pygame.draw.rect(screen, (255, 255, 255), (cx + 15, cy, 50, 12))
            pygame.draw.rect(screen, (255, 255, 255), (cx, cy + 10, 80, 20))
            pygame.draw.rect(screen, (255, 255, 255), (cx + 25, cy - 5, 25, 8))
        trunkt = ty + 170

        if trunkt < height:
            visiblet = max(0, trunkt)
            trunkh = height - visiblet

            pygame.draw.rect(screen, (115, 70, 35), (200, visiblet, 100, trunkh))
            pygame.draw.rect(screen, (85, 50, 30), (275, visiblet, 25, trunkh))
            pygame.draw.rect(screen, (150, 95, 50), (210, visiblet, 12, trunkh))

            for y in range(0, height, 120):
                barky = (y + int(ty)) % height
                if barky >= visiblet:
                    pygame.draw.rect(screen, (90, 55, 30), (235, barky, 8, 55))
                    pygame.draw.rect(screen, (90, 55, 30), (255, barky + 45, 8, 40))
                    pygame.draw.rect(screen, (145, 90, 45), (220, barky + 20, 6, 35))

        pygame.draw.rect(screen, (145, 90, 45), (255, ty + 450, 8, 50))

        pygame.draw.rect(screen, (115, 70, 35), (135, ty + 190, 100, 25))
        pygame.draw.rect(screen, (85, 50, 30), (135, ty + 210, 100, 5))

        pygame.draw.rect(screen, (115, 70, 35), (275, ty + 160, 100, 25))
        pygame.draw.rect(screen, (85, 50, 30), (275, ty + 180, 100, 5))

        pygame.draw.rect(screen, (35, 120, 50), (150, ty, 200, 40 ))
        pygame.draw.rect(screen, (35, 120, 50), (100, ty + 40, 300, 40))
        pygame.draw.rect(screen, (35, 120, 50), (50, ty + 80, 400, 80))
        pygame.draw.rect(screen, (35, 120, 50), (0, ty + 110, 500, 50))
        pygame.draw.rect(screen, (35, 120, 50), (100, ty + 160, 300, 40))
        pygame.draw.rect(screen, (35, 120, 50), (150, ty + 200, 200, 20))

        pygame.draw.rect(screen, (20, 95, 40), (150, ty + 205, 200, 15))
        pygame.draw.rect(screen, (20, 95, 40), (100, ty + 185, 50, 15))
        pygame.draw.rect(screen, (20, 95, 40), (350, ty + 185, 50, 15))
        pygame.draw.rect(screen, (20, 95, 40), (50, ty + 150, 50, 10))
        pygame.draw.rect(screen, (20, 95, 40), (400, ty + 150, 50, 10))
        pygame.draw.rect(screen, (20, 95, 40), (0, ty + 150, 50, 10))
        pygame.draw.rect(screen, (20, 95, 40), (450, ty + 150, 50, 10))

        pygame.draw.rect(screen, (55, 165, 65), (170, ty + 15, 70, 20))
        pygame.draw.rect(screen, (55, 165, 65), (260, ty + 25, 65, 15))
        pygame.draw.rect(screen, (55, 165, 65), (115, ty + 55, 90, 20))
        pygame.draw.rect(screen, (55, 165, 65), (300, ty + 65, 65, 20))
        pygame.draw.rect(screen, (55, 165, 65), (65, ty + 100, 75, 20))
        pygame.draw.rect(screen, (55, 165, 65), (355, ty + 110, 70, 20))

        pygame.draw.rect(screen, (85, 185, 80), (185, ty + 20, 25, 8))
        pygame.draw.rect(screen, (85, 185, 80), (315, ty + 70, 20, 8))
        pygame.draw.rect(screen, (85, 185, 80), (65, ty + 100, 75, 20))
        pygame.draw.rect(screen, (85, 185, 80), (375, ty + 115, 20, 8))

        pygame.draw.rect(screen, (25, 105, 40), (160, ty + 145, 65, 15))
        pygame.draw.rect(screen, (25, 105, 40), (275, ty + 155, 65, 15))
        pygame.draw.rect(screen, (25, 105, 40), (115, ty + 170, 40, 12))
        pygame.draw.rect(screen, (25, 105, 40), (360, ty + 145, 35, 15))


        

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

            if clear == True and landed == False:
                ty -= end_speed

            for s in sponges:

                s[1] -= end_speed

                if s[1] + sh > 0 and s[1] < height:
                    clear = False

                    pygame.draw.rect(screen, (220, 190, 70), (s[0] + 8, s[1], 64, 50))
                    pygame.draw.rect(screen, (220, 190, 70), (s[0], s[1] + 8, 80, 34))
                    pygame.draw.rect(screen, (175, 140, 45), (s[0] + 72, s[1] + 8, 8, 34))
                    pygame.draw.rect(screen, (175, 140, 45), (s[0] + 64, s[1] + 42, 8, 8))
                    pygame.draw.rect(screen, (175, 140, 45), (s[0] + 8, s[1] + 45, 64, 5))

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

            coin_y -= end_speed

            if coin_y + 22 > 0 and coin_y < height:

                clear = False

                drawc(coin_x, coin_y, coin_type)

            if landed == False and clear == True:

                falle += 1
                swing += 0.115

                fall += 0.12

                if fall > 5:
                    fall = 5

                ly += fall
                ty -= fall

                for c in clds:
                    c[1] -= fall * c[2]

                if groundy > ground:
                    groundy = max(ground, groundy - fall * 0.5)

                rem = max(0, (ground - 50 - ly) / 200)
                amp = 12 + 28 * min(1, rem)

                lx = (
                    fallo + math.sin(swing) * amp
                    + math.sin(swing * 0.43) * 12
                )

                lx = max(0, min(width - 100, lx))

                if ly >= ground - 50 and groundy <= ground:

                    ly = ground - 50
                    landed = True
                    fall = 0

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

                screen.blit(dry_text, dry_text.get_rect(center = (width // 2, 330)))  

            else:

                dry_text = font.render(
                    "GETTING DRY!",
                    True,
                    (0, 0, 0)
                )

                screen.blit(dry_text, dry_text.get_rect(center = (width // 2, 330)))

        if start == True and pause == False and over == False:

            if ly < 400:

                ly = min(400, ly + up)

            else:
                
                for s in sponges:

                    s[1] -= up

                    pygame.draw.rect(screen, (220, 190, 70), (s[0] + 8, s[1], 64, 50))
                    pygame.draw.rect(screen, (220, 190, 70), (s[0], s[1] + 8, 80, 34))
                    pygame.draw.rect(screen, (175, 140, 45), (s[0] + 72, s[1] + 8, 8, 34))
                    pygame.draw.rect(screen, (175, 140, 45), (s[0] + 64, s[1] + 42, 8, 8))
                    pygame.draw.rect(screen, (175, 140, 45), (s[0] + 8, s[1] + 45, 64, 5))

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
                        draw_x,
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
                            groundy = height + 10
                            fall = 0
                            swing = 0
                            falle = 0
                            fallo = lx

                            dry = 0
                            clear = False

                            break

                        far = max(height, max(other[1] for other in sponges))

                        s[1] = far + random.randint(170, 230)
                        s[0] = random.randint(0, width - sw)

                        for i in range (50):
                            if abs(s[0] - coin_x) >= 100 or abs(s[1] - coin_y) >= 100:
                                break
                            s[0] = random.randint(0, width - sw)

                        if abs(s[0] - coin_x) < 100 and abs(s[1] - coin_y) < 100:
                            s[1] = max(other[1] for other in sponges) + 250

                    elif s[1] < -sh:

                        score += 1

                        far = max(height, max(other[1] for other in sponges))

                        s[1] = far + random.randint(170, 230)
                        s[0] = random.randint(0, width - sw)

                        for i in range(50):

                            if abs(s[0] - coin_x) >= 100 or abs(s[1] - coin_y) >= 100:
                                break

                            s[0] = random.randint(0, width - sw)

                        if abs(s[0] - coin_x) < 100 and abs(s[1] - coin_y) < 100:
                            s[1] = max(other[1] for other in sponges) + 250

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
                        draw_x,
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

                    if leaf.colliderect(coin_box) or coin_y < -coin_size:

                        safe = False

                        for i in range(50):

                            coin_x = random.randint(
                                25,
                                width - 25
                            )

                            coin_y = random.randint(
                                800,
                                1100
                            )

                            safe = True

                            for s in sponges:

                                if (
                                        abs(coin_x - s[0]) < 100
                                        and abs(coin_y - s[1]) < 100
                                    ):
                                        safe = False
                                        break

                            if safe == True:
                                break

                        if safe == False:
                            coin_x = random.randint(25, width - 25)
                            coin_y = max(s[1] for s in sponges) + 250

                        if random.randint(1,5) == 1:
                            coin_type = 2

                        else:
                            coin_type = 1

                    drawc(coin_x, coin_y, coin_type)

        if pause == True and over == False:

                if ly >= 400:

                    for s in sponges:

                        pygame.draw.rect(screen, (220, 190, 70), (s[0] + 8, s[1], 64, 50))
                        pygame.draw.rect(screen, (220, 190, 70), (s[0], s[1] + 8, 80, 34))
                        pygame.draw.rect(screen, (175, 140, 45), (s[0] + 72, s[1] + 8, 8, 34))
                        pygame.draw.rect(screen, (175, 140, 45), (s[0] + 64, s[1] + 42, 8, 8))
                        pygame.draw.rect(screen, (175, 140, 45), (s[0] + 8, s[1] + 45, 64, 5))

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

                    drawc(coin_x, coin_y, coin_type)
        if over == True:
            pygame.draw.rect(screen, (120, 80, 45), (0, groundy, width, height - ground))
            pygame.draw.rect(screen, (95, 60, 35), (0, groundy + 35, width, 15))
            pygame.draw.rect(screen, (65, 155, 65), (0, groundy, width, 12))
            pygame.draw.rect(screen, (40, 115, 45), (0, groundy + 12, width, 5))

            for x in range(0, width, 60): 
                pygame.draw.rect(screen, (65, 155, 65), (x + 5, groundy - 8, 6, 10))
                pygame.draw.rect(screen, (85, 180, 75), (x + 12, groundy - 5, 5, 7))

            for x in range(15, width, 65):
                pygame.draw.rect(screen, (155, 105, 60), (x, groundy + 25, 12, 5))
                pygame.draw.rect(screen, (85, 55, 30), (x + 30, groundy + 38, 8, 4))
        
        ilx = int(draw_x)
        ily = int(ly)

        shadec = (
            max(0, draw_color[0] - 25),
            max(0, draw_color[1] - 25),
            max(0, draw_color[2] - 25)
        )

        pygame.draw.rect(screen, draw_color, (ilx + 10, ily, 80, 10))
        pygame.draw.rect(screen, draw_color, (ilx, ily + 10, 100, 30))
        pygame.draw.rect(screen, draw_color, (ilx + 10, ily + 40, 80, 10))

        pygame.draw.rect(screen, shadec, (ilx + 92, ily + 12, 6, 26))
        pygame.draw.rect(screen, shadec, (ilx + 84, ily + 40, 6, 8))

        pygame.draw.rect(screen, shadec, (ilx + 12, ily + 43, 72, 5))

        pygame.draw.rect(screen, (50, 80, 35), (ilx + 10, ily, 80, 2))
        pygame.draw.rect(screen, (50, 80, 35), (ilx + 10, ily + 48, 80, 2))

        pygame.draw.rect(screen, (50, 80, 35), (ilx, ily + 10, 2, 30))
        pygame.draw.rect(screen, (50, 80, 35), (ilx + 98, ily + 10, 2, 30))

        pygame.draw.rect(screen, (50, 80, 35), (ilx + 10, ily, 2, 10))
        pygame.draw.rect(screen, (50, 80, 35), (ilx + 88, ily, 2, 10))
        pygame.draw.rect(screen, (50, 80, 35), (ilx + 10, ily + 40, 2, 10))
        pygame.draw.rect(screen, (50, 80, 35), (ilx + 88, ily + 40, 2, 10))

        pygame.draw.rect(screen, (50, 80, 35), (ilx, ily + 10, 10, 2))
        pygame.draw.rect(screen, (50, 80, 35), (ilx + 90, ily + 10, 10, 2))
        pygame.draw.rect(screen, (50, 80, 35), (ilx, ily + 38, 10, 2))
        pygame.draw.rect(screen, (50, 80, 35), (ilx + 90, ily + 38, 10, 2))
        
        pygame.draw.rect(screen, (85, 105, 45), (ilx + 12, ily + 23, 76, 4))
                
        leafc = [
            (125, 70, 30),
            (180, 110, 40),
            (150, 145, 45),
            (105, 165, 55),
            (55, 175, 65)
        ]

        for i in range(5 - hits):
            hx = 15 + i * 26
            hy = 15

            pygame.draw.rect(screen, leafc[i], (hx + 4, hy, 14, 4))
            pygame.draw.rect(screen, leafc[i], (hx, hy + 4, 22, 12))
            pygame.draw.rect(screen, leafc[i], (hx + 4, hy + 16, 14, 4))
            pygame.draw.rect(screen, (75, 85, 35), (hx + 4, hy + 9, 14, 2))

        score_text = font.render(
            "Distance: " + str(score),
            True,
            (0, 0, 0)
        )

        screen.blit(score_text, (width // 2 - score_text.get_width() // 2, 15))

        coin_text = font.render(
            "Coins: " + str(coins),
            True,
            (0, 0, 0)
        )

        screen.blit(coin_text, (width - coin_text.get_width() - 15, 15))

        if start == False:

            start_text = font.render(
                "PRESS SPACE TO START",
                True,
                (0, 0, 0)
            )

            screen.blit(start_text, start_text.get_rect(center = (width // 2, 340)))

        if pause == True:

            pause_text = font.render(
                "PAUSED",
                True,
                (0, 0, 0)
            )

            screen.blit(pause_text, pause_text.get_rect(center = (width // 2, 300)))

            space_text = font.render(
                    "SPACE TO CONTINUE",
                    True,
                    (0, 0, 0)
                )

            screen.blit(space_text, space_text.get_rect(center = (width // 2, 350)))

        if over == True and landed == True:
            game_text = font.render(
                "GAME OVER",
                True,
                [0, 0, 0]
            )

            screen.blit(game_text, game_text.get_rect(center = (width // 2, 300)))

            restart_text = font.render(
                "SPACE TO RESTART",
                True,
                (0, 0, 0)
            )

            screen.blit(restart_text, restart_text.get_rect(center = (width // 2, 350)))

        pygame.display.update()

        clock.tick(60)
        await asyncio.sleep(0)

    pygame.quit()
asyncio.run(main())