
from PIL import ImageGrab, ImageOps, Image
import os
import time
import win32api, win32con
from numpy import *


x_pad = 929 # -1 from the point of left upper corner
y_pad = 232 #- 1 from the point of left upper corner

allWorking = False
counter = 0

class Coord:
    heroesListOpen = (499, 589)
    heroesListIcon = (494, 542)
    heroesListToScroll = (325, 332)
    heroesListClose = (553, 116)
    workButton = (411, 507)
    chestOpen = (868, 39)
    chestClose = (761, 120)
    nextMapButton = (500, 500)

class whatState:
    working = 116022
    bottomMenuUp = 119586
    heroesListOpened = 111219
    chestOpened = 110369
    nextMap = (101146, 267668)


def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print("Click.")          #completely optional. But nice for debugging purposes.

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print('left Down')
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print('left release')


def scrollUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0 ,0, -1)
    time.sleep(.1)
    print('scroll up')


def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))
     
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x,y)

def screenGrab():
    b1 = (x_pad+1, y_pad+1, x_pad+978, y_pad+659)
    im = ImageGrab.grab(b1)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +'.png', 'PNG')
    return im

def grab():
    box = (x_pad + 186,y_pad+91,x_pad+713,y_pad+540)
    # im = ImageOps.grayscale(Image.open(r".\bottom_1641218030.png"))
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\bottom_' + str(int(time.time())) + '.png', 'PNG')    
    return a


def openHeroesList():
    #location of first menu
    mousePos(Coord.heroesListOpen)
    time.sleep(1)
    leftClick()
    time.sleep(1)
    mousePos(Coord.heroesListIcon)
    time.sleep(1)
    leftClick()
    time.sleep(5)
    mousePos(Coord.heroesListToScroll)
    time.sleep(1)
    for i in range(40):
        scrollUp()
 
def gotToWork():
    for i in range(15):
        mousePos(Coord.workButton)
        time.sleep(1)
        leftClick()
        # time.sleep(1)

def closeHeroesList():
    mousePos(Coord.heroesListClose)
    time.sleep(1)
    leftClick()
    time.sleep(1)
    leftClick()

def openChest():
    mousePos(Coord.chestOpen)
    time.sleep(1)
    leftClick()

def closeChest():
    mousePos(Coord.chestClose)
    time.sleep(1)
    leftClick()

def startWorkingAll():
    global allWorking
    allWorking = True
    openHeroesList()
    time.sleep(1)
    gotToWork()
    time.sleep(1)
    closeHeroesList()

def ping():
    openChest()
    time.sleep(1)
    closeChest()

def nextMap():
    mousePos((500, 500))
    time.sleep(1)
    leftClick()        

def checkStates():
    global allWorking
    global counter
    if(counter == 30):
        allWorking = False
        counter = 0

    if (grab() in whatState.nextMap):
        print("Next map")
        nextMap()
    elif (allWorking == False):
        print("Start working all")
        startWorkingAll()
    elif (allWorking == True):
        print("ping")
        ping()

def main():
    global allWorking, counter

    while(1):
        checkStates()
        time.sleep(60)
        counter = counter + 1
        print("Counter " + str(counter))
    
 
if __name__ == '__main__':
    main()

