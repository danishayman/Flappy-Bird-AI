import pygame
pygame.font.init()

from bird import Bird
from pipe import Pipe
from base import Base
from variables import WIN_WIDTH, WIN_HEIGHT, BG_IMG, STAT_FONT
from control import Control
from menu import Menu

def draw_window(win, bird, pipes, base, score):
    win.blit(BG_IMG, (0, 0))
    
    for pipe in pipes:
        pipe.draw(win)
        
    text = STAT_FONT.render("Score: " + str(score), 1, (255,255,255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))
        
    base.draw(win)
    bird.draw(win)
    pygame.display.update()

def main():
    bird = Bird(230, 350)
    base = Base(730)
    pipes = [Pipe(600)]
    score = 0
    controller = Control(bird, pipes, base, score)
    menu = Menu()
    
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    
    # Start screen loop
    start_game = False
    while not start_game:
        clock.tick(30)
        events = pygame.event.get()
        
        # Handle quit events
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        # Check for start condition
        start_game = Menu.check_start_trigger(events)
        
        # Draw menu
        menu.draw_start_screen(win)
        pygame.display.update()

    # Main game loop
    run = True
    while run:
        clock.tick(30)

        controller.handle_events()
        draw_window(win, bird, pipes, base, controller.score)
    
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()