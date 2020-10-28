# Pandemic Delivery Game
# Fabio Takeshi Ishikawa
#
# This code is released under MIT by Fabio Ishikawa

import pygame, sys, os
from pygame.locals import *

COLOR_AQUA_BLUE = (146,244,255)

# initialize all imported pygame modules
pygame.init()

# my game screen resolution
# GAME_WIDTH_SCREEN = 1100
# GAME_HEIGHT_SCREEN = 800
GAME_WIDTH_SCREEN = 600
GAME_HEIGHT_SCREEN = 400
# GAME_WIDTH_SCREEN = 1216 # 19 x 64
# GAME_HEIGHT_SCREEN = 832 # 13 x 64

RED_COLOR = (255,0,0)
BLACK_COLOR = (0,0,0)

# -----------------------------------------------------------------------------
#  GAME - GLOBAL SCOPE
# -----------------------------------------------------------------------------
player = pygame.image.load('assets/test.png')
# player = pygame.image.load('assets/player32.png')
# player.set_colorkey((255,255,255))

# player_pos = [0, GAME_HEIGHT_SCREEN - player.get_height()]
player_pos = [16 * 5, 0]

air = False

momentum_limit = 5
momentum_speed = 1
# player_y_momentum = -momentum_limit
player_y_momentum = 0

player_collision_rect = pygame.Rect(player_pos[0], player_pos[1], player.get_width(), player.get_height())

# keys for arrows (LEFT, RIGHT, TOP, BOTTOM)
keys = [False, False, False, False]

# font = pygame.font.Font('freesansbold.ttf', 15)
# text = font.render('Seu texto aqui', True, RED, WHITE)

game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
			['0','0','1','1','0','0','0','0','0','0','0','0','0','0','0','1','1','0','0'],
			['0','0','1','0','0','0','0','0','0','0','0','0','0','0','1','0','0','0','0'],
			['0','0','1','0','0','0','0','0','0','0','0','0','1','1','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0'],
			['0','0','0','0','0','2','0','2','0','2','0','0','1','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','1','0','0','0','0','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','0','0'],
			['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']]

boxo_img = pygame.image.load('assets/boxo.png')
boxc_img = pygame.image.load('assets/boxc.png')
bkg_1_img = pygame.image.load('assets/bkg.png')

