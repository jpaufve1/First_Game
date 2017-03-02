import pygame
import platforms


class Level:

    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.platform_list_camera = pygame.sprite.Group()
        self.player = player
        self.background = None

        # updates all level components
    def update(self, cam):
        self.platform_list.update()
        for block in self.platform_list:
            block.rect.x += -cam.change_x
            block.rect.y += -cam.change_y

    def draw(self, screen, cam):
        # Draw all the sprite lists that we have
        screen.blit(cam.camera, [0, 0])
        self.platform_list.draw(screen)
        # for enemy in self.enemy_list:
        # platform[0].blit(screen, platform[1]-camera.camera_x, platform[2]-camera.camera_y)
        # self.enemy_list.draw(screen)


class Level_01(Level):

    def __init__(self, player):
        # Call the parent constructor
        Level.__init__(self, player)
        self.background = pygame.image.load('Background_Level_One.png').convert()
        # Array with type of platform, and x, y location of the platform.
        level = [[platforms.GROUND, 0, 1348], [platforms.TEST_PLATFORM, 1204, 1247]]
        # Go through the array above and add platforms
        for platform in level:
            # Platform Object
            block = platforms.Platform(platform[0])
            # rect co-ords of Object
            block.rect.x = platform[1]-600
            block.rect.y = platform[2]-700
            # adds player info?
            block.player = self.player
            self.platform_list.add(block)

    def startup(self, camera, player):
        camera.camera_x = 600
        camera.camera_y = 700
        player.rect.x = 454
        player.rect.y = 609
