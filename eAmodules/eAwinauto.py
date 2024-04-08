import warnings
warnings.simplefilter('ignore', category=UserWarning)

import pywinauto
from pywinauto.application import Application

import pygetwindow
import pyautogui

import main
from eAmodules import eAinput, eApopup, eAxys, eAutils

# UIA용 아직 많이 느려서.. 더 많은 정보를 받아올수는 있지만..
# app = Application(backend='uia').connect(path="C:\Mcc\Clinic\eGhis.exe")
# opd = app.window(title="eGhis  통합", auto_id="MDIContainer", control_type="Window")
# order = opd.child_window(title="[등록] 외래진료", auto_id="H2OpdOrderMain", control_type="Window")
# pnlorder = order.child_window(auto_id='pnlOrder')
# codenames = grid.descendants(title="코드명", control_type="DataItem")
# codeTexts = [codes.legacy_properties()['Value'] for codes in codenames]
# print(codeTexts)

# eGhis EMR Related.
app = Application().connect(path="C:\Mcc\Clinic\eGhis.exe")
eghis = app.top_window()
eghis_opd = eghis.child_window(auto_id="H2OpdOrder")


# eGhis 실행 여부 확인 및 process id 저장. 최초 eGhis Assistant 실행시 실행될 함수.
def find_eghis():
    try:
        app = Application().connect(path="C:\Mcc\Clinic\eGhis.exe")
        eghis = app.top_window()
        eghis_opd = eghis.child_window(auto_id="H2OpdOrder")
    except pywinauto.application.ProcessNotFoundError:
        print("eGhis not running")
        return
    return app, eghis, eghis_opd


# eGhis로 window focus 이동.
# eGhis 재 실행등의 이유로 process id가 다르거나 없다면, 다시 설정하기.
def to_eghis():
    global app, eghis, eghis_opd
    if eghis.exists():
        current_mouse = pyautogui.position()
        eghis.set_focus()
        pyautogui.moveTo(current_mouse)
    else:
        app, eghis, eghis_opd = find_eghis()
        eghis.set_focus()


# 보험 자격 조회 및 비보진료하기
def eghis_insurance(action: str = "check"):
    '''
    action: check -> 자격조회, no_ins -> 일반진료
    '''
    to_eghis()
    eghis_opd.child_window(auto_id="lblInsurance").click()
    if action == "check":
        pywinauto.keyboard.send_keys(keys="{DOWN},{ENTER}")
    elif action == "no_ins":
        pywinauto.keyboard.send_keys(keys="{DOWN}{DOWN}{DOWN}{DOWN}{ENTER}{ENTER}")
        eAinput.buy_time(sec=1)
        pywinauto.keyboard.send_keys(keys="{ENTER}")
        eAinput.buy_time(sec=2)
        pywinauto.keyboard.send_keys(keys="{F3}{UP}{DELETE}{ENTER}")
    else:
        return


def eghis_docs():
    menu_bar = eghis_opd.child_window(auto_id="mnuOrder")
    menu_bar.print_control_identifiers()


#: 환자정보 툴팁 나오는 위치로 이동
def eghis_pt_tooltip():
    show_tt = eghis_opd.child_window(auto_id="lblReceptNo").rectangle().mid_point()
    pywinauto.mouse.move(show_tt)


#: eGhis 증상에 입력하기.
def eghis_add_to_sx(text: str):
    symp = eghis_opd.child_window(auto_id="txtSymp").child_window(auto_id="mcctextBox").texts()[0].rstrip()
    symp = f'{symp}\r\n\r\n{text}'
    eghis_opd.child_window(auto_id="txtSymp").child_window(auto_id="mcctextBox").set_text(symp)


#: 초진 여부 확인 및 return Boolean
def eghis_check_cj():
    '''Returns True if 초진. False if 재진'''
    cjjj = eghis_opd.child_window(auto_id="btnChoJae", control_type="Mcc.Series.Controls.MccLabel").texts()[0]
    if cjjj == '초진':
        return True
    elif cjjj == '재진':
        return False
    else:
        print("Error")


#: 초진재진버튼 누르기
def eghis_toggle_cjjj():
    eghis_opd.child_window(auto_id="btnChoJae", control_type="Mcc.Series.Controls.MccLabel").click()


