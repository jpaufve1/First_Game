import pygame



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #speed vector
        self.vx = 0
        self.vy = 0
        #top left position
        self.x = 0
        self.y = 0
        #walking frames

        self.image = pygame.image.load('Player.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.left = True

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def hitcheck(self, level):
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.vx > 0:
                self.rect.right = block.rect.left
                self.vx = 0
            elif self.vx < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
                self.vx = 0
            print(block)
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.vy > 0:
                self.rect.bottom = block.rect.top
                self.vy = 0
            elif self.vy < 0:
                self.rect.top = block.rect.bottom
                self.vy = 0
            print(block)

    def draw(self, screen):
        if self.left:
            screen.blit(self.image, (self.x, self.y))
        else:
            screen.blit(pygame.transform.flip(self.image, True, False), (self.x, self.y))

