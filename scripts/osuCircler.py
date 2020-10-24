from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

from pynput.keyboard import Listener

keyboard = KeyboardController()
mouse = MouseController()

import _thread
import time

d = False

halfScreen = (1920 / 2, 1080 / 2)

def on_press(key):
	
	if not hasattr(key, 'char'): return
		
	if key.char == '1':
		global d
		d = True
		return
		
	if key.char == '2':
		mouse.position = halfScreen
		return


def on_release(key):
	
	if not hasattr(key, 'char'): return
	
	if key.char == '1':  
		global d
		d = False

x=30
y=30

def update_circle(idk,idfk):
	should = False
	while True:
		global d
		if d:
			global x
			global y
			if should:
				x = -x
				should = False
			else: should = True
			mouse.position = halfScreen
			mouse.move(x,y)
			y = x
		time.sleep(.01)

_thread.start_new_thread (update_circle, (0,0))

with Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()
	

