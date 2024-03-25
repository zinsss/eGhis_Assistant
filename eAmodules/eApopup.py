from PySide6.QtWidgets import QMessageBox, QDialogButtonBox, QInputDialog, QLineEdit, QPlainTextEdit
from PySide6.QtCore import Qt, QTimer

from eAmodules import eAstyles


## 경고 알림. yes_no : bool 값으로 버튼 한개 또는 2개.
#: ok = confbox.exec이 버튼 인덱스를 return, 순서가 Yes/Close이기 때문에, 
#: yes 선택시 ok = 0 (False) so, not ok를 return.
def warning(text:str, yes_no:bool = False):
    warnbox = QMessageBox()
    warnbox.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
    warnbox.setStyleSheet(eAstyles.WARNBOX)
    warnbox.setText(
        "<span style='font-family:Lucida Sans;font-weight:600;font-style:italic;font-size:18pt;color:#aa4252;'>WARNING !!!</span>"
    )
    warnbox.setInformativeText(text)
    if yes_no:
        warnbox.addButton('YES', QMessageBox.YesRole)
        warnbox.addButton('NO', QMessageBox.NoRole)
    else: warnbox.addButton('OK', QMessageBox.YesRole)
    ok = warnbox.exec()
    return not ok


## 단순 알림. 버튼 한개, return값 필요없는 경우.
def notify(text:str):
    notibox = QMessageBox()
    notibox.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
    notibox.setStyleSheet(eAstyles.NOTIBOX)
    notibox.setText(
        "<span style='font-family:Lucida Sans;font-weight:600;font-style:italic;font-size:18pt;color:#3b4252;'>Notifying !!!</span>"
    )
    notibox.setInformativeText(text)
    notibox.addButton('OK', QMessageBox.NoRole)
    ok = notibox.exec()
    

## Yes or No만 필요한 경우.
#: warning + yes_no = True와 겹칠 수 있지만, 색깔이 다름. 일반적 메세지에 적용 가능.
#: ok = confbox.exec이 버튼 인덱스를 return, 순서가 Yes/Close이기 때문에, not ok를 return.
def confirm(text:str):
    confbox = QMessageBox()
    confbox.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
    confbox.setStyleSheet(eAstyles.CONFBOX)
    confbox.setText(
        "<span style='font-family:Lucida Sans;font-weight:600;font-style:italic;font-size:18pt;color:#3b4252;'>Please Confirm !!!</span>"
    )
    confbox.setInformativeText(text)
    confbox.addButton('YES', QMessageBox.YesRole)
    confbox.addButton('NO', QMessageBox.NoRole)
    ok = confbox.exec()
    return not ok


def timed_confirm(text:str, msec:int):
    '''
    카운트 다운을, timer.remainingTime()으로 하면 훨씬 깨끗하겠지만,
    컴퓨터 또는 eGhisAssistant의 loading으로 약간의 delay라도 있는 경우에는 이쁘게 되지를 않음.
    (예를 들어, 5..4..3..3..1..0)
    따라서 msec을 sec으로 변환 한 후, 매초마다 1을 뺀 값을 카운트 다운 하는 방식으로..
    '''
    count_down = msec // 1000
    #~~~ Building MessageBox and Set Styles ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    confbox = QMessageBox()
    confbox.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
    confbox.setText(
            f"<span style='font-family:Lucida Sans;font-weight:600;font-style:italic;font-size:18pt;color:#3b4252;'>Waiting..for {count_down} seconds</span>"
        )
    confbox.setStyleSheet(eAstyles.CONFBOX)
    confbox.setInformativeText(text)
    default_button = confbox.addButton('YES', QMessageBox.YesRole)
    confbox.addButton('NO', QMessageBox.NoRole)
    # Set Default Button for AnimatedClicking after count down.
    confbox.setDefaultButton(default_button)
    
    #~~~ Timers x2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # First Timer, for msec before AnimatingClick
    timer = QTimer()
    timer.setSingleShot(True)
    timer.timeout.connect(confbox.defaultButton().animateClick)
    timer.start(msec)
    # Second Timer, for updating count down gui
    updater = QTimer()
    updater.setSingleShot(False)
    
    def update_title():
        nonlocal count_down #Nested function에서 상위 function의 variable을 사용하기 위함.
        if count_down > 0:
            count_down -= 1
        confbox.setText(
            f"<span style='font-family:Lucida Sans;font-weight:600;font-style:italic;font-size:18pt;color:#3b4252;'>Waiting..for {count_down} seconds</span>"
        )
    
    updater.timeout.connect(update_title)
    updater.start(1000)
    
    # Execute and Retrieve Result 
    ok = confbox.exec()
    
    # Clear non singleShot QTimer (updater) for resource management
    updater.stop()
    
    # Returns *not* ok because order of the buttons were [YES, NO]. Hence 'YES' will return 0.
    # For code readability, yes to 1 (True as bool), no to 0 (False if bool).
    return not ok


#: Big window size, confirm popup. For multiline text previews.
def confirm_big(text:str):
    confbox = QMessageBox()
    confbox.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
    confbox.setStyleSheet(eAstyles.CONFBOX_BIG)
    confbox.setText(
        "<span style='font-family:Lucida Sans;font-weight:600;font-style:italic;font-size:18pt;color:#3b4252;'>Please Confirm !!!</span>"
    )
    confbox.setInformativeText(text)
    confbox.addButton('YES', QMessageBox.YesRole)
    confbox.addButton('NO', QMessageBox.NoRole)
    ok = confbox.exec()
    return not ok   


