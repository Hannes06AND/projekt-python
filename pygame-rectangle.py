"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Reverse Pong")
 
# Loop until the user clicks the close button.
done = False

# Add visual elements to the game
font = pygame.font.Font(None, 36)
text = font.render('Game Over!', True, BLACK, WHITE)
textRect = text.get_rect()
textRect.center = (700 // 2, 500 // 2)
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
rect_x = 50
rect_y = 50

pad1_x = 5
pad1_y = 250

y_pad1_speed = 3
y_pad2_speed = -3

pad2_x = 695
pad2_y = 250

rect_change_x = 10
rect_change_y = 10
x_speed = 2
y_speed = 2
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
        # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -math.fabs(x_speed)
            elif event.key == pygame.K_RIGHT:
                x_speed = math.fabs(x_speed)
            elif event.key == pygame.K_UP:
                y_speed = -math.fabs(y_speed)
            elif event.key == pygame.K_DOWN:
                y_speed = math.fabs(y_speed)
    
        # User let up on a key
        '''elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0'''
    
    # Move the object according to the speed vector.
    rect_x += x_speed
    rect_y += y_speed
 
    pad1_y += y_pad1_speed
    pad2_y += y_pad2_speed

    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
 
    # --- Drawing code should go here
    rectangle = pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, GREEN, [rect_x + 10, rect_y + 10 ,30, 30])
    pad1 = pygame.draw.rect(screen, RED, [pad1_x, pad1_y, 5, 100])
    pad2 = pygame.draw.rect(screen, RED, [pad2_x, pad2_y, 5, 100])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    '''if rect_y > 450 or rect_y < 0:
        y_speed = y_speed * -1
    if rect_x > 650 or rect_x < 0:
        x_speed = x_speed * -1'''
    
    if rect_x > 650 or rect_x < 0:
        # Game over
         screen.blit(text, textRect)
         pygame.display.flip()
         done = True

    if pad1_y > 450 or pad1_y < 0:
       y_pad1_speed = y_pad1_speed * -1 
    
    if pad2_y > 450 or pad2_y < 0:
        y_pad2_speed = y_pad2_speed * -1

    # Studsar av botten eller taket
    if rect_y <= 0 or rect_y >= 450:
        y_speed *= -1

    # Studsar från pads
    if rectangle.colliderect(pad1) or rectangle.colliderect(pad2):
        x_speed *= -1.05
        y_speed *= 1.05

    # --- Limit to 60 frames per second
    clock.tick(60)
 
done = False
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
# Close the window and quit.
pygame.quit()