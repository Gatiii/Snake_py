import pygame
import time
import random

pygame.init()
dis = pygame.display.set_mode((600, 600))

pygame.display.set_caption("Snake")

white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

x1 = 300
y1 = 300

x1_change = 0
y1_change = 0

x2 = round(random.randrange(0, 580) / 10) * 10
y2 = round(random.randrange(0, 580) / 10) * 10

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 50)


def game_over_message(mess, color):
    msg = font.render(mess, False, color)
    dis.blit(msg, [250, 250])


game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10
            elif event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
    if x1 >= 600 or x1 < 0 or y1 < 0 or y1 >= 600:
        game = False

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, green, [x1, y1, 10, 10])
    pygame.draw.rect(dis, red, [x2, y2, 10, 10])

    pygame.display.update()
    clock.tick(20)

game_over_message("You lost", red)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()