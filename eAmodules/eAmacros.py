import main
from eAmodules import eAwinauto, eAlabeler
from eAmodules import eAinput, eAstr, eApopup, eAvacsys


# 진료관련
# 보험자격 확인
def check_ins():
    eAwinauto.to_eghis()
    eAwinauto.eghis_insurance()


# 다음환자
def next_pt():
    eAwinauto.to_eghis()
    eAwinauto.tab_wait_list(1)


# 직전환자
def prev_pt():
    eAwinauto.to_eghis()
    eAwinauto.tab_wait_list(7)


# Menu in dialogs, 비보험진료
def no_ins_choice(self):
    menu_items = ['현재환자, 일반진료', '직전환자, 일반 추가']
    choice = eApopup.menu(title="비보험진료", buttons=menu_items)
    if choice == 'CLOSE':
        return
    elif choice == menu_items[0]:
        no_ins()
    else:
        add_no_ins(self)


# 코멘트 모음
# 비보험 진료
def no_ins():
    eAwinauto.to_eghis()
    eAwinauto.eghis_insurance(action="no_ins")


# 직전환자 비보험진료 추가
def add_no_ins(self):
    eAwinauto.to_eghis()
    eAwinauto.tab_wait_list(7)
    eAinput.buy_time(3)
    eAwinauto.eghis_today_right_click(self)
    eAinput.repeat_key('down', repeat=3)
    eAinput.repeat_key('enter', repeat=2)


# 물리치료 코멘트 랜덤 입력 + 처방입력 on request
def physical_tx(self):
    menu_items = ['코멘트 ONLY', '코멘트 + 물치처방']
    choice = eApopup.menu(title='물리치료', buttons=menu_items)

    if choice == 'CLOSE':
        return
    elif choice == menu_items[1]:
        eAinput.rx_input('물치')
    eAinput.sx_cnp(eAstr.PT_LST)


# 만성질환
def chronic_management():
    menu_items = [
        '만성질환관리 신환',
        '만성질환 교육 코멘트',
        'Home Monitor (공통)',
        'Home Monitor (혈압)',
        'Home Monitor (혈당)'
    ]

    choice = eApopup.menu(title='만성질환 관련 코멘트', buttons=menu_items)
    if choice == 'CLOSE':
        return
    elif choice == menu_items[0]:
        eAinput.sx_cnp('만성질환관리')
    elif choice == menu_items[1]:
        eAinput.sx_cnp('만성질환교육')
    elif choice == menu_items[2]:
        eAinput.sx_cnp(eAstr.HOME_MON)
    elif choice == menu_items[3]:
        eAinput.sx_cnp(eAstr.REC_HOME_MON_BP)
    elif choice == menu_items[4]:
        eAinput.sx_cnp(eAstr.REC_HOME_MON_BST)


# WorkUP 관련 코멘트
def lab_studies():
    menu_items = ['혈액검사 예정', '혈액검사, 강조']
    choice = eApopup.menu(title='핼액검사 관련', buttons=menu_items)
    if choice == 'CLOSE':
        return
    elif choice == menu_items[0]:
        eAinput.sx_cnp(eAstr.LAB_PLAN_LST)
    else:
        eAinput.sx_cnp(eAstr.LAB_MUST_LST)


# WorkUP 관련 코멘트
def workups():
    menu_items = [
        '골밀도검사(BMD) 예정',
        '치매척도검사 예정',
        '엑스선 촬영: 이상없음',
        '엑스선 촬영 고려',
        '엑스선 촬영 거부'
    ]

    choice = eApopup.menu(title='각종 WORKUPs', buttons=menu_items)
    if choice == 'CLOSE':
        return
    elif choice == menu_items[0]:
        eAinput.sx_cnp(eAstr.BMD_PLAN)
    elif choice == menu_items[1]:
        eAinput.sx_cnp(eAstr.MMSE_PLAN)
    elif choice == menu_items[2]:
        eAinput.sx_cnp('엑스레이')
    elif choice == menu_items[3]:
        eAinput.sx_cnp(eAstr.XRAY_PLAN)
    else:
        eAinput.sx_cnp(eAstr.XRAY_REFUSE)


