import pygame
import os

class BaseGame:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = None
        self.running = False
        
    def run(self):
        raise NotImplementedError("Метод run должен быть реализован в дочернем классе")
    
    def handle_events(self):
        raise NotImplementedError("Метод handle_events должен быть реализован в дочернем классе")
    
    def update(self):
        raise NotImplementedError("Метод update должен быть реализован в дочернем классе")
    
    def draw(self):
        raise NotImplementedError("Метод draw должен быть реализован в дочернем классе")


class GameInfo:
    def __init__(self, name, description, game_class, image):
        self.name = name
        self.description = description
        self.game_class = game_class  
        self.image = image 
    
    def get_game_class(self):
        return self.game_class
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_image(self):
        return self.image


# Импортируем игры из соответствующих директорий
try:
    from tetris.tetris_main import TetrisGame
except ImportError:
    TetrisGame = None
    print("Предупреждение: Tetris не найден")

try:
    from F1Racing.Nepen import F1RacingGame
except ImportError:
    F1RacingGame = None
    print("Предупреждение: F1 Racing не найден")

try:
    # Импорт Block Blast
    from BlockBlast.main import BlockBlastGame
except ImportError as e:
    BlockBlastGame = None
    print(f"Предупреждение: Block Blast не найден: {e}")

# Создаем объекты игр
tetris = GameInfo("Тетрис", "Легендарная игра про блоки по новому", TetrisGame, "img/tetris.png")
f1_racing = GameInfo("F1 Racing", "Гоночная игра Формулы 1", F1RacingGame, "img/f1_racing.png")
block_blast = GameInfo("Block Blast", "Заполняйте сетку фигурами, чтобы составлять линии", BlockBlastGame, "img/block_blast.png")
tanks = GameInfo("Танчики", "Невероятно, но это не Т-34", None, "img/tanks.jpg")
snake = GameInfo("Змейка", "Поедайте плоды, становитесь длинее и покорите пищевую цепь, но не самим собой", None, "img/snake.jpg")
flappy = GameInfo("FlappyBird", "Пролетайте между трубами за неуклюжую птицу Flappy", None, "img/flappy.jpg")
dino = GameInfo("DinoGame", "Рассекайте пустыню за динозавра", None, "img/dino.jpg")

game_list = [
    tetris,
    f1_racing,
    block_blast,
    tanks,
    snake,
    dino,
    flappy
]