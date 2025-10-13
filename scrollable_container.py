import pygame

class ScrollableContainer:
    def __init__(self, x, y, width, height, content_height=0):
        self.rect = pygame.Rect(x, y, width, height)
        self.content_height = content_height
        self.scroll_y = 0
        self.scroll_speed = 20
        self.is_dragging = False
        self.drag_start_y = 0
        self.scroll_start_y = 0
        
        # Scrollbar settings
        self.scrollbar_width = 10
        self.scrollbar_padding = 2
        self.scrollbar_color = (100, 100, 100, 150)
        self.scrollbar_handle_color = (150, 150, 150, 200)
        self.scrollbar_rect = pygame.Rect(
            x + width - self.scrollbar_width - self.scrollbar_padding,
            y + self.scrollbar_padding,
            self.scrollbar_width,
            height - 2 * self.scrollbar_padding
        )
        
    def set_content_height(self, height):
        self.content_height = height
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll up
                self.scroll_y = min(0, self.scroll_y + self.scroll_speed)
                return True
            elif event.button == 5:  # Scroll down
                max_scroll = min(0, self.rect.height - self.content_height)
                self.scroll_y = max(max_scroll, self.scroll_y - self.scroll_speed)
                return True
            elif event.button == 1:  # Left click
                mouse_pos = pygame.mouse.get_pos()
                if self.scrollbar_rect.collidepoint(mouse_pos):
                    self.is_dragging = True
                    self.drag_start_y = mouse_pos[1]
                    self.scroll_start_y = self.scroll_y
                    return True
                    
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.is_dragging:
                self.is_dragging = False
                return True
                
        elif event.type == pygame.MOUSEMOTION:
            if self.is_dragging:
                mouse_y = event.pos[1]
                delta_y = mouse_y - self.drag_start_y
                scroll_ratio = self.content_height / self.rect.height
                self.scroll_y = self.scroll_start_y - (delta_y * scroll_ratio)
                max_scroll = min(0, self.rect.height - self.content_height)
                self.scroll_y = max(max_scroll, min(0, self.scroll_y))
                return True
                
        return False
        
    def get_scroll_offset(self):
        return self.scroll_y
        
    def draw(self, surface):
        # Draw scrollbar background
        scrollbar_bg = self.scrollbar_rect.copy()
        pygame.draw.rect(surface, self.scrollbar_color, scrollbar_bg, border_radius=5)
        
        # Calculate scrollbar handle
        if self.content_height > self.rect.height:
            handle_height = max(30, (self.rect.height / self.content_height) * self.rect.height)
            scroll_ratio = -self.scroll_y / (self.content_height - self.rect.height)
            handle_y = self.scrollbar_rect.y + scroll_ratio * (self.scrollbar_rect.height - handle_height)
            
            handle_rect = pygame.Rect(
                self.scrollbar_rect.x,
                handle_y,
                self.scrollbar_rect.width,
                handle_height
            )
            pygame.draw.rect(surface, self.scrollbar_handle_color, handle_rect, border_radius=5)