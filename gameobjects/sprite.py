# Pandemic Delivery Game
# This code is released under MIT by Fabio Ishikawa
import pygame, random
from gameobjects.vector2 import Vector2

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
		self.lifes = 6
		self.safe = False
		self.score = 0
		self.pedido = 0

	def set_image(self, filename):
		self.image = pygame.image.load(filename)
		self.image.set_colorkey((255,255,255))
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		self.collision_rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

	def flip_image(self, horizontal, vertical):
		self.image = pygame.transform.flip(self.image, horizontal, vertical)

	def set_pedido(self, pedido):
		self.pedido = pedido

	def get_pedido(self):
		return self.pedido

	def set_pos(self, x, y):
		self.pos_x = x
		self.pos_y = y

	def set_score(self, score):
		self.score = score

	def add_score(self):
		self.score += 10

	def get_score(self):
		return self.score

	def get_pos_x(self):
		return self.pos_x

	def get_pos_y(self):
		return self.pos_y

	def get_width(self):
		return self.width

	def get_height(self):
		return self.height

	def get_speed_x(self):
		return self.speed_x

	def get_speed_y(self):
		return self.speed_y

	def get_image(self):
		return self.image

	def set_lifes(self, lifes):
		self.lifes = lifes

	def get_lifes(self):
		return self.lifes

	def set_safe(self, safe):
		self.safe = safe

	def get_safe(self):
		return self.safe

	def set_collision_rect_pos(self, x, y):
		self.collision_rect.x = x
		self.collision_rect.y = y

	def get_collision_rect(self):
		return self.collision_rect

	def update(self, map_region):
		self.pos_x += self.speed_x
		self.pos_y += self.speed_y
		self.collision_rect.x = self.pos_x
		self.collision_rect.y = self.pos_y

		if map_region == 1:
			if self.pos_x + self.width < 0:
				self.pos_x = 304 + self.width
				self.collision_rect.x = self.pos_x
				self.speed_x = -random.randrange(1, 4)

	def get_move_intention(self, destiny):
			pos_vector = Vector2(self.pos_x, self.pos_y)

			# persegue o jogador
			destination_x = destiny.get_pos_x() - destiny.get_width() / 2.0
			destination_y = destiny.get_pos_y() - destiny.get_height() / 2.0
			destination = (destination_x, destination_y)

			heading = Vector2.from_points(pos_vector, destination)
			heading.normalize()

			time_passed_seconds = 120/ 1000.0
			distance_moved = time_passed_seconds * 5
			pos_vector += heading * distance_moved

			self.collision_rect.x += int(pos_vector.x)
			self.collision_rect.y += int(pos_vector.y)
			self.pos_x = pos_vector.x
			self.pos_y = pos_vector.y
			self.collision_rect.x = pos_vector.x
			self.collision_rect.y = pos_vector.y

	def get_away_intention(self, destiny):
		pos_vector = Vector2(self.pos_x, self.pos_y)

		# persegue o jogador
		destination_x = destiny.get_pos_x() - destiny.get_width() / 2.0
		destination_y = destiny.get_pos_y() - destiny.get_height() / 2.0
		destination = (destination_x, destination_y)

		heading = Vector2.from_points(pos_vector, destination)
		heading.normalize()

		time_passed_seconds = 120 / 1000.0
		distance_moved = time_passed_seconds * 5
		pos_vector -= heading * distance_moved 

		self.collision_rect.x += int(pos_vector.x)
		self.collision_rect.y += int(pos_vector.y)
		self.pos_x = pos_vector.x
		self.pos_y = pos_vector.y
		self.collision_rect.x = pos_vector.x
		self.collision_rect.y = pos_vector.y

		return pos_vector

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
		elif map_region == 5:
			if self.pos_x + self.width > 304:
				self.pos_x = 304 - self.width
			elif self.pos_x < 0:
				self.pos_x = 0
		
			if self.pos_y + self.height > 192:
				self.pos_y = 192 - self.height
			elif self.pos_y < 0:
				self.pos_y = 0


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

	def test_collision_enemy(self, enemy):
		if self.collision_rect.colliderect(enemy.get_collision_rect()):
			if enemy.get_safe() == False:
				self.lifes -= 1
				enemy.set_safe(True)
		else:
			if enemy.get_safe() == True:
				enemy.set_safe(False)

	def test_collision(self, sprite):
		if self.collision_rect.colliderect(sprite.get_collision_rect()):
			return True
		else:
			return False