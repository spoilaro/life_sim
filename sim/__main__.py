import pygame
from sim.carnivore import Carnivore
from sim.herbivore import Herbivore

from random import randint
from sim import GREEN, RED


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
            if c.physics.position[0] == x and c.physics.position[1] == y:
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
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                running = False
        screen.fill((0, 0, 0))
        world.update()
        world.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
