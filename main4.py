import pygame

# Initialize pygame
pygame.init()

# Set screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set title and font
pygame.display.set_caption("Simple Pygame Screen")
font = pygame.font.Font(None, 36)  # Default font with size 36

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Main loop
running = True
while running:
    # Fill screen with white background
    screen.fill(WHITE)
    
    # Draw a blue rectangle (x, y, width, height)
    pygame.draw.rect(screen, BLUE, (300, 200, 200, 100))
    
    # Render text
    text_surface = font.render("Hello, Pygame!", True, RED)
    screen.blit(text_surface, (320, 180))  # Display text at given position
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit loop when window is closed

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
