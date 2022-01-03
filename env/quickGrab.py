
from PIL import ImageGrab
import os
import time

 
x_pad = 929 # -1 from the point of left upper corner
y_pad = 232 #- 1 from the point of left upper corner

def screenGrab():
    box = (x_pad, y_pad, x_pad+978, y_pad+659)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')
 
def main():
    screenGrab()
 
if __name__ == '__main__':
    main()