import pygame
import numpy as np
import time

pygame.init()

w, h = 1000, 1000
screen = pygame.display.set_mode((h, w))
bg = 0,26,51
screen.fill(bg)

nxC, nyC = 100, 100
dimCW = w / nxC
dimCh = h / nyC

gameState = np.zeros((nxC, nyC))



gameState[50, 30] = 1
gameState[50, 31] = 1
gameState[50, 32] = 1
gameState[49, 32] = 1
gameState[48, 31] = 1




pause = False


while True:

	new_game_state = np.copy(gameState)
	screen.fill(bg)
	time.sleep(0.1)

	events = pygame.event.get()

	for event in events:
		if event.type == pygame.KEYDOWN:
			pause = not pause

		click = pygame.mouse.get_pressed()

		if sum(click) > 0:
			pos_x, pos_y = pygame.mouse.get_pos()
			cel_x, cel_y = int(np.floor(pos_x/dimCW)), int(np.floor(pos_y/dimCh))
			new_game_state[cel_x, cel_y] = not click[2]


	for y in range(0, nxC):
		for x in range(0, nyC):
			if not pause:

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
