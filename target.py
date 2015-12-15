# target.py

"""Imports randrange to set random x and y positions for the target."""
from random import randrange
from graphics import *
from math import sqrt

class Target:
	"""Creates a target to be hit by the projectile or other object in the
	cannonball program."""
	
	def __init__(self,window):
		x,y = randrange(100,681), randrange(1,650)
		self.center = Point(x,y)
		tout = Circle(self.center,30)
		tout.setFill("red")
		tout.setOutline("red")
		tmid = Circle(self.center,20)
		tmid.setFill("white")
		tmid.setOutline("white")
		tin = Circle(self.center,10)
		tin.setFill("red")
		tin.setOutline("red")
		tout.draw(window)
		tmid.draw(window)
		tin.draw(window)
		
	def Hit(self,object):
		return sqrt((object.getX() - self.center.getX())**2 + (object.getY() - self.center.getY())**2) <= 40