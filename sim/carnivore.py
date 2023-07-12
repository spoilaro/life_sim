from sim.creature import Creature
import math


class Carnivore(Creature):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

        self.type = "carnivore"

    def _hunt(self, creatures):
        closest = None
        min_dist = 9999

        for c in creatures:
            if id(c) != id(self) and c.type != "carnivore":
                x = c.physics.position[0] - self.physics.position[0]
                y = c.physics.position[1] - self.physics.position[1]

                dist = math.sqrt(x**2 + y**2)

                # Carnivore catches the pray
                if dist <= 4:
                    creatures.remove(c)

                elif dist < min_dist:
                    min_dist = dist
                    closest = c

        # Give acceleration towards the closest
        if closest.physics.position[0] > self.physics.position[0]:
            self.physics.acceleration[0] += 1
        elif closest.physics.position[0] < self.physics.position[0]:
            self.physics.acceleration[0] -= 1

        if closest.physics.position[1] > self.physics.position[1]:
            self.physics.acceleration[1] += 1
        elif closest.physics.position[1] < self.physics.position[1]:
            self.physics.acceleration[1] -= 1

    def update(self, creatures):
        self._hunt(creatures)
        self._move()
