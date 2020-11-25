# Pandemic Delivery Game
# This code is released under MIT by Fabio Ishikawa
import pygame

# -------------------------------------------------------------------------
#  CLASSE - SPRITE DE UM PERSONAGEM
# -------------------------------------------------------------------------
class Sprite(object):
	def __init__(self, x, y, speed_x, speed_y, filename):
		self.image = pygame.image.load(filename)
		self.image.set_colorkey((255,255,255))

		self.pos_x = x
		self.pos_y = y
		self.speed_x = speed_x
		self.speed_y = speed_y
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.collision_rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

	def set_image(self, filename):
		self.image = pygame.image.load(filename)
		self.image.set_colorkey((255,255,255))
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.collision_rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

	def flip_image(self, horizontal, vertical):
		self.image = pygame.transform.flip(self.image, horizontal, vertical)

	def get_pos_x(self):
		return self.pos_x

	def get_pos_y(self):
		return self.pos_y

	def get_speed_x(self):
		return self.speed_x

	def get_speed_y(self):
		return self.speed_y

	def get_image(self):
		return self.image

	def test_collision(self, map_region):
		print('teste collision')
		# if map_region == 1:
		# 	if player_pos[0] + player_movement[0] > 304:
		# 		bkgs = bkg_2_img
		# 		map_region = 2
		# 		game_map = game_map2
		# 		player_pos[0] = 0
		# 		player_movement[0] = 0
		# 	elif player_pos[0] + player_movement[0] < 0:
		# 		bkgs = bkg_1_img
		# 		map_region = 1
		# 		player_pos[0] = 0
		# 		player_movement[0] = 0

		# 	if player_pos[1] + player_movement[1] > 192:
		# 		bkgs = bkg_3_img
		# 		map_region = 3
		# 		game_map = game_map3
		# 		player_pos[1] = 0
		# 		player_movement[1] = 0
		# 	elif player_pos[1] + player_movement[1] < 0:
		# 		bkgs = bkg_1_img
		# 		map_region = 1
		# 		player_pos[1] = 0
		# 		player_movement[1] = 0

		# elif map_region == 2:
		# 	if player_pos[0] + player_movement[0] + player.get_width() > 304:
		# 		bkgs = bkg_2_img
		# 		map_region = 2
		# 		player_pos[0] = 304 - player.get_width()
		# 		player_movement[0] = 0
		# 	elif player_pos[0] + player_movement[0] + player.get_width() < 0:
		# 		bkgs = bkg_1_img
		# 		map_region = 1
		# 		game_map = game_map1
		# 		player_pos[0] = 304 - player.get_width()
		# 		player_movement[0] = 0

		# 	if player_pos[1] + player_movement[1] > 192:
		# 		bkgs = bkg_4_img
		# 		map_region = 4
		# 		game_map = game_map4
		# 		player_pos[1] = 0
		# 		player_movement[1] = 0
		# 	elif player_pos[1] + player_movement[1] < 0:
		# 		bkgs = bkg_2_img
		# 		map_region = 2
		# 		player_pos[1] = 0
		# 		player_movement[1] = 0

		# elif map_region == 3:
		# 	if player_pos[0] + player_movement[0] > 304:
		# 		bkgs = bkg_4_img
		# 		map_region = 4
		# 		game_map = game_map4
		# 		player_pos[0] = 0
		# 		player_movement[0] = 0
		# 	elif player_pos[0] + player_movement[0] < 0:
		# 		bkgs = bkg_3_img
		# 		map_region = 3
		# 		player_pos[0] = 0
		# 		player_movement[0] = 0

		# 	if player_pos[1] + player_movement[1] + player.get_height() > 192:
		# 		bkgs = bkg_3_img
		# 		map_region = 3
		# 		player_pos[1] = 192 - player.get_height()
		# 		player_movement[1] = 0
		# 	elif player_pos[1] + player_movement[1] < 0:
		# 		bkgs = bkg_1_img
		# 		map_region = 1
		# 		game_map = game_map1
		# 		player_pos[1] = 192 - player.get_height()
		# 		player_movement[1] = 0

		# elif map_region == 4:
		# 	if player_pos[0] + player_movement[0] + player.get_width() > 304:
		# 		bkgs = bkg_4_img
		# 		map_region = 4
		# 		player_pos[0] = 304 - player.get_width()
		# 		player_movement[0] = 0
		# 	elif player_pos[0] + player_movement[0] < 0:
		# 		bkgs = bkg_3_img
		# 		map_region = 3
		# 		game_map = game_map3
		# 		player_pos[0] = 304 - player.get_width()
		# 		player_movement[0] = 0

		# 	if player_pos[1] + player_movement[1] + player.get_height() > 192:
		# 		bkgs = bkg_4_img
		# 		map_region = 4
		# 		player_pos[1] = 192 - player.get_height()
		# 		player_movement[1] = 0
		# 	elif player_pos[1] + player_movement[1] < 0:
		# 		bkgs = bkg_2_img
		# 		map_region = 2
		# 		game_map = game_map2
		# 		player_pos[1] = 192 - player.get_height()
		# 		player_movement[1] = 0

