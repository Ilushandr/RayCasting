from Settings import *


class Level:
    def __init__(self, level):
        self.level_name = level
        self.level_map = self.create_level()
        self.distances = None

        self.map_w = len(self.level_map[0])
        self.map_h = len(self.level_map)
        self.cell_w = WIDTH // self.map_w
        self.cell_h = HEIGHT // self.map_h

        rects = self.merge_rects(self.get_horizontal_rects(), self.get_vertical_rects())
        self.walls = self.create_walls(rects)

        self.score = 0

    def player_location(self):
        # Возвращает положение игрока на карте
        for row in range(self.map_h):
            for col in range(self.map_w):
                if self.level_map[row][col] == '@':
                    self.level_map[row].replace('@', ' ')
                    return (col * self.cell_w + self.cell_w // 2,
                            row * self.cell_h + self.cell_h // 2)

    def create_level(self):
        # Создает карту уровня
        with open(f'levels/level_{self.level_name}.txt') as file:
            map = file.readlines()
            return [row.rstrip() for row in map]

    def create_walls(self, rects):
        walls = []
        for rect in rects:
            walls.append(Wall(rect.x, rect.y, rect.w, rect.h).rect)
        return walls

    def merge_rects(self, horizontal, vertical):
        rects = []
        for h_rect in horizontal:
            container = []
            for v_rect in vertical:
                if h_rect.contains(v_rect):
                    container.append(v_rect)
                    vertical.remove(v_rect)
            if container:
                rect = h_rect.unionall(container)
                rects.append(rect)
        for v_rect in vertical:
            container = []
            for h_rect in horizontal:
                if v_rect.contains(h_rect):
                    container.append(h_rect)
                    horizontal.remove(h_rect)
            if container:
                rect = v_rect.unionall(container)
                rects.append(rect)

        return rects

    def get_horizontal_rects(self):
        rects = []
        for row in range(self.map_h):
            row_rects = []
            is_rect = False
            for col in range(self.map_w):
                if self.level_map[row][col] == '#':
                    if not is_rect:
                        row_rects.append([])
                        is_rect = True
                    row_rects[-1].append(col)
                else:
                    is_rect = False
            for i in range(len(row_rects)):
                col, w = row_rects[i][0], len(row_rects[i])
                row_rects[i] = pygame.Rect(col * self.cell_w, row * self.cell_h,
                                           w * self.cell_w, self.cell_h)
            rects.extend(row_rects)
        return rects

    def get_vertical_rects(self):
        rects = []
        for col in range(self.map_w):
            col_rects = []
            is_rect = False
            for row in range(self.map_h):
                if self.level_map[row][col] == '#':
                    if not is_rect:
                        col_rects.append([])
                        is_rect = True
                    col_rects[-1].append(row)
                else:
                    is_rect = False
            for i in range(len(col_rects)):
                row, h = col_rects[i][0], len(col_rects[i])
                col_rects[i] = pygame.Rect(col * self.cell_w, row * self.cell_h,
                                           self.cell_w, h * self.cell_h)
            rects.extend(col_rects)
        return rects

    def cell_in_map(self, row, col):
        return 0 <= row < self.map_h and 0 <= col < self.map_w


class Wall:
    def __init__(self, x, y, w, h):
        super().__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(x, y, w, h)

    def update(self):
        pygame.draw.rect(SCREEN, 'black', (self.x, self.y,
                                           self.w, self.h))