# 기타 코멘트들. Dialog
# TODO needs working.
def other_comments():
    menu_items = [
        '보존적 치료',
        '감기 기본',
        '복불 기본',
        '엑스레이 정상',
        '골밀도 FORM',
        '연골주사 FORM'
    ]

    choice = eApopup.menu(title="기타 코멘트 모음", buttons=menu_items)
    if choice == 'CLOSE':
        return
    elif choice == menu_items[0]:
        eAinput.sx_cnp('보존;')
    elif choice == menu_items[1]:
        eAinput.sx_cnp('pharyn;')
    elif choice == menu_items[2]:
        eAinput.sx_cnp('abd;')
    elif choice == menu_items[3]:
        eAinput.sx_cnp('엑스레이;')
    elif choice == menu_items[4]:
        eAinput.sx_cnp('골밀도;')
    elif choice == menu_items[5]:
        eAinput.sx_cnp('연골;')


# 예방접종 관련
# = Vaccination! Call labeler with single button press
def call_labeler(self):
    self.apps_buttons('apps_labeler_btn')
    eAlabeler.fetch_and_write_ptinfo(self)

# = Vaccine System Management Main Menu


def vac_sys_manager(self):
    options = ['접종시스템 입력', '접종시스템 시작', '로그아웃 연장']
    choice = eApopup.menu(title='접종시스템 관리', buttons=options)
    if choice == 'CLOSE':
        return
    elif choice == options[0]:
        vac_sys_input(self)
    elif choice == options[1]:
        vac_sys_start(self)
    elif choice == options[2]:
        eAwinauto.vaccine_cont_all(self)

# = 접종시스템 직접 입력. Labeler 없이.
# TODO more specific exceptions is needed.


def vac_sys_input(self):
    vac_sys = ['예방접종시스템', '현물독감시스템', '코로나19시스템']
    choice = eApopup.menu(title='시스템 입력', buttons=vac_sys)
    if choice == 'CLOSE':
        return
    else:
        currentPT = eAwinauto.current_ptinfo()
        try:
            eAwinauto.vaccine_pt(self, vac_sys.index(
                choice), currentPT['ptjmno'])
        except IndexError:
            eApopup.notify(text="다시 확인해보세요!!")

# = 접종시스템 관리


def vac_sys_start(self):
    menu_items = ['통합예방접종시스템 (V)',
                  '현물독감접종시스템 (F)',
                  '코로나19접종시스템 (C)',
                  'V + F',
                  'V + C',
                  'F + C',
                  'V + F + C',
                  '홈페이지 로그인']
    choice = eApopup.menu(title="접종시스템 자동시작", buttons=menu_items)
    if choice == 'CLOSE':
        return
    elif choice == menu_items[0]:
        eAvacsys.iskdca_login(self, options=0)
    elif choice == menu_items[1]:
        eAvacsys.iskdca_login(self, options=1)
    elif choice == menu_items[2]:
        eAvacsys.iskdca_login(self, options=2)
    elif choice == menu_items[3]:
        eAvacsys.iskdca_login(self, options=3)
    elif choice == menu_items[4]:
        eAvacsys.iskdca_login(self, options=4)
    elif choice == menu_items[5]:
        eAvacsys.iskdca_login(self, options=5)
    elif choice == menu_items[6]:
        eAvacsys.iskdca_login(self, options=6)
    elif choice == menu_items[7]:
        eAvacsys.iskdca_login(self, options=7)
    else:
        return

# = Covid-19 Macro, Main Menu


def covid_19_menu():
    menu_items = ['RAT 처방', 'RAT 결과입력']
    choice = eApopup.menu(title="코로나19 관련 Macro", buttons=menu_items)
    if choice == 'CLOSE':
        return
    elif choice == menu_items[0]:
        RAT()
    elif choice == menu_items[1]:
        RAT_results()

# = Menu in dialogs, RAT


