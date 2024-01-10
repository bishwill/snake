import pygame

class KeyQueue:
    def __init__(self) -> None:
        self.queue = []
        self.last_key = "w"

    def __repr__(self) -> str:
        return str(self.queue)

    def produce(self, keys: pygame.key.ScancodeWrapper) -> None:

        if keys[pygame.K_w]:
            self.queue.append("w")
        if keys[pygame.K_s]:
            self.queue.append("s")
        if keys[pygame.K_a]:
            self.queue.append("a")
        if keys[pygame.K_d]:
            self.queue.append("d")

    def consume(self) -> str:
        if self.queue:
            self.last_key = self.queue.pop(0)
        return self.last_key
    


