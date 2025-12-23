# -*- coding: UTF-8 -*-
import pygame
import random
import time
import os

# Добавляем путь к текущей папке для импорта levels.py
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Пытаемся импортировать levels, если не получится - создадим заглушку
try:
    import levels
except ImportError:
    # Создаем заглушку для levels
    class Levels:
        lev = [
            # Уровень 0
            [
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            ],
            # Уровень 1
            [
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            ]
        ]
    
    levels = Levels()

# Класс игры для интеграции с каталогом
class BattleTanksGame:
    def __init__(self, screen_width, screen_height):
        # Игнорируем переданные размеры, используем фиксированные
        self.screen_width = 650
        self.screen_height = 500
        self.screen = None
        self.running = False
        self.game_instance = None
    
    def run(self):
        # Запускаем оригинальную игру
        self.game_instance = BattleTanks()
        return self.game_instance.run()

# Основной класс игры (оригинальный код, адаптированный)
class BattleTanks:
    def __init__(self):
        pygame.init()
        
        # Фиксированный размер окна как в оригинальной игре
        self.size = 650, 500
        self.screen = pygame.display.set_mode(self.size, pygame.DOUBLEBUF | pygame.HWSURFACE)
        pygame.display.set_caption('Battle Tanks')
        self.clock = pygame.time.Clock()
        self.color = 0, 0, 0
        self.color2 = 0, 255, 0
        
        # Получаем путь к папке с изображениями
        current_dir = os.path.dirname(os.path.abspath(__file__))
        images_dir = os.path.join(current_dir, 'images')
        
        # Загружаем изображения
        self.fs = pygame.image.load(os.path.join(images_dir, 'fs.png'))
        self.back = pygame.image.load(os.path.join(images_dir, 'back.jpg'))
        self.kir = pygame.image.load(os.path.join(images_dir, 'kir.png'))
        self.beton = pygame.image.load(os.path.join(images_dir, 'beton.png'))
        self.forest = pygame.image.load(os.path.join(images_dir, 'forest.png'))
        self.base = pygame.image.load(os.path.join(images_dir, 'base.png'))
        self.dbase = pygame.image.load(os.path.join(images_dir, 'dbase.png'))
        self.water = pygame.image.load(os.path.join(images_dir, 'water.png'))
        
        bullet1_img = pygame.image.load(os.path.join(images_dir, 'ammo.png'))
        self.bullet1 = bullet1_img
        self.bullet2 = pygame.transform.rotate(bullet1_img, 180)
        self.bullet3 = pygame.transform.rotate(bullet1_img, 90)
        self.bullet4 = pygame.transform.rotate(bullet1_img, 270)
        
        self.ggu = pygame.image.load(os.path.join(images_dir, 'ggu.png'))
        self.enu = pygame.image.load(os.path.join(images_dir, 'vrag1.png'))
        self.enu2 = pygame.image.load(os.path.join(images_dir, 'vrag2.png'))
        self.enu3 = pygame.image.load(os.path.join(images_dir, 'vrag3.png'))
        
        self.e = pygame.image.load(os.path.join(images_dir, 'e.png'))
        self.bb = pygame.image.load(os.path.join(images_dir, 'bboom.png'))
        self.bl = pygame.image.load(os.path.join(images_dir, 'blopatka.png'))
        self.bz = pygame.image.load(os.path.join(images_dir, 'bzvezdochka.png'))
        
        self.e_rect = self.e.get_rect()
        self.e_rect.width = self.e_rect.height
        self.slide_rect = self.e.get_rect()
        self.slide_rect.width = self.slide_rect.height
        
        # Инициализация игровых переменных
        self.reloads = 60
        self.bonuses = []
        self.level = 0
        self.ii = 0
        self.lopatka = 0
        self.lopatka_s = 0
        self.orient = 1
        self.move = 0
        self.lev = levels.lev[self.level]
        self.matrix = self.lev
        self.counten = 0
        self.betas = 0
        self.x = 0
        self.y = 0
        self.a = self.matrix
        self.shoot = 0
        self.fly = 0
        self.ilolo = 118
        self.shoots = []
        self.enemyes = []
        self.gmove = 0
        self.vermove = 0
        self.key = 0
        self.enable = 0
        
        self.font = pygame.font.Font(None, 36)
        self.font2 = pygame.font.Font(None, 18)
        self.font3 = pygame.font.Font(None, 64)
        self.font4 = pygame.font.Font(None, 96)
        
        self.zet = 0
        self.initbase = True
        self.basehp = 2
        self.plives = 3
        self.plshoot = 1
        self.shbonus = random.randint(300, 700)
        self.rect = []
        self.booms = []
        
        # Позиция игрока
        self.ggx = 9
        self.ggy = 22
        self.i = 0
        self.shet = 0
        self.player = 1
        self.player2 = 20
        self.fight = 0
        self.p2count = 20
        self.kleo = 100
        self.go = False
        self.done = False
        
        # Инициализация объектов
        self.play = None
        self.bbase = None
        
        # Меню
        self.menu = self.font3.render(u'Новая игра', 1, (255, 255, 10))
        self.menupos = pygame.Rect(45, 340, 247, 45)
        self.menu2 = self.font3.render(u'Выход', 1, (255, 255, 10))
        self.menupos2 = pygame.Rect(45, 400, 154, 45)
        self.menu3 = self.font4.render(u'Battle tanks', 1, (255, 0, 0))
        self.menupos3 = pygame.Rect(125, 40, 247, 45)
        
        # Создаем игрока
        if self.player == 1:
            self.player -= 1
            self.play = Player(self.ggx, self.ggy, self)
    
    def pole(self, a):
        x = 0
        y = 0
        i = 0
        while i < 625:
            if a[y][x] == 0:
                self.screen.blit(self.fs, (x*20, y*20))
            elif a[y][x] == 1:
                self.screen.blit(self.beton, (x*20, y*20))
            elif a[y][x] == 2:
                self.screen.blit(self.kir, (x*20, y*20))
            elif a[y][x] == 4:
                self.screen.blit(self.water, (x*20, y*20))
            elif a[y][x] == 6:
                self.screen.blit(self.base, (x*20, y*20))
            elif a[y][x] == 7:
                self.screen.blit(self.fs, (x*20, y*20))
            x += 1
            if x > 24:
                x = 0
                y += 1
            i += 1
    
    def poleFFF(self, a):
        x = 0
        y = 0
        i = 0
        while i < 625:
            if a[y][x] == 3:
                self.screen.blit(self.forest, (x*20, y*20))
            x += 1
            if x > 24:
                x = 0
                y += 1
            i += 1
    
    def mmenu(self, go):
        game = 0
        while not go:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                    go = True
                    return "quit"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.done = True
                        go = True
                        return "quit"
                elif event.type == pygame.MOUSEMOTION:
                    if self.menupos2.collidepoint(event.pos):
                        self.menu2 = self.font3.render(u'Выход', 1, (255, 0, 0))
                        self.menu = self.font3.render(u'Новая игра', 1, (255, 255, 10))
                        game = 2
                    elif self.menupos.collidepoint(event.pos):
                        self.menu = self.font3.render(u'Новая игра', 1, (255, 0, 0))
                        self.menu2 = self.font3.render(u'Выход', 1, (255, 255, 10))
                        game = 1
                    else:
                        self.menu = self.font3.render(u'Новая игра', 1, (255, 255, 10))
                        self.menu2 = self.font3.render(u'Выход', 1, (255, 255, 10))
                        game = 0
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if game == 1:
                        go = True
                        self.done = False
                    elif game == 2:
                        go = True
                        self.done = True
                        return "quit"
            
            self.screen.fill(self.color)
            self.screen.blit(self.back, (0, 0))
            self.screen.blit(self.menu, self.menupos)
            self.screen.blit(self.menu2, self.menupos2)
            self.screen.blit(self.menu3, self.menupos3)
            pygame.display.flip()
        
        return "continue"
    
    def run(self):
        # Показываем меню
        result = self.mmenu(self.go)
        if result == "quit":
            pygame.quit()
            return "quit"
        
        # Основной игровой цикл
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                    return "quit"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.done = True
                        return "quit"
                    
                    if event.key == pygame.K_LEFT and self.play.orient == 3 and self.play.wall != 3:
                        self.key = 3
                        self.enable = 1
                    elif event.key == pygame.K_RIGHT and self.play.orient == 4 and self.play.wall != 4:
                        self.key = 4
                        self.enable = 1
                    elif event.key == pygame.K_UP and self.play.orient == 1 and self.play.wall != 1:
                        self.key = 1
                        self.enable = 1
                    elif event.key == pygame.K_DOWN and self.play.orient == 2 and self.play.wall != 2:
                        self.key = 2
                        self.enable = 1
                    elif event.key == pygame.K_LEFT and self.play.orient != 3 and self.enable == 0 and self.play.move == 0:
                        self.play.orient = 3
                        self.play.gg = self.play.ggl
                    elif event.key == pygame.K_RIGHT and self.play.orient != 4 and self.enable == 0 and self.play.move == 0:
                        self.play.orient = 4
                        self.play.gg = self.play.ggr
                    elif event.key == pygame.K_UP and self.play.orient != 1 and self.enable == 0 and self.play.move == 0:
                        self.play.orient = 1
                        self.play.gg = self.play.ggu
                    elif event.key == pygame.K_DOWN and self.play.orient != 2 and self.enable == 0 and self.play.move == 0:
                        self.play.orient = 2
                        self.play.gg = self.play.ggd
                    elif event.key == pygame.K_SPACE:
                        if self.fight <= 0:
                            self.shoots.append(Shoot(self.play.ggx, self.play.ggy, self.play.orient, 1, self))
                            if self.play.power == 3:
                                self.plshoot = 9
                            elif self.play.power == 4:
                                self.plshoot = 19
                            self.fight = 20
                
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and self.play.orient == 3:
                        self.key = 0
                        self.enable = 0
                    elif event.key == pygame.K_RIGHT and self.play.orient == 4:
                        self.key = 0
                        self.enable = 0
                    elif event.key == pygame.K_UP and self.play.orient == 1:
                        self.key = 0
                        self.enable = 0
                    elif event.key == pygame.K_DOWN and self.play.orient == 2:
                        self.key = 0
                        self.enable = 0
            
            self.fight -= 1
            
            if self.initbase == True:
                self.bbase = Base(self.basehp)
                self.initbase = False
            
            if self.plshoot == 5:
                self.shoots.append(Shoot(self.play.ggx, self.play.ggy, self.play.orient, 1, self))
                self.plshoot = 1
            elif self.plshoot == 10:
                self.shoots.append(Shoot(self.play.ggx, self.play.ggy, self.play.orient, 1, self))
                self.plshoot -= 1
            elif self.plshoot == 1:
                pass
            else:
                self.plshoot -= 1
            
            self.play.moveP(self.key)
            self.play.walls(self.matrix)
            
            if self.player2 > 0:
                if len(self.enemyes) < 4:
                    if self.shet == 0:
                        self.player2 -= 1
                        respoun = random.randint(1, 3)
                        tip = random.randint(1, 3)
                        qwerty = Enemy(tip, respoun, self)
                        self.enemyes.append(qwerty)
                        self.shet = 100
                    self.shet -= 1
            
            for enemy in self.enemyes:
                enemy.walls(self.matrix)
                enemy.enshoot()
                enemy.move()
                enemy.walls(self.matrix)
            
            if self.shbonus == 0:
                self.bonuses.append(Bonus(self.matrix, self))
                self.shbonus = random.randint(300, 700)
            else:
                self.shbonus -= 1
            
            m1m = 0
            while m1m < len(self.shoots):
                m2m = 0
                while m2m < len(self.shoots):
                    dx = self.shoots[m2m].x - self.shoots[m1m].x
                    dy = self.shoots[m2m].y - self.shoots[m1m].y
                    if dx < 0:
                        dx = -dx
                    if dy < 0:
                        dy = -dy
                    if self.shoots[m2m].sight == self.shoots[m1m].sight:
                        pass
                    elif (self.shoots[m2m].x == self.shoots[m1m].x and self.shoots[m2m].y == self.shoots[m1m].y) or (dx < 3 and dy < 3):
                        self.booms.append(Boom((self.shoots[m1m].x*2+10, self.shoots[m1m].y*2+10), self))
                        self.shoots.pop(m2m)
                        self.shoots.pop(m1m)
                    m2m += 1
                m1m += 1
            
            fps = (str((float(int(self.clock.get_fps()*10))//10)))
            fps2 = 'fps: ' + fps
            
            text = self.font.render(fps2, 1, (255, 255, 10))
            textpos = text.get_rect()
            textpos = (510, 30)
            
            text2 = self.font2.render(u'Осталось врагов: ' + str(self.p2count), 1, (255, 255, 10))
            textpos2 = text2.get_rect()
            textpos2 = (510, 60)
            
            text3 = self.font3.render(u'Вы победили!', 1, (255, 10, 10))
            textpos3 = text3.get_rect(centerx=(self.screen.get_width()-140)//2, centery=self.screen.get_height()//2)
            text4 = self.font.render(u'Уровень: ' + str(self.level + 1), 1, (255, 255, 10))
            textpos4 = text4.get_rect()
            textpos4 = (510, 5)
            text5 = self.font3.render(u'Вы проиграли!', 1, (255, 10, 10))
            textpos5 = text5.get_rect(centerx=(self.screen.get_width()-140)//2, centery=self.screen.get_height()//2)
            
            text9 = self.font3.render(u'Вы прошли игру!', 1, (255, 10, 10))
            textpos9 = text5.get_rect(centerx=(self.screen.get_width())//2, centery=self.screen.get_height()//2)
            
            text6 = self.font2.render(u'Уровень игрока: ' + str(self.play.power - 1), 1, (255, 255, 10))
            textpos6 = text2.get_rect()
            textpos6 = (510, 80)
            
            text7 = self.font2.render(u'Здоровье игрока: ' + str(self.play.hp), 1, (255, 255, 10))
            textpos7 = text2.get_rect()
            textpos7 = (510, 100)
            
            text8 = self.font2.render(u'Жизни игрока: ' + str(self.plives), 1, (255, 255, 10))
            textpos8 = text2.get_rect()
            textpos8 = (510, 120)
            
            for i in reversed(range(0, len(self.enemyes))):
                for k in reversed(range(0, len(self.shoots))):
                    if self.shoots[k].sight == 0:
                        pass
                    else:
                        if self.enemyes[i].rect.colliderect(self.shoots[k].rect):
                            self.enemyes[i].hp -= 15
                            self.booms.append(Boom((self.shoots[k].rect.center), self))
                            self.shoots.pop(k)
                            if self.enemyes[i].hp <= 0:
                                self.enemyes.pop(i)
                                i -= 1
                                self.p2count -= 1
            
            for i in reversed(range(0, len(self.enemyes))):
                for k in reversed(range(0, len(self.bonuses))):
                    if self.enemyes[i].rect.colliderect(self.bonuses[k].rect):
                        self.bonuses.pop(k)
            
            for i in reversed(range(0, len(self.shoots))):
                if self.shoots[i].sight == 1:
                    pass
                else:
                    if self.play.rect.colliderect(self.shoots[i].rect):
                        self.play.hp -= 15
                        self.booms.append(Boom((self.shoots[i].rect.center), self))
                        self.shoots.pop(i)
                        if self.play.hp < 0:
                            self.booms.append(Boom((self.play.rect.center), self))
                            self.zet = 1
                            self.plives -= 1
            
            for k in reversed(range(0, len(self.bonuses))):
                if self.play.rect.colliderect(self.bonuses[k].rect):
                    if self.bonuses[k].type == 1:
                        for i in reversed(range(0, len(self.enemyes))):
                            self.booms.append(Boom((self.enemyes[i].rect.center), self))
                            self.enemyes.pop(i)
                            self.counten += 1
                        self.p2count -= self.counten
                        self.counten = 0
                        self.bonuses.pop(k)
                    elif self.bonuses[k].type == 2:
                        self.matrix[23][11] = 1
                        self.matrix[23][13] = 1
                        self.matrix[22][11] = 1
                        self.matrix[22][13] = 1
                        self.matrix[22][12] = 1
                        self.bonuses.pop(k)
                        self.lopatka = 1
                        self.lopatka_s = 300
                    elif self.bonuses[k].type == 3:
                        self.bonuses.pop(k)
                        self.play.power += 1
                        if self.play.power > 4:
                            self.play.power = 4
                        self.play.hp += 5
            
            if self.lopatka == 1:
                if self.lopatka_s == 0:
                    self.matrix[23][11] = 2
                    self.matrix[23][13] = 2
                    self.matrix[22][11] = 2
                    self.matrix[22][13] = 2
                    self.matrix[22][12] = 2
                    self.lopatka = 0
                else:
                    self.lopatka_s -= 1
            
            for i in reversed(range(0, len(self.booms))):
                self.booms[i].step()
                if self.booms[i].destroy():
                    self.booms.pop(i)
            
            for i in reversed(range(0, len(self.enemyes))):
                Rect = self.play.rect
                if Rect.colliderect(self.enemyes[i].rect):
                    if self.play.power > self.enemyes[i].tip:
                        self.booms.append(Boom((self.enemyes[i].rect.center), self))
                        self.enemyes.pop(i)
                        self.p2count -= 1
                    elif self.play.power <= self.enemyes[i].tip:
                        if self.zet == 0:
                            self.booms.append(Boom((self.play.rect.center), self))
                            self.plives -= 1
                            self.zet = 1
            
            for i in reversed(range(0, len(self.shoots))):
                self.shoots[i].step()
                if self.shoots[i].destroy(self.matrix):
                    self.shoots.pop(i)
            
            if self.zet != 0 and self.plives > 0:
                if self.zet == 20:
                    powerp = self.play.power
                    self.play = Player(self.ggx, self.ggy, self)
                    self.play.power = powerp
                    self.zet = 0
                else:
                    self.zet += 1
            
            if self.bbase.basehp == 0:
                self.base = self.dbase
            
            self.screen.fill(self.color)
            pygame.draw.rect(self.screen, self.color2, (0, 0, 500, 500), 5)
            self.pole(self.matrix)
            for enemy in self.enemyes:
                enemy.render(self.screen)
            if self.zet == 0:
                self.play.render(self.screen)
            for shoot in self.shoots:
                shoot.render(self.screen)
            for bonus in self.bonuses:
                bonus.render(self.screen)
            for boom in self.booms:
                boom.render(self.screen)
            self.poleFFF(self.matrix)
            self.screen.blit(text, textpos)
            self.screen.blit(text2, textpos2)
            self.screen.blit(text4, textpos4)
            self.screen.blit(text6, textpos6)
            self.screen.blit(text7, textpos7)
            self.screen.blit(text8, textpos8)
            
            if self.p2count == 0:
                self.screen.blit(text3, textpos3)
                if self.reloads != 0:
                    self.reloads -= 1
                else:
                    time.sleep(1)
                    self.p2count = 20
                    self.player2 = 20
                    for k in reversed(range(0, len(self.bonuses))):
                        self.bonuses.pop(k)
                    self.level += 1
                    if self.level == 3:
                        self.screen.fill((0, 0, 0))
                        self.screen.blit(text9, textpos9)
                        if self.reloads != 0:
                            self.reloads -= 1
                        else:
                            time.sleep(1)
                            self.reloads = 60
                            self.go = False
                            self.done = True
                            return "quit"
                    else:
                        self.matrix = levels.lev[self.level]
                    self.reloads = 60
                    self.shbonus = random.randint(300, 700)
                    self.enable = 0
                    powerp = self.play.power
                    self.play = Player(self.ggx, self.ggy, self)
                    self.play.power = powerp
            
            elif self.bbase.basehp < 1 or self.plives < 1:
                self.screen.blit(text5, textpos5)
                if self.reloads != 0:
                    self.reloads -= 1
                else:
                    time.sleep(1)
                    self.reloads = 60
                    self.go = False
                    self.done = True
                    return "quit"
            
            pygame.display.flip()
            self.clock.tick(30)
        
        return "quit"

# Классы из оригинальной игры (исправленные)
class Base:
    def __init__(self, basehp):
        self.basehp = basehp

class Boom:
    def __init__(self, e_rectcenter, game):
        self.game = game
        current_dir = os.path.dirname(os.path.abspath(__file__))
        images_dir = os.path.join(current_dir, 'images')
        
        self.explosion = pygame.image.load(os.path.join(images_dir, 'e.png'))
        self.e_rect = self.explosion.get_rect()
        self.e_rect.center = e_rectcenter
        self.slide_rect = self.explosion.get_rect()
        self.ilolo = 0
    
    def render(self, screen):
        screen.blit(self.explosion, self.e_rect, self.slide_rect)
    
    def step(self):
        self.ilolo += 1
        self.slide_rect.x = (self.ilolo // 2) * 20
    
    def destroy(self):
        if self.ilolo > 7:
            return True
        return False

class Bonus:
    def __init__(self, matrix, game):
        self.game = game
        current_dir = os.path.dirname(os.path.abspath(__file__))
        images_dir = os.path.join(current_dir, 'images')
        
        self.type = random.randint(1, 3)
        if self.type == 1:
            self.image = pygame.image.load(os.path.join(images_dir, 'bboom.png'))
        elif self.type == 2:
            self.image = pygame.image.load(os.path.join(images_dir, 'blopatka.png'))
        elif self.type == 3:
            self.image = pygame.image.load(os.path.join(images_dir, 'bzvezdochka.png'))
        
        self.x = 0
        self.y = 0
        while matrix[self.y][self.x] != 0:
            self.x = random.randint(1, 23)
            self.y = random.randint(1, 23)
        self.rect = pygame.Rect((self.x*20, self.y*20), (20, 20))
    
    def render(self, screen):
        screen.blit(self.image, (self.x*20, self.y*20))

class Shoot:
    def __init__(self, pos1, pos2, orient, sight, game):
        self.game = game
        current_dir = os.path.dirname(os.path.abspath(__file__))
        images_dir = os.path.join(current_dir, 'images')
        
        bullet1_img = pygame.image.load(os.path.join(images_dir, 'ammo.png'))
        self.bullet1 = bullet1_img
        self.bullet2 = pygame.transform.rotate(bullet1_img, 180)
        self.bullet3 = pygame.transform.rotate(bullet1_img, 90)
        self.bullet4 = pygame.transform.rotate(bullet1_img, 270)
        
        self.x = pos1
        self.y = pos2
        self.orient = orient
        self.speed = 2
        self.damage = 15
        self.sight = sight
        self.rect = pygame.Rect(self.x*2+5, self.y*2+5, 10, 10)
    
    def step(self):
        if self.orient == 1:
            self.y -= self.speed
        elif self.orient == 2:
            self.y += self.speed
        elif self.orient == 3:
            self.x -= self.speed
        elif self.orient == 4:
            self.x += self.speed
        self.rect = pygame.Rect(self.x*2+5, self.y*2+5, 10, 10)
    
    def destroy(self, matrix):
        if self.orient == 1:
            up = matrix[self.y // 10 + 1][self.x // 10]
            if up == 1:
                self.game.booms.append(Boom((self.x*2+10, self.y*2+20), self.game))
                return True
            elif up == 6:
                self.game.booms.append(Boom((self.x*2+10, self.y*2+10), self.game))
                self.game.bbase.basehp -= 1
                return True
            elif up == 2:
                matrix[self.y // 10 + 1][self.x // 10] = 0
                self.game.play.wall = 0
                self.game.booms.append(Boom((self.x*2+10, self.y*2+10), self.game))
                return True
            else:
                return False
        elif self.orient == 2:
            down = matrix[self.y // 10][self.x // 10]
            if down == 1:
                self.game.booms.append(Boom((self.x*2+10, self.y*2), self.game))
                return True
            elif down == 6:
                self.game.booms.append(Boom((self.x*2+10, self.y*2+10), self.game))
                self.game.bbase.basehp -= 1
                return True
            elif down == 2:
                matrix[self.y // 10][self.x // 10] = 0
                self.game.play.wall = 0
                self.game.booms.append(Boom((self.x*2+10, self.y*2+10), self.game))
                return True
            else:
                return False
        elif self.orient == 3:
            left = matrix[self.y // 10][self.x // 10 + 1]
            if left == 1:
                self.game.booms.append(Boom((self.x*2+20, self.y*2+10), self.game))
                return True
            elif left == 6:
                self.game.booms.append(Boom((self.x*2+14, self.y*2+10), self.game))
                self.game.bbase.basehp -= 1
                return True
            elif left == 2:
                matrix[self.y // 10][self.x // 10 + 1] = 0
                self.game.play.wall = 0
                self.game.booms.append(Boom((self.x*2+14, self.y*2+10), self.game))
                return True
            else:
                return False
        elif self.orient == 4:
            right = matrix[self.y // 10][self.x // 10]
            if right == 1:
                self.game.booms.append(Boom((self.x*2, self.y*2+10), self.game))
                return True
            elif right == 6:
                self.game.booms.append(Boom((self.x*2+10, self.y*2+10), self.game))
                self.game.bbase.basehp -= 1
                return True
            elif right == 2:
                matrix[self.y // 10][self.x // 10] = 0
                self.game.play.wall = 0
                self.game.booms.append(Boom((self.x*2+10, self.y*2+10), self.game))
                return True
            else:
                return False
    
    def render(self, screen):
        if self.orient == 1:
            screen.blit(self.bullet1, (self.x*2, self.y*2))
        elif self.orient == 2:
            screen.blit(self.bullet2, (self.x*2, self.y*2))
        elif self.orient == 3:
            screen.blit(self.bullet3, (self.x*2, self.y*2))
        elif self.orient == 4:
            screen.blit(self.bullet4, (self.x*2, self.y*2))

class Player:
    def __init__(self, pos1, pos2, game):
        self.game = game
        current_dir = os.path.dirname(os.path.abspath(__file__))
        images_dir = os.path.join(current_dir, 'images')
        
        self.ggx = pos1 * 10
        self.ggy = pos2 * 10
        self.orient = 1
        self.hp = 25
        self.lives = 3
        self.move = 0
        
        self.ggu = pygame.image.load(os.path.join(images_dir, 'ggu.png'))
        self.ggd = pygame.transform.rotate(self.ggu, 180)
        self.ggl = pygame.transform.rotate(self.ggu, 90)
        self.ggr = pygame.transform.rotate(self.ggu, 270)
        self.gg = self.ggu
        self.wall = 0
        self.rect = pygame.Rect(self.ggx*2, self.ggy*2, 20, 20)
        self.power = 2
    
    def moveP(self, key):
        if self.orient == 1 and self.wall != 1:
            if key == 1:
                self.ggy -= 1
                self.wall = 0
            elif key != 0:
                self.orient = key
                self.move = 0
            if (self.ggy % 10) == 0:
                key = 0
                self.move = 0
            elif key == 0:
                self.ggy -= 1
                self.move = 1
        
        elif self.orient == 2 and self.wall != 2:
            if key == 2:
                self.ggy += 1
                self.wall = 0
            elif key != 0:
                self.orient = key
                self.move = 0
            if (self.ggy % 10) == 0:
                key = 0
                self.move = 0
            elif key == 0:
                self.ggy += 1
                self.move = 1
        
        elif self.orient == 3 and self.wall != 3:
            if key == 3:
                self.ggx -= 1
                self.wall = 0
            elif key != 0:
                self.orient = key
                self.move = 0
            if (self.ggx % 10) == 0:
                key = 0
                self.move = 0
            elif key == 0:
                self.ggx -= 1
                self.move = 1
        
        elif self.orient == 4 and self.wall != 4:
            if key == 4:
                self.ggx += 1
                self.wall = 0
            elif key != 0:
                self.orient = key
                self.move = 0
            if (self.ggx % 10) == 0:
                key = 0
                self.move = 0
            elif key == 0:
                self.ggx += 1
                self.move = 1
        
        else:
            self.move = 0
        self.rect = pygame.Rect(self.ggx*2, self.ggy*2, 20, 20)
    
    def walls(self, matrix):
        if (self.ggy % 10) == 0 and (self.ggx % 10) == 0:
            Y_axisd = matrix[self.ggy // 10 + 1][self.ggx // 10]
            Y_axisu = matrix[self.ggy // 10 - 1][self.ggx // 10]
            X_axisr = matrix[self.ggy // 10][self.ggx // 10 + 1]
            X_axisl = matrix[self.ggy // 10][self.ggx // 10 - 1]
            if (Y_axisd == 1 or Y_axisd == 2 or Y_axisd == 4 or Y_axisd == 6) and self.orient == 2:
                self.wall = 2
            elif (Y_axisu == 1 or Y_axisu == 2 or Y_axisu == 4 or Y_axisu == 6) and self.orient == 1:
                self.wall = 1
            elif (X_axisr == 1 or X_axisr == 2 or X_axisr == 4 or X_axisr == 6) and self.orient == 4:
                self.wall = 4
            elif (X_axisl == 1 or X_axisl == 2 or X_axisl == 4 or X_axisl == 6) and self.orient == 3:
                self.wall = 3
    
    def render(self, screen):
        screen.blit(self.gg, (self.ggx*2, self.ggy*2))
    
    def touch(self, i):
        if self.orient == 1:
            if (self.ggx == self.game.enemyes[i].x and self.ggy - 10 == self.game.enemyes[i].y):
                self.wall = 1
                return True
            return False
        elif self.orient == 2:
            if (self.ggx == self.game.enemyes[i].x and self.ggy + 10 == self.game.enemyes[i].y):
                self.wall = 2
                return True
            return False
        elif self.orient == 3:
            if (self.ggx - 10 == self.game.enemyes[i].x and self.ggy == self.game.enemyes[i].y):
                self.wall = 3
                return True
            return False
        elif self.orient == 4:
            if (self.ggx + 10 == self.game.enemyes[i].x and self.ggy == self.game.enemyes[i].y):
                self.wall = 4
                return True
            return False

class Enemy:
    def __init__(self, tip, resp, game):
        self.game = game
        current_dir = os.path.dirname(os.path.abspath(__file__))
        images_dir = os.path.join(current_dir, 'images')
        
        self.orient = 2
        self.wall = 0
        self.shor = 0
        self.timer = 0
        self.k = 40
        self.lap = 0
        self.tip = tip
        self.resp = resp
        
        if self.tip == 1:
            self.enu = pygame.image.load(os.path.join(images_dir, 'vrag1.png'))
            self.end = pygame.transform.rotate(self.enu, 180)
            self.enl = pygame.transform.rotate(self.enu, 90)
            self.enr = pygame.transform.rotate(self.enu, 270)
            self.en = self.end
            self.hp = 15
        elif self.tip == 2:
            self.enu = pygame.image.load(os.path.join(images_dir, 'vrag2.png'))
            self.end = pygame.transform.rotate(self.enu, 180)
            self.enl = pygame.transform.rotate(self.enu, 90)
            self.enr = pygame.transform.rotate(self.enu, 270)
            self.en = self.end
            self.hp = 30
        elif self.tip == 3:
            self.enu = pygame.image.load(os.path.join(images_dir, 'vrag3.png'))
            self.end = pygame.transform.rotate(self.enu, 180)
            self.enl = pygame.transform.rotate(self.enu, 90)
            self.enr = pygame.transform.rotate(self.enu, 270)
            self.en = self.end
            self.hp = 45
        
        if resp == 1:
            self.x, self.y = 10, 10
        elif resp == 2:
            self.x, self.y = 120, 10
        elif resp == 3:
            self.x, self.y = 230, 10
        
        self.rect = pygame.Rect(self.x*2, self.y*2, 20, 20)
    
    def walls(self, matrix):
        if (self.y % 10) == 0 and (self.x % 10) == 0:
            Y_axisd = matrix[self.y // 10 + 1][self.x // 10]
            Y_axisu = matrix[self.y // 10 - 1][self.x // 10]
            X_axisr = matrix[self.y // 10][self.x // 10 + 1]
            X_axisl = matrix[self.y // 10][self.x // 10 - 1]
            if (Y_axisd == 1 or Y_axisd == 2 or Y_axisd == 4 or Y_axisd == 6) and self.orient == 2:
                self.wall = 2
            elif (Y_axisu == 1 or Y_axisu == 2 or Y_axisu == 4 or Y_axisu == 6) and self.orient == 1:
                self.wall = 1
            elif (X_axisr == 1 or X_axisr == 2 or X_axisr == 4 or X_axisr == 6) and self.orient == 4:
                self.wall = 4
            elif (X_axisl == 1 or X_axisl == 2 or X_axisl == 4 or X_axisl == 6) and self.orient == 3:
                self.wall = 3
            else:
                self.wall = 0
    
    def move(self):
        if self.wall != self.orient and self.timer == 0:
            self.shor += 1
            if self.orient == 1:
                self.en = self.enu
                self.y -= 1
            elif self.orient == 2:
                self.en = self.end
                self.y += 1
            elif self.orient == 3:
                self.en = self.enl
                self.x -= 1
            elif self.orient == 4:
                self.en = self.enr
                self.x += 1
        elif self.wall == self.orient and self.timer == 0:
            if self.lap == 0:
                if self.orient == 1:
                    self.game.shoots.append(Shoot(self.x, self.y - 4, self.orient, 0, self.game))
                elif self.orient == 2:
                    self.game.shoots.append(Shoot(self.x, self.y + 4, self.orient, 0, self.game))
                elif self.orient == 3:
                    self.game.shoots.append(Shoot(self.x - 4, self.y, self.orient, 0, self.game))
                elif self.orient == 4:
                    self.game.shoots.append(Shoot(self.x + 4, self.y, self.orient, 0, self.game))
                self.lap = 1
            elif self.lap == 1:
                oldor = self.orient
                if oldor == 1:
                    oldor2 = 2
                elif oldor == 2:
                    oldor2 = 1
                elif oldor == 3:
                    oldor2 = 4
                else:
                    oldor2 = 3
                while self.orient == oldor:
                    self.orient = random.randint(1, 4)
                self.timer = 30
                self.lap = 0
        
        elif self.timer == 10:
            if self.orient == 1:
                self.en = self.enu
            elif self.orient == 2:
                self.en = self.end
            elif self.orient == 3:
                self.en = self.enl
            elif self.orient == 4:
                self.en = self.enr
            self.timer -= 1
        else:
            self.timer -= 1
        
        if self.shor == 30 and self.wall == 0:
            oldor = self.orient
            if oldor == 1:
                oldor2 = 2
            elif oldor == 2:
                oldor2 = 1
            elif oldor == 3:
                oldor2 = 4
            else:
                oldor2 = 3
            self.orient = random.randint(1, 4)
            if oldor == self.orient or self.orient == oldor2:
                pass
            else:
                self.timer = 30
            self.shor = 0
        
        self.rect = pygame.Rect(self.x*2, self.y*2, 20, 20)
    
    def render(self, screen):
        screen.blit(self.en, (self.x*2, self.y*2))
    
    def enshoot(self):
        if self.k == 0:
            if self.orient == 1:
                self.game.shoots.append(Shoot(self.x, self.y - 4, self.orient, 0, self.game))
            elif self.orient == 2:
                self.game.shoots.append(Shoot(self.x, self.y + 4, self.orient, 0, self.game))
            elif self.orient == 3:
                self.game.shoots.append(Shoot(self.x - 4, self.y, self.orient, 0, self.game))
            elif self.orient == 4:
                self.game.shoots.append(Shoot(self.x + 4, self.y, self.orient, 0, self.game))
            self.k = 50
        elif self.timer != 0:
            pass
        else:
            self.k -= 1
    
    def touch(self):
        if self.game.play.orient == 1:
            oldor2 = 2
        elif self.game.play.orient == 2:
            oldor2 = 1
        elif self.game.play.orient == 3:
            oldor2 = 4
        else:
            oldor2 = 3
        
        if self.orient == 1:
            if self.x == self.game.play.ggx and self.y - 20 == self.game.play.ggy:
                self.orient = oldor2
                self.game.shoots.append(Shoot(self.x, self.y - 4, self.orient, 0, self.game))
                self.timer = 10
                self.wall = 1
        elif self.orient == 2:
            if self.x == self.game.play.ggx and self.y + 20 == self.game.play.ggy:
                self.orient = oldor2
                self.game.shoots.append(Shoot(self.x, self.y + 4, self.orient, 0, self.game))
                self.timer = 10
                self.wall = 2
        elif self.orient == 3:
            if self.x - 20 == self.game.play.ggx and self.y == self.game.play.ggy:
                self.orient = oldor2
                self.game.shoots.append(Shoot(self.x - 4, self.y, self.orient, 0, self.game))
                self.timer = 10
                self.wall = 3
        elif self.orient == 4:
            if self.x + 20 == self.game.play.ggx and self.y == self.game.play.ggy:
                self.orient = oldor2
                self.game.shoots.append(Shoot(self.x + 4, self.y, self.orient, 0, self.game))
                self.timer = 10
                self.wall = 4

if __name__ == "__main__":
    game = BattleTanks()
    game.run()