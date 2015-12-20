# projectile.py

"""projectile.py provides the class for modeling the flight of
a projectile."""

from math import pi, sin, cos
from time import sleep


class Projectile:
    """Simulates the flight of a projectile without wind resistance.
    Tracking is done in 2 dimensions: x and y."""

    def __init__(self, angle, velocity, height):
        """Initialize the projectile with input angle, velocity, and height."""
        self.xpos = 0.0
        self.ypos = height
        theta = pi * angle / 180.0
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self, time):
		"""Updates the state of the projectile at input time interval."""
		self.xpos = self.xpos + time * self.xvel
		yvel1 = self.yvel - 9.8 * time
		self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
		self.yvel = yvel1

    def getY(self):
        """Returns the y position (height) of the projectile."""
        return self.ypos

    def getX(self):
        """Returns the x position (distance) of the projectile."""
        return self.xpos
