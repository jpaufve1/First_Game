import pygame
from sprite_sheet_functions import SpriteSheet

#constant=
#Name, Xloc, Yloc, w, h
TEST_PLATFORM = (0, 0, 451, 41)
GROUND = (0, 41, 2700, 51)

class Platform(pygame.sprite.Sprite):

    def __init__(self, data):
        super().__init__()

        sprite_sheet = SpriteSheet('Platforms_SpriteSheet.png')

        self.image = sprite_sheet.get_image(data[0],data[1],data[2],data[3])
        self.rect = self.image.get_rect()
