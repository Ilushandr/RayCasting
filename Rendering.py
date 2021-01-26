from Settings import *
from math import sin, cos

mx, my = WIDTH - WIDTH // 5, 0


def draw_walls(tile_h, distances):
    for n, ray in enumerate(distances):
        lx, ly, dist = ray
        h = tile_h / dist
        rect = (n * WIDTH // RAYS_NUM, (HEIGHT - h) / 2,
                WIDTH // (RAYS_NUM // 2), h)
        c = 255 / dist * 40
        color = (c, c, c) if c <= 255 else (255, 255, 255)
        pygame.draw.rect(SCREEN, color, rect)


def draw_map(walls):
    pygame.draw.rect(SCREEN, 'gray', (mx, my, WIDTH / 5, HEIGHT / 5))
    for wall in walls:
        pygame.draw.rect(SCREEN, 'WHITE', (mx + wall.x / 5, my + wall.y / 5,
                                           wall.w / 5, wall.h / 5))


def draw_player(x, y, angle):
    x, y = mx + x // 5, my + y // 5
    pygame.draw.circle(SCREEN, 'red', (x, y), 5)
    pygame.draw.line(SCREEN, 'red', (x, y), (x + 50 * cos(angle), y + 50 * sin(angle)))
