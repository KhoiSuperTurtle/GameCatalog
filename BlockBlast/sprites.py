import pygame


class Square1x1(pygame.sprite.Sprite):
    def __init__(self, color, x, y, cell_size, game):
        super().__init__()
        self.game = game
        self.color = color
        self.image = pygame.Surface((cell_size + 4, cell_size + 4), pygame.SRCALPHA)
        pygame.draw.rect(self.image, color, (0, 0, cell_size + 4, cell_size + 4), border_radius=4)
        pygame.draw.rect(self.image, (240, 240, 255), (0, 0, cell_size + 4, cell_size + 4), 2, border_radius=4)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.cell_size = cell_size
        self.score = 1

    def check(self):
        x = self.rect.x + self.cell_size // 2
        y = self.rect.y + self.cell_size // 2
        cell = self.game.get_cell((x, y))

        if cell is not None:
            row, col = cell
            if self.game.grid[row][col] == self.game.colors['black']:
                return row, col
        return None

    def can_place(self):
        size = self.game.grid_size
        color = self.game.colors['black']
        for row in range(size):
            for col in range(size):
                if self.game.grid[row][col] == color:
                    return True
        return False


class Square2x2(pygame.sprite.Sprite):
    def __init__(self, color, x, y, cell_size, game):
        super().__init__()
        self.game = game
        self.color = color
        size = cell_size * 2 + 5
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.rect(self.image, color, (0, 0, size, size), border_radius=4)
        pygame.draw.rect(self.image, (240, 240, 255), (0, 0, size, size), 2, border_radius=4)
        pygame.draw.line(self.image, (240, 240, 255), (cell_size, 0), (cell_size, size), 2)
        pygame.draw.line(self.image, (240, 240, 255), (0, cell_size), (size, cell_size), 2)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.size = 2
        self.cell_size = cell_size
        self.score = 4

    def check(self):
        x = self.rect.x + self.cell_size // 2
        y = self.rect.y + self.cell_size // 2
        cell = self.game.get_cell((x, y))
        if cell is None:
            return None
        row, col = cell
        if row + self.size > self.game.grid_size or col + self.size > self.game.grid_size:
            return None

        for i in range(row, row + self.size):
            for j in range(col, col + self.size):
                if self.game.grid[i][j] != self.game.colors['black']:
                    return None

        return row, col

    def place_on_grid(self):
        x = self.rect.x + self.cell_size // 2
        y = self.rect.y + self.cell_size // 2
        cell = self.game.get_cell((x, y))
        if cell:
            row, col = cell
            for i in range(row, row + self.size):
                for j in range(col, col + self.size):
                    self.game.grid[i][j] = self.color

    def can_place(self):
        size = self.game.grid_size - 1
        color = self.game.colors['black']
        for row in range(size):
            for col in range(size):
                if (self.game.grid[row][col] == color and 
                    self.game.grid[row][col + 1] == color and 
                    self.game.grid[row + 1][col] == color and 
                    self.game.grid[row + 1][col + 1] == color):
                    return True
        return False


class Line1x3(pygame.sprite.Sprite):
    def __init__(self, color, x, y, cell_size, game):
        super().__init__()
        self.game = game
        self.color = color
        width = cell_size * 3 + 7
        height = cell_size + 4
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(self.image, color, (0, 0, width, height), border_radius=3)
        pygame.draw.rect(self.image, (240, 240, 255), (0, 0, width, height), 2, border_radius=3)
        # Разделительные линии
        for i in range(1, 3):
            x_pos = i * (cell_size + 1)
            pygame.draw.line(self.image, (240, 240, 255), (x_pos, 0), (x_pos, height), 2)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.cell_size = cell_size
        self.score = 3

    def check(self):
        x = self.rect.x + self.cell_size // 2
        y = self.rect.y + self.cell_size // 2
        cell = self.game.get_cell((x, y))
        if cell is None:
            return None
        row, col = cell
        if col + 3 > self.game.grid_size:
            return None

        for j in range(col, col + 3):
            if self.game.grid[row][j] != self.game.colors['black']:
                return None

        return row, col

    def place_on_grid(self):
        x = self.rect.x + self.cell_size // 2
        y = self.rect.y + self.cell_size // 2
        cell = self.game.get_cell((x, y))
        if cell:
            row, col = cell
            for j in range(col, col + 3):
                self.game.grid[row][j] = self.color

    def can_place(self):
        size = self.game.grid_size
        color = self.game.colors['black']
        for row in range(size):
            for col in range(size - 2):
                if (self.game.grid[row][col] == color and 
                    self.game.grid[row][col + 1] == color and 
                    self.game.grid[row][col + 2] == color):
                    return True
        return False


class Line3x1(pygame.sprite.Sprite):
    def __init__(self, color, x, y, cell_size, game):
        super().__init__()
        self.game = game
        self.color = color
        width = cell_size + 4
        height = cell_size * 3 + 7
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(self.image, color, (0, 0, width, height), border_radius=3)
        pygame.draw.rect(self.image, (240, 240, 255), (0, 0, width, height), 2, border_radius=3)
        # Разделительные линии
        for i in range(1, 3):
            y_pos = i * (cell_size + 1)
            pygame.draw.line(self.image, (240, 240, 255), (0, y_pos), (width, y_pos), 2)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.cell_size = cell_size
        self.score = 3

    def check(self):
        x = self.rect.x + self.cell_size // 2
        y = self.rect.y + self.cell_size // 2
        cell = self.game.get_cell((x, y))
        if cell is None:
            return None
        row, col = cell
        if row + 3 > self.game.grid_size:
            return None

        for i in range(row, row + 3):
            if self.game.grid[i][col] != self.game.colors['black']:
                return None

        return row, col

    def place_on_grid(self):
        x = self.rect.x + self.cell_size // 2
        y = self.rect.y + self.cell_size // 2
        cell = self.game.get_cell((x, y))
        if cell:
            row, col = cell
            for i in range(row, row + 3):
                self.game.grid[i][col] = self.color

    def can_place(self):
        size = self.game.grid_size
        color = self.game.colors['black']
        for row in range(size - 2):
            for col in range(size):
                if (self.game.grid[row][col] == color and 
                    self.game.grid[row + 1][col] == color and 
                    self.game.grid[row + 2][col] == color):
                    return True
        return False


