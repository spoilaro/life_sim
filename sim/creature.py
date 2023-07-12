import pygame

from sim import Physics, Direction
from random import randint, choice

from sim import PIXEL


class Creature():
    def __init__(self, x, y, color):

        # Creature Logic
        self.cycles = 0

        self.physics = Physics(
            velocity=[0, 0],
            acceleration=[0, 0],
            position=[x, y],

        )
        self.cells = [self.physics.position]
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

    def draw_multiple(self, screen):

        for cell in self.cells:
            surf = pygame.Surface(PIXEL)
            surf.fill(self.color)
            # screen.blit(surf, (self.core[0], self.core[1]))
            screen.blit(surf, (cell[0], cell[1]))

    def draw(self, screen):

        pos = self.physics.position
        surf = pygame.Surface(PIXEL)
        surf.fill(self.color)
        # screen.blit(surf, (self.core[0], self.core[1]))
        screen.blit(surf, (pos[0], pos[1]))

    def _move_multiple(self):

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

    def _move(self):

        acc = self.physics.acceleration
        vel = self.physics.velocity
        pos = self.physics.position

        x = pos[0] + (vel[0] + acc[0])
        y = pos[1] + (vel[1] + acc[1])

        self.physics.position = self._fit_boundries(x, y)

        self.physics.acceleration = [0, 0]

    def _fit_boundries(self, x, y):
        if x > 400:
            x = 0
        if y > 400:
            y = 0

        if x < 0:
            x = 400
        if y < 0:
            y = 400
        return [x, y]
