import pygame, sys
import level
from camera_functions import Camera
from player import Player
pygame.init()

# surface 700x900
size = [900, 700]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Valiant")

# Create camera
cam_01 = Camera()

# create player
player_1 = Player()

# Create all the level(s)
level_list = []
level_list.append(level.Level_01(player_1))

# Set the current level
current_level_no = 0
current_level = level_list[current_level_no]
current_level.startup(cam_01, player_1)

# initials values
gravity = True
clock = pygame.time.Clock()
Gravity_stagger = 8
# main game loop
while True:
    if Gravity_stagger != 1:
        Gravity_stagger += -1
    else:

        Gravity_stagger = 8

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #player movement
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_1.vx = -3
                player_1.left = False
            if event.key == pygame.K_RIGHT:
                player_1.vx = 3
                player_1.left = True
            if event.key == pygame.K_SPACE or pygame.K_UP:
                player_1.vy = -3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player_1.vx < 0:
                player_1.vx = 0
            if event.key == pygame.K_RIGHT and player_1.vx > 0:
                player_1.vx = 0
    if gravity and player_1.vy < 2:
        if Gravity_stagger ==1:
            player_1.vy += 1

    #move and draw
    player_1.move()
    player_1.hitcheck(current_level)
    cam_01.update_camera(player_1, current_level)
    current_level.update(cam_01)

    current_level.draw(screen,cam_01)
    player_1.draw(screen)

    pygame.display.flip()
    clock.tick(60)
    #for block in current_level.platform_list:
        #print(cam_01.change_x, block.rect.x)




