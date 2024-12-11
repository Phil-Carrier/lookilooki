import pygame
import sys
import math
pygame.init()

screen_wdt = 800
screen_hgt = 600
screen = pygame.display.set_mode((screen_wdt, screen_hgt))
pygame.display.set_caption("lookilooki")
pygame.display.set_icon (pygame.image.load("icon.png"))
WHITE = (255, 255, 255)

lookImg_original = pygame.image.load("Person_run1.png")
lookImg_original = pygame.transform.scale_by(lookImg_original, 5)
look_width, look_height = lookImg_original.get_size()
lookX = 100
lookY = -50

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the mouse position
    mouseX, mouseY = pygame.mouse.get_pos()

    # Calculate the angle between the image center and the mouse position
    deltaX = mouseX - (lookX + look_width // 2)
    deltaY = mouseY - (lookY + look_height // 2)
    angle = math.degrees((math.atan2(-deltaY, deltaX)) + 0.15)  # Negate deltaY to match screen coordinates

    # Rotate the image
    rotatedImg = pygame.transform.rotate(lookImg_original, angle)
    rotated_rect = rotatedImg.get_rect(center=(lookX + look_width // 2, lookY + look_height // 2))

    # Clear screen
    screen.fill(WHITE)

    # Draw the rotated image
    screen.blit(rotatedImg, rotated_rect.topleft)

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()