from Settings import *
from Level import Level
from Player import Player
from Rendering import draw_walls, draw_map, draw_player
from RayCasting import ray_cycle


def fps_counter():
    font = pygame.font.Font(None, 20)
    text = font.render(str(round(CLOCK.get_fps(), 4)), True, 'white')
    text_x = 0
    text_y = 0
    SCREEN.blit(text, (text_x, text_y))


level = Level('4')
obstacles = [(wall.x, wall.y, wall.w, wall.h) for wall in level.walls]
player = Player(*level.player_location(), 3, 90, level.walls)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()

    SCREEN.fill('black')

    player.update()
    points = ray_cycle(player.x, player.y, player.view_angle, obstacles,
                       level.cell_w, level.cell_h, level.map_w, level.map_h, player.fov, RAYS_NUM)
    draw_walls(100000, points)
    draw_map(level.walls)
    draw_player(player.x, player.y, player.view_angle)

    fps_counter()
    pygame.display.flip()
    CLOCK.tick(FPS)
