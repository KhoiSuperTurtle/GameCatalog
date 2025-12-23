import pygame
import sys
import random
import os

class SnakeGame:
    def __init__(self, screen_width, screen_height):
        # Игнорируем переданные размеры, используем собственные
        self.CELL = 32
        self.GRID_W = 20
        self.GRID_H = 20
        self.WIN_W = self.CELL * self.GRID_W
        self.WIN_H = self.CELL * self.GRID_H
        
        self.window = pygame.display.set_mode((self.WIN_W, self.WIN_H))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        
        # Загружаем ресурсы из текущей папки
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # ====== Звуки ======
        sound_path = os.path.join(current_dir, "chomp.mp3")
        self.SND_EAT = pygame.mixer.Sound(sound_path)
        
        sound_path = os.path.join(current_dir, "bonk.mp3")
        self.SND_HIT = pygame.mixer.Sound(sound_path)
        
        self.SND_EAT.set_volume(0.6)
        self.SND_HIT.set_volume(0.7)
        
        # Загружаем спрайты
        self.load_resources(current_dir)
        
        # Инициализация игры
        self.snake = Snake(self)
        self.apple = Apple(self)
        self.score = 0
        self.game_over = False
        self.best_score = self.load_best_score(current_dir)
        
    def load_resources(self, current_dir):
        def load(name):
            path = os.path.join(current_dir, name)
            return pygame.transform.scale(
                pygame.image.load(path).convert_alpha(),
                (self.CELL, self.CELL)
            )
        
        def load_rotated(name, angle):
            path = os.path.join(current_dir, name)
            img = pygame.image.load(path).convert_alpha()
            img = pygame.transform.scale(img, (self.CELL, self.CELL))
            return pygame.transform.rotate(img, angle)
        
        # ========= СПРАЙТЫ =========
        self.SPR_HEAD = load_rotated("Hsprite_0.png", 90)
        self.SPR_BODY1 = load_rotated("BODsprite_2.png", -90)
        self.SPR_BODY2 = load_rotated("BODsprite_3.png", -90)
        self.SPR_TAIL = load_rotated("TailUP.png", 90)
        self.SPR_APPLE = load("spritepaint (2).png")
        
        self.SPR_BG = pygame.transform.scale(
            pygame.image.load(os.path.join(current_dir, "backimg.jpg")).convert(),
            (self.WIN_W, self.WIN_H)
        )
        
        # ======== 8 УГЛОВЫХ СПРАЙТОВ ========
        self.CORNER = {
            ("UP", "LEFT"): load("sprite_1.png"),
            ("LEFT", "UP"): load("sprite_3.png"),
            ("UP", "RIGHT"): load("sprite_2.png"),
            ("RIGHT", "UP"): load("sprite_0.png"),
            ("DOWN", "LEFT"): load("sprite_0.png"),
            ("LEFT", "DOWN"): load("sprite_2.png"),
            ("DOWN", "RIGHT"): load("sprite_3.png"),
            ("RIGHT", "DOWN"): load("sprite_1.png"),
        }
    
    def load_best_score(self, current_dir):
        score_path = os.path.join(current_dir, "best_score.txt")
        if not os.path.exists(score_path):
            return 0
        with open(score_path, "r") as f:
            return int(f.read().strip())
    
    def save_best_score(self, current_dir):
        score_path = os.path.join(current_dir, "best_score.txt")
        with open(score_path, "w") as f:
            f.write(str(self.best_score))
    
    def dir_from_vec(self, dx, dy):
        if dx == 1 and dy == 0: return "RIGHT"
        if dx == -1 and dy == 0: return "LEFT"
        if dx == 0 and dy == -1: return "UP"
        if dx == 0 and dy == 1: return "DOWN"
    
    def run(self):
        # Показываем меню перед игрой
        self.main_menu()
        
        # Основной игровой цикл
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return "quit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        # Возвращаемся в каталог
                        running = False
                        return "quit"
                    
                    if not self.game_over:
                        self.snake.handle_input(event.key)
                    else:
                        if event.key == pygame.K_SPACE:
                            self.best_score = max(self.best_score, self.score)
                            current_dir = os.path.dirname(os.path.abspath(__file__))
                            self.save_best_score(current_dir)
                            self.snake = Snake(self)
                            self.apple = Apple(self)
                            self.score = 0
                            self.game_over = False
                            self.main_menu()
            
            if not self.game_over and running:
                head = self.snake.move()
                
                if not (0 <= head[0] < self.GRID_W and 0 <= head[1] < self.GRID_H):
                    self.SND_HIT.play()
                    self.game_over = True
                
                elif self.snake.collide_self():
                    self.SND_HIT.play()
                    self.game_over = True
                
                elif head == self.apple.position:
                    self.snake.grow = True
                    self.score += 1
                    self.SND_EAT.play()
                    self.apple.respawn()
            
            # Отрисовка
            self.snake.draw()
            self.apple.draw()
            
            # Счет
            font_score = pygame.font.SysFont("Arial Black", 28)
            text = font_score.render(f"Счет: {self.score}", True, (255, 255, 255))
            self.window.blit(text, (10, 10))
            
            # Экран Game Over
            if self.game_over:
                current_dir = os.path.dirname(os.path.abspath(__file__))
                self.best_score = max(self.best_score, self.score)
                self.save_best_score(current_dir)
                
                overlay = pygame.Surface((self.WIN_W, self.WIN_H))
                overlay.set_alpha(180)
                overlay.fill((0, 0, 0))
                self.window.blit(overlay, (0, 0))
                
                go_font = pygame.font.SysFont("Arial", 64, bold=True)
                go_text = go_font.render("GAME OVER", True, (255, 50, 50))
                self.window.blit(go_text, (self.WIN_W // 2 - go_text.get_width() // 2, self.WIN_H // 2 - 80))
                
                sub_font = pygame.font.SysFont("Arial", 32)
                sub_text = sub_font.render("SPACE — чтобы начать заново", True, (255, 255, 255))
                self.window.blit(sub_text, (self.WIN_W // 2 - sub_text.get_width() // 2, self.WIN_H // 2))
                
                best_text = go_font.render(f"Лучший: {self.best_score}", True, (255, 255, 0))
                self.window.blit(best_text, (self.WIN_W // 2 - best_text.get_width() // 2, self.WIN_H // 2 - 150))
            
            pygame.display.update()
            self.clock.tick(9)
        
        return "quit"
    
    def main_menu(self):
        title_font = pygame.font.SysFont("Arial Black", 72)
        btn_font = pygame.font.SysFont("Arial", 48)
        score_font = pygame.font.SysFont("Arial", 36)
        
        button_rect = pygame.Rect(self.WIN_W // 2 - 150, self.WIN_H // 2, 300, 80)
        
        menu_running = True
        while menu_running:
            self.window.blit(self.SPR_BG, (0, 0))
            
            title_text = title_font.render("SNAKE GAME", True, (255, 255, 0))
            self.window.blit(title_text, (self.WIN_W // 2 - title_text.get_width() // 2, 120))
            
            score_text = score_font.render(f"Лучший счёт: {self.best_score}", True, (255, 255, 255))
            self.window.blit(score_text, (self.WIN_W // 2 - score_text.get_width() // 2, 260))
            
            pygame.draw.rect(self.window, (0, 150, 0), button_rect)
            btn_text = btn_font.render("Играть", True, (255, 255, 255))
            self.window.blit(btn_text, (button_rect.centerx - btn_text.get_width() // 2,
                                       button_rect.centery - btn_text.get_height() // 2))
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        menu_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu_running = False
                        return

class Snake:
    def __init__(self, game):
        self.game = game
        self.reset()
    
    def reset(self):
        self.body = [(10, 10), (9, 10), (8, 10)]
        self.direction = (1, 0)
        self.grow = False
    
    def handle_input(self, key):
        dx, dy = self.direction
        if key == pygame.K_UP and dy != 1:
            self.direction = (0, -1)
        elif key == pygame.K_DOWN and dy != -1:
            self.direction = (0, 1)
        elif key == pygame.K_LEFT and dx != 1:
            self.direction = (-1, 0)
        elif key == pygame.K_RIGHT and dx != -1:
            self.direction = (1, 0)
    
    def move(self):
        hx, hy = self.body[0]
        dx, dy = self.direction
        new_head = (hx + dx, hy + dy)
        self.body.insert(0, new_head)
        
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
        
        return new_head
    
    def collide_self(self):
        return self.body[0] in self.body[1:]
    
    def rotate(self, sprite, dx, dy):
        if dx == 1:
            return sprite
        elif dx == -1:
            return pygame.transform.rotate(sprite, 180)
        elif dy == -1:
            return pygame.transform.rotate(sprite, 90)
        else:
            return pygame.transform.rotate(sprite, -90)
    
    def draw(self):
        self.game.window.blit(self.game.SPR_BG, (0, 0))
        
        for i, (x, y) in enumerate(self.body):
            pos = (x * self.game.CELL, y * self.game.CELL)
            
            if i == 0:
                dx, dy = self.direction
                self.game.window.blit(self.rotate(self.game.SPR_HEAD, dx, dy), pos)
                continue
            
            if i == len(self.body) - 1:
                px, py = self.body[i - 1]
                self.game.window.blit(self.rotate(self.game.SPR_TAIL, x - px, y - py), pos)
                continue
            
            prev = self.body[i - 1]
            nxt = self.body[i + 1]
            dxp, dyp = x - prev[0], y - prev[1]
            dxn, dyn = nxt[0] - x, nxt[1] - y
            
            if dxp == dxn or dyp == dyn:
                spr = self.game.SPR_BODY1 if i % 2 == 0 else self.game.SPR_BODY2
                if dxp == -1: spr = pygame.transform.rotate(spr, 180)
                elif dyp == -1: spr = pygame.transform.rotate(spr, 90)
                elif dyp == 1: spr = pygame.transform.rotate(spr, -90)
            else:
                spr = self.game.CORNER[(self.game.dir_from_vec(dxp, dyp), self.game.dir_from_vec(dxn, dyn))]
            
            self.game.window.blit(spr, pos)

class Apple:
    def __init__(self, game):
        self.game = game
        self.position = self.random_pos()
    
    def random_pos(self):
        return (
            random.randint(0, self.game.GRID_W - 1),
            random.randint(0, self.game.GRID_H - 1)
        )
    
    def respawn(self):
        self.position = self.random_pos()
    
    def draw(self):
        x, y = self.position
        self.game.window.blit(self.game.SPR_APPLE, (x * self.game.CELL, y * self.game.CELL))

if __name__ == "__main__":
    # Запуск игры напрямую (без лаунчера)
    pygame.init()
    pygame.mixer.init()
    game = SnakeGame(640, 480)  # Размеры игнорируются
    game.run()