import pygame as pg

# Initialize the game
pg.init()

# Set up display
width, height = 800, 600
window = pg.display.set_mode((width, height))
pg.display.set_caption("Pygame Beispiel")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

# Main game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Fill the background with white
    window.fill(white)

    # Draw a blue rectangle
    pg.draw.rect(window, blue, (width // 2 - 50, height // 2 - 50, 100, 100))

    # Update the display
    pg.display.flip()

# Quit the game
pg.quit()



