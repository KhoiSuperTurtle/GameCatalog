import pygame
import random
import time

class TextTypingGame:
    def __init__(self, screen_width, screen_height):
        # ВСЕГДА 900x600, игнорируем переданные параметры
        self.WIDTH = 900
        self.HEIGHT = 600
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Тайп-марафон — Уровни сложности!")
        
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (200, 200, 200)
        self.GREEN = (0, 200, 0)
        self.RED = (200, 0, 0)
        self.YELLOW = (255, 200, 0)
        self.GRAY_dark = (34, 39, 46)
        
        self.FONT_LARGE = pygame.font.SysFont('arial', 48, bold=True)
        self.FONT_MEDIUM = pygame.font.SysFont('arial', 36)
        self.FONT_SMALL = pygame.font.SysFont('arial', 28)
        
        self.LEVELS = {
            1: {
                "name": "Новичок",
                "color": self.GREEN,
                "words": ["кот", "дом", "друг", "мама", "папа", "сон", "день", "ночь", "вода", "еда"],
                "time": 60
            },
            2: {
                "name": "Средний",
                "color": self.YELLOW,
                "words": ["клавиатура", "программа", "компьютер", "монитор", "процессор", "интернет", "браузер", "сервер",
                         "файл", "папка"],
                "time": 60
            },
            3: {
                "name": "Профи",
                "color": self.RED,
                "words": ["разработчик", "алгоритм", "архитектура", "микросервис", "контейнер", "деплоймент", "инфраструктура",
                         "автоматизация", "тестирование", "документация"],
                "time": 45
            }
        }
        
        self.FPS = 60
        self.CLOCK = pygame.time.Clock()
        
        self.current_level = 1
        self.level_data = self.LEVELS[self.current_level]
        self.current_word = ""
        self.input_text = ""
        self.start_time = None
        self.correct_chars = 0
        self.total_chars = 0
        self.game_state = "menu"
        
        self.reset_game()
    
    def draw_text(self, text, font, color, x, y, center=True):
        surface = font.render(text, True, color)
        rect = surface.get_rect()
        if center:
            rect.center = (x, y)
        else:
            rect.topleft = (x, y)
        self.WIN.blit(surface, rect)
    
    def reset_game(self):
        self.current_word = random.choice(self.level_data["words"])
        self.input_text = ""
        self.start_time = time.time()
        self.correct_chars = 0
        self.total_chars = 0
    
    def get_accuracy(self):
        return (self.correct_chars / self.total_chars * 100) if self.total_chars > 0 else 0
    
    def get_wpm(self):
        elapsed = max(time.time() - self.start_time, 1)
        words_typed = self.correct_chars / 5
        return round(words_typed * 60 / elapsed)
    
    def draw_menu(self):
        self.WIN.fill(self.GRAY_dark)
        self.draw_text("ТАЙП-МАРАФОН", self.FONT_LARGE, self.GRAY, self.WIDTH // 2, 100)
        self.draw_text("Выбери уровень:", self.FONT_MEDIUM, self.GRAY, self.WIDTH // 2, 200)
        
        y = 280
        for level, data in self.LEVELS.items():
            color = data["color"] if self.current_level == level else self.GRAY
            self.draw_text(f"{level}. {data['name']}", self.FONT_MEDIUM, color, self.WIDTH // 2, y)
            y += 60
        
        self.draw_text("Стрелки ↑↓ — выбор, ENTER — старт", self.FONT_SMALL, self.GRAY, self.WIDTH // 2, self.HEIGHT - 100)
        self.draw_text("ESC — выход в каталог", self.FONT_SMALL, self.GRAY, self.WIDTH // 2, self.HEIGHT - 50)
    
    def draw_game(self):
        self.WIN.fill(self.GRAY_dark)
        
        self.draw_text(f"Уровень: {self.level_data['name']}", self.FONT_MEDIUM, self.level_data["color"], self.WIDTH // 2, 40)
        
        elapsed = int(time.time() - self.start_time) if self.start_time else 0
        remaining = max(self.level_data["time"] - elapsed, 0)
        timer_color = self.GRAY if remaining > 10 else self.RED
        self.draw_text(f"Время: {remaining}с", self.FONT_MEDIUM, timer_color, self.WIDTH // 2, 100)
        
        progress = elapsed / self.level_data["time"]
        pygame.draw.rect(self.WIN, self.GRAY, (150, 140, 600, 20))
        pygame.draw.rect(self.WIN, self.GREEN, (150, 140, 600 * progress, 20))
        
        word_y = 235
        self.draw_text("Напечатай:", self.FONT_MEDIUM, self.GRAY, 150, word_y, center=False)
        
        word_x = 350
        for i, char in enumerate(self.current_word):
            color = self.GREEN if i < len(self.input_text) and self.input_text[i] == char else \
                self.RED if i < len(self.input_text) else self.GRAY
            self.draw_text(char, self.FONT_LARGE, color, word_x + i * 38, word_y + 10, center=False)
        
        input_rect = pygame.Rect(150, 340, 600, 60)
        pygame.draw.rect(self.WIN, self.WHITE, input_rect, border_radius=15)
        pygame.draw.rect(self.WIN, self.GRAY, input_rect, 3, border_radius=15)
        
        text_surface = self.FONT_LARGE.render(self.input_text + "▎", True, self.GRAY_dark)
        text_rect = text_surface.get_rect()
        text_rect.centery = input_rect.centery
        text_rect.left = input_rect.left + 20
        
        if text_rect.width > input_rect.width - 40:
            text_rect.right = input_rect.right - 20
        
        self.WIN.blit(text_surface, text_rect)
        
        if self.start_time:
            wpm = self.get_wpm()
            acc = self.get_accuracy()
            self.draw_text(f"WPM: {wpm}", self.FONT_MEDIUM, self.GRAY, 200, 430, center=False)
            self.draw_text(f"Точность: {acc:.1f}%", self.FONT_MEDIUM, self.GRAY, 200, 480, center=False)
    
    def draw_game_over(self):
        overlay = pygame.Surface((self.WIDTH, self.HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(self.BLACK)
        self.WIN.blit(overlay, (0, 0))
        final_wpm = self.get_wpm()
        final_acc = self.get_accuracy()
        self.draw_text("ВРЕМЯ ВЫШЛО!", self.FONT_LARGE, self.WHITE, self.WIDTH // 2, 180)
        self.draw_text(f"Уровень: {self.level_data['name']}", self.FONT_MEDIUM, self.level_data["color"], self.WIDTH // 2, 240)
        self.draw_text(f"Скорость: {final_wpm} WPM", self.FONT_MEDIUM, self.GREEN, self.WIDTH // 2, 300)
        self.draw_text(f"Точность: {final_acc:.1f}%", self.FONT_MEDIUM, self.GREEN, self.WIDTH // 2, 350)
        self.draw_text("R — повторить, ESC — меню", self.FONT_SMALL, self.GRAY, self.WIDTH // 2, 440)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit_to_desktop"  # Полный выход из приложения
            
            if self.game_state == "menu":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.current_level = max(1, self.current_level - 1)
                        self.level_data = self.LEVELS[self.current_level]
                    elif event.key == pygame.K_DOWN:
                        self.current_level = min(3, self.current_level + 1)
                        self.level_data = self.LEVELS[self.current_level]
                    elif event.key == pygame.K_RETURN:
                        self.level_data = self.LEVELS[self.current_level]
                        self.reset_game()
                        self.game_state = "playing"
                    elif event.key == pygame.K_ESCAPE:
                        # Выход в каталог из меню игры
                        return "quit"  # Возврат в каталог
            
            elif self.game_state == "playing":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        # Нажатие ESC во время игры возвращает в меню игры
                        self.game_state = "menu"
                        return None
                    if event.key == pygame.K_RETURN:
                        if self.input_text == self.current_word:
                            self.correct_chars += len(self.current_word)
                        self.total_chars += len(self.input_text)
                        self.input_text = ""
                        self.current_word = random.choice(self.level_data["words"])
                    elif event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]
                    else:
                        char = event.unicode.lower()
                        if char.isalpha() or char in " -":
                            self.input_text += char
                            self.total_chars += 1
                            if len(self.input_text) <= len(self.current_word) and self.input_text[-1] == self.current_word[len(self.input_text) - 1]:
                                self.correct_chars += 1
            
            elif self.game_state == "game_over":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset_game()
                        self.game_state = "playing"
                    elif event.key == pygame.K_ESCAPE:
                        # Нажатие ESC в game_over возвращает в меню игры
                        self.game_state = "menu"
        
        return None
    
    def update(self):
        if self.game_state == "playing" and self.start_time and time.time() - self.start_time >= self.level_data["time"]:
            self.game_state = "game_over"
    
    def draw(self):
        if self.game_state == "menu":
            self.draw_menu()
        elif self.game_state == "playing":
            self.draw_game()
        elif self.game_state == "game_over":
            self.draw_game()
            self.draw_game_over()
    
    def run(self):
        while True:
            result = self.handle_events()
            if result == "exit_to_desktop":
                # Полный выход из приложения
                return "exit_to_desktop"
            elif result == "quit":
                # Возвращаемся в каталог
                return "quit"
            
            self.update()
            self.draw()
            
            pygame.display.update()
            self.CLOCK.tick(self.FPS)