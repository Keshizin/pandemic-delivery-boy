# Pandemic Delivery Game
# Fabio Takeshi Ishikawa
#
# This code is released under MIT by Fabio Ishikawa

import pygame, sys, os
from pygame.locals import *

# initialize all imported pygame modules
pygame.init()

# my game screen resolution
GAME_WIDTH_SCREEN = 640
GAME_HEIGHT_SCREEN = 480

def main():
	print("Pandemic Delivery Game")

	# clock = pygame.time.Clock()

	# set the current window caption
	pygame.display.set_caption("PANDEMIC DELIVERY BOY")

	# set the window screen position
	os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 100)

	# initialize a window or screen for display - SURFACE CREATION HERE!
	screen = pygame.display.set_mode((GAME_WIDTH_SCREEN, GAME_HEIGHT_SCREEN), 0, 32)

	while True:
		# get events from the queue
		for event in pygame.event.get():

			# quit the game
			if event.type == QUIT:
				pygame.quit()
				sys.exit()


		# update portions of the screen for software displays
		# pygame.display.update()

		# update the full display Surface to the screen
		pygame.display.flip()

if __name__ == '__main__':
	main()