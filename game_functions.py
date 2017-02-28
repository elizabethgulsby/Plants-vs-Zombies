import sys;
import pygame;
# Note: background not imported here - we'd have to create the object.  We created the object in main.py instead
from peashooter import Peashooter;
from bullet import Bullet;
from pygame.sprite import Group, groupcollide;

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


def update_screen(screen, game_settings, background, zombies, squares, plants, bullets, tick):
	screen.blit(background.image, background.rect);

	# draw zombies
	for zombie in zombies.sprites():
		zombie.update_me();
		zombie.draw_me();

	# draw plants when clicked (when a plant was added to plants)
	for plant in plants:
		plant.draw_me();
		if tick % 30 == 0:
			bullets.add(Bullet(screen, plant));

	zombie_died = groupcollide(zombies, bullets, True, True);

	# draw the bullets
	for bullet in bullets.sprites():
		bullet.update_me();
		bullet.draw_me();