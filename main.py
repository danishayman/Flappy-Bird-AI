import pygame

from bird import Bird
from pipe import Pipe
from base import Base
from variables import WIN_WIDTH, WIN_HEIGHT, BIRD_IMGS, PIPE_IMG, BASE_IMG, BG_IMG





def draw_window(win, bird, pipes, base):
    win.blit(BG_IMG, (0, 0))
    
    for pipe in pipes:
        pipe.draw(win)
        
    base.draw(win)
    bird.draw(win)
    pygame.display.update()





def main():
    bird = Bird(230, 350)
    base = Base(730)
    pipes = [Pipe(600)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # bird.move()
        base.move()
        draw_window(win, bird, pipes, base)
        
                
                
    pygame.quit()
    quit()
    
main()