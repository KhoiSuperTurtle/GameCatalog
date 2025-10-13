import pygame
import game
import menu_grid
import scrollable_container

class GameLauncher:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        
        # Screen setup
        self.screen_info = pygame.display.Info()
        self.width, self.height = self.screen_info.current_w - 100, self.screen_info.current_h - 100
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption("Game Launcher")
        
        # Game setup
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.running = True
        self.games = game.game_list
        
        # Create scrollable container
        container_margin = 50
        self.container = scrollable_container.ScrollableContainer(
            container_margin, 
            container_margin, 
            self.width - 2 * container_margin, 
            self.height - 2 * container_margin
        )
        
        # Create cards grid
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
        
        # Add bottom margin
        total_height += margin
        
        # Update container content height
        self.container.set_content_height(total_height)
        
        return cards
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    
            elif event.type == pygame.VIDEORESIZE:
                self.width, self.height = event.size
                self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
                # Recreate container and cards for new size
                container_margin = 50
                self.container = scrollable_container.ScrollableContainer(
                    container_margin, 
                    container_margin, 
                    self.width - 2 * container_margin, 
                    self.height - 2 * container_margin
                )
                self.cards = self._create_cards_grid()
            
            # Handle scroll events
            if self.container.handle_event(event):
                continue
                
            # Handle mouse clicks on cards
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                scroll_offset = self.container.get_scroll_offset()
                for card in self.cards:
                    if card.handle_click(mouse_pos, scroll_offset):
                        break
    
    def update(self):
        # Update card hover states
        mouse_pos = pygame.mouse.get_pos()
        scroll_offset = self.container.get_scroll_offset()
        for card in self.cards:
            card.check_hover(mouse_pos, scroll_offset)
    
    def draw(self):
        # Draw background
        self.screen.fill((30, 31, 38))
        
        # Draw container background
        pygame.draw.rect(self.screen, (40, 41, 48), self.container.rect, border_radius=10)
        pygame.draw.rect(self.screen, (60, 61, 68), self.container.rect, 2, border_radius=10)
        
        # Set clipping area for container
        clip_rect = self.container.rect.copy()
        self.screen.set_clip(clip_rect)
        
        # Draw cards with scroll offset
        scroll_offset = self.container.get_scroll_offset()
        for card in self.cards:
            card.draw(self.screen, scroll_offset)
        
        # Reset clipping
        self.screen.set_clip(None)
        
        # Draw scrollbar
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