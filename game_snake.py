import pygame
import random

# initialize pygame
pygame.init()

# set up the window
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake')

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = ()
RED = ()

# score
score = 0

# font
font = pygame.font.Font(None, 36)

# game settings
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH / GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT / GRID_SIZE

# direction constants
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# snake starting position and direction
snake_position = [100, 100]
snake_body = [[100, 100], [90, 100], [80, 100]]
snake_direction = RIGHT

# food starting position
food_position = [random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE]
food_spawned = True

# initialize game clock
clock = pygame.time.Clock()

# game loop
while True:
    # get user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != DOWN:
                snake_direction = UP
            if event.key == pygame.K_DOWN and snake_direction != UP:
                snake_direction = DOWN
            if event.key == pygame.K_LEFT and snake_direction != RIGHT:
                snake_direction = LEFT
            if event.key == pygame.K_RIGHT and snake_direction != LEFT:
                snake_direction = RIGHT

    # check if snake has collided with the borders
    if snake_position[0] >= SCREEN_WIDTH or snake_position[0] < 0 or snake_position[1] >= SCREEN_HEIGHT or snake_position[1] < 0:
        print(f"GAME OVER!\nYOU CAN'T TOUCH THE BORDERS\nYOUR SCORE: {score}")
        pygame.quit()
        quit()

    # check if snake has collided with itself
    for segment in snake_body[1:]:
        if snake_position[0] == segment[0] and snake_position[1] == segment[1]:
            print(f"GAME OVER!\nYOU ATE YOURSELF\nYOUR SCORE: {score}")
            pygame.quit()
            quit()

    # spawn food
    if not food_spawned:
        food_position = [random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE]
        food_spawned = True

    # check if snake has eaten food
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        food_spawned = False
        snake_body.insert(0, list(snake_position))
        score += 1
        

    # move snake
    for i in range(len(snake_body) - 1, 0, -1):
        snake_body[i] = list(snake_body[i - 1])

    snake_position[0] += snake_direction[0] * GRID_SIZE
    snake_position[1] += snake_direction[1] * GRID_SIZE
    snake_body[0] = snake_position

    # draw background
    screen.fill(BLACK)

    # draw snake
    for position in snake_body:
        pygame.draw.rect(screen, WHITE, pygame.Rect(position[0], position[1], GRID_SIZE, GRID_SIZE))

    #draw score
    text = font.render(str(score), True, WHITE, BLACK)
    screen.blit(text, (10, 10))
    
    # draw food
    pygame.draw.rect(screen, WHITE, pygame.Rect(food_position[0], food_position[1], GRID_SIZE, GRID_SIZE))

    # update display
    pygame.display.update()

    # set frame rate
    clock.tick(10)