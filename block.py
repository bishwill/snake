import pygame

class Block:

    def __init__(self, x: int, y: int, width: int, dimensions: tuple) -> None:
        self.width = width
        self.dimensions = dimensions
        self.rectangle = pygame.Rect(x, y, width, width)
        

    def __repr__(self):
         return str(self.rectangle)
    

    def __eq__(self, value) -> bool:
         if not isinstance(value, self.__class__):
              return False
         
         return self.rectangle.x == value.rectangle.x and self.rectangle.y == value.rectangle.y

    def __hash__(self) -> int:
         return hash((self.rectangle.x, self.rectangle.y))


    def update(self, key: str):


        dy, dx = (0, 0)

        if key == "w":
            dy = self.width
        elif key == "s":
            dy = -self.width
        elif key == "d":
            dx = self.width
        elif key == "a":
            dx = -self.width
        else:
            raise KeyError(f"invalid key entered: {key}")



        self.rectangle.x += dx
        self.rectangle.y -= dy


        # Boundaries
        if self.rectangle.x > self.dimensions[0]:
            self.rectangle.x = 0
        elif self.rectangle.x < 0 - self.width:
            self.rectangle.x = self.dimensions[0]

        if self.rectangle.y > self.dimensions[1]:
                self.rectangle.y = 0
        elif self.rectangle.y < 0 - self.width:
                self.rectangle.y = self.dimensions[1]
    

if __name__ == "__main__":
     print(Block(1, 1, 1, (1, 1)) == Block(1, 2, 1, (1, 1)))