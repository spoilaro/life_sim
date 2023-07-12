from sim.creature import Creature
import math


class Herbivore(Creature):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

        self.type = "herbivore"

    def update(self, creatures):
        closest = None
        min_dist = 9999

        for c in creatures:
            if id(c) != id(self) and c.type != "herbivore":
                x = c.physics.position[0] - self.physics.position[0]
                y = c.physics.position[1] - self.physics.position[1]

                dist = math.sqrt(x**2 + y**2)

                if dist < min_dist:
                    min_dist = dist
                    closest = c

        # Give acceleration towards the closest
        if closest.physics.position[0] > self.physics.position[0]:
            self.physics.acceleration[0] -= 1
        elif closest.physics.position[0] < self.physics.position[0]:
            self.physics.acceleration[0] += 1

        if closest.physics.position[1] > self.physics.position[1]:
            self.physics.acceleration[1] -= 1
        elif closest.physics.position[1] < self.physics.position[1]:
            self.physics.acceleration[1] += 1

        self._move()
