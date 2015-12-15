# tracker.py

from graphics import *

class Tracker:
	"""This class will create a visual element to track an object on the screen
	as a visual representation in a window."""
	
	def __init__(self,window,objToTrack):
		self.cball = Circle(Point(objToTrack.getX(),objToTrack.getY()),10)
		self.cball.setFill("grey")
		self.cball.setWidth(2)
		self.cball.draw(window)
		
	def update(self,window,objToTrack):
		self.cball.undraw()
		self.cball = Circle(Point(objToTrack.getX(),objToTrack.getY()),10)
		self.cball.setFill("grey")
		self.cball.setWidth(2)
		self.cball.draw(window)