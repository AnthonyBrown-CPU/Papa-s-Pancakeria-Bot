import win32api, win32con, win32gui
import time

from rect import *
from constants import *
from key_codes import *


def pressKey(k):
    win32api.keybd_event(VK_CODE[k], 0)
    time.sleep(.05)
    win32api.keybd_event(VK_CODE[k],0 ,win32con.KEYEVENTF_KEYUP ,0)

def holdKey(k):
    win32api.keybd_event(VK_CODE[k], 0)
    time.sleep(.05)
    
def releaseKey(k):
    win32api.keybd_event(VK_CODE[k],0 ,win32con.KEYEVENTF_KEYUP ,0) 
    time.sleep(.05)
    
def upperKey(k):
    win32api.keybd_event(VK_CODE['shift'], 0)
    time.sleep(.05)
    win32api.keybd_event(VK_CODE[k], 0)
    win32api.keybd_event(VK_CODE[k],0 ,win32con.KEYEVENTF_KEYUP ,0)
    time.sleep(.05)
    win32api.keybd_event(VK_CODE['shift'],0 ,win32con.KEYEVENTF_KEYUP ,0)

def writeString(string):
    for char in string:
        if char == ' ':
            pressKey('spacebar')
        elif char == '!':
            upperKey('1')
        elif char.isupper():
            upperKey(char.lower())
        else:
            pressKey(char)  
            
def mousePos(cord):
    win32api.SetCursorPos((cord[0] + Coor.X_PAD, cord[1] + Coor.Y_PAD))
    
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)

def leftUp(delay = 0.1):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(delay)

def clickPos(cord, delay=0):
    mousePos(cord)
    time.sleep(delay)
    leftClick()

def set_foreground_window(handle):
    win32gui.SetForegroundWindow(handle)