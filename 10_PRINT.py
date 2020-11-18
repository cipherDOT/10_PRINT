# 10 PRINT CHR$(205.5+RND(1)); : GOTO 10

# -------------------------------------------------------------------------------------------------------------------------#
import pygame
from pygame.draw import line
from pygame.time import Clock
from random import random

# -------------------------------------------------------------------------------------------------------------------------#

width = 600
height = 400

display = pygame.display.set_mode((width, height))
pygame.display.set_caption('10 PRINT CHR$(205.5+RND(1)); : GOTO 10')

# -------------------------------------------------------------------------------------------------------------------------#


def main():
    run = True
    x = 0
    y = 0
    rez = 20
    clock = Clock()

    while run:
        clock.tick(14)
        n = random()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if n > 0.5:
            line(display, (220, 220, 220), (x, y), (x + rez, y + rez), 4)
        elif n <= 0.5:
            line(display, (220, 220, 220), (x, y + rez), (x + rez, y), 4)

        x += rez
        if x > width:
            x = 0
            y += rez

        if (x > width and y > height):
            x = 0
            y = 0

        pygame.display.flip()

# -------------------------------------------------------------------------------------------------------------------------#


if __name__ == '__main__':
    main()

# -------------------------------------------------------------------------------------------------------------------------#
