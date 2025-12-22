import pygame
import game
import menu_grid
import scrollable_container

class GameLauncher:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        
        self.screen_info = pygame.display.Info()
        self.width, self.height = self.screen_info.current_w, self.screen_info.current_h
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption("Game Launcher")
        
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.running = True
        self.games = game.game_list
        
        self.current_game = None
        self.show_menu = True
        
        container_margin = 50
        self.container = scrollable_container.ScrollableContainer(
            container_margin, 
            container_margin, 
            self.width - 2 * container_margin, 
            self.height - 2 * container_margin
        )
        
        self.cards = self._create_cards_grid()
        
    def _create_cards_grid(self):
        """Create grid of cards"""
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
        """Запуск выбранной игры"""
        game_class = game_info.get_game_class()
        if game_class:
            self.show_menu = False
            
            original_screen = self.screen
            original_size = (self.width, self.height)
            
            self.current_game = game_class(self.width, self.height)
            
            result = self.current_game.run()
            
            self.screen = original_screen
            self.width, self.height = original_size
            self.show_menu = True
            self.current_game = None
            
            if result == "quit":
                self.running = False
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if not self.show_menu and self.current_game:
                        pass
                    else:
                        self.running = False
                    
            elif event.type == pygame.VIDEORESIZE:
                self.width, self.height = event.size
                self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
                container_margin = 50
                self.container = scrollable_container.ScrollableContainer(
                    container_margin, 
                    container_margin, 
                    self.width - 2 * container_margin, 
                    self.height - 2 * container_margin
                )
                self.cards = self._create_cards_grid()
            
            if self.show_menu:
                if self.container.handle_event(event):
                    continue
                    
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    scroll_offset = self.container.get_scroll_offset()
                    for card in self.cards:
                        if card.handle_click(mouse_pos, scroll_offset):
                            self.launch_game(card.game_info)
                            break
    
    def update(self):
        if self.show_menu:
            mouse_pos = pygame.mouse.get_pos()
            scroll_offset = self.container.get_scroll_offset()
            for card in self.cards:
                card.check_hover(mouse_pos, scroll_offset)
    
    def draw(self):
        if self.show_menu:
            # Белый фон
            self.screen.fill((255, 255, 255))
            
            # Светло-серый контейнер с тонкой серой рамкой
            pygame.draw.rect(self.screen, (245, 245, 245), self.container.rect, border_radius=10)
            pygame.draw.rect(self.screen, (220, 220, 220), self.container.rect, 1, border_radius=10)
            
            clip_rect = self.container.rect.copy()
            self.screen.set_clip(clip_rect)
            
            scroll_offset = self.container.get_scroll_offset()
            for card in self.cards:
                card.draw(self.screen, scroll_offset)
            
            self.screen.set_clip(None)
            
            self.container.draw(self.screen)
        else:
            pass
        
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