import ast
import sys
import pygame
from random import choice
import json
import os

# Импорты спрайтов должны быть из текущего каталога
from .sprites import Square1x1, Square2x2, Line1x3, Line3x1, LShape, TShape


class Button:
    def __init__(self, x, y, width, height, text, color=(80, 120, 200), hover_color=(100, 140, 220)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False
        self.font = pygame.font.Font(None, 32)

    def draw(self, surface):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=8)
        pygame.draw.rect(surface, (200, 200, 220), self.rect, 2, border_radius=8)

        text_surface = self.font.render(self.text, True, (240, 240, 240))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
        return self.is_hovered

    def is_clicked(self, pos, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(pos)
        return False


class Message:
    def __init__(self, game, message_type, additional_text=""):
        self.game = game
        self.type = message_type
        self.width = 400
        self.height = 250
        self.additional_text = additional_text
        self.allow_sounds = True

        self.captions = {
            "end": "Проигрыш",
            "record": "Рекорды"
        }

        self.texts = {
            "end": "Вы проиграли :(",
            "record": f"Текущий рекорд: {self.game.record}"
        }

        self.rect = pygame.Rect(
            (self.game.screen_width - self.width) // 2,
            (self.game.screen_height - self.height) // 2,
            self.width, self.height
        )

        ok_btn_x = self.rect.x + (self.width - 120) // 2
        ok_btn_y = self.rect.y + self.height - 70
        self.ok_btn = Button(ok_btn_x, ok_btn_y, 120, 40, "OK")

        self.visible = True

    def draw(self, surface):
        if not self.visible:
            return

        overlay = pygame.Surface((self.game.screen_width, self.game.screen_height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        surface.blit(overlay, (0, 0))

        pygame.draw.rect(surface, self.game.colors['panel'], self.rect, border_radius=12)
        pygame.draw.rect(surface, (100, 140, 220), self.rect, 3, border_radius=12)

        title_font = pygame.font.Font(None, 42)
        title_text = title_font.render(self.captions.get(self.type, "Сообщение"), True, self.game.colors['text'])
        title_rect = title_text.get_rect(center=(self.rect.centerx, self.rect.y + 50))
        surface.blit(title_text, title_rect)

        content_font = pygame.font.Font(None, 32)
        main_text = self.texts.get(self.type, "")

        if self.type == "record":
            lines = [main_text]
        elif self.type == "end":
            lines = [main_text, f"Ваш счет: {self.game.score}"]
        else:
            lines = [main_text]

        for i, line in enumerate(lines):
            text_surface = content_font.render(line, True, (220, 220, 240))
            text_rect = text_surface.get_rect(center=(self.rect.centerx, self.rect.y + 100 + i * 35))
            surface.blit(text_surface, text_rect)

        self.ok_btn.draw(surface)

    def handle_event(self, event):
        if not self.visible:
            return False

        mouse_pos = pygame.mouse.get_pos()
        self.ok_btn.check_hover(mouse_pos)

        if self.ok_btn.is_clicked(mouse_pos, event):
            self.game.sounds['menu_btn'].play()
            self.visible = False
            return True

        return False

    def is_active(self):
        return self.visible


class BlockBlastGame:
    def __init__(self, screen_width, screen_height):
        self.current_message = None
        self.record = 0
        self.score = 0
        self.grid = []
        
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Используем абсолютные пути для ресурсов
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        self.filename = os.path.join(current_dir, "saving.txt")

        self.colors = {
            'black': (20, 20, 30),
            'white': (240, 240, 255),
            'background': (30, 30, 40),
            'grid_bg': (40, 40, 55),
            'grid_line': (60, 60, 80),
            'button': (80, 120, 200),
            'button_hover': (100, 140, 220),
            'panel': (35, 35, 50),
            'text': (220, 220, 240),
            'score_text': (100, 200, 255),
            'record_text': (255, 200, 100),
        }

        self.random_colors = {
            'red': (220, 100, 100),
            'blue': (100, 150, 220),
            'green': (100, 200, 120),
            'pink': (220, 140, 180),
            'yellow': (220, 200, 100),
            'purple': (160, 100, 220),
            'orange': (220, 150, 80),
            'cyan': (100, 200, 220),
            'lime': (180, 220, 100)
        }

        self.grid_size = 8
        self.cell_size = 40
        self.num_sprites = 3

        pygame.init()
        pygame.mixer.init()
        
        # Используем абсолютные пути для звуков
        sounds_dir = os.path.join(current_dir, "sounds")
        icon_path = os.path.join(current_dir, "image.png")
        
        self.sounds = {
            'menu_btn': pygame.mixer.Sound(os.path.join(sounds_dir, 'menu_btn.wav')),
            'placed': pygame.mixer.Sound(os.path.join(sounds_dir, 'placed.wav')),
            'no': pygame.mixer.Sound(os.path.join(sounds_dir, 'no.wav')),
            'line_delete': pygame.mixer.Sound(os.path.join(sounds_dir, 'line_delete.mp3'))
        }
        
        self.all_sprites = pygame.sprite.Group()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Block Blast")
        
        try:
            if os.path.exists(icon_path):
                pygame.display.set_icon(pygame.image.load(icon_path))
        except:
            pass  # Если иконка не найдена, продолжаем без нее

        self.in_menu = True
        self.create_menu_buttons()
        self.create_game_buttons()

        self.load_saving()
        self.dragging = None
        self.drag_x, self.drag_y, self.start_x, self.start_y = 0, 0, 0, 0
        self.running = True

        # Центрируем сетку
        self.grid_start_x = (self.screen_width - (self.grid_size * (self.cell_size + 1))) // 2
        self.grid_start_y = (self.screen_height - (self.grid_size * (self.cell_size + 1))) // 2 + 30

        # Позиции для спрайтов в игровом режиме (справа от сетки)
        self.sprite_start_x = self.grid_start_x + self.grid_size * (self.cell_size + 1) + 50
        self.sprite_y_positions = []
        for i in range(self.num_sprites):
            self.sprite_y_positions.append(self.grid_start_y + i * (self.cell_size * 3 + 30))

    def create_menu_buttons(self):
        center_x = self.screen_width // 2
        self.menu_buttons = [
            Button(center_x - 100, 250, 200, 50, "Новая игра"),
            Button(center_x - 100, 320, 200, 50, "Продолжить"),
            Button(center_x - 100, 390, 200, 50, "Рекорды"),
            Button(center_x - 100, 460, 200, 50, "Выход", (180, 80, 80), (200, 100, 100))
        ]

    def create_game_buttons(self):
        self.game_buttons = [
            Button(20, 20, 120, 40, "Меню"),
            Button(20, 70, 120, 40, "Сохранить"),
            Button(20, 120, 120, 40, "Рекорды")
        ]

    def save(self):
        with open(self.filename, 'w+', encoding='utf-8') as file:
            file.write(f"{self.record}\n")
            file.write(f"{self.score}\n")
            for row in self.grid:
                line = '|'.join(map(str, row))
                file.write(line + '\n')
            for sprite in self.all_sprites:
                sprite_data = {
                    'type': sprite.__class__.__name__,
                    'color': sprite.color,
                    'x': sprite.rect.x,
                    'y': sprite.rect.y,
                    'cell_size': sprite.cell_size
                }
                file.write(f"{sprite_data}\n")

    def load_saving(self):
        try:
            with open(self.filename, 'r+', encoding='utf-8') as file:
                self.record = int(file.readline().strip())
                self.score = int(file.readline().strip())
                self.grid = []
                for i, line in enumerate(file):
                    if i < self.grid_size:
                        # Преобразуем строку обратно в кортеж цвета
                        row = []
                        for cell in line.strip().split('|'):
                            if cell.startswith('('):
                                row.append(ast.literal_eval(cell))
                            else:
                                row.append(self.colors['black'])
                        self.grid.append(row)
                    else:
                        sprite_data = ast.literal_eval(line)
                        self.create_sprite(sprite_data)
        except (FileNotFoundError, ValueError, IndexError):
            self.grid = [[self.colors['black'] for _ in range(self.grid_size)] for _ in range(self.grid_size)]
            if self.in_menu:
                self.all_sprites.empty()
            else:
                self.give_sprites()

    def create_sprite(self, sprite_data):
        sprite_type = sprite_data['type']
        color = sprite_data['color']
        x = sprite_data['x']
        y = sprite_data['y']
        cell_size = sprite_data.get('cell_size', self.cell_size)

        sprite_classes = {
            'Square1x1': Square1x1,
            'Square2x2': Square2x2,
            'Line1x3': Line1x3,
            'Line3x1': Line3x1,
            'LShape': LShape,
            'TShape': TShape
        }

        if sprite_type in sprite_classes:
            sprite = sprite_classes[sprite_type](color, x, y, cell_size, self)
            self.all_sprites.add(sprite)

    def check_loser(self):
        for sprite in self.all_sprites:
            if sprite.can_place():
                return
        self.current_message = Message(self, "end")
        self.check_record()

    def clean_all(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                self.grid[row][col] = self.colors['black']
        self.all_sprites.empty()
        self.score = 0
        self.give_sprites()

    def draw_grid(self):
        # Фон для сетки
        grid_size_px = self.grid_size * (self.cell_size + 1)
        pygame.draw.rect(self.screen, self.colors['grid_bg'],
                        (self.grid_start_x - 10, self.grid_start_y - 10,
                         grid_size_px + 20, grid_size_px + 20), border_radius=5)

        # Рисуем сетку
        for row in range(self.grid_size):
            y = self.grid_start_y + row * (self.cell_size + 1)
            for col in range(self.grid_size):
                x = self.grid_start_x + col * (self.cell_size + 1)
                # Ячейка
                pygame.draw.rect(self.screen, self.grid[row][col],
                                (x, y, self.cell_size, self.cell_size), border_radius=3)
                # Рамка ячейки
                pygame.draw.rect(self.screen, self.colors['grid_line'],
                                (x, y, self.cell_size, self.cell_size), 1, border_radius=3)

    def give_sprites(self):
        if len(self.all_sprites) != 0:
            return

        x = self.sprite_start_x
        sprite_classes = [Square1x1, Square2x2, Line1x3, Line3x1, LShape, TShape]

        for i in range(self.num_sprites):  # Теперь создаем только 3 фигуры
            y = self.sprite_y_positions[i]
            sprite_class = choice(sprite_classes)
            self.all_sprites.add(sprite_class(self.randomize_color(), x, y, self.cell_size, self))

    def check_grid(self):
        rows = []
        cols = []
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.grid[i][j] == self.colors['black']:
                    break
                elif j == self.grid_size - 1:
                    rows.append(i)

        for j in range(self.grid_size):
            for i in range(self.grid_size):
                if self.grid[i][j] == self.colors['black']:
                    break
                elif i == self.grid_size - 1:
                    cols.append(j)

        if not rows and not cols:
            return

        for i in rows:
            for j in range(self.grid_size):
                self.grid[i][j] = self.colors['black']
            self.score += 100
        for j in cols:
            for i in range(self.grid_size):
                self.grid[i][j] = self.colors['black']
            self.score += 100
        self.sounds['line_delete'].play()
        self.check_record()

    def randomize_color(self):
        return choice(list(self.random_colors.values()))

    def check_record(self):
        if self.score > self.record:
            self.record = self.score

    def get_cell(self, pos):
        x, y = pos
        x -= self.grid_start_x
        y -= self.grid_start_y

        if x < 0 or y < 0:
            return None
        col = x // (self.cell_size + 1)
        row = y // (self.cell_size + 1)
        if 0 <= row < self.grid_size and 0 <= col < self.grid_size:
            return row, col

        return None

    def draw_menu(self):
        self.screen.fill(self.colors['background'])

        # Заголовок
        title_font = pygame.font.Font(None, 72)
        title_text = title_font.render("BLOCK BLAST", True, self.colors['text'])
        title_rect = title_text.get_rect(center=(self.screen_width // 2, 150))
        self.screen.blit(title_text, title_rect)

        # Подзаголовок
        subtitle_font = pygame.font.Font(None, 36)
        subtitle_text = subtitle_font.render("Собери линии, чтобы заработать очки", True, (180, 180, 200))
        subtitle_rect = subtitle_text.get_rect(center=(self.screen_width // 2, 200))
        self.screen.blit(subtitle_text, subtitle_rect)

        # Кнопки
        for button in self.menu_buttons:
            button.draw(self.screen)

    def draw_game(self):
        self.screen.fill(self.colors['background'])

        # Левая панель
        pygame.draw.rect(self.screen, self.colors['panel'], (0, 0, 150, self.screen_height))

        # Кнопки игры
        for button in self.game_buttons:
            button.draw(self.screen)

        # Надпись "Перетащите блоки" сверху над сеткой
        hint_font = pygame.font.Font(None, 36)
        hint_text = hint_font.render("Перетащите блоки на сетку", True, self.colors['text'])
        hint_rect = hint_text.get_rect(center=(self.screen_width // 2, self.grid_start_y - 80))
        self.screen.blit(hint_text, hint_rect)

        # Счет и рекорд (над сеткой по центру)
        score_y_pos = self.grid_start_y - 40
        center_x = self.screen_width // 2

        font_large = pygame.font.Font(None, 42)
        font_small = pygame.font.Font(None, 36)

        score_text = font_large.render(f"Счет: {self.score}", True, self.colors['score_text'])
        record_text = font_small.render(f"Рекорд: {self.record}", True, self.colors['record_text'])

        score_rect = score_text.get_rect(center=(center_x - 100, score_y_pos))
        record_rect = record_text.get_rect(center=(center_x + 100, score_y_pos))

        self.screen.blit(score_text, score_rect)
        self.screen.blit(record_text, record_rect)

        # Подсказка на левой панели
        panel_hint_font = pygame.font.Font(None, 24)
        panel_hint_text = panel_hint_font.render("Используйте", True, (160, 160, 180))
        self.screen.blit(panel_hint_text, (20, 280))
        panel_hint_text2 = panel_hint_font.render("блоки справа", True, (160, 160, 180))
        self.screen.blit(panel_hint_text2, (20, 300))

        # Информация о фигурах справа
        info_font = pygame.font.Font(None, 28)
        info_text = info_font.render("Доступные фигуры:", True, self.colors['text'])
        self.screen.blit(info_text, (self.sprite_start_x - 10, self.grid_start_y - 40))

        # Игровые элементы
        self.draw_grid()
        self.all_sprites.draw(self.screen)

    def upd_screen(self):
        if self.in_menu:
            self.draw_menu()
        else:
            self.draw_game()

        if self.current_message and self.current_message.is_active():
            self.current_message.draw(self.screen)
        pygame.display.flip()

    def show_records(self):
        self.current_message = Message(self, "record")

    def run(self):
        try:
            while self.running:
                mouse_pos = pygame.mouse.get_pos()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            if not self.in_menu:
                                if self.current_message and self.current_message.is_active():
                                    self.current_message.visible = False
                                else:
                                    self.in_menu = True
                            else:
                                self.running = False

                    if self.current_message and self.current_message.is_active():
                        if self.current_message.handle_event(event):
                            if self.current_message.type == "end":
                                self.clean_all()
                                self.upd_screen()
                        continue

                    # Обработка меню
                    if self.in_menu:
                        for i, button in enumerate(self.menu_buttons):
                            button.check_hover(mouse_pos)
                            if button.is_clicked(mouse_pos, event):
                                self.sounds['menu_btn'].play()
                                if i == 0:  # Новая игра
                                    self.clean_all()
                                    self.in_menu = False
                                elif i == 1:  # Продолжить
                                    self.in_menu = False
                                    self.give_sprites()
                                elif i == 2:  # Рекорды
                                    self.show_records()
                                elif i == 3:  # Выход
                                    return "quit"

                    # Обработка игры
                    else:
                        for i, button in enumerate(self.game_buttons):
                            button.check_hover(mouse_pos)
                            if button.is_clicked(mouse_pos, event):
                                self.sounds['menu_btn'].play()
                                if i == 0:  # Меню
                                    self.save()
                                    self.in_menu = True
                                elif i == 1:  # Сохранить
                                    self.save()
                                elif i == 2:  # Рекорды
                                    self.show_records()

                        # Оригинальная логика игры
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                for sprite in self.all_sprites:
                                    if sprite.rect.collidepoint(event.pos):
                                        self.dragging = sprite
                                        self.drag_x = sprite.rect.x - event.pos[0]
                                        self.drag_y = sprite.rect.y - event.pos[1]
                                        self.start_x = sprite.rect.x
                                        self.start_y = sprite.rect.y
                                        break

                        elif event.type == pygame.MOUSEBUTTONUP:
                            if event.button == 1 and self.dragging is not None:
                                cell = self.dragging.check()

                                if cell is not None:
                                    row, col = cell
                                    # Для фигур, которые занимают несколько клеток
                                    if hasattr(self.dragging, 'place_on_grid'):
                                        self.dragging.place_on_grid()
                                    else:
                                        self.grid[row][col] = self.dragging.color

                                    self.sounds['placed'].play()
                                    self.score += self.dragging.score
                                    self.dragging.kill()
                                    self.check_grid()
                                    self.give_sprites()

                                else:
                                    self.sounds['no'].play()
                                    self.dragging.rect.x = self.start_x
                                    self.dragging.rect.y = self.start_y

                                self.dragging = None

                        elif event.type == pygame.MOUSEMOTION:
                            if self.dragging is not None:
                                new_x = event.pos[0] + self.drag_x
                                new_y = event.pos[1] + self.drag_y

                                sprite_width, sprite_height = self.dragging.rect.size

                                new_x = max(0, min(new_x, self.screen_width - sprite_width))
                                new_y = max(0, min(new_y, self.screen_height - sprite_height))

                                self.dragging.rect.x = new_x
                                self.dragging.rect.y = new_y

                if not self.in_menu:
                    self.check_record()
                    self.check_loser()

                self.upd_screen()

        except KeyboardInterrupt:
            self.save()

        finally:
            self.save()
            return "menu"

    def quit(self):
        self.save()
        pygame.quit()