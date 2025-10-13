import pygame

class Card:
    def __init__(self, x, y, width, height, game_info):
        self.rect = pygame.Rect(x, y, width, height)
        self.game_info = game_info
        self.corner_radius = 15
        self.shadow_offset = 5
        
        # Colors with modern palette
        self.colors = {
            'background': (40, 42, 54),
            'header': (98, 114, 164),
            'image_area': (68, 71, 90),
            'description': (68, 71, 90),
            'footer': (98, 114, 164),
            'shadow': (0, 0, 0, 100),
            'text': (248, 248, 242),
            'button_hover': (80, 250, 123)
        }
        
        # Section rectangles
        header_height = 50
        image_height = 200
        description_height = 80
        footer_height = 50
        
        self.sections = {
            'header': pygame.Rect(0, 0, width, header_height),
            'image_area': pygame.Rect(0, header_height, width, image_height),
            'description': pygame.Rect(0, header_height + image_height, width, description_height),
            'footer': pygame.Rect(0, header_height + image_height + description_height, width, footer_height)
        }
        
        # Fonts
        self.fonts = {
            'title': pygame.font.Font(None, 24),
            'description': pygame.font.Font(None, 18),
            'footer': pygame.font.Font(None, 20)
        }
        
        self.title = game_info.get_name()
        self.description = game_info.get_description()
        self.footer_text = "Играть"
        self.is_hovered = False
        
        # Load and scale image
        self.image = None
        if game_info.get_image():
            try:
                loaded_image = pygame.image.load(game_info.get_image())
                # Scale image to fit with padding
                target_width = width - 20
                target_height = image_height - 20
                self.image = pygame.transform.scale(loaded_image, (target_width, target_height))
            except (pygame.error, FileNotFoundError):
                print(f"Не удалось загрузить изображение: {game_info.get_image()}")
                self.image = None
        
    def draw(self, surface, scroll_offset=0):
        # Adjust position for scrolling
        draw_rect = self.rect.move(0, scroll_offset)
        
        # Draw shadow
        shadow_rect = draw_rect.move(self.shadow_offset, self.shadow_offset)
        shadow_surf = pygame.Surface((shadow_rect.width, shadow_rect.height), pygame.SRCALPHA)
        pygame.draw.rect(shadow_surf, self.colors['shadow'], 
                        (0, 0, shadow_rect.width, shadow_rect.height), 
                        border_radius=self.corner_radius)
        surface.blit(shadow_surf, shadow_rect)
        
        # Draw main card background
        pygame.draw.rect(surface, self.colors['background'], draw_rect, 
                        border_radius=self.corner_radius)
        pygame.draw.rect(surface, (100, 100, 100), draw_rect, 
                        2, border_radius=self.corner_radius)
        
        # Draw sections with rounded corners only where needed
        self._draw_section(surface, 'header', draw_rect, 
                          top_left=True, top_right=True)
        self._draw_section(surface, 'image_area', draw_rect)
        self._draw_section(surface, 'description', draw_rect)
        
        # Footer with hover effect
        footer_color = self.colors['button_hover'] if self.is_hovered else self.colors['footer']
        self._draw_section(surface, 'footer', draw_rect, 
                          bottom_left=True, bottom_right=True, 
                          color=footer_color)
        
        # Draw image or placeholder
        image_draw_rect = self.sections['image_area'].move(draw_rect.x, draw_rect.y)
        if self.image:
            # Center image in the area
            image_rect = self.image.get_rect(center=image_draw_rect.center)
            surface.blit(self.image, image_rect)
        else:
            # Draw placeholder
            placeholder_rect = image_draw_rect.inflate(-20, -20)
            pygame.draw.rect(surface, (50, 50, 60), placeholder_rect, border_radius=10)
            placeholder_text = self.fonts['description'].render("Нет изображения", True, (150, 150, 150))
            text_rect = placeholder_text.get_rect(center=placeholder_rect.center)
            surface.blit(placeholder_text, text_rect)
        
        # Draw title (centered in header)
        title_surf = self.fonts['title'].render(self.title, True, self.colors['text'])
        title_rect = title_surf.get_rect(center=self.sections['header'].move(draw_rect.x, draw_rect.y).center)
        surface.blit(title_surf, title_rect)
        
        # Draw description with word wrap
        desc_lines = self._wrap_text(self.description, self.fonts['description'], 
                                   self.sections['description'].width - 20)
        desc_draw_rect = self.sections['description'].move(draw_rect.x, draw_rect.y)
        for i, line in enumerate(desc_lines):
            desc_surf = self.fonts['description'].render(line, True, self.colors['text'])
            desc_rect = desc_surf.get_rect(centerx=desc_draw_rect.centerx, 
                                         top=desc_draw_rect.top + 10 + i * 18)
            surface.blit(desc_surf, desc_rect)
        
        # Draw footer text
        footer_surf = self.fonts['footer'].render(self.footer_text, True, self.colors['text'])
        footer_draw_rect = self.sections['footer'].move(draw_rect.x, draw_rect.y)
        footer_rect = footer_surf.get_rect(center=footer_draw_rect.center)
        surface.blit(footer_surf, footer_rect)
        
    def _draw_section(self, surface, section_name, card_rect, 
                     top_left=False, top_right=False, 
                     bottom_left=False, bottom_right=False, color=None):
        """Draw a section with specific rounded corners"""
        section = self.sections[section_name]
        draw_rect = section.move(card_rect.x, card_rect.y)
        
        if color is None:
            color = self.colors.get(section_name, self.colors['background'])
            
        # Determine which corners to round
        radius = self.corner_radius
        corners = [bottom_right, bottom_left, top_left, top_right]
        
        if any(corners):
            # Create surface with alpha for rounded corners
            section_surf = pygame.Surface((draw_rect.width, draw_rect.height), pygame.SRCALPHA)
            pygame.draw.rect(section_surf, color, (0, 0, draw_rect.width, draw_rect.height),
                            border_radius=radius, 
                            border_top_left_radius=radius if top_left else 0,
                            border_top_right_radius=radius if top_right else 0,
                            border_bottom_left_radius=radius if bottom_left else 0,
                            border_bottom_right_radius=radius if bottom_right else 0)
            surface.blit(section_surf, draw_rect)
        else:
            pygame.draw.rect(surface, color, draw_rect)
    
    def _wrap_text(self, text, font, max_width):
        """Wrap text to fit within max_width"""
        words = text.split(' ')
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            test_width = font.size(test_line)[0]
            
            if test_width <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word] if font.size(word)[0] <= max_width else [word[:len(word)//2]]
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines
    
    def check_hover(self, pos, scroll_offset=0):
        """Check if mouse is hovering over the card"""
        adjusted_rect = self.rect.move(0, scroll_offset)
        self.is_hovered = adjusted_rect.collidepoint(pos)
        return self.is_hovered
    
    def handle_click(self, pos, scroll_offset=0):
        """Handle click on card"""
        adjusted_rect = self.rect.move(0, scroll_offset)
        if adjusted_rect.collidepoint(pos):
            print(f"Запуск игры: {self.title}")
            return True
        return False