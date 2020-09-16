import os
from PIL import ImageGrab
import time

"""
Below are the coordinates for the game, trex run. All
coordinates are under the assumptions
that it is run in 1920x1080, any modern browser w/o any extensions that may
change the screen
"""
xPad = 659
yPad = 184

def screenGrab():
    box = (xPad + 1, yPad + 1, xPad + 601, yPad + 140)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' 
    + str(int(time.time())) + '.png', 'PNG')

def main():
    screenGrab()

if __name__ == "__main__":
    main()