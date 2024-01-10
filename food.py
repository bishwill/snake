from block import Block
import random


class Food:

    def __init__(self, dimensions: tuple, block_width: int) -> None:
        self.dimensions = dimensions
        self.block_width = block_width
        self.food = None
        self.generate_food()


    def generate_food(self):

        x = round((random.randint(0, self.dimensions[0] - self.block_width) / self.block_width)) * self.block_width
        y = round((random.randint(0, self.dimensions[1] - self.block_width) / self.block_width)) * self.block_width

        self.food = Block(x, y, self.block_width, dimensions=self.dimensions)