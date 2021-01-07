# Python 3.8.2
# Last updated 09/11/2020 (MM/DD/YYYY)
# By StrayPyramid

from PIL import ImageOps, ImageGrab
import numpy as np

from constants import *
from rect import *

def grabArea(rect):
    rect = Rect(rect)
    rect.translate(Coor.X_PAD, Coor.Y_PAD)
    
    im = ImageGrab.grab((rect.left(), rect.top(), rect.right(), rect.bottom()))
    return im

def sumArea(rect):
    #rect: Xpos, YPos, Width, Height
    im = ImageOps.grayscale(grabArea(rect))
    a = np.array(im.getcolors())
    a = a.sum()
    return a    
    
def saveArea(rect):
    im = grabArea(rect)
    sum = sumArea(rect)
    im.save("./"+str(sum)+".png", 'PNG') 

if __name__ == "__main__":
    while True:
        print("Please enter area coordinates")
        print("FORMAT: LEFT TOP WIDTH HEIGHT")
        
        coor = input().split(" ")
        if(len(coor) != 4):
            print("INVALID")
            continue
            
        rect = tuple([int(i) for i in coor])
        sum = sumArea(rect)
        saveArea(rect)
        
            
        print(sum)