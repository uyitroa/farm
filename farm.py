import sys
sys.path.append("/usr/local/lib/python2.7/site-packages/")
import pyautogui
import random
import time

def move():
	dir = ['left', 'right', 'down', 'up']
	pyautogui.keyDown('up')
	time.sleep(0.1)
	pyautogui.keyUp('up')
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

	for x in range(2):
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
