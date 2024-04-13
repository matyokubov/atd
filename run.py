import pyautogui
from PIL import ImageGrab
from time import sleep

def main():
    pyautogui.FAILSAFE = False
    def hasNoOneReplied():
        darkColorOfThePost = ImageGrab.grab(bbox=(789, 689, 790, 690)).load()[0,0] == (24, 37, 51)
        blueColorNextToTheDarkColor = ImageGrab.grab(bbox=(816, 696, 817, 697)).load()[0,0] == (106, 178, 242)
        if darkColorOfThePost and blueColorNextToTheDarkColor:
            return True
        else: return False
    
    # Waiting for the next post that noone has commented it yet
    temp_ = hasNoOneReplied()
    while not temp_:
        sleep(2)
        temp_ = hasNoOneReplied()

    # To enter the discussion
    pyautogui.click(790, 690, button='left')
    sleep(10) # Waiting exception to internet slowness
    
    # Typing
    pyautogui.typewrite("I'm 1 all the time")
    pyautogui.press('enter')
    
    # Go back to the channel
    pyautogui.click(780, 120, button='left')
    print("Succeeded")
    
if __name__ == '__main__':
    while True: main() # Repeat the algorithm infinitely
