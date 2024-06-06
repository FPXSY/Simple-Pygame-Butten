import pygame
import time
from button import *

pygame.init()

WIDTH = 1900
HEIGHT = 1020
FPS = 120
timer = pygame.time.Clock()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
pygame.display.toggle_fullscreen()

mPointX = (screen.get_width() / 2) 
mPointY = (screen.get_height() / 2) 


rect_1 = pygame.Rect(mPointX, mPointY, 100, 100)
button_1 = Button(Cyan, 50, 50, 250, 90, "Reimbow")


def Update_display():
    # Draw the circle
    screen.fill(Black)
    button_1.draw(screen, True, (255,255,255))
    button_1.font(screen, "arial", 40, True)
    if (button_1.get_clicked() == True):
        pygame.draw.rect(screen, next(calor_rainbow), rect_1, 0)
        pygame.time.delay(50)
    elif (button_1.get_clicked() == False):
        pygame.draw.rect(screen, Red, rect_1, 0)
    pygame.display.update()



# Game loop
run = True
while run:
    timer.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.display.toggle_fullscreen()
            else:
                pygame.display.is_fullscreen()


    Update_display()


pygame.quit()
