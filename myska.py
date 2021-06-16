import time
from datetime import datetime
import os
from pynput.mouse import Button, Controller

mouse = Controller()

while (True):
    # datetime object containing current date and time
    now = datetime.now()
    print(now, "Moving with mouse to stay awake")
    #os.system('say "moving"') #say moving
    os.system('afplay /System/Library/Sounds/Tink.aiff') #play system sound Tink
    # Move pointer relative to current position
    mouse.move(5, 5)
    time.sleep(1)
    mouse.move(-5, -5)
    time.sleep(300) #move every 5 minutes

# Press and release
##mouse.press(Button.right)
##mouse.release(Button.right)

# Double click; this is different from pressing and releasing
# twice on Mac OSX
##mouse.click(Button.left, 2)

# Scroll two steps down
##mouse.scroll(0, 2)