import time
import keyboard
import pyautogui
import cv2 as cv
import numpy as np
import os
from pyautogui import locateOnScreen as LoS
from random import randint

# Pixel coordinates 
area = (528, 124, 1243, 1142)
successarea = (697, 980, 1250, 230)\

while True:
# Casting
    READY = LoS('ready.png', confidence=.8, region=area)
    if READY:
        print("Casting in 5 seconds...")
        time.sleep(5)
        pyautogui.mouseDown()
        time.sleep(1.9)
        pyautogui.mouseUp()
        time.sleep(1)

        endREADY = None
        while endREADY == None:
            endREADY = LoS('hook.jpg', confidence= .8, region=area)

# Waiting for the hook
    HOOK = LoS('hook.jpg', confidence= .8, region=area)
    if HOOK:
        print('HOOKED')
        pyautogui.click()
        time.sleep(1)

        endHOOK = None
        while endHOOK == None:
            endHOOK = LoS('one.png', confidence= .8, region=area)
       
# Reel tolerances 1
    ONE = LoS('one.png', confidence= .8, region=area)
    if ONE:
        print("25% Tight")
        pyautogui.mouseDown()

        endONE = None
        while endONE == None:
            endONE = LoS('four.png', confidence= .8, region=area)

# Reel tolerances 2
    TWO = LoS('two.png', confidence= .8, region=area)
    if TWO:
        print("50% Tight")
        pyautogui.mouseDown()

        endTWO = None
        while endTWO == None:
            endTWO = LoS('four.png', confidence= .8, region=area)

# Reel tolerances 3
    THREE = LoS('three.png', confidence= .8, region=area)
    if THREE:
        print("75% Tight")
        pyautogui.mouseDown()
       
        endTHREE = None
        while endTHREE == None:
            endTHREE = LoS('four.png', confidence= .8, region=area)

# Loosen 
    TIGHT = LoS('four.png', confidence= .8, region=area)
    if TIGHT:
        print("WARNING GETTING TIGHT!")
        pyautogui.mouseUp()
       
        endTIGHT = None
        while endTIGHT == None:
            endTIGHT = LoS('three.png', confidence= .8, region=area)

# About to Snap 
    SNAP = LoS('snap.png', confidence= .8, region=area)
    if SNAP:
        print("WARNING SEVERE TIGHTNESS")
        pyautogui.mouseUp()
       
        endSNAP = None
        while endSNAP == None:
            endSNAP = LoS('two.png', confidence= 1, region=area)

# Caught NOT WORKING
    CATCH = LoS('catch.png', confidence= .8, region=area)
    if CATCH:
        print("Nice catch!")
        pyautogui.click(clicks=3)
        time.sleep(10)
    
        endCATCH = None
        while endCATCH == None:
            endCATCH != LoS('ready.png', confidence= .8, region=area)