import pygame


class SpriteSheet(object):

    # class for operating and cutting spreadsheets

    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):

        # create image
        image = pygame.Surface([width, height]).convert()

        # draw image from sheet
        image.blit(self.sprite_sheet, (0,0), (x, y, width, height))

        # remove alpha = 0
        image.convert_alpha()

        return image
