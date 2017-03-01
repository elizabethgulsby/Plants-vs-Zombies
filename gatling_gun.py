import pygame;
from pygame.sprite import Sprite;
from plant import Plant;

class Gatling_Gun(Plant):
	def __init__(self, screen, square):
		self.shoot_speed = 4;
		self.health = 7;
		self.image_file = './images/Gatling_Pea_Fixed.png';
		self.screen = screen;
		self.square = square;
		
		super(Gatling_Gun, self).__init__();

