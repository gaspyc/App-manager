import win32api, win32con, time, keyboard, pyautogui

"""
mousepos - rastrea el cursor
click    - click en pixel definido, click en el lugar si no se define
hover    - fuerza info del elemento apuntado
wintab   -
alttab   -
"""

def mousepos():
    x, y = win32api.GetCursorPos()
    print(x,y)

def click(x=None,y=None):
    if x and y:
        win32api.SetCursorPos((x,y))
    time.sleep(.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def hover(x=None,y=None):
    if x and y:
        win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 2, 2, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -2, -2, 0, 0)
    time.sleep(.5)

def wintab():
    keyboard.press_and_release('win+tab')
    time.sleep(2)

def alttab():
    keyboard.press_and_release('alt+tab')
    time.sleep(2)