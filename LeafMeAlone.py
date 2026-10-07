import pygame

pygame.init()

width = 500
height = 700

screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill((180, 220, 250))

    pygame.display.update()

    clock.tick(60)

pygame.quit()