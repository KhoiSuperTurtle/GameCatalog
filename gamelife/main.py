import random
import pygame

class GOL:
    def __init__(self, screen_width, screen_height):
        self.BLACK   = (0,0,0)
        self.GREY    = (128,128,128)
        self.YELLOW  = (255,255,0)

        self.WIDTH   = screen_width
        self.HEIGH   = 800
        self.TILE_S  = screen_height

        self.GRID_W  = self.WIDTH // self.TILE_S
        self.GRID_H  = self.HEIGH // self.TILE_S
        self.FPS     = 60


        screen  = pygame.display.set_mode((self.WIDTH, self.HEIGH))
        clock   = pygame.time.Clock()
        self.title = "Game of Life"
        self.description = "The Game of Life, also known as Conway's Game of Life or simply Life," \
        " is a cellular automaton devised by the British mathematician John Horton Conway in 1970. " \
        "It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input."
    
    def __del__(self):
        print("Quit")

    def set_speed(self, speed):
        self.speed = speed

    def get_title(self):
        return self.title
    
    def get_desc(self):
        return self.description
    

    def run(self):
        run  = True
        play = False
        count = 0
        update_freq = 10
        
        possitions  = set()
        possitions.add((10,10))

        while run:
            clock.tick(self.FPS)

            if play:
                count+=1
            
            if count >= update_freq:
                count = 0
                possitions = adjust(possitions)

            pygame.display.set_caption("Playing" if play else "Paused")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    col = x // self.TILE_S
                    row = y // self.TILE_S
                    pos = (col, row)

                    if pos in possitions:
                        possitions.remove(pos)
                    else:
                        possitions.add(pos)
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        play = not play
                    if event.key == pygame.K_c:
                        possitions = set()
                        play  = False
                        count = 0

                    if event.key == pygame.K_g:
                        possitions = gen(random.randrange(1,10)* self.GRID_W)
            
            screen.fill(self.GREY)
            draw(possitions = possitions)
            pygame.display.update()

        pygame.quit()
    def stop():
        pass
        

BLACK   = (0,0,0)
GREY    = (128,128,128)
YELLOW  = (255,255,0)

WIDTH   = 800
HEIGH   = 800
TILE_S  = 20

GRID_W  = WIDTH // TILE_S
GRID_H  = HEIGH // TILE_S
FPS     = 60
pygame.init()


screen  = pygame.display.set_mode((WIDTH, HEIGH))
clock   = pygame.time.Clock()

def gen(num):
    return set([(random.randrange(0, GRID_H), random.randrange(0, GRID_W)) for _ in range(num)])

def draw(possitions):
    for possition in possitions:
        col, row = possition
        top_left = (col * TILE_S, row * TILE_S)
        pygame.draw.rect(screen, YELLOW, (*top_left, TILE_S, TILE_S))

    for row in range(GRID_H):
        pygame.draw.line(screen, BLACK, (0, row * TILE_S), (WIDTH, row * TILE_S))
    
    for col in range(GRID_W):
        pygame.draw.line(screen, BLACK, (col * TILE_S, 0), (col * TILE_S, HEIGH))

def adjust(possitions):
    all_neighbors   = set()
    new_possitions  = set()

    for pos in possitions:
        neighbors = get_n(pos)
        all_neighbors.update(neighbors)
        neighbors = list(filter(lambda x : x in possitions, neighbors))

        if len(neighbors) in [2,3]:
            new_possitions.add(pos)

    for pos in all_neighbors:
        neighbors = get_n(pos)
        neighbors = list(filter(lambda x : x in possitions, neighbors))
        if len(neighbors) == 3:
            new_possitions.add(pos)
    
    return new_possitions

def get_n(pos):
    x,y = pos
    neighbors = []
    for dx in [-1,0,1]:
        if x + dx < 0 or x + dx > GRID_W:
            continue
        for dy in [-1,0,1]:
            if y + dy < 0 or y + dy > GRID_H:
                continue
            if dx == 0 and dy == 0:
                continue
            neighbors.append((x+dx, y + dy))

    return neighbors

def main():
    run  = True
    play = False
    count = 0
    update_freq = 10
    
    possitions  = set()
    possitions.add((10,10))

    while run:
        clock.tick(FPS)

        if play:
            count+=1
        
        if count >= update_freq:
            count = 0
            possitions = adjust(possitions)

        pygame.display.set_caption("Playing" if play else "Paused")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                col = x // TILE_S
                row = y // TILE_S
                pos = (col, row)

                if pos in possitions:
                    possitions.remove(pos)
                else:
                    possitions.add(pos)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play = not play
                if event.key == pygame.K_c:
                    possitions = set()
                    play  = False
                    count = 0

                if event.key == pygame.K_g:
                    possitions = gen(random.randrange(1,10)* GRID_W)
        
        screen.fill(GREY)
        draw(possitions = possitions)
        pygame.display.update()

    pygame.quit()
if __name__ == "__main__":
    main()