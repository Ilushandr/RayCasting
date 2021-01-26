import pygame


RAYS_NUM = 500
pygame.init()
display_info = pygame.display.Info()
size = WIDTH, HEIGHT = display_info.current_w, display_info.current_h
SCREEN = pygame.display.set_mode(size, flags=pygame.FULLSCREEN)
pygame.mouse.set_visible(False)

FPS = 60
CLOCK = pygame.time.Clock()



