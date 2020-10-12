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
GAME_WIDTH_SCREEN = 1100
GAME_HEIGHT_SCREEN = 800

player = pygame.image.load('assets/player.png')
player_pos = [0, 0]

keys = [False, False, False, False]

# -----------------------------------------------------------------------------
#  MAIN
# -----------------------------------------------------------------------------
def main():
	print("Pandemic Delivery Game")

	# clock = pygame.time.Clock()

	# set the current window caption
	pygame.display.set_caption("PANDEMIC DELIVERY BOY")

	# set the window screen position
	os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 100)

	# initialize a window or screen for display - SURFACE CREATION HERE!
	screen = pygame.display.set_mode((GAME_WIDTH_SCREEN, GAME_HEIGHT_SCREEN), 0, 32)

	# -------------------------------------------------------------------------
	#  GAME LOOP
	# -------------------------------------------------------------------------
	while True:
		# get events from the queue
		for event in pygame.event.get():

			# quit the game
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			# MOUSE INPUT
			if event.type == MOUSEBUTTONDOWN:
				print("MOUSE DOWN")

			if event.type == MOUSEMOTION:
				print("MOUSE MOTION")

			if event.type == MOUSEBUTTONUP:
				print("MOUSE UP")

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
		if keys[0]:
			player_pos[0] -= 1
		
		if keys[1]:
			player_pos[0] += 1
		
		if keys[2]:
			player_pos[1] -= 1
		
		if keys[3]:
			player_pos[1] += 1	

		# ---------------------------------------------------------------------
		#  CLEAR SCREEN
		# ---------------------------------------------------------------------
		screen.fill(COLOR_AQUA_BLUE)

		screen.blit(player, player_pos)

		# update portions of the screen for software displays
		# pygame.display.update()

		# update the full display Surface to the screen
		pygame.display.flip()

if __name__ == '__main__':
	main()