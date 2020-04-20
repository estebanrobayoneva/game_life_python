import pygame
import numpy as np
import time

pygame.init()

w, h = 800, 800
screen = pygame.display.set_mode((h, w))
bg = 0,26,51
screen.fill(bg)

nxC, nyC = 50, 50
dimCW = w / nxC
dimCh = h / nyC

gameState = np.zeros((nxC, nyC))

gameState[5, 3] = 1
gameState[5, 4] = 1
gameState[5, 5] = 1

gameState[21, 21] = 1
gameState[22,22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1





while True:

	new_game_state = np.copy(gameState)
	screen.fill(bg)
	time.sleep(0.1)

	for y in range(0, nxC):
		for x in range(0, nyC):
			n_neigh = gameState[(x-1)%nxC, (y-1)%nyC] +\
					  gameState[(x)%nxC, (y-1)%nyC] +\
					  gameState[(x+1)%nxC, (y-1)%nyC] +\
					  gameState[(x-1)%nxC, (y)%nyC] +\
					  gameState[(x+1)%nxC, (y)%nyC] +\
					  gameState[(x-1)%nxC, (y+1)%nyC] +\
					  gameState[(x)%nxC, (y+1)%nyC] +\
					  gameState[(x+1)%nxC, (y+1)%nyC]

			#Rules
	
			if gameState[x, y] == 0 and n_neigh == 3:
				new_game_state[x, y] = 1

			elif gameState[x,y]==1 and n_neigh > 1 and (n_neigh > 3 or n_neigh < 2):
				new_game_state[x,y]=0

			poly = [((x)*dimCW, y*dimCh), 
					((x+1)*dimCW, y*dimCh),
					((x+1)*dimCW, (y+1)*dimCh),
					((x)*dimCW, (y+1)*dimCh)]

			if new_game_state[x,y] == 0:
				pygame.draw.polygon(screen, (100, 100, 100), poly, 1)
				#pygame.display.update()

			else:
				pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
				#pygame.display.update()

	gameState = np.copy(new_game_state)


	pygame.display.flip()
