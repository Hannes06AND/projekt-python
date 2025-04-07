'''
Maze Game
Loaded from a file.

Tasks:
7. Add score to the game. Show the score on the screen.
8. When all objects are picked up, show a message on the screen.

Extra tasks:
1. Show the doors in the maze.
'''
import pygame
import random


# --- Define helper functions
def get_one_colliding_object(object_1, objects):
    '''Returns the first object in the list of objects
    that collides with object_1.
    Returns None if no object collides.'''
    for object_2 in objects:
        obj_1_rect = pygame.Rect(object_1['x'], object_1['y'], object_1['image'].get_width(), object_1['image'].get_height())
        obj_2_rect = pygame.Rect(object_2['x'], object_2['y'], object_2['image'].get_width(), object_2['image'].get_height())
        if obj_1_rect.colliderect(obj_2_rect):
            return object_2
    return None

def check_item_collision():
    """Tar bort objekt från listan om spelaren plockar upp det."""
    global items
    items = [item for item in items if not get_one_colliding_object(player, [item])]

# --- Initialize Pygame
pygame.init()

# --- Add elements to the game.
# load graphics
sand_image = pygame.image.load("img/floor_sand_stone_0.png")
wall_image = pygame.image.load("img/brick_brown_0.png")
#door "img/open_door.png"
player_image = pygame.image.load("img/deep_elf_knight_old.png")
item_image = pygame.image.load("img/crystal_wall_lightmagenta.png")

# Add visual elements to the game
wall_size = wall_image.get_width()
walls = []

# Create the player
player = {}
player['image'] = player_image
player['speed'] = 4

# Skapa monster
monster_image = pygame.image.load("img/ogre_old.png")
monsters = []

# Lägga till dörrar
door_image = pygame.image.load("img/open_door.png")
doors = []

# Lista för objekt som kan plockas upp
items = []

# Read the maze from the file.
file = open('maze.txt', 'r')
line = file.readline()
maze_width = len(line) - 1  # Do not count the newline character.
maze_height = 0
x = 0
y = 0
while len(line) > 1:
    maze_height += 1
    for char in line:
        if char == 'x':
            wall = {}
            wall['x'] = x
            wall['y'] = y
            wall['image'] = wall_image
            walls.append(wall)
        elif char == 'p':
            player['x'] = x
            player['y'] = y
            print(player)
        elif char == 'd': # 'd' för dörrar
            door = {'x': x, 'y': y, 'image': door_image}
            doors.append(door)
        elif char == 'm':  # 'm' för monster
            monsters.append({
                'x': x,
                'y': y,
                'image': monster_image,
                'direction': random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)]),
                'speed': 3
        })
        elif char == 'o':  # 'o' representerar objekt eller kristaller i filen
            item = {'x': x, 'y': y, 'image': item_image}
            items.append(item)

        x += wall_size
    x = 0
    y += wall_size
    line = file.readline()

file.close()

# --- Set the width and height of the screen [width, height]
size = (maze_width * wall_size, maze_height * wall_size)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Maze Game")

# Cooldown för teleportering
teleport_cooldown = 0  # Hur lång tid kvar tills teleport tillåts igen
cooldown_duration = 30  # Frames

# --- Game time
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
is_running = True
while is_running:
    # --- Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    # --- Game logic should go here
    # --- Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player['x'] -= player['speed']
        if get_one_colliding_object(player, walls):
            player['x'] += player['speed']
    
    if keys[pygame.K_RIGHT]:
        player['x'] += player['speed']
        if get_one_colliding_object(player, walls):
            player['x'] -= player['speed']

    if keys[pygame.K_UP]:
        player['y'] -= player['speed']
        if get_one_colliding_object(player, walls):
            player['y'] += player['speed']

    if keys[pygame.K_DOWN]:  
        player['y'] += player['speed']
        if get_one_colliding_object(player, walls):
            player['y'] -= player['speed']
    
    '''else:
        # snap player to grid
        player['x'] = round(player['x'] / wall_size) * wall_size
        player['y'] = round(player['y'] / wall_size) * wall_size'''

    if teleport_cooldown > 0:
        teleport_cooldown -= 1

    # Rörelse för monster
    for monster in monsters:
        if random.random() < 0.02:
            monster['direction'] = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])

        monster['x'] += monster['direction'][0] * monster['speed']
        monster['y'] += monster['direction'][1] * monster['speed']

        if get_one_colliding_object(monster, walls):
            monster['x'] -= monster['direction'][0] * monster['speed']
            monster['y'] -= monster['direction'][1] * monster['speed']
            monster['direction'] = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
            
        if get_one_colliding_object(player, [monster]):
            print("Game Over!")
            is_running = False

    check_item_collision()

    # Kolla om spelaren kolliderar med en dörr och teleportera till den andra
    if teleport_cooldown == 0:
        colliding_door = get_one_colliding_object(player, doors)
        if colliding_door:
            for other_door in doors:
                if other_door != colliding_door:
                    player['x'] = other_door['x']
                    player['y'] = other_door['y']
                    teleport_cooldown = cooldown_duration
                    break

    # --- Screen-clearing code goes here
    # fill widh sand
    for y in range(0, size[1], wall_size):
        for x in range(0, size[0], wall_size):
            screen.blit(sand_image, (x, y))
    # --- Drawing code should go here
    for wall in walls:
        screen.blit(wall_image, (wall['x'], wall['y']))

    # Rita ut objekten
    for item in items:
        screen.blit(item['image'], (item['x'], item['y']))

    # Rita monster
    for monster in monsters:
        screen.blit(monster['image'], (monster['x'], monster['y']))
    
    # Rita dörrar
    for door in doors:
        screen.blit(door['image'], (door['x'], door['y']))

    screen.blit(player_image, [player['x'], player['y']])
    pygame.display.update()  # or pygame.display.flip()
    # --- Increase game time
    clock.tick(60)  # 60 frames per second

# Clean up when the game exits.
pygame.quit()