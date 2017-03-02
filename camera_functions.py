import pygame


class Camera(object):

    def __init__(self):
        super().__init__()
        self.camera = pygame.Surface([900,700]).convert()
        self.camera_x = 0
        self.camera_y = 0
        self.change_x = 0
        self.change_y = 0

    def update_camera(self, player, current_level):
        # camera motion and the bounding box
        if player.rect.x <= 250:
            if self.camera_x <= 0:
                self.camera_x = 0
                self.change_x = 0
            else:
                player.rect.x = 250
                self.camera_x += player.vx
                self.change_x = player.vx
        elif player.rect.x >= 450:
            if self.camera_x >= 1800:
                self.camera_x = 1800
                self.change_x = 0
            else:
                player.rect.x = 450
                self.camera_x += player.vx
                self.change_x = player.vx
        if player.rect.y <= 409:
            if self.camera_y <= 0:
                self.camera_y = 0
                self.change_y = 0
            else:
                player.rect.y = 409
                self.camera_y += player.vy
                self.change_y = player.vy
        elif player.rect.y >= 609:
            if self.camera_y >= 700:
                self.camera_y = 700
                self.change_y = 0
            else:
                player.rect.y = 609
                self.camera_y += player.vy
                self.change_y = player.vy
        else:
            self.change_x = 0
            self.change_y = 0
        self.camera.blit(current_level.background, (0,0) , (self.camera_x,self.camera_y,900,700))