#: eGhis 내 달력에서 오늘 찾기 + 우클릭.
def eghis_today_right_click(self):
    today_dd = int(self.infos.date_today.toString("d"))
    cal_today = eghis_opd.child_window(auto_id="tblMonth").child_window(title=str(today_dd))
    cal_today.right_click_input()


#: 청구안함
def eghis_do_not_claim():
    no_claim = eghis_opd.child_window(title="청구안함", auto_id="chkInspTargetYn",
                                      control_type="System.Windows.Forms.CheckBox")
    if not no_claim.is_checked():
        no_claim.click()


#: 진료대기,보류,완료 control
def tab_wait_list(tab: int, first_in_line: bool = True):
    '''tab: 1 -> 대기, 3 -> 보류, 5 -> 예약, 7 -> 완료, 9 -> 취소
first_in_line: True (default) -> 첫번째 목록 더블클릭\n
!!! 1,3,5,7,9 이외의 숫자는 return None\n
UIA backend는 각각의 탭으로 접근가능.\n
win32에서는 각각의 탭까지 접근이 불가하고,\n
탭이 있는 창까지는 접근가능. 탭은 총 5개가 설정되어있고\n
대략적으로 각각 20퍼센트씩 차지한다고 가정하면,\n
탭의 위치, 탭의 넓이를 알수 있으면 (rectangle 함수로..)\n
좌측에서 넓이의 10%, 30%, 50%, 70%, 90%를 클릭하면 됨.\n
'''
    to_eghis()

    if tab not in [1, 3, 5, 7, 9]:
        return
    tab_window_rect = eghis_opd.child_window(auto_id='tabWait').rectangle()
    tab_l, tab_t = tab_window_rect.left, tab_window_rect.top
    tab_w, tab_h = tab_window_rect.width(), tab_window_rect.height()
    tab_v_mid = tab_t + int(tab_h / 2)
    tab_w_10p = int(tab_w / 10)
    pywinauto.mouse.click(coords=(tab_l + (tab * tab_w_10p), tab_v_mid))
    if first_in_line:
        pywinauto.mouse.double_click(coords=(tab_l + (tab * tab_w_10p), tab_v_mid + 40))


#: 환자 기본정보 불러오기. (환자정보창 열고..)
def current_ptinfo_window():
    if not eghis.exists():
        return "이지스를 먼저 실행하세요."

    to_eghis()

    # Predefined Dictionary for Return
    currentPTinfo = {
        "ptno": "",
        "ptname": "",
        "ptsex": "",
        "ptage": "",
        "ptjmno": "",
        "ptbirthd": "",
        "ptphone": "",
        "pttel": "",
        "ptzipcode": "",
        "ptaddress1": "",
        "ptaddress2": "",
    }

    eghis_opd.child_window(auto_id="lblChartNm").click()
    eAinput.buy_time(1.5)
    ptinfoMain = app.window(auto_id="H0ComPatientInfo")
    ptinfo_win1 = ptinfoMain.child_window(auto_id="mccTableLayoutPanel1")
    ptinfo_win2 = ptinfoMain.child_window(auto_id="pnlTop")

    currentPTinfo['ptno'] = ptinfo_win1.window(auto_id="txtPtntNo").texts()[0]
    currentPTinfo['ptname'] = ptinfo_win1.window(auto_id="txtPtntNm").texts()[0]
    currentPTinfo['ptsex'] = ptinfo_win1.window(auto_id="txtSexAge").texts()[0].split(" / ")[0]
    currentPTinfo['ptage'] = ptinfo_win1.window(auto_id="txtSexAge").texts()[0].split(" / ")[1]
    currentPTinfo['ptjmno'] = ptinfo_win2.window(auto_id="mbxPeoid").child_window(
        control_type="System.Windows.Forms.MaskedTextBox").texts()[0]
    currentPTinfo['ptbirthd'] = ptinfo_win2.child_window(auto_id="dtpBirthYmd").child_window(
        control_type="System.Windows.Forms.TextBox").texts()[0]
    currentPTinfo['ptphone'] = ptinfo_win2.child_window(auto_id="mbxHp").child_window(
        control_type="System.Windows.Forms.MaskedTextBox").texts()[0]
    currentPTinfo['pttel'] = ptinfo_win2.child_window(auto_id="mbxTel").child_window(
        control_type="System.Windows.Forms.MaskedTextBox").texts()[0]
    currentPTinfo['ptzipcode'] = ptinfo_win2.child_window(auto_id="txtPostNo").child_window(
        control_type="System.Windows.Forms.TextBox").texts()[0]
    currentPTinfo['ptaddress1'] = ptinfo_win2.child_window(auto_id="txtAddr").child_window(
        control_type="System.Windows.Forms.TextBox").texts()[0]
    currentPTinfo['ptaddress2'] = ptinfo_win2.child_window(auto_id="txtAddrDetail").child_window(
        control_type="System.Windows.Forms.TextBox").texts()[0]
    print(currentPTinfo)

    return currentPTinfo


