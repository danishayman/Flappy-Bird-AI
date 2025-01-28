import pygame
pygame.font.init()
from bird import Bird
from pipe import Pipe
from base import Base
from variables import WIN_WIDTH, WIN_HEIGHT, BG_IMG, STAT_FONT
from control import Control

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
    
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(30)
        
        controller.handle_events()
        game_over = controller.update_game_state()
        
        if game_over:
            # Optional: Add game over screen or delay before quitting
            run = False
        
        draw_window(win, bird, pipes, base, controller.score)
    
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()