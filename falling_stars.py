import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Stars")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Star:
    def __init__(self):
        self.reset()
        self.tail_length = random.randint(5, 15)
        self.tail_color = (
            random.randint(200, 255),
            random.randint(200, 255),
            random.randint(200, 255)
        )
        self.speed = random.uniform(3, 7)
        self.angle = random.uniform(-30, -60)
        self.tail_positions = []

    def reset(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-100, 0)

    def move(self):
        # Convert angle to radians and calculate movement
        rad_angle = math.radians(self.angle)
        self.x += math.cos(rad_angle) * self.speed
        self.y -= math.sin(rad_angle) * self.speed

        # Add current position to tail
        self.tail_positions.append((self.x, self.y))
        
        # Keep only the recent positions for the tail
        if len(self.tail_positions) > self.tail_length:
            self.tail_positions.pop(0)

        # Reset if star goes off screen
        if self.y > HEIGHT or self.x < 0 or self.x > WIDTH:
            self.reset()
            self.tail_positions = []

    def draw(self, screen):
        # Draw tail
        if len(self.tail_positions) > 1:
            for i in range(len(self.tail_positions) - 1):
                alpha = int(255 * (i / len(self.tail_positions)))
                color = (
                    min(255, self.tail_color[0] * alpha // 255),
                    min(255, self.tail_color[1] * alpha // 255),
                    min(255, self.tail_color[2] * alpha // 255)
                )
                pygame.draw.line(screen, color, 
                               self.tail_positions[i],
                               self.tail_positions[i + 1],
                               2)

        # Draw star
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), 2)

# Create stars
stars = [Star() for _ in range(20)]

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Clear screen
    screen.fill(BLACK)

    # Update and draw stars
    for star in stars:
        star.move()
        star.draw(screen)

    # Update display
    pygame.display.flip()
    
    # Control frame rate
    clock.tick(60)

pygame.quit() 