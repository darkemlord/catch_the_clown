import pygame as pg
import random

# Initialize hame
pg.init()

# Display surface
WINDOW_HEIGHT = 945
WINDOW_WIDTH = 600
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Game speed
FPS = 60
clock = pg.time.Clock()

# Load Game values

PLAYER_STARTING_LIVES = 5
CLOWN_STARTING_VELOCITY = 5
CLOWN_ACCELERATION = 1

score = 0
player_lives = PLAYER_STARTING_LIVES
clown_velocity = CLOWN_STARTING_VELOCITY
clown_dx = random.choice([-1, 1])
clown_dy = random.choice([-1, 1])

# Set Colors
BLACK = (0, 0, 0)
BLUE = (1, 175, 209)
YELLOW = (248, 231, 28)
# Set text and fonts

# Characters Images
clown_image = pg.image.load("./assets/clown.png")
clown_rect = clown_image.get_rect()
clown_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Main Game loop
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Fill surface and remove duplicated images
    display_surface.fill(BLACK)

    # Display characters
    display_surface.blit(clown_image, clown_rect)
    # Update display
    pg.display.update()


pg.quit()
