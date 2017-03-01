import sys;
import pygame;
# Note: background not imported here - we'd have to create the object.  We created the object in main.py instead
from peashooter import Peashooter;
from gatling_gun import Gatling_Gun;
from bullet import Bullet;
from pygame.sprite import groupcollide;

def check_events(screen, game_settings, squares, plants, bullets):
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit();
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos();
				# print mouse_x; 
				# print mouse_y;

				for square in squares:
					if square.rect.collidepoint(mouse_x, mouse_y):
						print "Square: ", square.square_number;
						plants.add(Peashooter(screen, square));

			elif event.type == pygame.MOUSEMOTION:
				# print event.pos will give tuple of mouse location
				for square in squares:
					if square.rect.collidepoint(event.pos):
						game_settings.highlighted_square = square; #single sprite from group of sprites (called squares)
						# print game_settings.highlighted_square

def update_screen(screen, game_settings, background, zombies, squares, plants, bullets, tick):
	screen.blit(background.image, background.rect);


	if game_settings.highlighted_square != 0:
		# params for draw...
		# 1. Where (screen)
		# 2. Color (tuple in rgb format)
		# 3. Coords (tuple: left, top, width, height)
		# 4. Radius in px
		pygame.draw.rect(screen, (255, 215, 0), (game_settings.highlighted_square.rect.left, game_settings.highlighted_square.rect.top, game_settings.squares['square_width'], game_settings.squares['square_height']), 5);

	# draw zombies
	for zombie in zombies.sprites():
		zombie.update_me();
		zombie.draw_me();
		if zombie.rect.left <= zombie.screen_rect.left:
			game_settings.game_active = False;

	# draw plants when clicked (when a plant was added to plants), needs to know if there's a zombie in the row
	for plant in plants:
		plant.draw_me();
		# print plant.yard_row;
		if tick % 20 == 0:
			if game_settings.zombie_in_row[plant.yard_row] > 0:  #checks to see if there's > 0 zombies in the row
				bullets.add(Bullet(screen, plant));

	# draw the bullets - needs to know which row it's in
	for bullet in bullets.sprites():
		bullet.update_me();
		bullet.draw_me();
		# if bullet reaches the current width of screen, remove it from bullets list
		if bullet.rect.centerx > game_settings.screen_size:
			bullet.pop(bullet)
		


	
