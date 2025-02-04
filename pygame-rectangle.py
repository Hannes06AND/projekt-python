"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
rect_x = 50
rect_y = 50

pad1_x = 5
pad1_y = 50

pad2_x = 5
pad2_y = 50

rect_change_x = 10
rect_change_y = 10
x_speed = 0
y_speed = 0
 
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
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
    
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
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
 
    # --- Drawing code should go here
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, GREEN, [rect_x + 10, rect_y + 10 ,30, 30])
    # --- Drawing code for pads
    pygame.draw.rect(screen, RED, [pad1_x, pad2_y, 5, 100])
    pygame.draw.rect(screen, RED, [pad2_x, pad2_y, 5, 100])
    #rect_x += rect_change_x
    #rect_y += rect_change_y

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    if rect_y > 450 or rect_y < 0:
        y_speed = y_speed * -1
    if rect_x > 650 or rect_x < 0:
        x_speed = x_speed * -1
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