#: 환자 기본정보 불러오기. (환자정보창 열지않고..)
def current_ptinfo():
    if not eghis.exists():
        return "이지스를 먼저 실행하세요."

    # Predefined Dictionary for Return
    currentPTinfo = {
        "ptno": "",
        "ptname": "",
        "ptsex": "",
        "ptage": "",
        "ptjmno": "",
        "ptbirthd": "",
        "ptphone": "",
        "ptzipcode": "",
        "ptaddress": "",
    }

    # Focus on eGhis.
    to_eghis()

    # Places in eGhis Main window
    main_ptno = eghis_opd.child_window(auto_id="lblChartNo")
    main_ptname = eghis_opd.child_window(auto_id="lblChartNm")
    main_ptsexage = eghis_opd.child_window(auto_id="lblSexAge", top_level_only=True)
    eghis_pt_tooltip()

    try:
        main_tooltip = app.window(class_name="WindowsForms10.tooltips_class32.app.0.1ca0192_r8_ad1").texts()
        main_ptjmno = (main_tooltip[0].split('주민등록번호 : ')[1]).split('\r\n집 ')[0]
    except pywinauto.findwindows.ElementNotFoundError:
        return

    main_ptphone = eghis_opd.child_window(auto_id="txtPhoneNo").child_window(
        auto_id="textBox", control_type="System.Windows.Forms.MaskedTextBox")
    main_ptaddress = eghis_opd.child_window(auto_id="lblAddress", control_type="Mcc.Series.Controls.MccLabel")

    # Actual Values from eGhis Main Window
    try:
        currentPTinfo["ptno"] = main_ptno.texts()[0]
        currentPTinfo["ptname"] = main_ptname.texts()[0]
        currentPTinfo["ptsex"] = main_ptsexage.texts()[0].split("/")[0]
        currentPTinfo["ptage"] = main_ptsexage.texts()[0].split("/")[1][:-1]
        currentPTinfo["ptjmno"] = main_ptjmno
        currentPTinfo["ptbirthd"] = eAutils.jmno_to_birthd(main_ptjmno)
        currentPTinfo["ptphone"] = main_ptphone.texts()[0]
        currentPTinfo["ptzipcode"] = main_ptaddress.texts()[0].rstrip().replace("[", "").split("] ")[0]
        currentPTinfo["ptaddress"] = main_ptaddress.texts()[0].rstrip().replace("[", "").split("] ")[1]
    except IndexError:
        pass
    except TypeError:
        pass

    # Verify if Patient is currently selected in eGhis.
    if main_ptno.texts()[0] == "":
        eApopup.warning(text="환자를 먼저 선택해주세요")
        return
    if main_ptaddress.texts()[0].rstrip().replace("[", "").split("] ")[0] == "":
        ok = eApopup.confirm(text="주소가 정확하지 않습니다.\n그래도 진행할까요?")
        if not ok:
            return

    return currentPTinfo


# 환자이름 가져오기. 환자정보 가져올 필요성 있는지 확인하기.
# 동명이인 2번 연속으로 볼 가능성은 적으니까.. 일단은 만족하자.
# TODO 그래도 나중에 시간될때 보완은 해보자.
def patient_change():
    if not eghis_opd.exists():
        return
    try:
        return eghis_opd.child_window(auto_id="lblChartNm").texts()[0]
    except pywinauto.remote_memory_block.AccessDenied:
        return ""


# 환자정보 가져오기. '***' 유무 확인. *** = 알러지 또는 환자관련 중요사항.
def get_pt_memo():
    if not eghis_opd.exists():
        return
    pt_memo = ""
    try:
        pt_memo = eghis_opd.child_window(auto_id="txtPtntMemo").child_window(
            control_type="System.Windows.Forms.TextBox").texts()[0]
    except pywinauto.remote_memory_block.AccessDenied:
        pass
    return pt_memo


