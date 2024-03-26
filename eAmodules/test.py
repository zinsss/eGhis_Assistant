import pyautogui
import time

while True:
    print(pyautogui.position())
    time.sleep(1)

# import pywinauto
# from pywinauto.application import Application
# # dd = Application().connect(title=":::::  질병관리청 현물공급 인플루엔자등록시스템  :::::").top_window()
# dd = Application().connect(title="::::: 질병관리청 현물공급 인플루엔자등록시스템 ::::: - Chrome").top_window()
# # dd.set_focus()
# dd.

# import pygetwindow as gw
# # dd = gw.getAllWindows()
# # for each in dd:
# #     print(each.title)
    
# ee = gw.getWindowsWithTitle('::::: 질병관리청 현물공급 인플루엔자등록시스템 ::::: - Chrome')[0]
# print(ee)
# ee.activate()