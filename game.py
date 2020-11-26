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

# ESTADOS DO JOGO
# 1 - MENU
# 2 - GAME
# 3 - GAME OVER
GAME_STATE = 1

# sprite = Sprite("teste")
# sprite.print_name()

# Resolução da janela do jogo
WINDOW_WIDTH_SCREEN = 912
WINDOW_HEIGHT_SCREEN = 576

# Inicializando todos os módulos de PyGame
pygame.init()

# objeto de tratamento de tempo
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()

# texto da barra de título da janela
pygame.display.set_caption("PANDEMIC DELIVERY BOY")

# posição da janela na tela
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 100)

# criação da surface para a janela principal - SURFACE CREATION HERE!
window_surface = pygame.display.set_mode((WINDOW_WIDTH_SCREEN, WINDOW_HEIGHT_SCREEN), 0, 32)

# criação da surface com o tamanho correto dos sprites (304x192 pixels) - melhor desempenho
display = pygame.Surface((304, 192))

# Quantidade de quadros por segundo
FPS = 120

# Constantes para as cores
AQUA_BLUE_COLOR = (146,244,255)
RED_COLOR       = (255,0,0)
BLACK_COLOR     = (0,0,0)
WHITE_COLOR     = (255,255,255)

# Array para armazenar o status de pressionamento das teclas (LEFT, RIGHT, TOP, BOTTOM)
keys = [False, False, False, False, False, False]

# -----------------------------------------------------------------------------
#  DECLARAÇÃO DE PERSONAGENS E OBJETOS
# -----------------------------------------------------------------------------
# criação do personagem do jogador (pos_x, pos_y, speed_x, speed_y, imagem)
player = Sprite(50, 150, 1, 1, 'assets/p1.png')

# criação dos carros
car1 = Sprite(354, 42, -random.randrange(1, 4), 0, 'assets/car1.png')
car2 = Sprite(354, 135, -random.randrange(1, 4), 0, 'assets/car2.png')
car3 = Sprite(354, 39, -random.randrange(1, 4), 0, 'assets/car3.png')

# criação dos contaminadores
enemy1 = Sprite(60, 100, -random.randrange(1, 2), -random.randrange(1, 2), 'assets/enemy1.png')
enemy2 = Sprite(random.randrange(40, 70), random.randrange(100, 190), -random.randrange(1, 2), -random.randrange(1, 2), 'assets/enemy2.png')
enemy3 = Sprite(random.randrange(40, 70), random.randrange(100, 190), -random.randrange(1, 2), -random.randrange(1, 2), 'assets/enemy3.png')

# criação dos moradores
people1 = Sprite(112, 140, 0, 0, 'assets/people1.png')
people2 = Sprite(32, 64, 0, 0, 'assets/people2.png')
people3 = Sprite(240, 140, 0, 0, 'assets/people3.png')

heart_img = pygame.image.load('assets/heart.png')
heart_img.set_colorkey((255,255,255))
boxo_img = pygame.image.load('assets/boxo.png')
boxc_img = pygame.image.load('assets/boxc.png')
barrel_img = pygame.image.load('assets/barrel.png')
cone_img = pygame.image.load('assets/cone.png')
cone_img.set_colorkey((255,255,255))

gameover_img = pygame.image.load('assets/gameover.png')
menu_img = pygame.image.load('assets/menu.png')

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
	['1','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','4','0','0','1']]

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
	['3','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','0','0'],
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
game_map = game_map4

# (!) identificador da região atual
current_map_region = 4

# lista de tiles
collision_tiles_rects = []

# imagens de background de cada região
bkg_1_img = pygame.image.load('assets/bkg.png')
bkg_2_img = pygame.image.load('assets/bkg2.png')
bkg_3_img = pygame.image.load('assets/bkg3.png')
bkg_4_img = pygame.image.load('assets/bkg4.png')

# (!) imagem de backgroud atual
bkgs = bkg_1_img

# Texto de interface
font = pygame.font.Font('assets/pixelart.ttf', 8)
font2 = pygame.font.Font('freesansbold.ttf', 20)
font3 = pygame.font.Font('assets/pixelart.ttf', 20)

# -----------------------------------------------------------------------------
#  MAIN
# -----------------------------------------------------------------------------
def main():
	print("Pandemic Delivery Game !!!")
	global player
	global game_map
	global bkgs
	global keys

	global GAME_STATE
	global collision_tiles_rects

	# lista de tiles
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
				if event.key == K_BACKSPACE:
					print("debug 1")
					keys[4] = True
				if event.key == K_RETURN:
					print("debug 2")
					keys[5] = True

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
				if event.key == K_BACKSPACE:
					keys[4] = False
				if event.key == K_RETURN:
					keys[5] = False

		if GAME_STATE == 1:
			menu_loop()
		elif GAME_STATE == 2:
			game_main_loop()
		elif GAME_STATE == 3:
			game_over_loop()

def menu_loop():
	global GAME_STATE
	global keys
	global start_ticks
	
	if keys[5]:
		GAME_STATE = 2
		start_ticks = pygame.time.get_ticks()
		return 0

	display.fill(AQUA_BLUE_COLOR)
	display.blit(menu_img, (0, 0))

	textRegion = font.render('pressione  ENTER para iniciar', True, BLACK_COLOR, WHITE_COLOR)
	display.blit(textRegion, (75, 160))

	window_surface.blit(pygame.transform.scale(display, (WINDOW_WIDTH_SCREEN, WINDOW_HEIGHT_SCREEN)),(0,0))
	pygame.display.flip()
	clock.tick(FPS)



