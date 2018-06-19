import pyautogui
import random
import time

def move():
        dir = ['left', 'right', 'down', 'up']
        pyautogui.keyDown('down')
        time.sleep(0.1)
        pyautogui.keyUp('down')
        for x in range(5):
                for d in dir:
                        pyautogui.keyDown(d)
                        time.sleep(0.1)
                        pyautogui.keyUp(d)
                        time.sleep(0.2)


def battle():
        pyautogui.press('up')
        time.sleep(0.2)
        pyautogui.press('left')
        time.sleep(0.2)

        for x in range(3):
                pyautogui.press('z')
                time.sleep(0.1)
                pyautogui.press('z')
                time.sleep(0.2)
                for y in range(20):
                        pyautogui.press('z')
                        time.sleep(0.1)
                        pyautogui.keyDown('x')
                        time.sleep(0.2)
                        pyautogui.keyUp('x')
                        time.sleep(0.1)

while True:
        move()
        time.sleep(9)
        battle()
