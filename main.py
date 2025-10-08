import pygame
import random
import game
import menu_grid

fps = 30

pygame.init()
pygame.mixer.init()
screen_info = pygame.display.Info()
width, height = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((width-20, height-20), pygame.RESIZABLE)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
games = game.game_list

running = True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Добавляем выход по ESC
                running = False
    
    # ВСЮ ОТРИСОВКУ делаем внутри цикла:
    screen.fill((52, 49, 63)) # Заливаем белым каждый кадр
    i = 0
    y = 10
    row_count = 5
    for game_info in game.game_list:
        card = menu_grid.card(10 + i * 360, y, 330, 500, game_info)
        card.draw(screen)
        y = y + 550 if i==row_count-1 else y
        i = 0 if i==row_count-1 else i+1
        
    
    pygame.display.flip()  # Обновляем экран

pygame.quit()