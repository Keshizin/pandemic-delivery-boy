# Pandemic Delivery Game
# This code is released under MIT by Fabio Ishikawa

import pygame, sys, os, random
from pygame.locals import *

# minhas dependências
from gameobjects.sprite import Sprite
from gameobjects.vector2 import Vector2

# -----------------------------------------------------------------------------
#  GAME - GLOBAL SCOPE
# -----------------------------------------------------------------------------

# sprite = Sprite("teste")
# sprite.print_name()

# Inicializando todos os módulos de PyGame
pygame.init()

# Quantidade de quadros por segundo
FPS = 120

# Resolução da janela do jogo
WINDOW_WIDTH_SCREEN = 912
WINDOW_HEIGHT_SCREEN = 576

# Constantes para as cores
AQUA_BLUE_COLOR = (146,244,255)
RED_COLOR       = (255,0,0)
BLACK_COLOR     = (0,0,0)
WHITE_COLOR     = (255,255,255)

# Array para armazenar o status de pressionamento das teclas (LEFT, RIGHT, TOP, BOTTOM)
keys = [False, False, False, False]

# -----------------------------------------------------------------------------
#  DECLARAÇÃO DE PERSONAGENS E OBJETOS
# -----------------------------------------------------------------------------
# criação do personagem do jogador (pos_x, pos_y, speed_x, speed_y, imagem)
player = Sprite(50, 150, 1, 1, 'assets/p1.png')
car1 = Sprite(354, 42, -random.randrange(1, 4), 0, 'assets/car1.png')
car2 = Sprite(354, 135, -random.randrange(1, 4), 0, 'assets/car2.png')
car3 = Sprite(354, 39, -random.randrange(1, 4), 0, 'assets/car3.png')

enemy = pygame.image.load('assets/enemy1.png')
enemy.set_colorkey((255,255,255))
enemy_pos = [100, 100]
enemy_collision_rect = pygame.Rect(enemy_pos[0], enemy_pos[1], 15, 15)

boxo_img = pygame.image.load('assets/boxo.png')
boxc_img = pygame.image.load('assets/boxc.png')
barrel_img = pygame.image.load('assets/barrel.png')
cone_img = pygame.image.load('assets/cone.png')
cone_img.set_colorkey((255,255,255))

# -----------------------------------------------------------------------------
#  DECLARAÇÃO DE PERSONAGENS E OBJETOS
# -----------------------------------------------------------------------------

