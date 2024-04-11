import pyautogui
from PIL import ImageGrab
from time import sleep

pyautogui.FAILSAFE = False
hasNoOneReplied = lambda: True if ImageGrab.grab(bbox=(789, 689, 790, 690)).load()[0,0] == (24, 37, 51) else False
temp_ = hasNoOneReplied()

while not temp_:
    sleep(2)
    temp_ = hasNoOneReplied()

pyautogui.click(790, 690, button='left')
sleep(3)
pyautogui.typewrite("I'm 1 all the time")
pyautogui.press('enter')
print("Succeeded")
