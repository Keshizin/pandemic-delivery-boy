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

	def get_collision_rect(self):
		return self.collision_rect

	def test_collision(self, map_region, new_x, new_y):
		# ETAPA 1 - TESTE DE COLISÃO COM AS BORDAS DA JANELA
		if map_region == 1:
			if self.pos_x + new_x > 304:
				map_region = 2
				self.pos_x = 0
				new_x = 0
			elif self.pos_x + new_x < 0:
				self.pos_x = 0
				new_x = 0

			if self.pos_y + new_y > 192:
				map_region = 3
				self.pos_y = 0
				new_y = 0
			elif self.pos_y + new_y < 0:
				self.pos_y = 0
				new_y = 0

		elif map_region == 2:
			if self.pos_x + new_x + self.width > 304:
				self.pos_x = 304 - self.width
				new_x = 0

			elif self.pos_x + new_x + self.width < 0:
				map_region = 1
				self.pos_x = 304 - self.width
				new_x = 0

			if self.pos_y + new_y > 192:
				map_region = 4
				self.pos_y = 0
				new_y = 0
			elif self.pos_y + new_y < 0:
				map_region = 2
				new_y = 0

		elif map_region == 3:
			if self.pos_x + new_x > 304:
				map_region = 4
				self.pos_x = 0
				new_x = 0
			elif self.pos_x + new_x < 0:
				self.pos_x = 0
				new_x = 0

			if self.pos_y + new_y + self.height > 192:
				self.pos_y = 192 - self.height
				new_y = 0
			elif self.pos_y + new_y < 0:
				map_region = 1
				self.pos_y = 192 - self.height
				new_y = 0

		elif map_region == 4:
			if self.pos_x + new_x + self.width > 304:
				self.pos_x = 304 - self.width
				new_x = 0
			elif self.pos_x + new_x < 0:
				map_region = 3
				self.pos_x = 304 - self.width
				new_x = 0

			if self.pos_y + new_y + self.height > 192:
				self.pos_y = 192 - self.height
				new_y = 0
			elif self.pos_y + new_y < 0:
				map_region = 2
				self.pos_y = 192 - self.height
				new_y = 0

		self.pos_x += new_x
		self.pos_y += new_y

		print("POS X: " + str(self.pos_x))
		print("POS Y: " + str(self.pos_y))

		return map_region