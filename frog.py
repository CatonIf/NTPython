from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

keyboard = KeyboardController()
mouse = MouseController()

d = 0

def on_press(key):

    global d
    
    c = key.char
    
    if c == 'w':
        d |= 1
    elif c == 'a':
        d |= 2
    elif c == 's':
        d |= 4
    elif c == 'd':
        d |= 8 
    if d > 0:
        mouse.release(Button.right)


def on_release(key):

    global d
    
    c = key.char
    
    if c == 'w':
        d &= ~1
    elif c == 'a':
        d &= ~2
    elif c == 's':
        d &= ~4
    elif c == 'd':
        d &= ~8
    if not d:
        mouse.press(Button.right)

with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
