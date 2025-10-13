import pygame

class GameInfo:
    def __init__(self, name, description, context, image):
        self.name = name
        self.description = description
        self.context = context
        self.image = image 
    
    def get_context(self):
        return self.context
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_image(self):
        return self.image

# Пример использования
tetris = GameInfo("Тетрис", "Легендарная игра про блоки по новому", None, r"img\tetris.png")
tanks = GameInfo("Танчики", "Невероятно, но это не Т-34", None, None)

game_list = []
game_list.append(tetris)
game_list.append(tetris)
game_list.append(tetris)
game_list.append(tetris)
game_list.append(tetris)
game_list.append(tetris)
game_list.append(tanks)
game_list.append(tanks)
game_list.append(tanks)
game_list.append(tanks)
game_list.append(tanks)
game_list.append(tanks)
game_list.append(tanks)
game_list.append(tanks)
game_list.append(tanks)

