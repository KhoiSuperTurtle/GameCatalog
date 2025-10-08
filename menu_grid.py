import pygame
import game

class card:
    def __init__(self, x, y, width, height, game_info):
        self.rect = pygame.Rect(x,y,width,height)
        self.sections = {
            'header': pygame.Rect(x, y, width, 40),
            'image_area': pygame.Rect(x, y + 40, width, height-150),
            'description': pygame.Rect(x, y + 40 + height - 150, width, 60),
            'footer': pygame.Rect(x, y + 100 + height - 150, width, 50)
        }
        self.colors = {
            'header': (70, 130, 180),
            'image_area': (29, 31, 43),
            'description': (29, 31, 43),
            'footer': (70, 130, 180)
        }
        self.fonts = {
            'title': pygame.font.Font(None, 28),
            'description': pygame.font.Font(None, 20),
            'footer': pygame.font.Font(None, 18)
        }
        self.title = game_info.getName()
        self.description = game_info.description
        self.footer_text = "Играть"
        self.game_info = game_info
        
        # Загружаем изображение, если путь указан
        self.image = None
        if game_info.image:
            try:
                loaded_image = pygame.image.load(game_info.image)
                # Масштабируем изображение под размер image_area
                self.image = pygame.transform.scale(loaded_image, 
                                                  (self.sections['image_area'].width - 20, 
                                                   self.sections['image_area'].height - 20))
            except pygame.error as e:
                print(f"Не удалось загрузить изображение: {game_info.image}")
                print(f"Ошибка: {e}")
                self.image = None
        
    def draw(self, surface):
        # Рисуем разделы карточки
        for section_name, section_rect in self.sections.items():
            pygame.draw.rect(surface, self.colors[section_name], section_rect)
            pygame.draw.rect(surface, (100, 100, 100), section_rect, 1)
        
        # Рисуем изображение, если оно загружено
        if self.image:
            # Центрируем изображение в области image_area
            image_rect = self.image.get_rect()
            image_rect.center = self.sections['image_area'].center
            surface.blit(self.image, image_rect)
        else:
            # Если изображения нет, показываем placeholder
            placeholder_text = self.fonts['description'].render("Нет изображения", True, (255, 255, 255))
            placeholder_rect = placeholder_text.get_rect(center=self.sections['image_area'].center)
            surface.blit(placeholder_text, placeholder_rect)
        
        # Заголовок
        title_surf = self.fonts['title'].render(self.title, True, (255, 255, 255))
        title_rect = title_surf.get_rect(center=self.sections['header'].center)
        surface.blit(title_surf, title_rect)
        
        # Описание (с переносом строк)
        desc_lines = self._wrap_text(self.description, self.fonts['description'], self.sections['description'].width - 20)
        for i, line in enumerate(desc_lines):
            desc_surf = self.fonts['description'].render(line, True, (255, 255, 255))
            desc_rect = desc_surf.get_rect(centerx=self.sections['description'].centerx, 
                                         top=self.sections['description'].top + 10 + i * 20)
            surface.blit(desc_surf, desc_rect)
        
        # Футер
        footer_surf = self.fonts['footer'].render(self.footer_text, True, (255, 255, 255))
        footer_rect = footer_surf.get_rect(center=self.sections['footer'].center)
        surface.blit(footer_surf, footer_rect)
    
    def _wrap_text(self, text, font, max_width):
        """Перенос текста по словам"""
        words = text.split(' ')
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            test_width = font.size(test_line)[0]
            
            if test_width <= max_width:
                current_line.append(word)
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines