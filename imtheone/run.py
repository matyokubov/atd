import pyautogui
import cv2
import numpy as np
from PIL import ImageGrab
from time import sleep

def main():
    pyautogui.FAILSAFE = False
    def identifyCoordinateOfTarget(screen, target):
        target = cv2.imread(target)
        result = cv2.matchTemplate(screen, target, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val > 0.8:  # Adjust threshold for better/worse matches
            top_left = max_loc
            bottom_right = (top_left[0] + target.shape[1], top_left[1] + target.shape[0])
            center = ((top_left[0]+bottom_right[0])/2, (top_left[1]+bottom_right[1])/2)
            return center
        else: return False

    def sendMessage(text):
        pyautogui.typewrite(text)
        pyautogui.press('enter')
        quit()
        
    screen = cv2.cvtColor(np.array(ImageGrab.grab()), cv2.COLOR_RGB2BGR)

    # Go down if the post remains below
    goDown = identifyCoordinateOfTarget(screen, target="target1.png")
    if goDown:
        pyautogui.click(goDown[0], goDown[1], button='left')
        sleep(2)
        
    # Click "Leave a comment" button
    leaveComment = identifyCoordinateOfTarget(screen, target="target2.png")
    if leaveComment:
        pyautogui.click(leaveComment[0], leaveComment[1], button='left')
        sleep(10)
        sendMessage("1")
    
if __name__ == '__main__':
    while True: main() # Repeat the algorithm infinitely

