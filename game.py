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
    from BlockBlast.main import BlockBlastGame
except ImportError as e:
    BlockBlastGame = None
    print(f"Предупреждение: Block Blast не найден: {e}")

try:
    # Импортируем напрямую из файла
    import sys
    sys.path.insert(0, 'TextTypingGame')
    from TextTypingGame import TextTypingGame
    print("TextTypingGame успешно импортирован")
except ImportError as e:
    print(f"Ошибка импорта TextTypingGame: {e}")
    # Создаем заготовку класса для тестирования
    class TextTypingGame:
        def __init__(self, screen_width, screen_height):
            print(f"Создан TextTypingGame с размером {screen_width}x{screen_height}")
        
        def run(self):
            print("Запущен TextTypingGame")
            return "quit"
try:
    from snake.Snake123 import SnakeGame
except ImportError as e:
    SnakeGame = None
    print(f"Предупреждение: Snake не найден: {e}")
try:
    # Импортируем наш класс игры из папки tanks
    from tanks.test2 import BattleTanksGame
except ImportError as e:
    print(f"Предупреждение: Танчики не найдены: {e}")
    # Создаем заготовку класса для тестирования
    class BattleTanksGame:
        def __init__(self, screen_width, screen_height):
            print(f"Создан BattleTanksGame с размером {screen_width}x{screen_height}")
        
        def run(self):
            print("Запущен BattleTanksGame")
            return "quit"

tetris = GameInfo("Тетрис", "Легендарная игра про блоки по новому", TetrisGame, "img/tetris.png")
f1_racing = GameInfo("F1 Racing", "Гоночная игра Формулы 1", F1RacingGame, "img/f1race.png")
block_blast = GameInfo("Block Blast", "Заполняйте сетку фигурами, чтобы составлять линии", BlockBlastGame, "img/blockblast.jpg")
text_typing = GameInfo("Тайп-марафон", "Проверьте свою скорость печати на разных уровнях сложности", TextTypingGame, "img/stg.jpg")
tanks_game = GameInfo("Танчики", "Классическая игра Battle Tanks", BattleTanksGame, "img/tanks.jpg")
snake = GameInfo("Змейка", "Поедайте плоды, становитесь длинее и покорите пищевую цепь, но не самим собой", SnakeGame, "img/snake.jpg")

game_list = [
    tetris,
    f1_racing,
    block_blast,
    text_typing,
    tanks_game,
    snake
]