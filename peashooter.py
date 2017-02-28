import pygame;
from pygame.sprite import Sprite;
from plant import Plant;
# Child class can send up what specifically different about itself relative to the parent class (Plant) - otherwise they're exactly the same

class Peashooter(Plant):
	def __init__(self, screen, square):
		self.shoot_speed = 2;
		self.health = 5;
		self.image_file = './images/peashooter.png';
		self.screen = screen;
		self.square = square; #child is setting this, parent doesn't need to as well.
		
		super(Peashooter, self).__init__();  #sending self up to parent class (Plant) - child will also grab everything parent class has
