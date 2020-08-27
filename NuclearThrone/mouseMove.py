from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

import time

keyboard = KeyboardController()
mouse = MouseController()

halfScreen = (1920 / 2, 1080 / 2)

# set inverse to False if you want the player to go in the mouse direction (default)
# to True if you want the player to go in the opposite direction
inverse = False

while True:
	
	x = halfScreen[0] - mouse.position[0]
	y = halfScreen[1] - mouse.position[1]
	
	xKey = 'd'
	if inverse == (x < 0):
		xKey = 'a'
	
	yKey = 's'
	if inverse == (y < 0):
		yKey = 'w'
		
	keyboard.press(xKey)
	time.sleep(abs(x / 10000))
	keyboard.release(xKey)
	
	keyboard.press(yKey)
	time.sleep(abs(y / 10000))
	keyboard.release(yKey)
