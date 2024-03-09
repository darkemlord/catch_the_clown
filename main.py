import pygame as pg

# Initialize hame
pg.init()

# Display surface
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Game speed
FPS = 60
clock = pg.time.Clock()

# Load Game values

# Set Colors
BLACK = (0, 0, 0)
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
