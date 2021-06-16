import time
from datetime import datetime
from pynput.mouse import Button, Controller
import beepy

mouse = Controller()

while (True):
    # datetime object containing current date and time
    now = datetime.now()
    print(now, "Pressing left button on mouse to stay awake")
    
    #choose one from 'coin','robot_error','error','ping','ready','success','wilhelm'
    beepy.beep(sound="coin")
    
    # Move pointer relative to current position
    #mouse.moe(5, 0)
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