def RAT():
    ins_comment = """# 경상북도 영덕군 영해면 소재 의료기관.
  - 발열/상기도 감염증세/근육통 호소하여 50/100 급여로 RAT 시행."""
    menu_items = ['급여RAT', '비보RAT', '비급여단체RAT']
    choice = eApopup.menu(title="RAT검사 처방", buttons=menu_items)
    if choice == 'CLOSE':
        return
    else:
        eAwinauto.to_eghis()
        eAinput.rx_input(choice)
        eAinput.copy_it(ins_comment)
        eApopup.notify(text="클립보드에 급여 용 코멘트를 복사했습니다.")

# = Menu in dialogs, RAT results


def RAT_results():
    menu_items = ['음성 - Negative', '양성 - Positive']
    choice = eApopup.menu(title="RAT 결과입력", buttons=menu_items)
    if choice == 'CLOSE':
        return
    elif choice == menu_items[0]:
        RAT_result_input()
    else:
        RAT_result_input(positive=True)
        # ok = eApopup.confirm(text = "확진자 진료 진행할까요?\n(원스톱 진료기관 통합진료료)")
        # if not ok: return
        # else: COVID_pos(self, one_stop = True)

# = RAT 결과 입력 logics


def RAT_result_input(positive: bool = False):
    eAwinauto.to_eghis()
    eAinput.press_key('f3')
    eAinput.find_and_click(png='resources/macros/rat_rx_los.png',
                           area=(1400, 1100, 1000, 1000), rt_click=True)
    eAinput.repeat_key('down', repeat=13)
    if not positive:
        eAinput.repeat_key('enter', repeat=2)
        eAinput.sx_cnp(eAstr.RAT_NEGA)
    else:
        eAinput.press_keys('enter', 'down', 'enter')
        eAinput.sx_cnp(eAstr.RAT_POSI)

# = Menu in dialogs, RAT 진료
# def COVID_pos(self, one_stop:bool = False):
#     eAinput.icd_delete_all()
#     if one_stop:
#         eAinput.rx_input(rx = "코로나기본")
#         eAinput.press_key('enter')
#         report = eApopup.confirm(text = "확진자 신고로 이동할까요?")
#         if report:
#             eAutils.apps_stack_menu(self, self.covid_19_report_btn.text())
#             eAcovid19R.covid_19_get_ptinfo(self)
#     else:
#         eAinput.rx_input("ah410")
#         eAinput.icd_input("u071")
#         eAinput.press_key('enter')


# = 비대면진료
# def covid_tel():
#     eAwinauto.to_eghis()
#     # 초진 재진 여부에 따라 코드 알아서 넣어주고..
#     # 항상 첫줄은 아닐수도 있으니까... 초진/재진 코드의 위치를 확인하기.
#     if eAwinauto.eghis_check_cj():
#         eAinput.rx_input('재택 초진')
#         cjjj = eAinput.locateCenterOnScreen(image = 'pag_los/chojin_code.png', region = (250, 1150, 100, 450))
#     elif eAwinauto.eghis_check_cj() == False:
#         eAinput.rx_input('재택 재진')
#         cjjj = eAinput.locateCenterOnScreen(image = 'pag_los/jaejin_code.png', region = (250, 1150, 100, 450))
#     # 혹시 모를 에러 상황에 대비해서..
#     else:
#         eApopup.warning(text = "Something went wrong!")
#         return
#     # 초진/재진 코드에 우클릭, 메뉴에 내려가서 'H/전화상담처방' 누르기.
#     eAinput.right_click_it(cjjj)
#     eAinput.repeat_key('down', repeats=21)
#     eAinput.press_key('enter')
#     eAinput.repeat_key('down', repeats=5)
#     eAinput.press_key('enter')
#     eAinput.buy_time(0.5)
#     eAinput.press_key('f5')


# 인플루엔자 관련
# = 보육원 학생 여부 확인.
def influenza_candidate():
    menu_items = ['일반 환자', '보육원 환자(할인)']
    candidate = eApopup.menu(title='독감검사, 환자', buttons=menu_items)
    if candidate == 'CLOSE':
        return
    elif candidate == menu_items[0]:
        eAinput.rx_input('플루코비드')
    else:
        eAinput.rx_input('플루-보')


