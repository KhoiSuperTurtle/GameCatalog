import pygame
import sys

class TetrisGame:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Тетрис")
        
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.running = True
        
        self.background_color = (20, 20, 30)
        self.text_color = (255, 255, 255)
        self.accent_color = (80, 250, 123)
        
        self.title_font = pygame.font.Font(None, 74)
        self.info_font = pygame.font.Font(None, 36)
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return "quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    return "menu" 
                elif event.key == pygame.K_RETURN:
                    pass
        return "tetris"
    
    def update(self):
        pass
    
    def draw(self):
        self.screen.fill(self.background_color)
        
        title_text = self.title_font.render("ТЕТРИС", True, self.accent_color)
        title_rect = title_text.get_rect(center=(self.screen_width//2, self.screen_height//2 - 50))
        self.screen.blit(title_text, title_rect)
        
        instr_text = self.info_font.render("Нажмите ESC для возврата в меню", True, self.text_color)
        instr_rect = instr_text.get_rect(center=(self.screen_width//2, self.screen_height//2 + 50))
        self.screen.blit(instr_text, instr_rect)
        
        soon_text = self.info_font.render("Скоро будет реализовано...", True, (200, 200, 200))
        soon_rect = soon_text.get_rect(center=(self.screen_width//2, self.screen_height//2 + 120))
        self.screen.blit(soon_text, soon_rect)
        
        pygame.display.flip()
    
    def run(self):
        """Запуск игры тетрис"""
        while self.running:
            result = self.handle_events()
            if result != "tetris":
                return result
            self.update()
            self.draw()
            self.clock.tick(self.fps)
        return "quit"

def main():
    pygame.init()
    game = TetrisGame(800, 600)
    game.run()
    pygame.quit()

if __name__ == "__main__":
    main()