def game_main_loop():
	global current_map_region
	global collision_tiles_rects
	global GAME_STATE
	global clock
	global font2

	seconds = (pygame.time.get_ticks() - start_ticks) / 1000

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

	# ESPAÇO
	# if keys[4]

	# ---------------------------------------------------------------------
	#  ATUALIZANDO A POSIÇÃO DOS OBJETOS
	# ---------------------------------------------------------------------
	if current_map_region == 1:
		car1.update(current_map_region)
		car2.update(current_map_region)

	elif current_map_region == 3:
		car3.update(1)
		# obter o vetor para perseguir o jogador
		enemy1.get_move_intention(player)
		enemy1.get_away_intention(enemy2)
		enemy2.get_move_intention(player)
		enemy2.get_away_intention(enemy3)
		enemy3.get_move_intention(player)

		enemy1.test_collision_border(5)
		enemy2.test_collision_border(5)
		enemy3.test_collision_border(5)
	
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
	if current_map_region == 1:
		player.test_collision_enemy(car1)
		player.test_collision_enemy(car2)
	elif current_map_region == 3:
		player.test_collision_enemy(car3)
		player.test_collision_enemy(enemy1)
		player.test_collision_enemy(enemy2)
		player.test_collision_enemy(enemy3)

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
	#  DESENHA PERSNAGENS
	# ---------------------------------------------------------------------
	if current_map_region == 1:
		display.blit(car1.get_image(), (int(car1.get_pos_x()), int(car1.get_pos_y())))
		display.blit(car2.get_image(), (int(car2.get_pos_x()), int(car2.get_pos_y())))
	elif current_map_region == 3:
		display.blit(car3.get_image(), (int(car3.get_pos_x()), int(car3.get_pos_y())))
		display.blit(enemy1.get_image(), (int(enemy1.get_pos_x()), int(enemy1.get_pos_y())))
		display.blit(enemy2.get_image(), (int(enemy2.get_pos_x()), int(enemy2.get_pos_y())))
		display.blit(enemy3.get_image(), (int(enemy3.get_pos_x()), int(enemy3.get_pos_y())))
	elif current_map_region == 4:
		display.blit(people1.get_image(), (int(people1.get_pos_x()), int(people1.get_pos_y())))
		display.blit(people2.get_image(), (int(people2.get_pos_x()), int(people2.get_pos_y())))
		display.blit(people3.get_image(), (int(people3.get_pos_x()), int(people3.get_pos_y())))

	# if map_region == 3:
	# 	display.blit(enemy, (enemy_vector.x, enemy_vector.y))

	# desenha o personagem DO JOGADOR
	display.blit(player.get_image(), (int(player.get_pos_x()), int(player.get_pos_y())))
	# rect = player.get_collision_rect();
	# pygame.draw.rect(display, RED_COLOR, rect)

	# ---------------------------------------------------------------------
	#  USER INTERFACE
	# ---------------------------------------------------------------------
	# print("seconds: " + str(int(seconds)))
	counter_text = font2.render(str(int(seconds)), True, BLACK_COLOR, WHITE_COLOR)
	counter_text.set_colorkey((255,255,255))

	display.blit(counter_text, (270, 10))

	# if current_map_region == 1:
	# 	textRegion = font.render('LOJAS', True, BLACK_COLOR, AQUA_BLUE_COLOR)
	# elif current_map_region == 2:
	# 	textRegion = font.render('CAMINHO 2', True, BLACK_COLOR, AQUA_BLUE_COLOR)
	# elif current_map_region == 3:
	# 	textRegion = font.render('CAMINHO 1', True, BLACK_COLOR, AQUA_BLUE_COLOR)
	# elif current_map_region == 4:
	# 	textRegion = font.render('CASAS', True, BLACK_COLOR, AQUA_BLUE_COLOR)

	# display.blit(textRegion, (10, 10))

	# desenha a vida do jogador
	x = 10
	for life in range(player.get_lifes()):
		display.blit(heart_img, (x, 10))
		x += 10 + heart_img.get_width()

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

	# ---------------------------------------------------------------------
	#  END GAME
	# ---------------------------------------------------------------------
	if player.get_lifes() == 0:
		print("GAME OVER")
		GAME_STATE = 3
		return 0

	if int(seconds) > 90:
		GAME_STATE = 3
		return 0

def game_over_loop():
	global player
	global GAME_STATE
	global game_map
	global current_map_region
	global keys
	global start_ticks

	if keys[5]:
		player.set_pos(50, 150)
		game_map = game_map4
		current_map_region = 4
		player.set_lifes(6)
		start_ticks = pygame.time.get_ticks()
		GAME_STATE = 2
		return 0

	display.fill(AQUA_BLUE_COLOR)
	display.blit(gameover_img, (0, 0))

	if player.get_lifes() == 0:
		textRegion = font3.render('VOCE PERDEU', True, WHITE_COLOR, BLACK_COLOR)
	else:
		textRegion = font3.render('SEUS PONTOS: ', True, WHITE_COLOR, BLACK_COLOR)

	textRegion.set_colorkey((0,0,0))

	display.blit(textRegion, (80, 80))
	
	textRegion2 = font.render('Pressione  ENTER para jogar de novo', True, WHITE_COLOR, BLACK_COLOR)
	textRegion2.set_colorkey((0,0,0))
	display.blit(textRegion2, (55, 160))

	window_surface.blit(pygame.transform.scale(display, (WINDOW_WIDTH_SCREEN, WINDOW_HEIGHT_SCREEN)),(0,0))
	pygame.display.flip()
	clock.tick(FPS)

if __name__ == '__main__':
	main()