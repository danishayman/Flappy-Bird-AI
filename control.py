import pygame
from pipe import Pipe




class Control:
    def __init__(self, bird, pipes, base, score):
        self.bird = bird
        self.pipes = pipes
        self.base = base
        self.score = score
        self.game_over = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not self.game_over:
                    self.bird.jump()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not self.game_over:
                    self.bird.jump()

    def update_game_state(self):
        if self.game_over:
            return self.game_over

        self.bird.move()
        add_pipe = False
        remove_pipes = []

        for pipe in self.pipes:
            pipe.move()
            if pipe.collide(self.bird):
                self.game_over = True

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                remove_pipes.append(pipe)

            if not pipe.passed and pipe.x < self.bird.x:
                pipe.passed = True
                add_pipe = True

        if add_pipe:
            self.score += 1
            self.pipes.append(Pipe(600))

        for pipe in remove_pipes:
            self.pipes.remove(pipe)

        if self.bird.y + self.bird.img.get_height() >= self.base.y or self.bird.y < 0:
            self.game_over = True

        self.base.move()
        return self.game_over