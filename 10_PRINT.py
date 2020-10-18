import pygame
import random

width = 600
height = 400
rez = 20

display = pygame.display.set_mode((width, height))
pygame.display.set_caption('10 PRINT')

def main():
    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                display.fill((0, 0, 0))
                for i in range(width // rez):
                    for j in range(height // rez):
                        n = random.randint(0, 1)
                        if n == 0:
                            pygame.draw.line(display, (169, 169, 169), (i*rez, j*rez), (i*rez + rez, j*rez + rez), 4)
                        elif n == 1:
                            pygame.draw.line(display, (169, 169, 169), (i*rez + rez, j*rez), (i*rez, j*rez + rez), 4)

        pygame.display.flip()

main()
