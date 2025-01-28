import pygame
from bird import Bird
from pipe import Pipe
from base import Base
from variables import WIN_HEIGHT, WIN_WIDTH

class Control:
    def __init__(self, bird, pipes, base, score):
        self.bird = bird
        self.pipes = pipes
        self.base = base
        self.score = score
        self.game_over = False
        self.game_started = False  # New state flag

    def handle_start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            # Handle both button click and spacebar to start
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.check_button_click(pygame.mouse.get_pos()):
                    self.game_started = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game_started = True
        return self.game_started

    def check_button_click(self, mouse_pos):
        # Button dimensions and position
        button_width = 200
        button_height = 50
        button_x = (WIN_WIDTH - button_width) // 2
        button_y = (WIN_HEIGHT - button_height) // 2
        
        # Check if click is within button bounds
        return (button_x <= mouse_pos[0] <= button_x + button_width and 
                button_y <= mouse_pos[1] <= button_y + button_height)