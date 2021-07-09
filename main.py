import pyautogui
import keyboard
import time
import winsound as sd

def beepsound():
    fr = 2000    # range : 37 ~ 32767
    du = 500     # 0.5 second
    sd.Beep(fr, du) # winsound.Beep(frequency, duration)

def reserve():
    reservation = pyautogui.locateCenterOnScreen('reservation.png')
    pyautogui.click(reservation[0], reservation[1])

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
#time.sleep(1)
#pyautogui.screenshot('refresh.png', region=(1560,857,30,30))

while True:
    if keyboard.is_pressed('S'):
        beepsound()
        break

refresh_location = pyautogui.locateCenterOnScreen('refresh.png')
pyautogui.click(refresh_location[0], refresh_location[1])
while True:
    if keyboard.is_pressed('E'):
        beepsound()
        break
    red = pyautogui.locateCenterOnScreen('red.png')
    blue = pyautogui.locateCenterOnScreen('blue.png')
    green = pyautogui.locateCenterOnScreen('green.png')
    #test = pyautogui.locateCenterOnScreen('test.png')

    if red or blue or green:
        print(red, blue, green)
        beepsound()
        #if test:
        #    pyautogui.click(test[0],test[1])
        #    reserve()
        #    break
        if red:
            pyautogui.click(red[0], red[1])
            reserve()
            break
        elif blue:
            pyautogui.click(blue[0], blue[1])
            reserve()
            break
        elif green:
            pyautogui.click(green[0], green[1])
            reserve()
            break

    if keyboard.is_pressed('E'):
        beepsound()
        break
    pyautogui.click(refresh_location[0], refresh_location[1])



