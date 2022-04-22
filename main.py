import pygame
import time
import math
from utils import scale_image


GRASS = scale_image(pygame.image.load("assets/grass.jpg"), 2.4)
TRACK = scale_image(pygame.image.load("assets/track.png"), 0.9)

TRACK_BORDER = scale_image(pygame.image.load("assets/track-border.png"), 0.9)
FINISH = pygame.image.load("assets/finish.png")

RED_CAR = scale_image(pygame.image.load("assets/red-car.png"), 0.55)
GREEN_CAR = scale_image(pygame.image.load("assets/green-car.png"), 0.55)


WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()

# create the window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Okey, runn")

FPS = 60

run = True
clock = pygame.time.Clock()

while run:
    clock.tick(FPS)

    WIN.blit(GRASS, (0, 0))
    WIN.blit(TRACK, (0, 0))
    WIN.blit(RED_CAR, (0, 0))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

pygame.quit()