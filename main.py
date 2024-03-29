import pygame as pg
import random

# Initialize hame
pg.init()

# Display surface
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
display_surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Catch the Clown")

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

# Set fonts
font = pg.font.Font("./assets/Franxurter.ttf")

# Set text

title_text = font.render("Catch the Clown", True, BLUE)
title_rect = title_text.get_rect()
title_rect.topleft = (50, 10)

score_text = font.render("Score: " + str(score), True, YELLOW)
score_rect = score_text.get_rect()
score_rect.topright = (WINDOW_WIDTH - 50, 10)

lives_text = font.render("Lives: " + str(player_lives), True, YELLOW)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 50, 50)

game_over_text = font.render("Game Over", True, BLUE, YELLOW)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

continue_text = font.render("Click anywhere and play again ", True, YELLOW, BLUE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 64)

# Set sound music

click_sound = pg.mixer.Sound("./assets/click_sound.wav")
miss_sound = pg.mixer.Sound("./assets/miss_sound.wav")
pg.mixer.music.load("./assets/ctc_background_music.wav")

# Characters Images
background_image = pg.image.load("./assets/background.png")
background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)

clown_image = pg.image.load("./assets/clown.png")
clown_rect = clown_image.get_rect()
clown_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)


# Main Game loop
pg.mixer.music.play(-1, 0.0)
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # Check if the click was made
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            # The clown was clicked
            if clown_rect.collidepoint(mouse_x, mouse_y):
                click_sound.play()
                score += 1
                clown_velocity += CLOWN_ACCELERATION
                # Move the clown in a new direction
                previous_dx = clown_dx
                previous_dy = clown_dy
                while previous_dx == clown_dx and previous_dy == clown_dy:
                    clown_dx = random.choice([-1, 1])
                    clown_dy = random.choice([-1, 1])
            # We missed the clown
            else:
                miss_sound.play()
                player_lives -= 1

    # Move the clown
    clown_rect.x += clown_dx * clown_velocity
    clown_rect.y += clown_dy * clown_velocity

    # Bounce the clown off edges of the display
    if clown_rect.left <= 0 or clown_rect.right >= WINDOW_WIDTH:
        clown_dx = -1 * clown_dx
    if clown_rect.top <= 0 or clown_rect.bottom >= WINDOW_HEIGHT:
        clown_dy = -1 * clown_dy

    # Update HUD
    score_text = font.render("Score: " + str(score), True, YELLOW)
    lives_text = font.render("Lives: " + str(player_lives), True, YELLOW)

    # Check game over
    if player_lives == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pg.display.update()

        # Pause until the player clicks then reset game
        pg.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pg.event.get():
                # the player wants to play again
                if event.type == pg.MOUSEBUTTONDOWN:
                    score = 0
                    player_lives = PLAYER_STARTING_LIVES

                    clown_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
                    clown_velocity = CLOWN_STARTING_VELOCITY
                    clown_dx = random.choice([-1, 1])
                    clown_dy = random.choice([-1, 1])

                    pg.mixer.music.play(-1, 0.0)
                    is_paused = False
                if event.type == pg.QUIT:
                    is_paused = False
                    running = False

    # Fill surface and remove duplicated images background
    display_surface.blit(background_image, background_rect)

    # Display Text
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)
    # Display characters
    display_surface.blit(clown_image, clown_rect)
    # Update display
    pg.display.update()
    clock.tick(FPS)

pg.quit()
