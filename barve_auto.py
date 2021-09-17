import os
import pyautogui
from time import sleep

pyautogui.hotkey('altleft', 'tab')
sleep(0.5)
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.click(currentMouseX, currentMouseY)
pyautogui.press('f6')
sleep(0.2)
pyautogui.write('test test')
sleep(0.3)
pyautogui.press('return')
sleep(0.3)
pyautogui.write('IDNUM')
pyautogui.hotkey('tab')
pyautogui.write('PASSWORD')
pyautogui.hotkey('enter')
