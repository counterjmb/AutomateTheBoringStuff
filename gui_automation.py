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


##keyboard functions
#pyautogui.click(636,982)
#interval for delay between each key press
#pyautogui.typewrite('Hello Wold', interval=0.2)
#pyautogui.typewrite(['left', 'left', 'r'])
#get all keys
#print(pyautogui.KEYBOARD_KEYS)
#pyautogui.press('f1')
#hotkeys
#pyautogui.hotkey('ctrl', 'o')


#screen shots and image recognition
#create pillow image object
#more pillow methods: https://automatetheboringstuff.com/chapter17
pyautogui.screenshot('screenshot.png')
#locate in screenshot another image
#retuns x, y, width, hieght
print(pyautogui.locateOnScreen('windows_button.png'))
#just coordinates
print(pyautogui.locateCenterOnScreen('windows_button.png'))
