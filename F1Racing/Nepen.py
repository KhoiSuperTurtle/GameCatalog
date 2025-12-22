import pygame
import time
import random
import os
import math

class F1RacingGame:
    def __init__(self, screen_width, screen_height):
        # Игнорируем переданные размеры и используем фиксированные для игры
        self.original_width = 580
        self.original_height = 800
        
        # Создаем окно игры с собственным разрешением
        self.screen = pygame.display.set_mode((self.original_width, self.original_height))
        pygame.display.set_caption('F1 Race Road Game')
        
        # Центрируем окно на экране
        self.center_window()
        
        self.clock = pygame.time.Clock()
        self.running = False
        self.return_status = "menu"
        
        self.BASE_PATH = "F1Racing"
        
        self.init_game()
    
    def center_window(self):
        import ctypes
        
        hwnd = pygame.display.get_wm_info()['window']
        
        user32 = ctypes.windll.user32
        screen_width = user32.GetSystemMetrics(0)
        screen_height = user32.GetSystemMetrics(1)
        
        x_pos = (screen_width - self.original_width) // 2
        y_pos = (screen_height - self.original_height) // 2
        
        SWP_NOZORDER = 0x0004
        SWP_NOACTIVATE = 0x0010
        user32.SetWindowPos(hwnd, 0, x_pos, y_pos, 0, 0, SWP_NOZORDER | SWP_NOACTIVATE)
    
    def init_game(self):
        self.btn_width = 247
        self.btn_height = 50
        
        self.black_color = (0, 0, 0)
        self.white_color = (255, 255, 255)
        self.red_color = (255, 0, 0)
        self.yellow_color = (238, 151, 38)
        self.redLight_color = (169, 36, 15)
        self.gray_color = (112, 128, 144)
        self.green_color = (0, 255, 0)
        self.greenLight_color = (36, 115, 12)
        self.blue_color = (30, 59, 246)
        self.purple_color = (128, 0, 128)
        
        self.load_images()
        
        self.load_sounds()
        
        self.car_animation_counter = 0
        self.obstacle_animation_counter = 0
        self.powerup_animation_counter = 0
        self.ANIMATION_SPEED = 5
        
        self.btn_starting_x = (self.original_width - self.btn_width) // 2
        self.nw_gm_y = self.original_height * 0.45
        self.exit_y = self.original_height * 0.55
        self.pause_btn_y = self.original_height * 0.4
        self.crash_btn_y = self.original_height * 0.4
        
    def load_images(self):
        try:
            self.car_frames = []
            for i in range(1, 4):
                frame_path = os.path.join(self.BASE_PATH, 'images', 'car', f'car{i}.png')
                frame = pygame.image.load(frame_path).convert_alpha()
                self.car_frames.append(frame)
            
            self.boost_transform_frames = []
            for i in range(1, 13):
                frame_path = os.path.join(self.BASE_PATH, 'images', 'car', 'car_boost_transform', f'boost_transform{i}.png')
                frame = pygame.image.load(frame_path).convert_alpha()
                self.boost_transform_frames.append(frame)
            
            self.shield_transform_frames = []
            for i in range(1, 13):
                frame_path = os.path.join(self.BASE_PATH, 'images', 'car', 'car_shield_transform', f'shield_transform{i}.png')
                frame = pygame.image.load(frame_path).convert_alpha()
                self.shield_transform_frames.append(frame)
            
            self.car_boost_frames = []
            for i in range(1, 4):
                frame_path = os.path.join(self.BASE_PATH, 'images', 'car', f'car_boost{i}.png')
                frame = pygame.image.load(frame_path).convert_alpha()
                self.car_boost_frames.append(frame)
            
            self.car_shield_frames = []
            for i in range(1, 4):
                frame_path = os.path.join(self.BASE_PATH, 'images', 'car', f'car_shield{i}.png')
                frame = pygame.image.load(frame_path).convert_alpha()
                self.car_shield_frames.append(frame)
            
            self.pilot_texture = pygame.image.load(os.path.join(self.BASE_PATH, 'images', 'pilot.png')).convert_alpha()
            
            self.obstacle_frames = []
            for i in range(1, 4):
                frame_path = os.path.join(self.BASE_PATH, 'images', 'obstacle', f'obstacle{i}.png')
                frame = pygame.image.load(frame_path).convert_alpha()
                self.obstacle_frames.append(frame)
            
            self.boost_frames = []
            for i in range(1, 4):
                frame_path = os.path.join(self.BASE_PATH, 'images', 'powerups', f'powerup_boost{i}.png')
                frame = pygame.image.load(frame_path).convert_alpha()
                self.boost_frames.append(frame)
            
            self.shield_frames = []
            for i in range(1, 4):
                frame_path = os.path.join(self.BASE_PATH, 'images', 'powerups', f'powerup_shield{i}.png')
                frame = pygame.image.load(frame_path).convert_alpha()
                self.shield_frames.append(frame)
            
            self.texture_photo = pygame.image.load(os.path.join(self.BASE_PATH, 'images', 'texture_wide.png'))
            self.icon = pygame.image.load(os.path.join(self.BASE_PATH, 'images', 'logo.png'))
            self.image_background = pygame.image.load(os.path.join(self.BASE_PATH, 'images', 'texture_wide.png'))
            pygame.display.set_icon(self.icon)
            
            self.explosion_frames = []
            for i in range(1, 20):
                frame_path = os.path.join(self.BASE_PATH, 'images', 'explosion', f'explosion{i}.png')
                frame = pygame.image.load(frame_path).convert_alpha()
                self.explosion_frames.append(frame)
            
            self.logo_menu = pygame.image.load(os.path.join(self.BASE_PATH, 'images', 'buttons', 'logo_menu.png')).convert_alpha()
            self.game_over = pygame.image.load(os.path.join(self.BASE_PATH, 'images', 'buttons', 'game_over.png')).convert_alpha()
            self.start_menu = pygame.image.load(os.path.join(self.BASE_PATH, 'images', 'buttons', 'start_menu.png')).convert_alpha()
            
            self.continue_off = pygame.image.load(os.path.join(self.BASE_PATH, 'images', 'buttons', 'continue_off.png')).convert_alpha()
            self.continue_on = pygame.image.load(os.path.join(self.BASE_PATH, 'images', 'buttons', 'continue_on.png')).convert_alpha()
            self.menu_off = pygame.image.load(os.path.join(self.BASE_PATH, 'images', 'buttons', 'menu_off.png')).convert_alpha()
            self.menu_on = pygame.image.load(os.path.join(self.BASE_PATH, 'images', 'buttons', 'menu_on.png')).convert_alpha()
            self.new_game_off = pygame.image.load(os.path.join(self.BASE_PATH, 'images', 'buttons', 'new_game_off.png')).convert_alpha()
            self.new_game_on = pygame.image.load(os.path.join(self.BASE_PATH, 'images', 'buttons', 'new_game_on.png')).convert_alpha()
            self.quit_pause_off = pygame.image.load(os.path.join(self.BASE_PATH, 'images', 'buttons', 'quit_pause_off.png')).convert_alpha()
            self.quit_pause_on = pygame.image.load(os.path.join(self.BASE_PATH, 'images', 'buttons', 'quit_pause_on.png')).convert_alpha()
            self.play_off = pygame.image.load(os.path.join(self.BASE_PATH, 'images', 'buttons', 'play_off.png')).convert_alpha()
            self.play_on = pygame.image.load(os.path.join(self.BASE_PATH, 'images', 'buttons', 'play_on.png')).convert_alpha()
            self.quit_off = pygame.image.load(os.path.join(self.BASE_PATH, 'images', 'buttons', 'quit_off.png')).convert_alpha()
            self.quit_on = pygame.image.load(os.path.join(self.BASE_PATH, 'images', 'buttons', 'quit_on.png')).convert_alpha()
            self.pause_logo = pygame.image.load(os.path.join(self.BASE_PATH, 'images', 'buttons', 'pause.png')).convert_alpha()
            
            self.c_width, self.c_height = self.car_frames[0].get_rect().size
            self.t_width, self.t_height = self.obstacle_frames[0].get_rect().size
            self.p_width, self.p_height = self.boost_frames[0].get_rect().size
            self.pilot_width, self.pilot_height = self.pilot_texture.get_rect().size
            
            self.logo_menu_rect = self.logo_menu.get_rect()
            self.game_over_rect = self.game_over.get_rect()
            self.start_menu_rect = self.start_menu.get_rect()
            self.pause_logo_rect = self.pause_logo.get_rect()
            
            self.play_width, self.play_height = self.play_off.get_size()
            self.quit_width, self.quit_height = self.quit_off.get_size()
            self.continue_width, self.continue_height = self.continue_off.get_size()
            self.menu_width, self.menu_height = self.menu_off.get_size()
            self.new_game_width, self.new_game_height = self.new_game_off.get_size()
            self.quit_pause_width, self.quit_pause_height = self.quit_pause_off.get_size()
            
            self.bckgrndRect = self.image_background.get_rect()
            
            self.texture_photo = self.texture_photo.convert()
            self.image_background = self.image_background.convert()
            
        except Exception as e:
            print(f"Ошибка загрузки изображений: {e}")
            pygame.quit()
            exit()
    
    def load_sounds(self):
        try:
            pygame.mixer.music.load(os.path.join(self.BASE_PATH, 'sounds', 'RightToTheFin.wav'))
            self.explosion_sound = pygame.mixer.Sound(os.path.join(self.BASE_PATH, 'sounds', 'explosion.wav'))
            self.powerup_sound = pygame.mixer.Sound(os.path.join(self.BASE_PATH, 'sounds', 'powerup.wav'))
        except Exception as e:
            print(f"Ошибка загрузки звуков: {e}")
            self.explosion_sound = None
            self.powerup_sound = None
    
    class PowerUp:
        def __init__(self, x, y, powerup_type, game_instance):
            self.x = x
            self.y = y
            self.type = powerup_type
            self.active = True
            self.game = game_instance
        
        def move(self, speed):
            self.y += speed
            if self.y > self.game.original_height:
                self.active = False
        
        def draw(self, frame_index):
            if self.type == 'boost':
                self.game.screen.blit(self.game.boost_frames[frame_index], (self.x, self.y))
            elif self.type == 'shield':
                self.game.screen.blit(self.game.shield_frames[frame_index], (self.x, self.y))
    
    def rotate_image(self, image, angle):
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect()
        rot_rect.center = orig_rect.center
        return rot_image, rot_rect
    
    def play_obstacle_explosion(self, x, y):
        explosion_rect = self.explosion_frames[0].get_rect()
        explosion_rect.center = (x + self.t_width // 2, y + self.t_height // 2)
        
        start_frame = 8
        frame_delay = 45
        
        for i in range(start_frame, len(self.explosion_frames)):
            frame = self.explosion_frames[i]
            self.screen.blit(frame, explosion_rect)
            pygame.display.update()
            pygame.time.wait(frame_delay)
    
    def play_explosion_animation(self, x, y, obstacle_x, obstacle_y, direction, car_frame_index, obstacle_frame_index):
        explosion_rect = self.explosion_frames[0].get_rect()
        explosion_rect.center = (x + self.c_width // 2, y + self.c_height // 2)
        
        if self.explosion_sound:
            self.explosion_sound.play()
        
        for i, frame in enumerate(self.explosion_frames):
            self.screen.blit(self.image_background, self.bckgrndRect)
            self.screen.blit(self.texture_photo, (0, 0))
            
            self.draw_things(obstacle_x, obstacle_y, obstacle_frame_index)
            
            if i < 14:
                self.draw_car(x, y, direction, car_frame_index)
            else:
                pilot_rect = self.pilot_texture.get_rect()
                pilot_rect.center = (x + self.c_width // 2, y + self.c_height // 2)
                self.screen.blit(self.pilot_texture, pilot_rect)
            
            self.screen.blit(frame, explosion_rect)
            
            pygame.display.update()
            pygame.time.wait(50)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return True
        
        return False
    
    def things_dodged(self, counting, highest_score, everything_speed, invulnerable_time_left=0, boost_time_left=0):
        fnt = pygame.font.Font(os.path.join(self.BASE_PATH, 'Fonts', 'CaveFont.ttf'), 16)
        score = fnt.render("Score: " + str(counting), True, self.white_color)
        h_score = fnt.render("High Score: " + str(highest_score), True, self.white_color)
        speed = fnt.render("Speed: " + str(int(everything_speed * 2)) + "Km/H", True, self.white_color)
        self.screen.blit(score, (48, 5))
        self.screen.blit(h_score, (48, 32))
        self.screen.blit(speed, (self.original_width - 190, 5))
        
        if invulnerable_time_left > 0:
            invul_text = fnt.render(f"Shield: {invulnerable_time_left:.1f}s", True, self.blue_color)
            self.screen.blit(invul_text, (self.original_width - 158, 32))
        
        if boost_time_left > 0:
            boost_text = fnt.render(f"Boost: {boost_time_left:.1f}s", True, self.yellow_color)
            self.screen.blit(boost_text, (self.original_width - 158, 59))
    
    def high_score_update(self, dodged):
        try:
            with open(os.path.join(self.BASE_PATH, 'textfile', 'high_score.txt'), 'w') as high_scores:
                high_scores.write(str(dodged))
        except:
            print("Ошибка сохранения рекорда")
    
    def draw_things(self, th_x, th_y, frame_index=0):
        self.screen.blit(self.obstacle_frames[frame_index], (th_x, th_y))
    
    def draw_car(self, x, y, direction, frame_index=0, invulnerable=False, boost_active=False, transform_animation=False, transform_type=None, transform_frame=0):
        current_frame = None
        
        if transform_animation:
            if transform_type == 'boost':
                if transform_frame < len(self.boost_transform_frames):
                    current_frame = self.boost_transform_frames[transform_frame]
            elif transform_type == 'shield':
                if transform_frame < len(self.shield_transform_frames):
                    current_frame = self.shield_transform_frames[transform_frame]
        elif boost_active:
            current_frame = self.car_boost_frames[frame_index]
        elif invulnerable:
            current_frame = self.car_shield_frames[frame_index]
        else:
            current_frame = self.car_frames[frame_index]
        
        if direction == -1:
            rotated_frame, rot_rect = self.rotate_image(current_frame, 12)
            self.screen.blit(rotated_frame, (x - (rot_rect.width - self.c_width) // 2, y - (rot_rect.height - self.c_height) // 2))
        elif direction == 1:
            rotated_frame, rot_rect = self.rotate_image(current_frame, -12)
            self.screen.blit(rotated_frame, (x - (rot_rect.width - self.c_width) // 2, y - (rot_rect.height - self.c_height) // 2))
        else:
            self.screen.blit(current_frame, (x, y))
        
        return transform_animation
    
    def get_animation_frame(self, counter, speed, num_frames):
        return (counter // speed) % num_frames
    
    def text_objects(self, text, font, color):
        txtSurf = font.render(text, True, color)
        return txtSurf, txtSurf.get_rect()
    
    def message_display_screen(self, txt, sh_x, sh_y, color, time_sleeping=0):
        lar_txt = pygame.font.Font(os.path.join(self.BASE_PATH, 'Fonts', 'CaveFont.ttf'), 48)
        txtSurf, TxtRect = self.text_objects(txt, lar_txt, color)
        TxtRect.center = ((self.original_width / 2 - sh_x), (self.original_height / 2 - sh_y))
        self.screen.blit(txtSurf, TxtRect)
        pygame.display.update()
        if time_sleeping > 0:
            time.sleep(time_sleeping)
    
    def draw_menu_background(self):
        self.screen.blit(self.image_background, self.bckgrndRect)
        
        self.start_menu_rect.center = (self.original_width // 2, self.original_height // 2)
        self.screen.blit(self.start_menu, self.start_menu_rect)
        
        self.logo_menu_rect.center = (self.original_width // 2, self.original_height // 3 - 100)
        self.screen.blit(self.logo_menu, self.logo_menu_rect)
        
        small_txt = pygame.font.Font(os.path.join(self.BASE_PATH, 'Fonts', 'CaveFont.ttf'), 16)
        instr1 = small_txt.render("ARROWS  or  A/D  to  move", True, self.white_color)
        instr2 = small_txt.render("P  to  pause", True, self.white_color)
        instr3 = small_txt.render("ESC  to  quit", True, self.white_color)
        self.screen.blit(instr1, (self.original_width//2 - 120, 550))
        self.screen.blit(instr2, (self.original_width//2 - 120, 580))
        self.screen.blit(instr3, (self.original_width//2 - 120, 610))
    
    def image_button(self, off_image, on_image, x, y, width, height):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        button_rect = pygame.Rect(x - width // 2, y - height // 2, width, height)
        
        if button_rect.collidepoint(mouse):
            self.screen.blit(on_image, (x - width // 2, y - height // 2))
            if click[0] == 1:
                return True
        else:
            self.screen.blit(off_image, (x - width // 2, y - height // 2))
        
        return False
    
    def crash_function(self, car_x, car_y, obstacle_x, obstacle_y, direction, car_frame_index, obstacle_frame_index):
        pygame.mixer.music.stop()
        
        if self.play_explosion_animation(car_x, car_y, obstacle_x, obstacle_y, direction, car_frame_index, obstacle_frame_index):
            self.return_status = "menu"
            return True
        
        self.screen.blit(self.image_background, self.bckgrndRect)
        
        self.game_over_rect.center = (self.original_width // 2, 210)
        self.screen.blit(self.game_over, self.game_over_rect)
        
        pygame.event.clear()
        pygame.mouse.get_rel()
        time.sleep(0.1)
        
        while True:
            playAgain = self.image_button(self.new_game_off, self.new_game_on, self.btn_starting_x + self.btn_width // 2, self.crash_btn_y + self.btn_height // 2, self.new_game_width, self.new_game_height)
            menu_btn = self.image_button(self.menu_off, self.menu_on, self.btn_starting_x + self.btn_width // 2, self.crash_btn_y + 60 + self.btn_height // 2 + 15, self.menu_width, self.menu_height)
            exit_game = self.image_button(self.quit_pause_off, self.quit_pause_on, self.btn_starting_x + self.btn_width // 2, self.crash_btn_y + 120 + self.btn_height // 2 + 30, self.quit_pause_width, self.quit_pause_height)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.return_status = "quit"
                    return True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.return_status = "menu"
                        return True
                    if event.key == pygame.K_SPACE:
                        try:
                            pygame.mixer.music.play(-1)
                        except:
                            pass
                        self.looping_gameplay()
                        return False
                    if event.key == pygame.K_m:
                        self.return_status = "menu"
                        return True
            
            if playAgain:
                try:
                    pygame.mixer.music.play(-1)
                except:
                    pass
                self.looping_gameplay()
                return False
            if menu_btn:
                pygame.event.clear()
                pygame.mouse.get_rel()
                time.sleep(0.1)
                self.return_status = "menu"
                return True
            if exit_game:
                self.return_status = "quit"
                return True
                
            pygame.display.update()
            self.clock.tick(60)
    
    def welcome_gameplay(self):
        welcome = True
        
        while welcome:
            self.draw_menu_background()
            
            playGame = self.image_button(self.play_off, self.play_on, self.btn_starting_x + self.btn_width // 2 -2, self.nw_gm_y + self.btn_height // 2 -27, self.play_width, self.play_height)
            exit_game = self.image_button(self.quit_off, self.quit_on, self.btn_starting_x + self.btn_width // 2 -2, self.exit_y + self.btn_height // 2 -33, self.quit_width, self.quit_height)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.return_status = "quit"
                    return True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.return_status = "menu"
                        return True
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        welcome = False
                        try:
                            pygame.mixer.music.play(-1)
                        except:
                            pass
                        self.looping_gameplay()
                        return False
            
            if playGame:
                welcome = False
                try:
                    pygame.mixer.music.play(-1)
                except:
                    pass
                self.looping_gameplay()
                return False
            if exit_game:
                self.return_status = "menu"
                return True
                
            pygame.display.update()
            self.clock.tick(60)
        
        return False
    
    def counting_three_two_one(self):
        counting = 3
        pygame.mixer.music.pause()
        
        for i in range(3, -1, -1):
            self.screen.blit(self.image_background, self.bckgrndRect)
            self.draw_car((self.original_width -85) * 0.5, self.original_height * 0.6, 0, 0)
            
            if i == 0:
                self.message_display_screen("GO!", 0, 0, self.green_color, 0)
            else:
                self.message_display_screen(str(i), 0, 0, self.red_color, 0)
                
            pygame.display.update()
            
            if i > 0:
                pygame.time.wait(700)
        
        pygame.mixer.music.unpause()
        self.clock.tick(60)
    
    def gameplay_paused(self):
        pygame.mixer.music.pause()
        original_volume = pygame.mixer.music.get_volume()
        
        pause = True
        
        self.screen.blit(self.image_background, self.bckgrndRect)
        
        self.pause_logo_rect.center = (self.original_width // 2, self.original_height // 3 -20)
        self.screen.blit(self.pause_logo, self.pause_logo_rect)
        
        while pause:
            continue_btn = self.image_button(self.continue_off, self.continue_on, self.btn_starting_x + self.btn_width // 2, self.pause_btn_y + self.btn_height // 2, self.continue_width, self.continue_height)
            menu_btn = self.image_button(self.menu_off, self.menu_on, self.btn_starting_x + self.btn_width // 2, self.pause_btn_y + 60 + self.btn_height // 2 + 15, self.menu_width, self.menu_height)
            exit_btn = self.image_button(self.quit_pause_off, self.quit_pause_on, self.btn_starting_x + self.btn_width // 2, self.pause_btn_y + 120 + self.btn_height // 2 + 30, self.quit_pause_width, self.quit_pause_height)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.return_status = "quit"
                    return True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE or event.key == pygame.K_p:
                        pygame.mixer.music.unpause()
                        pygame.mixer.music.set_volume(original_volume)
                        pause = False
                        return False
                    if event.key == pygame.K_m:
                        pygame.mixer.music.unpause()
                        pygame.mixer.music.set_volume(original_volume)
                        self.return_status = "menu"
                        return True
            
            if continue_btn:
                pygame.mixer.music.unpause()
                pygame.mixer.music.set_volume(original_volume)
                pause = False
                return False
            if menu_btn:
                pygame.mixer.music.unpause()
                pygame.mixer.music.set_volume(original_volume)
                self.return_status = "menu"
                return True
            if exit_btn:
                self.return_status = "quit"
                return True
                
            pygame.display.update()
            self.clock.tick(60)
    
    def motion_texture(self, th_starting, texture_speed):
        th_starting += texture_speed
        if th_starting >= self.original_height:
            th_starting = 0
        self.screen.blit(self.texture_photo, (0, th_starting - self.original_height))
        self.screen.blit(self.texture_photo, (0, th_starting))
        return th_starting
    
    def looping_gameplay(self):
        width_x = ((self.original_width -85) * 0.5)
        height_y = (self.original_height * 0.6)
        ch_x = 0

        th_st_x = random.randrange(17, self.original_width - self.t_width - 17)
        th_st_y = -100
        th_speed = 7
        side_speed = 0

        texture_y = 0
        texture_speed = 10

        dodg = 0
        direction = 0
        
        powerups = []
        powerup_spawn_chance = 25
        powerup_speed = th_speed - 2
        
        invulnerable = False
        invulnerable_timer = 0
        INVULNERABLE_DURATION = 3.0
        
        boost_active = False
        boost_timer = 0
        BOOST_DURATION = 5.0
        original_speed = th_speed
        original_texture_speed = texture_speed
        
        transform_animation = False
        transform_type = None
        transform_frame = 0
        transform_counter = 0
        TRANSFORM_ANIMATION_SPEED = 2

        try:
            with open(os.path.join(self.BASE_PATH, 'textfile', 'high_score.txt'), 'r') as file:
                high_score = file.read().strip()
                if not high_score:
                    high_score = "0"
        except:
            high_score = "0"

        gameExit = False
        self.counting_three_two_one()

        self.car_animation_counter = 0
        self.obstacle_animation_counter = 0
        self.powerup_animation_counter = 0
        
        last_time = time.time()

        while not gameExit:
            current_time = time.time()
            delta_time = current_time - last_time
            last_time = current_time
            
            if invulnerable:
                invulnerable_timer -= delta_time
                if invulnerable_timer <= 0:
                    invulnerable = False
            
            if boost_active:
                boost_timer -= delta_time
                if boost_timer <= 0:
                    boost_active = False
                    th_speed = original_speed
                    texture_speed = original_texture_speed
                    powerup_speed = th_speed - 2

            self.car_animation_counter += 1
            self.obstacle_animation_counter += 1
            self.powerup_animation_counter += 1
            
            if transform_animation:
                transform_counter += 1
                transform_frame = transform_counter // TRANSFORM_ANIMATION_SPEED
                if transform_frame >= 12:
                    transform_animation = False
                    transform_frame = 0
                    transform_counter = 0
            
            car_frame_index = self.get_animation_frame(self.car_animation_counter, self.ANIMATION_SPEED, 3)
            obstacle_frame_index = self.get_animation_frame(self.obstacle_animation_counter, self.ANIMATION_SPEED, len(self.obstacle_frames))
            powerup_frame_index = self.get_animation_frame(self.powerup_animation_counter, self.ANIMATION_SPEED, len(self.boost_frames))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.return_status = "quit"
                    return True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.return_status = "menu"
                        return True
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        ch_x = -8 - side_speed
                        direction = -1
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        ch_x = 8 + side_speed
                        direction = 1
                    if event.key == pygame.K_SPACE or event.key == pygame.K_p:
                        if self.gameplay_paused():
                            return True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                        ch_x = 0
                        direction = 0

            width_x += ch_x
            
            if width_x > self.original_width - self.c_width + 20:
                width_x = self.original_width - self.c_width + 20
            if width_x < -20:
                width_x = -20
            
            self.screen.blit(self.image_background, self.bckgrndRect)
            texture_y = self.motion_texture(texture_y, texture_speed)
            
            self.draw_things(th_st_x, th_st_y, obstacle_frame_index)
            
            for powerup in powerups[:]:
                powerup.move(powerup_speed)
                if powerup.active:
                    powerup.draw(powerup_frame_index)
                else:
                    powerups.remove(powerup)
            
            self.draw_car(width_x, height_y, direction, car_frame_index, invulnerable, boost_active, transform_animation, transform_type, transform_frame)
            
            self.things_dodged(dodg, high_score, th_speed, 
                             invulnerable_timer if invulnerable else 0,
                             boost_timer if boost_active else 0)

            th_st_y += th_speed - 5
            
            collision = (height_y + self.c_height > th_st_y + 15 and
                        height_y < th_st_y + self.t_height - 15 and
                        width_x < th_st_x + self.t_width - 5 and
                        width_x + self.c_width > th_st_x + 5)
            
            if collision:
                if invulnerable:
                    self.play_obstacle_explosion(th_st_x, th_st_y)
                    th_st_y = -self.t_height - 50
                    th_st_x = random.randrange(17, self.original_width - self.t_width - 17)
                    dodg += 1
                    
                    powerup_spawn_chance = min(powerup_spawn_chance + 10, 80)
                    
                    texture_speed = min(texture_speed + 0.8, 40)
                    th_speed = min(th_speed + 0.8, 40)
                    powerup_speed = th_speed - 2

                    side_speed += 0.5
                    
                    if dodg > int(high_score):
                        self.high_score_update(dodg)
                        high_score = str(dodg)
                else:
                    if self.crash_function(width_x, height_y, th_st_x, th_st_y, direction, car_frame_index, obstacle_frame_index):
                        return
            
            if th_st_y > self.original_height:
                th_st_y = -self.t_height - 50
                th_st_x = random.randrange(17, self.original_width - self.t_width - 17)
                dodg += 1
                
                powerup_spawn_chance = min(powerup_spawn_chance + 10, 80)
                
                if random.randint(1, 100) <= powerup_spawn_chance:
                    powerup_type = random.choice(['boost', 'shield'])
                    powerup_x = random.randrange(17, self.original_width - self.p_width - 17)
                    powerups.append(self.PowerUp(powerup_x, -100, powerup_type, self))
                    powerup_spawn_chance = 25
                
                texture_speed = min(texture_speed + 0.8, 40)
                th_speed = min(th_speed + 0.8, 40)
                powerup_speed = th_speed - 2

                side_speed += 0.5
                
                if dodg > int(high_score):
                    self.high_score_update(dodg)
                    high_score = str(dodg)
            
            for powerup in powerups[:]:
                if (powerup.active and
                    height_y + self.c_height > powerup.y + 15 and
                    height_y < powerup.y + self.p_height - 15 and
                    width_x < powerup.x + self.p_width - 5 and
                    width_x + self.c_width > powerup.x + 5):
                    
                    if powerup.type == 'boost':
                        boost_active = True
                        boost_timer = BOOST_DURATION
                        
                        if not transform_animation:
                            original_speed = th_speed
                            original_texture_speed = texture_speed
                            th_speed += 5
                            side_speed += 1
                            texture_speed += 5
                            powerup_speed = th_speed - 2
                            transform_animation = True
                            transform_type = 'boost'
                            transform_frame = 0
                            transform_counter = 0
                        
                    elif powerup.type == 'shield':
                        invulnerable = True
                        invulnerable_timer = INVULNERABLE_DURATION
                        
                        if not transform_animation:
                            transform_animation = True
                            transform_type = 'shield'
                            transform_frame = 0
                            transform_counter = 0
                    
                    if self.powerup_sound:
                        self.powerup_sound.play()
                    
                    powerups.remove(powerup)

            pygame.display.update()
            self.clock.tick(60)
        
        return False
    
    def run(self):
        pygame.display.set_caption('F1 Race Road Game')
        
        self.running = True
        self.return_status = "menu"
        
        if self.welcome_gameplay():
            return self.return_status
        
        return self.return_status