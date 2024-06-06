import pygame
import itertools

pygame.init()

class Button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.clicked = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.mRect = ((self.width /2) + (self.height /2)) /2


    
    def draw(self, screen, outline=False, outlineCaler = (255,255,255)):
        self.outlineCaler = outlineCaler
        # Call this method to draw the button on the screen
        if outline == True:
            pygame.draw.rect(screen, outlineCaler, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)


            
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

    def font(self,screen, stayl= "arial", size = 60, bold = False):
        self.stayl = stayl
        self.size = size
        self.bold = bold
        if self.text != '':
            font = pygame.font.SysFont(self.stayl, self.size, self.bold)
            text = font.render(self.text, 1, (0, 0, 0))
            screen.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2),
                self.y + (self.height / 2 - text.get_height() / 2)))
    
    def get_clicked(self):
        return self.clicked

# Colors
colors = [(255,255,255),(255, 0, 0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255),(192,192,192),(128,128,128)
,(128,0,0),(128,128,0),(0,128,0),(128,0,128),(0,128,128),(0,0,128)]
calor_rainbow = itertools.cycle(colors)


Black = (0, 0, 0)
White = (255,255,255)
Red = (255, 0, 0)
Lime =	(0,255,0)
Blue = (0,0,255)
Yellow = (255,255,0)
Cyan = (0,255,255)
Magenta = (255,0,255)
Silver = (192,192,192)
Gray = (128,128,128)
Maroon = (128,0,0)
Olive = (128,128,0)
Green = (0,128,0)
Purple = (128,0,128)
Teal = (0,128,128)
Navy = (0,0,128)

DarkBlue = (0,82,147)
LightBlue = (100,160,200)
LighterBlue = (152,198,234)