# eGhis 종료, 설정에 따라 backup 및 backup 후 컴퓨터 종료.
def close_eghis(self):
    if not eghis.exists():
        return
    if not self.stgn_auto_backup_btn.isChecked():
        return

    if self.infos.lpdom:
        eAutils.send_discord(self, text="오늘은 청구일입니다. eGhis가 종료되지 않습니다.")
        return
    else:
        eAutils.send_discord(self, text="eGhis를 종료하고, 백업을 진행합니다.")

    to_eghis()
    eAinput.buy_time(1)
    eAinput.write_enter('1qazxcv.')
    eAinput.buy_time(2)
    to_eghis()
    eAinput.buy_time(1)
    eAinput.hotkeys('alt', 'f4')
    eAinput.buy_time(2)
    eAinput.press_key('enter')
    eAinput.buy_time(2)
    eAinput.press_key('enter')

    if self.stgn_auto_shutdown_btn.isChecked():
        eAinput.buy_time(2)
        eAinput.press_key(' ')
        eAutils.send_discord(self, text="백업 후 컴퓨터를 자동으로 종료합니다.")


# 청구집계
def start_stats(self):
    if not eghis.exists():
        return
    if not self.popup.stng_auto_stats_btn.isChecked():
        return
    if not self.infos.lpdom:
        return

    eAutils.send_discord(self, text="오늘은 청구일입니다. 청구집계를 시작합니다.")

    to_eghis()
    eAinput.buy_time(1)
    eAinput.write_enter('1qazxcv.')
    eAinput.buy_time(1)
    eAinput.click_at(*eAxys.eGhis.MENU_CLAIM)
    eAinput.buy_time(1)
    eAinput.click_at(*eAxys.eGhis.CLAIM_START_STAT)


# Vaccine Systems Window Manipulation

VACCINE_SYSTEMS = ["예방접종통합관리시스템",
                   "::::: 질병관리청 현물공급 인플루엔자등록시스템 ::::: - Chrome",
                   "코로나19통합관리시스템"]
VACCINE_XYS = [eAxys.VacGen, eAxys.VacFlu, eAxys.VacCovid19]

# # 각 접종 시스템 set focus
# def vaccine_focus(self, sys:int):
#     try:
#         target_sys = Application().connect(title=VACCINE_SYSTEMS[sys]).top_window()
#     except pywinauto.findwindows.ElementNotFoundError:
#         pass

#     target_sys.set_focus()
#     self.delayed_exec(0.5)

# 각 접종 시스템 환자정보 입력


def vaccine_pt(self, sys: int, ptjmno: str):
    if "-" in ptjmno:
        ptjmno = ptjmno.replace("-", "")

    try:
        target_sys = pygetwindow.getWindowsWithTitle(VACCINE_SYSTEMS[sys])[0]
    except IndexError:
        return

    target_sys.activate()
    eAinput.buy_time(0.5)

    eAinput.click_at(*VACCINE_XYS[sys].DEL_PTJMNO)
    eAinput.click_at(*VACCINE_XYS[sys].INPUT_PTJMNO)
    eAinput.write_enter(ptjmno)


# 각 접종 시스템 로그아웃 연장 버튼 누르기
def vaccine_cont_all(self):
    # Block mouse and keyboard input during PyAutoGui
    # windll.user32.BlockInput(True)

    # 현물 인플루엔자 독감접종 시스템 변경으로 log out 연장 없어짐. (제외 시킴)
    for i in range(0, 3):
        if i == 1:
            continue
        try:
            target_sys = pygetwindow.getWindowsWithTitle(VACCINE_SYSTEMS[i])[0]
        except IndexError:
            return

        target_sys.activate()
        eAinput.buy_time(0.5)
        eAinput.click_at(*VACCINE_XYS[i].CONT_LOGIN)

    # Unblock mouse and keyboard input after PyAutoGui
    # windll.user32.BlockInput(False)


# 기본접종시스템은 시작시 접종화면으로 가는 버튼을 눌러줘야함. 해당 기능.
def gen_sys_prepare(self):
    try:
        target_sys = pygetwindow.getWindowsWithTitle(VACCINE_SYSTEMS[0])[0]
    except IndexError:
        return
    target_sys.activate()
    eAinput.buy_time(0.5)
    eAinput.click_at(*eAxys.VacGen.TO_MAIN)