## Menu. buttons를 리스트값으로 주는 모든 항목에 대해서 버튼을 생성하고, click한 button text를 return.
def menu(title:str, buttons:list):
    msgbox = QMessageBox()
    msgbox.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
    # QMessageBox의 qdialogbuttonbox는 기본설정이 horizontal.
    # 새로운 클래스를 생성할 수 있지만, object이름을 findchild하여 설정만 바꿈.
    qt_msgbox_buttonbox = msgbox.findChild(QDialogButtonBox, "qt_msgbox_buttonbox")
    qt_msgbox_buttonbox.setOrientation(Qt.Vertical)
    # 기본 스타일 설정.
    msgbox.setStyleSheet(eAstyles.MENUBOX)
    msgbox.setText(f'## {title}')
    msgbox.setIcon(QMessageBox.NoIcon)
    # for loop으로 전달받은 리스트의 모든 항목에 대해 버튼을 추가하기.
    for button in buttons:
        msgbox.addButton(button, QMessageBox.YesRole)
    # 마지막에 '닫기'버튼을 만들어주고, 해당 버튼을 기본버튼으로 선택.   
    close_btn = msgbox.addButton('CLOSE', QMessageBox.NoRole)
    close_btn.setDefault(True)
    # CLOSE 버튼을 추가했기때문에, CLOSE를 클릭하면 추후 버튼 이름 값 리턴할때 인덱스 에러.
    # 따라서 미리 buttons 리스트에 CLOSE를 추가해준다.
    buttons.append('CLOSE')    
    selected = msgbox.exec()
    choice = buttons[selected]
    return choice

## Reminders Status Select Menu. 
def reminders_menu(buttons:list, disable:int = None):
    msgbox = QMessageBox()
    msgbox.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
    # QMessageBox의 qdialogbuttonbox는 기본설정이 horizontal.
    # 새로운 클래스를 생성할 수 있지만, object이름을 findchild하여 설정만 바꿈.
    qt_msgbox_buttonbox = msgbox.findChild(QDialogButtonBox, "qt_msgbox_buttonbox")
    qt_msgbox_buttonbox.setOrientation(Qt.Vertical)
    # 기본 스타일 설정.
    msgbox.setIcon(QMessageBox.NoIcon)
    msgbox.setStyleSheet(eAstyles.REMINDERS_MENU)
    msgbox.setText("# Status Update")
    # for loop으로 전달받은 리스트의 모든 항목에 대해 버튼을 추가하기.
    for button in buttons:
        msgbox.addButton(button, QMessageBox.YesRole)
    close_btn = msgbox.addButton('CLOSE', QMessageBox.NoRole)
    close_btn.setDefault(True)
    buttons.append('CLOSE')    
    choice = msgbox.exec()
    selected = buttons[choice]
    return selected

## Single line text input. (QLineEdit)
def get_text(text:str, default_text:str="", password:bool = False):
    inputbox = QInputDialog()
    inputbox.setWindowFlags(Qt.FramelessWindowHint)
    inputbox.setStyleSheet(eAstyles.INPUTBOX)
    inputbox.setLabelText(text)
    inputbox.setTextValue(default_text)
    if password: inputbox.setTextEchoMode(QLineEdit.Password)    
    inputbox.setInputMode(QInputDialog.TextInput)
    ok = inputbox.exec()
    if not ok: return
    else: return inputbox.textValue()

## Single line text input, long text
def get_text_big(text:str, default_text:str="", password:bool = False):
    inputbox = QInputDialog()
    inputbox.setWindowFlags(Qt.FramelessWindowHint)
    inputbox.setStyleSheet(eAstyles.INPUTBOX_BIG)
    inputbox.setLabelText(text)
    inputbox.setTextValue(default_text)
    if password: inputbox.setTextEchoMode(QLineEdit.Password)    
    inputbox.setInputMode(QInputDialog.TextInput)
    ok = inputbox.exec()
    if not ok: return
    else: return inputbox.textValue()

## Multi-line text input. (QPlainTextEdit)
def get_multiline_text(title:str, default_text:str = ""):
    inputbox = QInputDialog()
    inputbox.setWindowFlags(Qt.FramelessWindowHint)
    inputbox.setStyleSheet(eAstyles.MULTILINEBOX)
    inputbox.setLabelText(title)
    inputbox.setTextValue(default_text)
    inputbox.setInputMode(QInputDialog.TextInput)
    inputbox.setOption(QInputDialog.UsePlainTextEditForTextInput)
    pte = inputbox.findChild(QPlainTextEdit)
    pte.setLineWrapMode(QPlainTextEdit.WidgetWidth)
    ok = inputbox.exec()
    if not ok: return
    else: return inputbox.textValue()

## Get Integer input 
def get_int(self, content:str, default_val:int=0, min_val:int=0, max_val:int=100, step_by:int=1):
    inputbox = QInputDialog()
    inputbox.setWindowFlags(Qt.FramelessWindowHint)
    inputbox.setStyleSheet(eAstyles.INPUTBOX)
    inputbox.setLabelText(content)
    inputbox.setIntValue(default_val)
    inputbox.setIntMinimum(min_val)
    inputbox.setIntMaximum(max_val)
    inputbox.setIntStep(step_by)    
    inputbox.setInputMode(QInputDialog.IntInput)
    ok = inputbox.exec()
    if not ok: return
    else: return inputbox.intValue()