class LShape(pygame.sprite.Sprite):
    def __init__(self, color, x, y, cell_size, game):
        super().__init__()
        self.game = game
        self.color = color
        width = cell_size * 2 + 5
        height = cell_size * 2 + 5
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        # Рисуем L-образную фигуру (ориентация: ┌)
        pygame.draw.rect(self.image, color, (0, 0, cell_size + 2, height), border_radius=3)  # Вертикальная часть
        pygame.draw.rect(self.image, color, (0, 0, width, cell_size + 2), border_radius=3)  # Горизонтальная часть
        pygame.draw.rect(self.image, (240, 240, 255), (0, 0, cell_size + 2, height), 2, border_radius=3)
        pygame.draw.rect(self.image, (240, 240, 255), (0, 0, width, cell_size + 2), 2, border_radius=3)
        # Внутренние линии
        pygame.draw.line(self.image, (240, 240, 255), (cell_size, 0), (cell_size, height), 2)
        pygame.draw.line(self.image, (240, 240, 255), (0, cell_size), (width, cell_size), 2)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.cell_size = cell_size
        self.score = 3

    def check(self):
        x = self.rect.x + self.cell_size // 2
        y = self.rect.y + self.cell_size // 2
        cell = self.game.get_cell((x, y))
        if cell is None:
            return None
        row, col = cell
        if row + 2 > self.game.grid_size or col + 2 > self.game.grid_size:
            return None

        # Проверяем L-образную область (ориентация: ┌)
        if (self.game.grid[row][col] != self.game.colors['black'] or
            self.game.grid[row + 1][col] != self.game.colors['black'] or
            self.game.grid[row][col + 1] != self.game.colors['black']):
            return None

        return row, col

    def place_on_grid(self):
        x = self.rect.x + self.cell_size // 2
        y = self.rect.y + self.cell_size // 2
        cell = self.game.get_cell((x, y))
        if cell:
            row, col = cell
            self.game.grid[row][col] = self.color
            self.game.grid[row + 1][col] = self.color
            self.game.grid[row][col + 1] = self.color

    def can_place(self):
        size = self.game.grid_size - 1
        color = self.game.colors['black']
        for row in range(size):
            for col in range(size):
                if (self.game.grid[row][col] == color and 
                    self.game.grid[row + 1][col] == color and 
                    self.game.grid[row][col + 1] == color):
                    return True
        return False


class TShape(pygame.sprite.Sprite):
    def __init__(self, color, x, y, cell_size, game):
        super().__init__()
        self.game = game
        self.color = color
        width = cell_size * 3 + 7
        height = cell_size * 2 + 5
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        # Рисуем T-образную фигуру (ориентация: T - горизонтальная палочка сверху)
        pygame.draw.rect(self.image, color, (0, 0, width, cell_size + 2), border_radius=3)  # Горизонтальная часть (сверху)
        pygame.draw.rect(self.image, color, (cell_size + 2, 0, cell_size + 2, height), border_radius=3)  # Вертикальная часть
        pygame.draw.rect(self.image, (240, 240, 255), (0, 0, width, cell_size + 2), 2, border_radius=3)
        pygame.draw.rect(self.image, (240, 240, 255), (cell_size + 2, 0, cell_size + 2, height), 2, border_radius=3)
        # Внутренние линии
        for i in range(1, 3):
            x_pos = i * (cell_size + 1)
            pygame.draw.line(self.image, (240, 240, 255), (x_pos, 0), (x_pos, height), 2)
        pygame.draw.line(self.image, (240, 240, 255), (0, cell_size), (width, cell_size), 2)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.cell_size = cell_size
        self.score = 4

    def check(self):
        x = self.rect.x + self.cell_size // 2
        y = self.rect.y + self.cell_size // 2
        cell = self.game.get_cell((x, y))
        if cell is None:
            return None
        row, col = cell
        if row + 2 > self.game.grid_size or col + 3 > self.game.grid_size:
            return None

        # Проверяем T-образную область (ориентация: T - горизонтальная палочка сверху)
        if (self.game.grid[row][col] != self.game.colors['black'] or
            self.game.grid[row][col + 1] != self.game.colors['black'] or
            self.game.grid[row][col + 2] != self.game.colors['black'] or
            self.game.grid[row + 1][col + 1] != self.game.colors['black']):
            return None

        return row, col

    def place_on_grid(self):
        x = self.rect.x + self.cell_size // 2
        y = self.rect.y + self.cell_size // 2
        cell = self.game.get_cell((x, y))
        if cell:
            row, col = cell
            self.game.grid[row][col] = self.color
            self.game.grid[row][col + 1] = self.color
            self.game.grid[row][col + 2] = self.color
            self.game.grid[row + 1][col + 1] = self.color

    def can_place(self):
        size_row = self.game.grid_size - 1
        size_col = self.game.grid_size - 2
        color = self.game.colors['black']
        for row in range(size_row):
            for col in range(size_col):
                if (self.game.grid[row][col] == color and 
                    self.game.grid[row][col + 1] == color and 
                    self.game.grid[row][col + 2] == color and 
                    self.game.grid[row + 1][col + 1] == color):
                    return True
        return False