# # 독감 접종시 노인 및 소아 시스템은 동일하나 수동으로 백신 LOT번호를 변경해줘야해서...자동화.
# def flu_sys_LOT(self, lot:str):
#     try:
#         target_sys = Application().connect(title=VACCINE_SYSTEMS[1]).top_window()
#     except pywinauto.findwindows.ElementNotFoundError:
#         pass

#     target_sys.set_focus()
#     self.delayed_exec(0.5)
#     eAinput.double_click_at(VACCINE_XYS[1]["LOT번호"])
#     #+ eAinput.write_enter(lot번호)

# PYWINAUTO KEYS
# {SCROLLLOCK}, {VK_SPACE}, {VK_LSHIFT}, {VK_PAUSE}, {VK_MODECHANGE},
# {BACK}, {VK_HOME}, {F23}, {F22}, {F21}, {F20}, {VK_HANGEUL}, {VK_KANJI},
# {VK_RIGHT}, {BS}, {HOME}, {VK_F4}, {VK_ACCEPT}, {VK_F18}, {VK_SNAPSHOT},
# {VK_PA1}, {VK_NONAME}, {VK_LCONTROL}, {ZOOM}, {VK_ATTN}, {VK_F10}, {VK_F22},
# {VK_F23}, {VK_F20}, {VK_F21}, {VK_SCROLL}, {TAB}, {VK_F11}, {VK_END},
# {LEFT}, {VK_UP}, {NUMLOCK}, {VK_APPS}, {PGUP}, {VK_F8}, {VK_CONTROL},
# {VK_LEFT}, {PRTSC}, {VK_NUMPAD4}, {CAPSLOCK}, {VK_CONVERT}, {VK_PROCESSKEY},
# {ENTER}, {VK_SEPARATOR}, {VK_RWIN}, {VK_LMENU}, {VK_NEXT}, {F1}, {F2},
# {F3}, {F4}, {F5}, {F6}, {F7}, {F8}, {F9}, {VK_ADD}, {VK_RCONTROL},
# {VK_RETURN}, {BREAK}, {VK_NUMPAD9}, {VK_NUMPAD8}, {RWIN}, {VK_KANA},
# {PGDN}, {VK_NUMPAD3}, {DEL}, {VK_NUMPAD1}, {VK_NUMPAD0}, {VK_NUMPAD7},
# {VK_NUMPAD6}, {VK_NUMPAD5}, {DELETE}, {VK_PRIOR}, {VK_SUBTRACT}, {HELP},
# {VK_PRINT}, {VK_BACK}, {CAP}, {VK_RBUTTON}, {VK_RSHIFT}, {VK_LWIN}, {DOWN},
# {VK_HELP}, {VK_NONCONVERT}, {BACKSPACE}, {VK_SELECT}, {VK_TAB}, {VK_HANJA},
# {VK_NUMPAD2}, {INSERT}, {VK_F9}, {VK_DECIMAL}, {VK_FINAL}, {VK_EXSEL},
# {RMENU}, {VK_F3}, {VK_F2}, {VK_F1}, {VK_F7}, {VK_F6}, {VK_F5}, {VK_CRSEL},
# {VK_SHIFT}, {VK_EREOF}, {VK_CANCEL}, {VK_DELETE}, {VK_HANGUL}, {VK_MBUTTON},
# {VK_NUMLOCK}, {VK_CLEAR}, {END}, {VK_MENU}, {SPACE}, {BKSP}, {VK_INSERT},
# {F18}, {F19}, {ESC}, {VK_MULTIPLY}, {F12}, {F13}, {F10}, {F11}, {F16},
# {F17}, {F14}, {F15}, {F24}, {RIGHT}, {VK_F24}, {VK_CAPITAL}, {VK_LBUTTON},
# {VK_OEM_CLEAR}, {VK_ESCAPE}, {UP}, {VK_DIVIDE}, {INS}, {VK_JUNJA},
# {VK_F19}, {VK_EXECUTE}, {VK_PLAY}, {VK_RMENU}, {VK_F13}, {VK_F12}, {LWIN},
# {VK_DOWN}, {VK_F17}, {VK_F16}, {VK_F15}, {VK_F14}
