from math import cos, sin, pi

from Settings import *


class Player:
    def __init__(self, x, y, v, fov, obstacles):
        self.x, self.y = x, y
        self.v = v
        self.view_angle = 0
        self.fov = fov
        self.collision_point = pygame.Rect(x, y, 1, 1)

        self.obstacles = obstacles
        self.last_mouse_pos = (0, 0)

    def movement(self, v, angle):
        # Метод обрабатывает столкновение игрока с препятствиями и меняет его координаты
        # Изменение по x
        self.x += v * cos(angle)
        for block in self.obstacles:
            if self.collision_point.colliderect(block):
                if v < 0:
                    self.collision_point.left = block.right
                elif v > 0:
                    self.collision_point.right = block.left
                break

        # Изменение по y
        self.y += v * sin(angle)
        for block in self.obstacles:
            if self.collision_point.colliderect(block):
                if v < 0:
                    self.collision_point.top = block.bottom
                elif v > 0:
                    self.collision_point.bottom = block.top
                break

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.movement(self.v, self.view_angle)
        if keys[pygame.K_s]:
            self.movement(self.v, -(pi - self.view_angle))
        if keys[pygame.K_a]:
            self.movement(self.v, self.view_angle - pi / 2)
        if keys[pygame.K_d]:
            self.movement(self.v, self.view_angle + pi / 2)

    def rotate(self):
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] <= 1 or mouse_pos[0] >= WIDTH - 1:
            self.last_mouse_pos = (WIDTH // 2, HEIGHT // 2)
            pygame.mouse.set_pos(self.last_mouse_pos)
        else:
            self.view_angle -= (self.last_mouse_pos[0] - mouse_pos[0]) / 100
            self.last_mouse_pos = mouse_pos

    def update(self):
        self.move()
        self.rotate()
