import pygame;

class Settings():
	def __init__(self):
		# Set the screen size dynamically
		display_info = pygame.display.Info();
		self.screen_size = (display_info.current_w, display_info.current_h);
		self.bg_color = (82,111,53);
		self.zombie_speed = 5;
		self.zombie_health = 5;
		self.game_active = True;

		# square stuff - starting pos is determined by where mouse button clicked (pygame.mouse.gete_pos() in game_functions)
		self.squares = {
			"start_left": 367,
			"start_top": 245,
			"square_width": 110,
			"square_height": 105,
			"rows": [
				245, 
				350,
				455,
				560,
				665
			]
		};
		self.highlighted_square = 0;
		self.zombie_in_row = [  #initialized with no zombies in rows - this index will be updated as the game starts (at each index) - entire game becomes aware of zombie in row (set to an integer)
			0,
			0,
			0,
			0,
			0
		]


