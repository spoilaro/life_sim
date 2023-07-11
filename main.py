import pygame
from random import randint, choice
from enum import Enum
import math

PIXEL_SIZE = 4
PIXEL = (PIXEL_SIZE, PIXEL_SIZE)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Direction(Enum):
    UP = 0,
    DOWN = 1,
    LEFT = 2,
    RIGHT = 3


class Creature():
    def __init__(self, x, y, color):

        # Creature Logic
        self.cycles = 0

        # Core location
        self.core = (x, y)
        self.cells = [self.core]
        self.color = color

        # Traits
        self.traits = []

        self.range = randint(1, 3)

    def update(self, creatures):
        """
        Update the creature every cycle
        Args:
            - creatures: a list of creatures from the World
        """

        self.cycles += 1

        self._move()

    def draw(self, screen):

        for cell in self.cells:
            surf = pygame.Surface(PIXEL)
            surf.fill(self.color)
            # screen.blit(surf, (self.core[0], self.core[1]))
            screen.blit(surf, (cell[0], cell[1]))

    def _move(self):

        dir = choice(list(Direction))
        new_cells = []

        for cell in self.cells:

            x = cell[0]
            y = cell[1]

            match dir:
                case Direction.UP:
                    y -= self.range
                case Direction.DOWN:
                    y += self.range
                case Direction.RIGHT:
                    x += self.range
                case Direction.LEFT:
                    x -= self.range

            new_cell = self._fit_boundries(x, y)
            new_cells.append(new_cell)
        self.cells = new_cells

    def _fit_boundries(self, x, y):
        if x > 400:
            x = 0
        if y > 400:
            y = 0

        if x < 0:
            x = 400
        if y < 0:
            y = 400
        return (x, y)


class Herbivore(Creature):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)


class Carnivore(Creature):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)


class World():
    def __init__(self):
        self.creatures = []
        self._init_pops()

    def _init_pops(self):
        pop_count = 100

        for i in range(pop_count):
            while True:
                x = randint(10, 390)
                y = randint(10, 390)
                if not self._check_collision(x, y):
                    c = Herbivore(x, y, GREEN)
                    self.creatures.append(c)
                    break
        for i in range(pop_count):
            while True:
                x = randint(10, 390)
                y = randint(10, 390)
                if not self._check_collision(x, y):
                    c = Carnivore(x, y, RED)
                    self.creatures.append(c)
                    break

        print(f"{pop_count} creatures initialized")

    def _check_collision(self, x, y):
        for c in self.creatures:
            if c.core[0] == x and c.core[1] == y:
                return True
        return False

    def draw(self, screen):
        for c in self.creatures:
            c.draw(screen)

    def update(self):
        """
        Updates all the creatures
        """
        for c in self.creatures:
            c.update(self.creatures)


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((400, 400))
    world = World()

    running = True
    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                running = False
        screen.fill((0, 0, 0))
        world.update()
        world.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
