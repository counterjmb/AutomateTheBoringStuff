#python -m pip install pyautogui
import pyautogui

##mouse controlling
#screen is 0,0 in upper left then then Y going down, X across
print('Screen Resolution: ' + str(pyautogui.size()))
pyautogui.moveTo(100,100)
pyautogui.moveTo(400,100, duration=1.5)
pyautogui.moveRel(100,100, duration=2)
#get current position
print(pyautogui.position())
pyautogui.click()
pyautogui.click(100,100)
#double, right, middle also works
#drag, dragRel functions 

#get position live updates terminal: 
#open terminal
#start python
#import pyautogui
#pyautogui.displayMousePosition()