# matriz de objetos colisores da região 1 (lojas - pedidos)
game_map1 = [
	['1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','1','1','1','1'],
	['1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','1','1','1','1'],
	['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
	['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
	['1','1','1','1','1','1','0','0','0','0','0','1','1','1','1','1','1','1','1','1'],
	['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
	['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
	['1','1','1','1','1','1','0','0','0','0','0','1','1','1','1','1','1','1','1','1'],
	['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
	['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
	['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
	['1','1','1','0','0','0','1','1','1','1','1','1','1','0','0','0','1','1','1','1']]

# matriz de objetos colisores da região 2 (caminho 1)
game_map2 = [
	['1','1','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1'],
	['1','1','0','0','0','0','0','1','1','1','1','1','1','1','1','1','1','1','1','1'],
	['1','0','0','0','0','0','0','4','0','0','0','0','0','4','0','0','0','0','0','1'],
	['1','0','0','0','4','0','0','4','0','0','0','0','0','4','0','0','0','0','0','1'],
	['1','1','0','0','4','0','0','4','0','0','4','0','0','4','0','0','4','0','0','1'],
	['0','0','0','0','4','0','0','4','0','0','4','0','0','4','0','0','4','0','0','1'],
	['0','0','0','0','4','0','0','4','0','0','4','0','0','4','0','0','4','0','0','1'],
	['1','1','4','4','4','0','0','4','0','0','4','0','0','4','0','0','4','0','0','1'],
	['1','0','0','0','0','0','0','4','0','0','4','0','0','4','0','0','4','0','0','1'],
	['1','0','0','0','0','0','0','0','0','0','4','0','0','0','0','0','4','0','0','1'],
	['1','0','0','4','0','0','0','0','0','0','4','0','0','0','0','0','4','0','0','1'],
	['1','0','0','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','1']]

# matriz de objetos colisores da região 3 (caminho 2)
game_map3 = [
	['1','1','1','0','0','0','1','1','1','1','1','1','1','0','0','0','1','1','1','1'],
	['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
	['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
	['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
	['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1'],
	['2','1','2','2','2','2','0','0','0','0','0','2','0','0','0','2','2','1','2','1'],
	['0','0','0','0','0','0','0','0','0','0','0','2','0','0','0','0','0','0','0','0'],
	['0','0','0','0','0','0','0','0','0','0','0','2','0','0','0','0','0','0','0','0'],
	['0','0','0','0','0','2','2','2','2','0','0','0','0','0','2','0','0','0','0','0'],
	['0','0','2','0','0','0','0','0','0','0','0','0','0','0','2','0','0','0','0','0'],
	['0','0','2','0','0','0','0','0','0','0','0','0','0','0','2','0','0','0','0','0'],
	['0','0','2','0','0','0','0','0','0','0','0','0','0','0','2','0','0','2','2','2']]

# matriz de objetos colisores da região 4 (moradores - entregas)
game_map4 = [
	['3','0','0','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2'],
	['3','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
	['3','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
	['3','0','0','0','0','0','0','1','1','1','1','1','0','0','1','1','1','1','1'],
	['3','0','0','0','0','0','0','1','1','1','1','1','0','0','1','1','1','1','1'],
	['3','0','0','0','0','0','0','1','1','1','1','1','0','0','1','1','1','1','1'],
	['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2'],
	['0','0','0','3','3','0','0','0','0','0','0','0','0','0','0','0','0','0','2'],
	['0','0','0','3','3','0','0','0','0','0','0','0','0','0','0','0','0','0','2'],
	['0','0','0','0','0','0','0','0','0','0','0','3','3','0','0','0','0','0','2'],
	['0','0','0','0','0','0','0','0','0','0','0','3','3','0','0','0','0','0','2'],
	['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2']]

# (!) matriz de objetos atual
game_map = game_map1

# (!) identificador da região atual
current_map_region = 1

# imagens de background de cada região
bkg_1_img = pygame.image.load('assets/bkg.png')
bkg_2_img = pygame.image.load('assets/bkg2.png')
bkg_3_img = pygame.image.load('assets/bkg3.png')
bkg_4_img = pygame.image.load('assets/bkg4.png')

# (!) imagem de backgroud atual
bkgs = bkg_1_img

# Texto de interface
font = pygame.font.Font('assets/pixelart.ttf', 8)

# -----------------------------------------------------------------------------
#  MAIN
# -----------------------------------------------------------------------------
def main():
	print("Pandemic Delivery Game")

	global player
	global current_map_region
	global game_map
	global bkgs

	# objeto de tratamento de tempo
	clock = pygame.time.Clock()

	# texto da barra de título da janela
	pygame.display.set_caption("PANDEMIC DELIVERY BOY")

	# posição da janela na tela
	os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 100)

	# criação da surface para a janela principal - SURFACE CREATION HERE!
	window_surface = pygame.display.set_mode((WINDOW_WIDTH_SCREEN, WINDOW_HEIGHT_SCREEN), 0, 32)

	# criação da surface com o tamanho correto dos sprites (304x192 pixels) - melhor desempenho
	display = pygame.Surface((304, 192))

	# lista de tiles/objetos colisores
	collision_tiles_rects = []

	# preenche a lista de tiles/objetos de acordo com a matriz game_map
	y = 0
	for layer in game_map:
		x = 0
		for tile in layer:
			if tile != '0':
				collision_tiles_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))

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

		# ESQUERDA
		if keys[0]:
			player.set_image('assets/p3.png')
			player_movement[0] = -player.get_speed_x()

		# DIREITA
		if keys[1]:			
			player.set_image('assets/p3.png')
			player.flip_image(True, False) # flip imagem na horizontal
			player_movement[0] = player.get_speed_x()

		# CIMA
		if keys[2]:
			player.set_image('assets/p2.png')
			player_movement[1] = -player.get_speed_y()
		
		# EMBAIXO
		if keys[3]:
			player.set_image('assets/p1.png')
			player_movement[1] = player.get_speed_y()

		# ---------------------------------------------------------------------
		#  ATUALIZANDO A POSIÇÃO DOS OBJETOS
		# ---------------------------------------------------------------------
		if current_map_region == 1:
			car1.update(current_map_region)
			car2.update(current_map_region)

		elif current_map_region == 3:
			car3.update(1)

		# enemy_vector = Vector2(enemy_pos[0], enemy_pos[1])
		
		# destination_x = player_pos[0] - player.get_width() / 2.0
		# destination_y = player_pos[1] - player.get_height() / 2.0
		# destination = (destination_x, destination_y)

		# heading = Vector2.from_points(enemy_vector, destination)
		# heading.normalize()

		# time_passed_seconds = FPS / 1000.0

		# distance_moved = time_passed_seconds * 5
		# enemy_vector += heading * distance_moved 

		# enemy_collision_rect.x += int(enemy_vector.x)
		# enemy_collision_rect.y += int(enemy_vector.y)

		# print("@debug | enemy_vector.x: " +  str(enemy_vector.x))
		# print("@debug | enemy_vector.y: " +  str(enemy_vector.y))
		# enemy_pos[0] = enemy_vector.x
		# enemy_pos[1] = enemy_vector.y

		# enemy_collision_rect.x = enemy_vector.x
		# enemy_collision_rect.y = enemy_vector.y

		# ---------------------------------------------------------------------
		#  TESTE DE COLISÃO COM A BORDA, TILES e INIMIGOS
		# ---------------------------------------------------------------------

		# teste de colisão com os tiles
		player_movement[0], new_y = player.test_collision_tiles(player_movement[0], player_movement[1], collision_tiles_rects)

		# teste de colisão com as bordas da janela
		current_map_region = player.test_collision_border(current_map_region)

		# troca de regiões~
		if current_map_region == 1:
			bkgs = bkg_1_img
			game_map = game_map1
		elif current_map_region == 2:
			bkgs = bkg_2_img
			game_map = game_map2
		elif current_map_region == 3:
			bkgs = bkg_3_img
			game_map = game_map3
		elif current_map_region == 4:
			bkgs = bkg_4_img
			game_map = game_map4

		# ---------------------------------------------------------------------
		#  TESTE DE COLISÃO COM INIMIGOS
		# ---------------------------------------------------------------------

		# if player_collision_rect.colliderect(enemy_collision_rect):
		# 	print("OUCH")
		# else:
		# 	print("...")

		# ---------------------------------------------------------------------
		#  CLEAR SCREEN
		# ---------------------------------------------------------------------

		# limpa a tela com a cor branca
		display.fill(WHITE_COLOR)
		# desenha o background da região atual
		display.blit(bkgs, (0, 0))

		# ---------------------------------------------------------------------
		#  DRAW GAME MAP
		# ---------------------------------------------------------------------
		collision_tiles_rects = []
		y = 0

		for layer in game_map:
			x = 0
			for tile in layer:
			
				if tile == '2':
					display.blit(barrel_img, (x * 16, y * 16))

				if tile == '3':
					display.blit(boxc_img, (x * 16, y * 16))

				if tile == '4':
					display.blit(barrel_img, (x * 16, y * 16))
					
				if tile != '0':
					collision_tiles_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))

				x += 1
			y += 1

		# ---------------------------------------------------------------------
		#  USER INTERFACE
		# ---------------------------------------------------------------------
		# if map_region == 1:
		# 	textRegion = font.render('LOJAS', True, BLACK_COLOR, AQUA_BLUE_COLOR)
		# elif map_region == 2:
		# 	textRegion = font.render('CAMINHO 2', True, BLACK_COLOR, AQUA_BLUE_COLOR)
		# elif map_region == 3:
		# 	textRegion = font.render('CAMINHO 1', True, BLACK_COLOR, AQUA_BLUE_COLOR)
		# elif map_region == 4:
		# 	textRegion = font.render('CASAS', True, BLACK_COLOR, AQUA_BLUE_COLOR)

		# display.blit(textRegion, (10, 10))

		# ---------------------------------------------------------------------
		#  DESENHA PERSNAGENS
		# ---------------------------------------------------------------------
		if current_map_region == 1:
			display.blit(car1.get_image(), (int(car1.get_pos_x()), int(car1.get_pos_y())))
			display.blit(car2.get_image(), (int(car2.get_pos_x()), int(car2.get_pos_y())))
		elif current_map_region == 3:
			display.blit(car3.get_image(), (int(car3.get_pos_x()), int(car3.get_pos_y())))


		# if map_region == 3:
		# 	display.blit(enemy, (enemy_vector.x, enemy_vector.y))

		# desenha o personagem DO JOGADOR
		display.blit(player.get_image(), (int(player.get_pos_x()), int(player.get_pos_y())))
		# rect = player.get_collision_rect();
		# pygame.draw.rect(display, RED_COLOR, rect)

		# ---------------------------------------------------------------------
		#  ATUALIZA O FRAME
		# ---------------------------------------------------------------------

		# faz a escala da surface para o tamanho da janela
		window_surface.blit(pygame.transform.scale(display, (WINDOW_WIDTH_SCREEN, WINDOW_HEIGHT_SCREEN)),(0,0))
		
		# atualiza uma porção da janela com a surface
		# pygame.display.update()
		# atualiza a Surface para a tela inteira
		pygame.display.flip()

		clock.tick(FPS)

if __name__ == '__main__':
	main()