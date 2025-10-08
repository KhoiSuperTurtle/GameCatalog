import pygame

class gameInfo:
    def __init__(self, name, description, context, image):
        self.name = name
        self.description = description
        self.context = context
        self.image = image 
    
    def getContext(self):
        return self.context
    
    def getName(self):
        return self.name
    
    def getDescription(self):
        return self.description
    
    def getImage(self):
        return self.image

# Пример использования
tetris = gameInfo("Тетрис", "Легендарная игра про блоки по новому", None, r"img\tetris.png")
tanks = gameInfo("Танчики", "Невероятно, но это не Т-34", None, None)

game_list = []
game_list.append(tetris)
game_list.append(tetris)
game_list.append(tetris)
game_list.append(tetris)
game_list.append(tetris)
game_list.append(tetris)
game_list.append(tanks)

