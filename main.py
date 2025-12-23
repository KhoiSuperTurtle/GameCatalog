import pygame
import game
import menu_grid
import scrollable_container
import os

class GameLauncher:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        
        import ctypes
        user32 = ctypes.windll.user32
        screen_width = user32.GetSystemMetrics(0)
        screen_height = user32.GetSystemMetrics(1)
        
        self.catalog_width = 1024
        self.catalog_height = 768
        
        self.block_blast_size = (1000, 700)
        
        self.screen = pygame.display.set_mode((self.catalog_width, self.catalog_height))
        pygame.display.set_caption("Game Launcher")
        
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.running = True
        self.games = game.game_list
        
        self.container = None
        self.cards = None
        self.setup_container()
        
        pygame.display.flip()
    
    def setup_container(self):
        container_margin = 50
        self.container = scrollable_container.ScrollableContainer(
            container_margin, 
            container_margin, 
            self.catalog_width - 2 * container_margin, 
            self.catalog_height - 2 * container_margin
        )
        self.cards = self._create_cards_grid()
    
    def _create_cards_grid(self):
        if not self.container:
            return []
            
        cards = []
        card_width = 300
        card_height = 380
        margin = 20
        cards_per_row = max(1, (self.container.rect.width + margin) // (card_width + margin))
        
        total_height = margin
        current_row = 0
        current_col = 0
        
        for i, game_info in enumerate(self.games):
            x = self.container.rect.x + margin + current_col * (card_width + margin)
            y = self.container.rect.y + margin + current_row * (card_height + margin)
            
            card = menu_grid.Card(x, y, card_width, card_height, game_info)
            cards.append(card)
            
            current_col += 1
            if current_col >= cards_per_row:
                current_col = 0
                current_row += 1
                total_height += card_height + margin
        
        if current_col > 0: 
            total_height += card_height + margin
        
        self.container.set_content_height(total_height)
        
        return cards
    
    def launch_game(self, game_info):
        game_class = game_info.get_game_class()
        if game_class:
            self.screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 36)
            text = font.render(f"Запуск {game_info.name}...", True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.catalog_width//2, self.catalog_height//2))
            self.screen.blit(text, text_rect)
            pygame.display.flip()
            
            pygame.time.wait(500)
            
            try:
                if game_info.name == "Block Blast":
                    game_instance = game_class(*self.block_blast_size)
                elif game_info.name == "Тайп-марафон":
                    # Для Тайп-марафон игнорируем переданные размеры и используем фиксированные
                    game_instance = game_class(900, 600)
                else:
                    game_instance = game_class(self.catalog_width, self.catalog_height)
                    
                result = game_instance.run()
                
                # Восстанавливаем экран каталога
                self.screen = pygame.display.set_mode((self.catalog_width, self.catalog_height))
                pygame.display.set_caption("Game Launcher")
                
                # Обрабатываем результат
                if result == "exit_to_desktop":
                    # Полный выход из приложения
                    self.running = False
                elif result == "quit":
                    # Просто возвращаемся в каталог (игнорируем)
                    pass
                    
            except Exception as e:
                print(f"Ошибка запуска игры: {e}")
                self.screen.fill((0, 0, 0))
                error_font = pygame.font.Font(None, 24)
                error_text = error_font.render(f"Ошибка запуска игры: {e}", True, (255, 0, 0))
                error_rect = error_text.get_rect(center=(self.catalog_width//2, self.catalog_height//2))
                self.screen.blit(error_text, error_rect)
                pygame.display.flip()
                pygame.time.wait(2000)
        else:
            self.screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 36)
            text = font.render(f"Игра '{game_info.name}' еще в разработке", True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.catalog_width//2, self.catalog_height//2))
            self.screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # ESC в каталоге закрывает приложение
                    self.running = False
            
            if self.container and self.container.handle_event(event):
                continue
                    
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                scroll_offset = self.container.get_scroll_offset()
                for card in self.cards:
                    if card.handle_click(mouse_pos, scroll_offset):
                        self.launch_game(card.game_info)
                        break
    
    def update(self):
        if not self.cards:
            return
            
        mouse_pos = pygame.mouse.get_pos()
        scroll_offset = self.container.get_scroll_offset()
        for card in self.cards:
            card.check_hover(mouse_pos, scroll_offset)
    
    def draw(self):
        if not self.container or not self.cards:
            return
            
        self.screen.fill((255, 255, 255))
        
        pygame.draw.rect(self.screen, (245, 245, 245), self.container.rect, border_radius=10)
        pygame.draw.rect(self.screen, (220, 220, 220), self.container.rect, 1, border_radius=10)
        
        clip_rect = self.container.rect.copy()
        self.screen.set_clip(clip_rect)
        
        scroll_offset = self.container.get_scroll_offset()
        for card in self.cards:
            card.draw(self.screen, scroll_offset)
        
        self.screen.set_clip(None)
        
        self.container.draw(self.screen)
        
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)
        
        pygame.quit()

if __name__ == "__main__":
    app = GameLauncher()
    app.run()