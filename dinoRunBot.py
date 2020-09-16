import os
from PIL import ImageGrab, ImageOps
from numpy import *
import time
import win32api, win32con



"""
Below are the coordinates for the game, trex run. All
coordinates are under the assumptions
that it is run in 1920x1080, any modern browser w/o any extensions that may
change the screen
nn
"""
xPad = 659
yPad = 184
cactusPosThresh = (139, 110)

def screenGrab():
    b1 = (xPad + 1, yPad + 1, xPad + 601, yPad + 140)
    im = ImageGrab.grab(b1)
   # im.save(os.getcwd() + '\\full_snap__'  + str(int(time.time())) + '.png', 'PNG')
    return im
    
def grab():
    b1 = (xPad + 1, yPad + 1, xPad + 601, yPad + 140)
    im = ImageOps.grayscale(ImageGrab.grab(b1))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    return a

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print('click')


def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print('left click down')

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print('left click up (released)')

def mousePos(cord):
    #add xpad and ypad to x and y coordinate
    #FOR SOME REASON SETCURSORPOS METHOD ONLY TAKES 1 ARGUMENT WHEN THE DOCS
    #SAY IT CAN TAKE 2????
    win32api.SetCursorPos((xPad + cord[0], yPad + cord[1]))

def getCords():
    x,y = win32api.GetCursorPos()
    x = x- xPad
    y = y - yPad
    print(x,y)

def restartGame():
    mousePos((301, 87)) #Location of the restart button
    leftClick()
    time.sleep(.1)

def spaceBar():
    win32api.keybd_event(32, 0,0,0) #Press space bar
    time.sleep(.1)
    print('space')

def downArrow():
    win32api.keybd_event(40, 0,0,0) #Press down arrow
    time.sleep(.1)
    print('duck')
    
"""
Coords of when cactus is close: 139, 114

Box(es) that the bot will focus on, if anything passes that box, the dino will respond appropriately:
x,y = 129, 92
"""    
def getObstacleBox():
    box = (xPad + 129, yPad + 92, (xPad + 129) + 20, (yPad + 92) + 38)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #print(a)
    #im.save(os.getcwd() + '\\_snap__'  + str(int(time.time())) + '.png', 'PNG')
    return a

def dinoJump():
    s = screenGrab()
    #time.sleep(.15)
    #getObstacleBox != Blank.blank1 (Box method)
    #s.getpixel((xPad+ 139, yPad + 114)) != (247, 247, 247) (Single pixel method)
    if s.getpixel(cactusPosThresh)!= (247, 247, 247):
        spaceBar()
        print('cactus!')

def stopGame():
    box = (xPad + 273, yPad + 73, xPad + 316, yPad + 102)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    #im.save(os.getcwd() + '\\_snap__'  + str(int(time.time())) + '.png', 'PNG')
    #print(a)
    return a
    
def startGame():
    STOPCODE = 1577
    restartGame()
    while True:
        dinoJump()
        if stopGame() == STOPCODE:
            print("Game Over!")
            break
    

def main():
    #screenGrab()
    pass

if __name__ == "__main__":
    main()

"""
#getMouseCords()
class Blank:
    blank1 = 1090


#leftClick()
"""