import pygame
from food import Food
from block import Block



class Snake:

    def __init__(self, start_x: int, start_y: int, block_size: tuple, dimensions: tuple):
        self.block_size = block_size
        self.dimensions = dimensions
        self.body = [Block(start_x, start_y, block_size, self.dimensions)]

    def __len__(self):
        return len(self.body)

    def get_tail_position(self):
        return (self.body[-1].rectangle.x, self.body[-1].rectangle.y)

    def check_food(self, food: Food, key: str):
        head = self.body[0]
        if head.rectangle.x == food.food.rectangle.x and head.rectangle.y == food.food.rectangle.y:
            self.consume_food(food, key)


    def consume_food(self, food: Food, last_key: str) -> None:
        food.generate_food()
        tail_position_x, tail_position_y = self.get_tail_position()
        tail_block = Block(tail_position_x, tail_position_y, self.block_size, self.dimensions)
        tail_block.update(last_key)
        self.body.append(tail_block)


    def draw(self, screen):
        for block in self.body:
            pygame.draw.rect(screen, "white", block.rectangle)


    def update(self, key: str, food: Food):
        new_block_x = self.body[0].rectangle.x
        new_block_y = self.body[0].rectangle.y
        new_block = Block(new_block_x, new_block_y, self.block_size, self.dimensions)
        new_block.update(key)
        self.body.pop(-1)
        self.body.insert(0, new_block)

        self.check_food(food, key)



    def check_death(self):
        return len(self.body) > len(set(self.body))

       





if __name__ == "__main__":
    snake = Snake(100, 100, 1, (1, 1))

    snake.body = [Block(100, 100, 10, (1,1)), Block(101, 100, 10, (1,1)), Block(100, 100, 10, (1,1))]




    print(set(snake.body))


