# Pandemic Delivery Game
# This code is released under MIT by Fabio Ishikawa
import pygame, random

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
		self.lifes

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

	def set_collision_rect_pos(self, x, y):
		self.collision_rect.x = x
		self.collision_rect.y = y

	def get_collision_rect(self):
		return self.collision_rect

	def update(self, map_region):
		self.pos_x += self.speed_x
		self.pos_y += self.speed_y

		if map_region == 1:
			if self.pos_x + self.width < 0:
				self.pos_x = 304 + self.width
				self.speed_x = -random.randrange(1, 4)

	def test_collision_border(self, map_region):
		# -------------------------------------------------------------------------
		#  ETAPA 1 - TESTE DE COLISÃO COM BORDAS DA JANELA
		# -------------------------------------------------------------------------
		if map_region == 1:
			if self.pos_x > 304:
				map_region = 2
				self.pos_x = 0
			elif self.pos_x < 0:
				self.pos_x = 0
			
			if self.pos_y > 192:
				map_region = 3
				self.pos_y = 0
			elif self.pos_y < 0:
				self.pos_y = 0

		elif map_region == 2:
			if self.pos_x + self.width > 304:
				self.pos_x = 304 - self.width
			elif self.pos_x + self.width < 0:
				map_region = 1
				self.pos_x = 304 - self.width

			if self.pos_y > 192:
				map_region = 4
				self.pos_y = 0
			elif self.pos_y < 0:
				self.pos_y = 0

		elif map_region == 3:
			if self.pos_x > 304:
				map_region = 4
				self.pos_x = 0
			elif self.pos_x < 0:
				self.pos_x = 0

			if self.pos_y + self.height > 192:
				self.pos_y = 192 - self.height
			elif self.pos_y < 0:
				map_region = 1
				self.pos_y = 192 - self.height

		elif map_region == 4:
			if self.pos_x + self.width > 304:
				self.pos_x = 304 - self.width
			elif self.pos_x < 0:
				map_region = 3
				self.pos_x = 304 - self.width
		
			if self.pos_y + self.height > 192:
				self.pos_y = 192 - self.height
			elif self.pos_y < 0:
				map_region = 2
				self.pos_y = 192 - self.height

		self.collision_rect.x = self.pos_x
		self.collision_rect.y = self.pos_y

		return map_region

	def test_collision_tiles(self, new_x, new_y, test_collision_tiles):
		# -------------------------------------------------------------------------
		#  ETAPA 2 - TESTE DE COLISÃO COM TILES
		# -------------------------------------------------------------------------

		# verificação de colisão no eixo X
		self.collision_rect.x = int(self.pos_x) + new_x

		for tile in test_collision_tiles:
			if self.collision_rect.colliderect(tile):
				# print("hit tiles!")
				if new_x > 0:
					# print("RIGHT")
					self.collision_rect.x = tile[0] -  self.collision_rect.width
				elif new_x < 0:
					# print("LEFT")
					self.collision_rect.x  = tile[0] + tile[2]

		# verificação de colisão no eixo Y
		self.collision_rect.y = int(self.pos_y) + new_y

		for tile in test_collision_tiles:
			if self.collision_rect.colliderect(tile):
				if new_y > 0:
					# print("BOTTOM")
					self.collision_rect.y = tile[1] - self.collision_rect.height
				elif new_y < 0:
					# print("TOP")
					self.collision_rect.y = tile[1] + tile[3]

		self.pos_x = self.collision_rect.x
		self.pos_y = self.collision_rect.y

		return new_x, new_y
