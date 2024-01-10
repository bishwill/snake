import pygame
import snake
import keyqueue
import food

DIMENSIONS = (500, 500)
FRAME_RATE = 15
BLOCK_SIZE = 20
START_X = round(DIMENSIONS[0] / 2 / BLOCK_SIZE) * BLOCK_SIZE
START_Y = round(DIMENSIONS[1] / 2 / BLOCK_SIZE) * BLOCK_SIZE

assert DIMENSIONS[0] % BLOCK_SIZE == 0
assert DIMENSIONS[1] % BLOCK_SIZE == 0

pygame.init()
screen = pygame.display.set_mode(DIMENSIONS)
clock = pygame.time.Clock()
running = True



snake_instance = snake.Snake(START_X, START_Y, BLOCK_SIZE, DIMENSIONS)
food_instance = food.Food(DIMENSIONS, BLOCK_SIZE)
queue = keyqueue.KeyQueue()



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")


    # Add to key queue
    keys = pygame.key.get_pressed()
    queue.produce(keys)

    # Draw food
    pygame.draw.rect(screen, "green", food_instance.food.rectangle)
    
    # Draw snake
    snake_instance.draw(screen)

    # Update snake
    latest_key = queue.consume()
    snake_instance.update(latest_key, food_instance)

    # Check death
    if snake_instance.check_death():
        screen.fill("red")
        print("dead")



    pygame.display.flip()
    clock.tick(FRAME_RATE) 


pygame.quit()