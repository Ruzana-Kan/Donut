# rotating donut by Ruzana khan with python
# fun prioject
import pygame
import sys
import math


pygame.init()

# Constants
width, height = 800, 600
bg_color = (0, 0, 0)
donut_color = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Rotating Donut')

# Main loop
running = True
angle = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    screen.fill(bg_color)

    # Set up constants for the donut
    donut_radius = 150
    donut_radius2 = 50
    k2 = width / 2
    k1 = height / 2

    # Calculate the donut's position
    A = math.cos(angle)
    B = math.sin(angle)

    for i in range(0, 628, 10):
        cA = math.cos(i)
        sA = math.sin(i)

        for j in range(0, 628, 10):
            cB = math.cos(j)
            sB = math.sin(j)

            x = k2 + donut_radius * cA
            y = k1 + donut_radius * sA

            z = donut_radius * sB

            x2 = x * A - z * B
            z2 = x * B + z * A
            y2 = y

            x3 = int(width / 2 + x2)
            y3 = int(height / 2 + y2)

            pygame.draw.circle(screen, donut_color, (x3, y3), 2)

    pygame.display.flip()
    angle += 0.01


pygame.quit()
sys.exit()





