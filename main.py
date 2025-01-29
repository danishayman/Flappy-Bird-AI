import pygame
import os
import neat
pygame.font.init()

from bird import Bird
from pipe import Pipe
from base import Base
from variables import WIN_WIDTH, WIN_HEIGHT, BG_IMG, STAT_FONT, GEN

def draw_window(win, birds, pipes, base, score, gen):
    """
    Draw all game elements on the window
    """
    # Draw background
    win.blit(BG_IMG, (0, 0))
    
    # Draw all pipes
    for pipe in pipes:
        pipe.draw(win)
    
    # Draw score    
    text = STAT_FONT.render("Score: " + str(score), 1, (255,255,255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))
    
    # Draw Generation    
    text = STAT_FONT.render("Gen: " + str(gen), 1, (255,255,255))
    win.blit(text, (10, 50))
    
    # Draw alive birds count
    text = STAT_FONT.render("Alive: " + str(len(birds)), 1, (255,255,255))
    win.blit(text, (10, 10))
    
    # Draw base and birds    
    base.draw(win)
    for bird in birds:
        bird.draw(win)
        
    pygame.display.update()

def main(genomes, config):
    """
    Main game loop function for NEAT training
    """
    global GEN
    GEN += 1
    # Initialize lists to track neural networks, genomes, and birds
    nets = []
    ge = []
    birds = []

    
    # Create neural network for each genome
    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird(230, 350))
        g.fitness = 0
        ge.append(g)
        
    # Initialize game objects    
    base = Base(730)
    pipes = [Pipe(600)]
    score = 0
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(30)  # Set game FPS to 30
        # Handle quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        
        # Determine which pipe to focus on        
        pipe_ind = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_ind = 1
        else:
            run = False
            break
        
        # Move birds and activate neural networks        
        for x, bird in enumerate(birds):
            bird.move()
            ge[x].fitness += 0.1  # Reward birds for staying alive
            
            # Neural network inputs: bird's y position, distance to top pipe, distance to bottom pipe
            output = nets[x].activate((bird.y, abs(bird.y - pipes[pipe_ind].height), abs(bird.y - pipes[pipe_ind].bottom)))
            
            # Make bird jump if network output is > 0.5
            if output[0] > 0.5:
                bird.jump()

        # Handle pipe movement and collision
        add_pipe = False
        remove = []
        for pipe in pipes:
            # Check for collisions with pipes
            for x in reversed(range(len(birds))):
                bird = birds[x]
                if pipe.collide(bird):
                    ge[x].fitness -= 1  # Penalize birds that hit pipes
                    birds.pop(x)
                    nets.pop(x)
                    ge.pop(x)
            
            # Check if birds passed the pipe
            for bird in birds:
                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True
            
            # Remove pipes that are off screen        
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                remove.append(pipe)
                
            pipe.move()
            
        # Add new pipe and increase score
        if add_pipe:
            score += 1
            # Reward birds that pass pipes
            for g in ge:
                g.fitness += 5 
            pipes.append(Pipe(600))
            
        # Remove passed pipes
        for r in remove:
            pipes.remove(r)
            
        # Check for birds hitting boundaries
        for x in reversed(range(len(birds))):
            bird = birds[x]
            if bird.y + bird.img.get_height() >= 730 or bird.y < 0:
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)
            
        # Update base position and draw everything
        base.move()
        draw_window(win, birds, pipes, base, score, GEN)
    
def run(config_path):
    """
    Setup and run the NEAT algorithm
    """
    # Load NEAT configuration
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)
    
    # Create population and add reporters
    population = neat.Population(config)
    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)
    # Run for up to 50 generations
    winner = population.run(main, 50)
    

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)  
    config_path = os.path.join(local_dir, "config_feedforward.txt")
    run(config_path)