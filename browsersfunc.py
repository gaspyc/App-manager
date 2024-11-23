import time, keyboard, pyautogui
from windowsfunc import *

"""
reload      - recarga la pagina
openbrowser - abre navegadores y su incognito
searchib    - 
"""

def reload(x=None,y=None):
    if x and y:
        click(x,y)
    time.sleep(.5)
    keyboard.press_and_release('f5')

def openbrowser(z,url):
    time.sleep(.5)
    keyboard.press_and_release('win')
    time.sleep(.5)
    pyautogui.write(str(z))
    time.sleep(1.5)
    keyboard.press_and_release('enter')
    time.sleep(1.5)
    searchib(url)
    time.sleep(1.5)
    if z[-1] == ('x' or 'v'):
        keyboard.press_and_release('ctrl+shift+p')
    else:
        keyboard.press_and_release('ctrl+shift+n')
    time.sleep(1.5)
    searchib(url)

def searchib(url):
    time.sleep(.5)
    pyautogui.write(url)
    time.sleep(.5)
    keyboard.press_and_release('enter')

def searchAcc(linea_num):
    with open(r'C:\coding\python\afk\scripts\data.txt', 'r', encoding='utf-8') as f:
        for i, linea in enumerate(f):
            pos = linea.find('@')        
            if i == linea_num - 1:
                if linea_num%2 != 0:
                    keyboard.press_and_release('altgr+q')
                    if linea[pos+1] == 'g':
                        pyautogui.write('gmail.com')
                    else:
                        pyautogui.write('outlook.com')
                    keyboard.press_and_release('home')
                pyautogui.write(linea[:pos])

def login(index,field):
    click(*field)
    searchAcc(index)
    time.sleep(1.5)
    searchAcc(index+1)
    time.sleep(1)
    keyboard.press_and_release('enter')

def GreenButton_Detector(x,y):
    ss = pyautogui.screenshot()
    r,g,b = ss.getpixel((x,y))
    print(r,g,b)
    if g == 135:
        click(x,y)

if __name__ == '__main__':
    print('aca no')