# = 키트 처방여부 확인
def flu_kit_ordered():
    ordered = eAinput.find_if_exists(
        png='resources/macros/flucovid_kit_rx_los.png', area=(1400, 1100, 1000, 1000))
    if not ordered:
        ok = eApopup.confirm(
            text="플루 키트가 처방되지 않았습니다.\n타기관 결과? 금일 이전 결과?\n금일 처방없이 진행할까요?")
        if ok:
            return
        else:
            influenza_candidate()


# = 독감 양성, 아형은?
def influenza_result():
    flu_kit_ordered()

    result_items = ['독감키트 음성', '독감키트 양성']
    nega_posi = eApopup.menu(title='독감키트 결과는?', buttons=result_items)
    if nega_posi == 'CLOSE':
        return 'CLOSE'

    elif nega_posi == result_items[0]:
        eAinput.sx_cnp(eAstr.FLU_NEGA)
        return

    elif nega_posi == result_items[1]:
        eAinput.icd_input('j101')
        eAinput.press_key('enter')
        type_items = ['Influenza Type A', 'Influenza Type B']
        flu_type = eApopup.menu(title='Influenza Type', buttons=type_items)
        if flu_type == 'CLOSE':
            return
        elif flu_type == type_items[0]:
            eAinput.sx_cnp(eAstr.FLU_A)
        else:
            eAinput.sx_cnp(eAstr.FLU_B)

        order = eApopup.confirm(text="타미플루 처방?")
        if not order:
            return
        else:
            influenza_tamiflu(flu_type)


# = 양성, 타미플루 처방. JX999, 상병명, 체중 별 타미플루 용량
def influenza_tamiflu(type: str = None):
    flu_kit_ordered()

    if type is None:
        type_items = ['Influenza Type A', 'Influenza Type B']
        type = eApopup.menu(title='Influenza Type', buttons=type_items)
        if type == 'CLOSE':
            return 'CLOSE'
        eAinput.icd_input('j101')
        eAinput.press_key('enter')

    jx999 = getattr(eAstr, f'FLU_{type[-1]}')

    menu_items = ['<15Kg', '15~23Kg', '23~40Kg', '40Kg 이상']
    weight = eApopup.menu(title="타미플루 용량 선택", buttons=menu_items)
    if weight == 'CLOSE':
        return 'CLOSE'
    elif weight == menu_items[0]:
        eAinput.rx_input(rx='타미플루캡슐30', regimen=(2, 2, 5))
    elif weight == menu_items[1]:
        eAinput.rx_input(rx='타미플루캡슐45', regimen=(2, 2, 5))
    elif weight == menu_items[2]:
        eAinput.rx_input(rx='타미플루캡슐30', regimen=(4, 2, 5))
    else:
        eAinput.rx_input(rx='타미비어캡슐75', regimen=(2, 2, 5))
    eAinput.buy_time(0.2)
    # 몸무게에 맞는 처방약이 입력이 되면 타미플루의 '특정내역'에 독감 확진임을 입력해주고.
    eAinput.hotkeys('ctrl', 't')
    eAinput.repeat_key('tab', repeat=4)
    eAinput.write(jx999)
    eAinput.press_key('f5')


# = 양성, 상병입력, 타미플루입력, JX999 및 학교제출용 확인서.
# TODO 현재는 확인서 처방코드만 입력. 추후 확인서 출력까지 자동화 시켜보자.
def influenza_docs(self):
    docs = influenza_tamiflu()
    if docs != 'CLOSE':
        eAinput.rx_input('진료확인서')
        self.apps_buttons('apps_med_docs_btn')

# = 인플루엔자 최종


def influenza(self):
    menu_items = ['독감 신속 검사입력', '검사결과 입력', '타미플루 처방', '결과입력/처방 및 확인서']
    choice = eApopup.menu(title="Macro; Influenza", buttons=menu_items)
    if choice == 'CLOSE':
        return
    elif choice == menu_items[0]:
        influenza_candidate()
    elif choice == menu_items[1]:
        influenza_result()
    elif choice == menu_items[2]:
        influenza_tamiflu()
    else:
        influenza_docs(self)
