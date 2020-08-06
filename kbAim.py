from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

keyboard = KeyboardController()
mouse = MouseController()

direction = [(-1,1),(0,1),(1,1),(-1,0),(0,0),(1,0),(-1,-1),(0,-1),(1,-1)]

halfScreen = (1920 / 2, 1080 / 2)

def on_press(key):
    
    if hasattr(key, 'vk'):
        
        i = key.vk - 96
        
        if 0 <= i <= 9:
            
            if i == 0:
                mouse.press(Button.left)
                return
                
            if i == 5:
                mouse.press(Button.right)
                return
                
            global direction
            tup = direction[i - 1]
            mouse.position = (tup[0] * 300 + screenResolution[0], tup[1] * 300 + screenResolution[1])
        

def on_release(key):

    if hasattr(key, 'vk'):
        
        i = key.vk - 96
        
            if key.vk == 0:
                mouse.release(Button.left)
                return
                
            if key.vk == 5:
                mouse.release(Button.right)
                return
    
with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
