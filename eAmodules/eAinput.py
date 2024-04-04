import pyautogui
import random
from pywinauto import keyboard

from PySide6.QtGui import QClipboard

from eAmodules import eAwinauto, eApopup

# * This file is mostly used only for the developer's readability of the main code of the app.
# * Which means, this is COMPLETELY UNNECESSARY MODULE.

#: PyAutoGui does not type strings written in Korean.
#: PyWinAuto's keyboard modules can. Hence some use pyautogui(easier useage) and some use pywinauto.

# General input methods predefined.


def press_key(key: str):
    pyautogui.press(key)


def press_keys(*keys: str):
    keys = list(keys)
    pyautogui.press(keys)


def repeat_key(key: str, repeat: int):
    pyautogui.press(key, presses=repeat)


def write(txt: str):
    keyboard.send_keys(keys=txt, with_spaces=True,
                       with_newlines=True, pause=0.02)


def write_enter(txt: str):
    keyboard.send_keys(keys=txt, with_spaces=True,
                       with_newlines=True, pause=0.02)
    pyautogui.press('enter')


def mouse_at(x, y):
    pyautogui.moveTo(x, y)


def click_at(x, y):
    pyautogui.click(x, y)


def db_click_at(x, y):
    pyautogui.click(x, y, clicks=2)


def rt_click_at(x, y):
    pyautogui.click(x, y, button='Right')


def hotkeys(mod_key, key):
    with pyautogui.hold(mod_key):
        pyautogui.press(key)

# By some reason hotkeys with modifier as shift act strangely in pyautogui.


def shift_hotkeys(key: str):
    pyautogui.keyDown('shiftleft')
    pyautogui.keyDown('shiftright')
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)
    pyautogui.keyUp('shiftright')
    pyautogui.keyUp('shiftleft')


def copy_it(txt: str):
    clipboard = QClipboard()
    clipboard.setText(txt)


def paste_it():
    with pyautogui.hold('ctrl'):
        pyautogui.press('v')

# Copy and Paste in single function for better readability of code;
# Also included 'to_sx' option to call eghis and paste to symptoms.


def copy_paste_it(txt: str, to_sx: bool = False):
    copy_it(txt)
    if to_sx:
        eAwinauto.to_eghis()
        pyautogui.press('f1')
    else:
        with pyautogui.hold('alt'):
            pyautogui.press('tab')
    paste_it()


# * eGhis Shortcuts
# TODO Overlap between copy_paste_it(txt, to_sx=True).
def sx_cnp(text):
    if type(text) is str:
        copy_it(text)
    elif type(text) is list:
        copy_it(random.choice(text))
    eAwinauto.to_eghis()
    buy_time(0.2)
    pyautogui.press(['f1', 'enter'])
    paste_it()
    pyautogui.press('enter')

# Can write in Korean using pywinauto.keyboard while pyautogui can't
# Only available options for pyautogui is copy and paste.


def sx_write(text):
    eAwinauto.to_eghis()
    buy_time(0.2)
    pyautogui.press(['f1', 'enter'])
    write_enter(text)
    pyautogui.press('enter')


def icd_delete_all():
    eAwinauto.to_eghis()
    buy_time(0.2)
    press_key('f2')
    shift_hotkeys('del')


def icd_input(icd: str):
    copy_it(icd)
    eAwinauto.to_eghis()
    buy_time(0.2)
    pyautogui.press('f2')
    paste_it()
    pyautogui.press('enter')


def rx_input(rx: str, regimen: tuple[int, int, int] = None):
    eAwinauto.to_eghis()
    buy_time(0.2)
    pyautogui.press('f3')
    write_enter(rx)
    if regimen:
        for i in regimen:
            write_enter(str(i))


def rx_jx999(text: str):
    keyboard.send_keys("^t" + text + "{F5}")


def rx_ins(ins_type: str):
    '''ins_type: 00 -> 보험급여, 01 -> 비보험, 02 -> 100/100'''
    hotkeys('ctrl', 'b')
    write_enter(ins_type)
    repeat_key('enter', repeat=2)


# * Find location of image. Area for faster process
# TODO Need to figure what's needed and what's not.

def find_xy(png: str, area: tuple[int, int, int, int]):
    xy = pyautogui.locateCenterOnScreen(image=png, region=area)
    print(xy)
    return xy


def find_if_exists(png: str, area: tuple[int, int, int, int]):
    xy = pyautogui.locateCenterOnScreen(
        image=png, region=area, grayscale=True, confidence=0.8)
    if xy is None:
        return False
    else:
        return True


def find_and_click(png: str, area: tuple[int, int, int, int], rt_click: bool = False, clicks: int = 1):
    if rt_click:
        button = 'Right'
    else:
        button = 'Left'
    xy = pyautogui.locateCenterOnScreen(
        image=png, region=area, grayscale=True, confidence=0.8)
    if xy is None:
        eApopup.notify(text="대상을 찾을 수 없습니다.")
        return
    else:
        pyautogui.click(*xy, button=button, clicks=clicks)


# * Although creating QEventLoop and QTimer for time.sleep functionality won't affect GUI,
# * Blocking user input(if nescessary) and running below function seems to be easier way.
def buy_time(sec: float):
    pyautogui.move(-30 * sec, 0, duration=sec / 4)
    pyautogui.move(60 * sec, 0, duration=sec / 2)
    pyautogui.move(-30 * sec, 0, duration=sec / 4)