# -----------------------------------------------------------------------------
#  MAIN
# -----------------------------------------------------------------------------
def main():
	print("Pandemic Delivery Game")

	global air
	global player_y_momentum
	global momentum_speed
	global player_collision_rect
	global true_scroll

	# create an object to help track time
	clock = pygame.time.Clock()

	# set the current window caption
	pygame.display.set_caption("PANDEMIC DELIVERY BOY")

	# set the window screen position
	os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 100)

	# initialize a window or screen for display - SURFACE CREATION HERE!
	screen = pygame.display.set_mode((GAME_WIDTH_SCREEN, GAME_HEIGHT_SCREEN), 0, 32)

	# criando uma Surface menor para aumentar o desempenho
	# display = pygame.Surface((300,200))
	display = pygame.Surface((304, 192))

	tile_rects = []
	y = 0

	for layer in game_map:
		x = 0
		for tile in layer:
			if tile != '0':
				tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))

			x += 0
		y += 1

	# -------------------------------------------------------------------------
	#  GAME LOOP
	# -------------------------------------------------------------------------
	while True:
		# get events from the queue
		for event in pygame.event.get():
			# QUIT THE GAME
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			# MOUSE INPUT
			# if event.type == MOUSEBUTTONDOWN:
				# print("MOUSE DOWN")

			# if event.type == MOUSEMOTION:
				# print("MOUSE MOTION")

			# if event.type == MOUSEBUTTONUP:
				# print("MOUSE UP")

			# KEYBOARD INPUT (PRESS DOWN)
			if event.type == KEYDOWN:
				if event.key == K_LEFT:
					keys[0] = True
				if event.key == K_RIGHT:
					keys[1] = True
				if event.key == K_UP:
					keys[2] = True
				if event.key == K_DOWN:
					keys[3] = True

			# KEYBOARD INPUT (RELEASE)
			if event.type == KEYUP:
				if event.key == K_LEFT:
					keys[0] = False
				if event.key == K_RIGHT:
					keys[1] = False
				if event.key == K_UP:
					keys[2] = False
				if event.key == K_DOWN:
					keys[3] = False
		
		# ---------------------------------------------------------------------
		#  PLAYER INPUT
		# ---------------------------------------------------------------------
		# player_movement representa o quanto devemos deslocar o personagem!
		player_movement = [0, 0]

		if keys[0]:
			player_movement[0] = -2

		if keys[1]:
			player_movement[0] = 2
	
		if keys[2]:
			player_movement[1] = -2
			# if air == False:
			# 	air = True
			# 	player_y_momentum = -momentum_limit
		
		if keys[3]:
			player_movement[1] = 2

		# ---------------------------------------------------------------------
		#  ATUALIZANDO A POSIÇÃO DOS OBJETOS
		# ---------------------------------------------------------------------		
		# player_movement[1] += player_y_momentum
		# player_y_momentum += 0.2

		# if player_y_momentum > 3:
		# 	player_y_momentum = 3

		# ---------------------------------------------------------------------
		#  TESTE DE COLISÃO DE OBJETOS
		# ---------------------------------------------------------------------
		temp = [0, 0]
		
		# TESTE DE COLISÃO COM OS TILES

		# verificação de colisão no eixo X
		player_collision_rect.x = int(player_pos[0]) + player_movement[0]
		temp[0] = player_collision_rect.x

		for tile in tile_rects:
			if player_collision_rect.colliderect(tile):
				if player_movement[0] > 0:
					# print("RIGHT")
					temp[0] = tile[0] - player_collision_rect.width
					player_collision_rect.x = temp[0]
				elif player_movement[0] < 0:
					# print("LEFT")
					temp[0] = tile[0] + tile[2]
					player_collision_rect.x = temp[0]

		# verificação de colisão no eixo Y
		player_collision_rect.y = int(player_pos[1]) + int(player_movement[1])
		temp[1] = player_collision_rect.y

		for tile in tile_rects:
			if player_collision_rect.colliderect(tile):
				if player_movement[1] > 0:
					# print("BOTTOM")
					temp[1] = tile[1] - player_collision_rect.height
					player_collision_rect.y = temp[1]

					air = False
					player_y_momentum = 0

				elif player_movement[1] < 0:
					# print("TOP")
					temp[1] = tile[1] + tile[3]
					player_collision_rect.y = temp[1]
			
					player_y_momentum = 0

		player_pos[0] = temp[0]
		player_pos[1] = temp[1]

		# ---------------------------------------------------------------------
		#  CLEAR SCREEN
		# ---------------------------------------------------------------------
		display.fill(COLOR_AQUA_BLUE)
		display.blit(bkg_1_img, (0, 0))

		# ---------------------------------------------------------------------
		#  DRAW GAME MAP
		# ---------------------------------------------------------------------
		tile_rects = []
		y = 0

		for layer in game_map:
			x = 0
			for tile in layer:
	
				if tile == '1':
					display.blit(boxo_img, (x * 16, y * 16))
					
				if tile == '2':
					display.blit(boxc_img, (x * 16, y * 16))

				# if tile == '3':
				# 	display.blit(floor1_img, (x * 16, y * 16))
					
				if tile != '0':
					tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))

				x += 1
			y += 1

		# ---------------------------------------------------------------------
		#  DRAW FRAME
		# ---------------------------------------------------------------------
		# pygame.draw.rect(display, test_object_color, test_object_rect)

		display.blit(player, (int(player_pos[0]), int(player_pos[1])))
		# screen.blit(text, (5, 10))

		screen.blit(pygame.transform.scale(display, (GAME_WIDTH_SCREEN, GAME_HEIGHT_SCREEN)),(0,0))
		
		# update portions of the screen for software displays
		# pygame.display.update()

		# update the full display Surface to the screen
		pygame.display.flip()

		clock.tick(120)

if __name__ == '__main__':
	main()