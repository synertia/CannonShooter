# vcball.py
# A program to visually track the path of a cannonball fired with user input
# velocity and angles.

from projectile import Projectile
from tracker import Tracker
from graphics import *
from time import sleep
from cbutton import CButton
from target import Target

def main():
	# Draw the window to simulate green field and sky.
	
	win = GraphWin("Shoot a Cannon!", 850,850)
	win.setCoords(0,-50,700,700)
	win.setBackground("lightblue")
	ground = Rectangle(Point(0,-100),Point(700,0))
	ground.setFill("green")
	cloud1 = Oval(Point(153,420),Point(390,580))
	cloud1.setFill("white")
	cloud1.setWidth(2)
	cloud2 = Oval(Point(23,232),Point(230,400))
	cloud2.setFill("white")
	cloud2.setWidth(2)
	cloud3 = Oval(Point(434,370),Point(610,520))
	cloud3.setFill("white")
	cloud3.setWidth(2)
	tangle = Text(Point(30,680), "     Angle: ")
	tvel = Text(Point(30,650), "Velocity:")
	anginp = Entry(Point(70,680),3)
	velinp = Entry(Point(70,650),3)
	fbutton = CButton(win,Point(55,590),30,"FIRE!")
	fbutton.activate()
	quitbutton = CButton(win,Point(630,660),30,"Quit")
	ground.draw(win)
	cloud1.draw(win)
	cloud2.draw(win)
	cloud3.draw(win)
	tangle.draw(win)
	tvel.draw(win)
	anginp.draw(win)
	anginp.setText("0")
	velinp.setText("0")
	velinp.draw(win)
	target = Target(win)
	
	
	
	
	
	pt = win.getMouse()
	shots = 0
	while not quitbutton.clicked(pt):
		try:
			if fbutton.clicked(pt):
			
				ang = float(anginp.getText())
				vel = float(velinp.getText())
				
				shot = Projectile(ang,vel,0)
				ball = Tracker(win,shot)
				
				
				
					
				
				while shot.getY() >= 0 and target.Hit(shot) == False:
					sleep(.025)
					shot.update(.1)
					ball.update(win,shot)
					target.Hit(shot)
					
					
					if target.Hit(shot) == True:
						shots += 1
						wintxt = Text(Point(325,500), "You Hit the Target in %d shot(s)!" % shots)
						wintxt.setSize(36)
						wintxt.setTextColor("red")
						wintxt.draw(win)
						exit
					
				shots += 1
		except ValueError:
			exit
			
			
		quitbutton.activate()
		pt = win.getMouse()
		
		
			
		
		
main()