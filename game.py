import pygame

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

from tetris.tetris_main import TetrisGame
from F1Racing.Nepen import F1RacingGame

tetris = GameInfo("Тетрис", "Легендарная игра про блоки по новому", TetrisGame, r"img\tetris.png")
f1_racing = GameInfo("F1 Racing", "Гоночная игра Формулы 1", F1RacingGame, r"img\f1_racing.png")
tanks = GameInfo("Танчики", "Невероятно, но это не Т-34", None, r"img\tanks.jpg")
snake = GameInfo("Змейка", "Поедайте плоды, становитесь длинее и покорите пищевую цепь, но не самим собой", None, r"img\snake.jpg")
flappy = GameInfo("FlappyBird", "Пролетайте между трубами за неуклюжую птицу Flappy", None, r"img\flappy.jpg")
dino = GameInfo("DinoGame", "Рассекайте пустыню за динозавра", None, r"img\dino.jpg")

game_list = [
    tetris,
    f1_racing,
    tanks,
    snake,
    dino,
    flappy
]