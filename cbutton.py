# cbutton.py
# A class that will construct circular buttons for use in graphical programs
# using the library "graphics.py".

from graphics import *
from math import sqrt


class CButton:
    """This class will construct interactive buttons that are round in shape.
    It allows the user to click them, automatically activate and deactivate, and
    return a value for being clicked."""

    def __init__(self, win, position, radius, label):
		self.radius = radius
		self.position = position
		self.x, self.y = position.getX(), position.getY()
		self.circ = Circle(Point(self.x, self.y), self.radius)
		self.circ.setFill("lightgray")
		self.circ.draw(win)
		self.label = Text(position, label)
		self.label.draw(win)
		self.deactivate()

    def clicked(self, p):
        """Returns True if the button is clicked while it is active and if the click
        is inside the parameters of the button."""
        return self.active and sqrt((p.getX() - self.position.getX())**2 + (p.getY() - self.position.getY())**2) <= self.radius

    def activate(self):
        """Activates the button and indicates it is usable by turning the text black and
        making the border 2 pixels thick."""
        self.label.setFill("black")
        self.circ.setWidth(2)
        self.active = True

    def deactivate(self):
        """Deactivates the button to prevent clicking. This is visually indicated by
        changing the label to "darkgrey" and making the border 1 pixel."""
        self.label.setFill("darkgrey")
        self.circ.setWidth(1)
        self.active = False

    def getLabel(self):
        """Retrieves the label of the button as a string."""
        return self.label.getText()
