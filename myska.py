import time
from datetime import datetime
import os
from pynput.mouse import Button, Controller

mouse = Controller()

while (True):
    # datetime object containing current date and time
    now = datetime.now()
    print(now, "Pressing left button on mouse to stay awake")
    #os.system('say "moving"') #say moving
    os.system('afplay /System/Library/Sounds/Morse.aiff') #play system sound Tink
    
    # Move pointer relative to current position
    #mouse.move(5, 0)
    #time.sleep(0.2)
    #mouse.move(-5, 0)
    
    # Press and release
    mouse.press(Button.left)
    mouse.release(Button.left)
    
    time.sleep(300) #move every 5 minutes



# Double click; this is different from pressing and releasing
# twice on Mac OSX
##mouse.click(Button.left, 2)

# Scroll two steps down
##mouse.scroll(0, 2)