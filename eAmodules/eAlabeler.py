from PySide6.QtCore import QDate, QPoint, QSizeF, QMarginsF
from PySide6.QtGui import QPainter, QPageSize
from PySide6.QtPrintSupport import QPrinter
import sqlite3

import main
from eAmodules import eAwinauto, eAutils, eApopup, eAinput


class FluSettings:
    # 지정 값은 어짜피 세팅 불러오면서 바뀜. 구색맞추기 용.
    AUTO_INPUT_SYS: bool = True
    CHILD_LOT_CHANGE: bool = True
    CHILD_LOT: str = "5555555"
    FLU_NIP_AUTO: bool = True
    FLU_OLD_EX_ENABLE: bool = True
    DATE_75_OVER: QDate = QDate.fromString("20221012", "yyyyMMdd")
    DATE_7074: QDate = QDate.fromString("20221017", "yyyyMMdd")
    DATE_6569: QDate = QDate.fromString("20221020", "yyyyMMdd")
    OLD_END_DATE: QDate = QDate.fromString("20221231", "yyyyMMdd")
    BIRTH_75_OVER: QDate = QDate.fromString("19471231", "yyyyMMdd")
    BIRTH_7074_FROM: QDate = QDate.fromString("19480101", "yyyyMMdd")
    BIRTH_7074_UNTIL: QDate = QDate.fromString("19521231", "yyyyMMdd")
    BIRTH_6569_FROM: QDate = QDate.fromString("19530101", "yyyyMMdd")
    BIRTH_6569_UNTIL: QDate = QDate.fromString("19571231", "yyyyMMdd")
    DATE_CHILD_TWICE: QDate = QDate.fromString("20220921", "yyyyMMdd")
    TWICE_CHILD_END_DATE: QDate = QDate.fromString("20230430", "yyyyMMdd")
    DATE_CHILD_ONCE: QDate = QDate.fromString("20221005", "yyyyMMdd")
    ONCE_CHILD_END_DATE: QDate = QDate.fromString("20230430", "yyyyMMdd")
    BIRTH_CHILD_FROM: QDate = QDate.fromString("20090101", "yyyyMMdd")
    BIRTH_CHILD_UNTIL: QDate = QDate.fromString("20220831", "yyyyMMdd")


def load_FluSettings(self):
    global FluSettings
    FluSettings.AUTO_INPUT_SYS: bool = self.stlb_auto_input_cbx.isChecked()
    FluSettings.CHILD_LOT_CHANGE: bool = self.stlb_auto_child_flu_lot_cbx.isChecked()
    FluSettings.CHILD_LOT = self.stlb_child_flu_lot_led.text()
    FluSettings.FLU_NIP_AUTO = self.stlb_flu_auto_sort_cbx.isChecked()
    FluSettings.FLU_OLD_EX_ENABLE = self.stlb_flu_allow_ex_cbx.isChecked()
    FluSettings.DATE_75_OVER = QDate.fromString(self.stlb_flu_old_over75_start_led.text(), "yyyyMMdd")
    FluSettings.DATE_7074 = QDate.fromString(self.stlb_flu_old_7074_start_led.text(), "yyyyMMdd")
    FluSettings.DATE_6569 = QDate.fromString(self.stlb_flu_old_6569_start_led.text(), "yyyyMMdd")
    FluSettings.OLD_END_DATE = QDate.fromString(self.stlb_flu_old_end_led.text(), "yyyyMMdd")
    FluSettings.BIRTH_75_OVER = QDate.fromString(self.stlb_flu_age_75over_led.text(), "yyyyMMdd")
    FluSettings.BIRTH_7074_FROM = QDate.fromString(self.stlb_flu_age_7074_led1.text(), "yyyyMMdd")
    FluSettings.BIRTH_7074_UNTIL = QDate.fromString(self.stlb_flu_age_7074_led2.text(), "yyyyMMdd")
    FluSettings.BIRTH_6569_FROM = QDate.fromString(self.stlb_flu_age_6569_led1.text(), "yyyyMMdd")
    FluSettings.BIRTH_6569_UNTIL = QDate.fromString(self.stlb_flu_age_6569_led2.text(), "yyyyMMdd")
    FluSettings.DATE_CHILD_TWICE = QDate.fromString(self.stlb_flu_date_child_twice_led1.text(), "yyyyMMdd")
    FluSettings.TWICE_CHILD_END_DATE = QDate.fromString(self.stlb_flu_date_child_twice_led2.text(), "yyyyMMdd")
    FluSettings.DATE_CHILD_ONCE = QDate.fromString(self.stlb_flu_date_child_once_led1.text(), "yyyyMMdd")
    FluSettings.ONCE_CHILD_END_DATE = QDate.fromString(self.stlb_flu_date_child_once_led2.text(), "yyyyMMdd")
    FluSettings.BIRTH_CHILD_FROM = QDate.fromString(self.stlb_flu_age_child_led1.text(), "yyyyMMdd")
    FluSettings.BIRTH_CHILD_UNTIL = QDate.fromString(self.stlb_flu_age_child_led2.text(), "yyyyMMdd")


# 1단계 2단계 실행했는지 파악하기.
class Steps:
    ONE = False
    TWO = False


# 백신 카운터
class Count:
    # Vaccine Counters; influenza
    Flu_Old: int = 0
    Flu_Ex: int = 0
    Flu_Child: int = 0
    Flu_Total_Count: int = Flu_Old + Flu_Child
    Flu_Total_All: int = Flu_Total_Count + Flu_Ex
    # Vaccine Counters; covid19
    PF_XBB_1_5: int = 0
    MD_XBB_1_5: int = 0
    COVID_Total: int = PF_XBB_1_5 + MD_XBB_1_5
    # Temp Storage of Current Patient's Vaccine Counter to Be Added
    Selected: str = ""
    # All list of Counting Vaccines with Counter_code
    Vaccines = {
        '화이자XBB.1.5': "PF_XBB_1_5",
        '모더나XBB.1.5': "MD_XBB_1_5",
        '무료독감:노인': "Flu_Old",
        '무료독감:예외': "Flu_Ex",
        '무료독감:소아': "Flu_Child"
    }

    # Updating All Total Counters
    def update_counter():
        Count.Flu_Total_Count = Count.Flu_Old + Count.Flu_Child
        Count.Flu_Total_All = Count.Flu_Total_Count + Count.Flu_Ex
        Count.COVID_Total = Count.PF_XBB_1_5 + Count.MD_XBB_1_5

    # Add 1 to each specified Counters
    def add_counter():
        add_vac = Count.Vaccines[Count.Selected]
        setattr(Count, add_vac, getattr(Count, add_vac) + 1)
        Count.update_counter()

    # Edit the counter value of specified counters.
    def edit_counter(vac, edit_value: int):
        setattr(Count, vac, edit_value)
        Count.update_counter()


# 백신 목록
class Vaccines:
    # 모든 접종가능 백신 항목. 'sep'은 separator.
    # separator도 GUI적용 시 combobox의 index에 포함됨으로 리스트에도 포함해놓자.
    LIST = [
        'sep',
        '인플루엔자',
        'sep',
        '무료:프로디악스',
        '무료:대상포진',
        '무료:가다실4',
        'sep',
        '프리베나13',
        '조스타박스',
        '싱그릭스',
        '가다실9',
        'sep',
        'A형 간염',
        'B형 간염',
        'sep',
        '화이자XBB.1.5',
        '모더나XBB.1.5']
    # 코로나 백신 목록 (for easier organizing the counters)
    COVID = [
        '화이자XBB.1.5',
        '모더나XBB.1.5']


# UI setup
def prepare_labeler(self):
    self.lblr_vaccines_cmb.addItem("접종 백신을 선택하세요.")
    for vac in Vaccines.LIST:
        if vac != 'sep':
            self.lblr_vaccines_cmb.addItem(vac)
        else:
            index = self.lblr_vaccines_cmb.count()
            self.lblr_vaccines_cmb.insertSeparator(index)
    self.lblr_preview_date_lbl.setText(self.infos.date_today.toString("yyyy년MM월dd일(ddd)"))
    connect_DB(self)
    counter_update(self)
    flu_date_check(self)


# 카운터 갱신. (class 및 GUI)
def counter_update(self):
    Count.update_counter()
    # 코로나 19 카운트
    self.lblr_count_total_covid_led.setText(str(Count.COVID_Total))
    self.lblr_count_pf_led.setText(str(Count.PF_XBB_1_5))
    self.lblr_count_md_led.setText(str(Count.MD_XBB_1_5))
    # 독감 카운트
    self.lblr_count_total_flu_led.setText(str(Count.Flu_Total_Count) + f'({Count.Flu_Total_All})')
    self.lblr_count_old_flu_led.setText(str(Count.Flu_Old))
    self.lblr_count_child_flu_led.setText(str(Count.Flu_Child))
    self.lblr_count_old_flu_ex_led.setText(str(Count.Flu_Ex))


# DB 연결. DB가 없으면 새로 작성하고, 테이블도 작성함.
def connect_DB(self):
    # Load DB
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()
    # Create table if not exists
    con.execute(
        '''CREATE TABLE if not exists Counter(
        Date TEXT UNIQUE,
        Covid INTEGER,
        PFXBB INTEGER,
        MDXBB INTEGER,
        FLU_TOTALC INTEGER,
        FLU_ALL INTEGER,
        FLU_OLD INTEGER,
        FLU_OLD_EX INTEGER,
        FLU_CHILD INTEGER)'''
    )
    # Load Dates. And check if today already exist.
    dates_in_db = [item[0] for item in cur.execute('SELECT Date FROM Counter').fetchall()]
    today = self.infos.date_today.toString("yyyyMMdd")
    # DB 테이블에 오늘이 없다면 새로 작성해야하니 패스
    if today not in dates_in_db:
        return
    # 있다면 불러와서 순서 맞춰 입력하기
    today_counter = cur.execute(f'SELECT * FROM Counter WHERE Date={today}').fetchall()[0]
    Count.COVID_Total = int(today_counter[1])
    Count.PF_XBB_1_5 = int(today_counter[2])
    Count.MD_XBB_1_5 = int(today_counter[3])
    Count.Flu_Total_Count = int(today_counter[4])
    Count.Flu_Total_All = int(today_counter[5])
    Count.Flu_Old = int(today_counter[6])
    Count.Flu_Ex = int(today_counter[7])
    Count.Flu_Child = int(today_counter[8])
    # Close DB connection
    con.commit()
    con.close()


# DB 연결(입력)
def write_DB(self):
    # 먼저 Counter를 업데이트하고..
    Count.update_counter()
    # GUI도 업데이트 해주고..
    counter_update(self)
    # 먼저 입력될 순서에 맞게 리스트로 만들어주자.
    today = self.infos.date_today.toString("yyyyMMdd")
    data_to_write = []
    data_to_write.append(today)
    data_to_write.append(Count.COVID_Total)
    data_to_write.append(Count.PF_XBB_1_5)
    data_to_write.append(Count.MD_XBB_1_5)
    data_to_write.append(Count.Flu_Total_Count)
    data_to_write.append(Count.Flu_Total_All)
    data_to_write.append(Count.Flu_Old)
    data_to_write.append(Count.Flu_Ex)
    data_to_write.append(Count.Flu_Child)
    # Load DB to write.
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()
    # Load Dates.
    dates_in_db = [item[0] for item in cur.execute('SELECT Date FROM Counter').fetchall()]
    # 없다면 새로운 row 추가.
    if today not in dates_in_db:
        cur.execute(f'INSERT INTO Counter VALUES {str(tuple(data_to_write))}')
    # 있다면 일단 지우고
    else:
        cur.execute(f'DELETE FROM Counter WHERE Date = {today}')
        cur.execute(f'INSERT INTO Counter VALUES {str(tuple(data_to_write))}')
    # Write and close connection.
    con.commit()
    con.close()


# eGhis 차트에서 환자정보 불러오기.
def fetch_and_write_ptinfo(self):
    try:
        currentPT = eAwinauto.current_ptinfo()
        self.lblr_preview_ptname_lbl.setText(f"{currentPT['ptname']}({currentPT['ptno']})")
        self.lblr_preview_ptjmno_lbl.setText(currentPT['ptjmno'])
        self.lblr_preview_ptphone_lbl.setText(currentPT['ptphone'])
    except TypeError:
        return
    # 1단계 완료.
    Steps.ONE = True


# Vaccine을 선택했다면...
def vac_combo_selected(self):
    # '접종 백신을 선택하세요'로 바뀐경우(combobox currentindex changed에 발동함으로) 무시하기
    if self.lblr_vaccines_cmb.currentIndex() == 0:
        return
    # 코로나 접종 현재 일시 중단 상태이니 제일 먼저 확인 후 return
    if self.lblr_vaccines_cmb.currentText() in Vaccines.COVID:
        # 코로나 비접종 기간
        # eApopup.warning(text = "코로나19 접종은 현재 시행 안함.")
        # self.lblr_vaccines_cmb.setCurrentIndex(0)
        # 코로나 접종 기간
        covid_org(self, self.lblr_vaccines_cmb.currentText())
        return

    # 1단계 무시하고 선택 먼저했다면, 환자불러오도록..
    if not Steps.ONE:
        ok = eApopup.confirm(text="환자정보를 먼저 불러오시겠습니까?")
        if ok:
            fetch_and_write_ptinfo(self)
        else:
            eApopup.notify(text="환자 불러오기 후 진행해주세요.")
            return
    # 백신 분류하기. 인플루엔자/코로나19/기타 접종.
    elif self.lblr_vaccines_cmb.currentText() == "인플루엔자":
        flu_group_org(self, self.lblr_preview_ptjmno_lbl.text())
    # 기타 접종의 경우 바로 프린트 준비하기.
    else:
        self.lblr_preview_count_vac_lbl.setText("")
        self.lblr_preview_counter_lbl.setText("")
        self.lblr_preview_nocount_vac_lbl.setText(self.lblr_vaccines_cmb.currentText())
        # 미리 시스템에 띄우기
        eAwinauto.vaccine_pt(self, 0, self.lblr_preview_ptjmno_lbl.text())
        Steps.TWO = True

# Influenza Vaccination
# FLU사업날짜는 미리 >> fluolddate[X, 75~, 70~, 65~] : fluchilddate [X, x1~, x2~]
# 환자 연령별로 그룹화 >> fluoldgroup[1, 2, 3] : fluchildgroup[1,2] : flupaying
# 날짜및카운터확인


# 국가독감접종사업 날짜 확인.
def flu_date_check(self):
    # 노인독감 사업기간
    if self.infos.date_today < FluSettings.DATE_75_OVER:
        self.lblr_flu_date_checker_old.setText("X")
    elif FluSettings.DATE_75_OVER <= self.infos.date_today < FluSettings.DATE_7074:
        self.lblr_flu_date_checker_old.setText("75~")
    elif FluSettings.DATE_7074 <= self.infos.date_today < FluSettings.DATE_6569:
        self.lblr_flu_date_checker_old.setText("70~")
    elif FluSettings.DATE_6569 <= self.infos.date_today <= FluSettings.OLD_END_DATE:
        self.lblr_flu_date_checker_old.setText("65~")
    elif FluSettings.OLD_END_DATE < self.infos.date_today:
        self.lblr_flu_date_checker_old.setText("X")
    # 소아독감 사업기간
    if self.infos.date_today < FluSettings.DATE_CHILD_TWICE:
        self.lblr_flu_date_checker_child.setText("X")
    elif FluSettings.DATE_CHILD_TWICE <= self.infos.date_today < FluSettings.DATE_CHILD_ONCE:
        self.lblr_flu_date_checker_child.setText("x2~")
    elif FluSettings.DATE_CHILD_ONCE <= self.infos.date_today < FluSettings.ONCE_CHILD_END_DATE:
        self.lblr_flu_date_checker_child.setText("x1~")
    elif FluSettings.ONCE_CHILD_END_DATE < self.infos.date_today:
        self.lblr_flu_date_checker_child.setText("X")


def flu_group_org(self, ptjmno: str):
    # 환자 생일을 구하고.
    if eAutils.jmno_isValid(ptjmno):
        ptBDstr = eAutils.jmno_to_birthd(ptjmno)
    if ptBDstr is not None:
        pt_birthday = QDate.fromString(ptBDstr, "yyyyMMdd")
    # 연령만을 가지고 그룹으로 나눔.
    # (0: 일반독감, 1: 75세이상, 노인, 2: 70~74, 노인, 3: 65~69, 노인, 4: 소아(1회/2회접종 구분X))
    if FluSettings.BIRTH_6569_UNTIL < pt_birthday < FluSettings.BIRTH_CHILD_FROM:
        influ_group = 0
    elif pt_birthday <= FluSettings.BIRTH_75_OVER:
        influ_group = 1
    elif FluSettings.BIRTH_7074_FROM <= pt_birthday <= FluSettings.BIRTH_7074_UNTIL:
        influ_group = 2
    elif FluSettings.BIRTH_6569_FROM <= pt_birthday <= FluSettings.BIRTH_6569_UNTIL:
        influ_group = 3
    elif FluSettings.BIRTH_CHILD_FROM <= pt_birthday <= FluSettings.BIRTH_CHILD_UNTIL:
        influ_group = 4

    flu_vac_check(self, influ_group)


def flu_vac_check(self, influ_group: int):
    count = False
    paying = False
    as_Ex = False
    flu_old_today_list = ["X", "75~", "70~", "65~"]
    flu_child_today_list = ["X", "x1~", "x2~"]
    flu_old_today = flu_old_today_list.index(self.lblr_flu_date_checker_old.text())
    flu_child_today = flu_child_today_list.index(self.lblr_flu_date_checker_child.text())
    if flu_old_today == 0 and influ_group in [1, 2, 3]:
        eApopup.warning(text="사업기간이 아닙니다.")
        return
    elif flu_child_today == 0 and influ_group == 4:
        eApopup.warning(text="사업기간이 아닙니다.")
        return

    if influ_group == 0:
        paying = True

    elif influ_group == 4:
        if flu_child_today == 2:
            ok = eApopup.confirm(text="지금은 2회 접종자 접종기간입니다.\n2회 접종 대상자인가요?")
            if not ok:
                eApopup.notify(text="사업기간에 재방문 안내 필요.")
                return
            else:
                count = True
        else:
            count = True

    elif influ_group in [1, 2, 3]:
        if influ_group <= flu_old_today:
            count = True
        else:
            as_Ex = True

    flu_count_check(self, influ_group, count, paying, as_Ex)


def flu_count_check(self, influ_group: int, count: bool, paying: bool, as_Ex: bool):
    if influ_group == 0 and paying:
        flu_label_write(self, influ_group, paying=True)
        return
    if count:
        if int(self.lblr_count_total_flu_led.text().split("(")[0]) <= 99:
            flu_label_write(self, influ_group, count=True)
        else:
            eApopup.warning(text="하루 100회 접종이 마감되었습니다.")
            return
    if as_Ex:
        ok = eApopup.warning(text="현 대상자는 예외 접종 대상자입니다.\n대상자의 주소지가 의료취약지역으로 되어있나요?",
                             yes_no=True)
        if not ok:
            eApopup.warning(text="접종이 불가능합니다.")
            return
        else:
            flu_label_write(self, influ_group, as_Ex=True)


def flu_label_write(self, influ_group: int, count: bool = False, as_Ex: bool = False, paying: bool = False):
    # 일반 접종의 경우 빠르게 처리해주고.
    if paying:
        vaccine = "유료 독감접종"
        self.lblr_preview_nocount_vac_lbl.setText(vaccine)
        self.lblr_preview_count_vac_lbl.setText("")
        self.lblr_preview_counter_lbl.setText("")
        # 미리 시스템에 띄우기
        eAwinauto.vaccine_pt(self, 0, self.lblr_preview_ptjmno_lbl.text())
        Steps.TWO = True
        return

    # 접종 종류별, 카운터별 지정.
    if influ_group in [1, 2, 3]:
        if count:
            vaccine = "무료독감:노인"
            counter = Count.Flu_Old
            total_counter = 1
        if as_Ex:
            vaccine = "무료독감:예외"
            counter = Count.Flu_Ex
            total_counter = 0

    if influ_group == 4:
        vaccine = "무료독감:소아"
        counter = Count.Flu_Child
        total_counter = 1

    self.lblr_preview_nocount_vac_lbl.setText("")
    self.lblr_preview_count_vac_lbl.setText(vaccine)
    self.lblr_preview_counter_lbl.setText(
        f'{str(counter +1)}({str(Count.Flu_Total_Count + total_counter)}/100)'
    )
    # 미리 시스템에 띄우기
    eAwinauto.vaccine_pt(self, 1, self.lblr_preview_ptjmno_lbl.text())
    Steps.TWO = True
    Count.Selected = vaccine


# #- Flu접종이라면, 우선 환자를 분류한다.
# def flu_grouper(self, ptjmno:str):
#     '''
#     1. 환자의 주민번호를 토대로, 나이를 계산.
#     2. 국가독감접종사업 계획을 토대로 환자를 분류함.
#       - 일반 (group 0), 75세 이상 (group 1), 70~74세 (group 2), 65~69세 (group 3), 소아대상자 (group 4)
#     3. 또한 노인독감여부, 소아대상자의 경우 2회접종 필요 여부를 boolean으로 지정.
#     '''
#     # 기본 VAR 설정
#     if not FluSettings.FLU_NIP_AUTO:
#         ok = eApopup.warning(text = "국가독감접종의 자동분류가 해제!!!\n그대로 진행할까요?", yes_no = True)
#         if not ok: return
#         else:
#             self.lblr_preview_count_vac_lbl.setText("")
#             self.lblr_preview_counter_lbl.setText("")
#             self.lblr_preview_nocount_vac_lbl.setText(self.lblr_vaccines_cmb.currentText())
#             Steps.TWO = True
#             return
#     vac_twice = False
#     flu_old = True
#     # 환자 생일을 구하고.
#     if eAutils.jmno_isValid(ptjmno):
#         ptBDstr = eAutils.jmno_to_birthd(ptjmno)
#     if ptBDstr != None:
#         pt_birthday = QDate.fromString(ptBDstr, "yyyyMMdd")
#     # 환자 생일을 토대로 대상자에 해당하지 않으면,
#     if FluSettings.BIRTH_6569_UNTIL < pt_birthday < FluSettings.BIRTH_CHILD_FROM:
#         flu_old = False
#         flu_date_checker(self, group = 0)
#     # 75세 이상, 70~74세, 65~69세에 해당하는지 확인 후 group 지정.
#     elif pt_birthday <= FluSettings.BIRTH_75_OVER:
#         flu_date_checker(self, group = 1)
#     elif FluSettings.BIRTH_7074_FROM <= pt_birthday <= FluSettings.BIRTH_7074_UNTIL:
#         flu_date_checker(self, group = 2)
#     elif FluSettings.BIRTH_6569_FROM <= pt_birthday <= FluSettings.BIRTH_6569_UNTIL:
#         flu_date_checker(self, group = 3)
#     # 소아 대상자라면, 2회접종자 여부 확인하기.
#     # 2회 접종자 여부는 자동으로 확인 할 수 없기에 msgbox를 이용해 수동 확인하기.
#     elif FluSettings.BIRTH_CHILD_FROM <= pt_birthday <= FluSettings.BIRTH_CHILD_UNTIL:
#         flu_old = False
#         flu_twice = eApopup.confirm(text = "2회 접종 대상자 입니까?")
#         if flu_twice == "YES":
#             vac_twice = True
#         flu_date_checker(self, group = 4, vacTwice = vac_twice, fluOld = flu_old)
#     else:
#         return

# #- 환자분류 이후 전달받은 정보를 토대로 날짜를 기준으로 다시 분류.
# def flu_date_checker(self, group:int, vacTwice:bool = False, fluOld:bool = True):
#     Flu_Old_NotNOW = False
#     Flu_Child_NotNOW = False
#     canVac = False
#     OKasEX = False
#     PaidFlu = False
#     result = []
#     # 노인독감 사업기간이 시작 전 이거나 지났다면..
#     if self.parent.infos.date_today <= FluSettings.DATE_75_OVER:
#         Flu_Old_NotNOW = True
#     elif FluSettings.OLD_END_DATE <= self.parent.infos.date_today:
#         Flu_Old_NotNOW = True
#     # 소아독감 사업기간이 지났다면 Flu_Child_Ended를 True로.
#     if vacTwice:
#         if FluSettings.TWICE_CHILD_END_DATE <= self.parent.infos.date_today:
#             Flu_Child_NotNOW = True
#     else:
#         if FluSettings.ONCE_CHILD_END_DATE <= self.parent.infos.date_today:
#             Flu_Child_NotNOW = True
#     # 현재 날짜를 기준으로, 카운트가 필요한 접종가능 group을 리스트로 작성 - 노인
#     if FluSettings.DATE_75_OVER <= self.parent.infos.date_today < FluSettings.DATE_7074:
#         result = [1]
#     elif FluSettings.DATE_7074 <= self.parent.infos.date_today < FluSettings.DATE_6569:
#         result = [1, 2]
#     elif FluSettings.DATE_6569 <= self.parent.infos.date_today:
#         result = [1, 2, 3]
#     elif FluSettings.OLD_END_DATE <= self.parent.infos.date_today:
#         result = []
#     # 전달받은 2회 접종여부에 따라 사업기간여부 확인 및 접종 가능날짜를 자동으로 확인.
#     if vacTwice:
#         if self.parent.infos.date_today < FluSettings.DATE_CHILD_TWICE:
#             Flu_Child_NotNOW = True
#         if FluSettings.DATE_CHILD_TWICE <= self.parent.infos.date_today:
#             result.append(4)
#     else:
#         if self.parent.infos.date_today < FluSettings.DATE_CHILD_ONCE:
#             Flu_Child_NotNOW = True
#         if FluSettings.DATE_CHILD_ONCE <= self.parent.infos.date_today:
#             result.append(4)
#     # 노인독감 True이면서 Flu_Old_Ended가 참이라면, 사업기간 아님!
#     if fluOld and Flu_Old_NotNOW:
#         eApopup.notify(text = "노인 독감 접종 사업기간이 아닙니다.")
#         return
#     # 노인독감아니면서 (소아독감) Flu_Child_Ended가 참이라면, 사업기간 아님!
#     if not fluOld and Flu_Child_NotNOW:
#         eApopup.notify(text = "소아 독감 접종 사업기간이 아닙니다.")
#         return
#     # Group 0 (즉, 일반접종)은 100명 카운트 필요없으니 바로 프리뷰에 작성.
#     if group == 0:
#         PaidFlu = True
#         write_flu_preview(self, fluOld, canVac, OKasEX, PaidFlu)
#     # 그 이외의 경우에는 접종가능여부, 예외접종 여부 등을 boolean 작성 후 전달.
#     elif not Flu_Old_NotNOW and group != 4 and group in result:
#         canVac = True
#     elif not Flu_Old_NotNOW and group != 4 and group not in result:
#         OKasEX = True
#     elif not Flu_Child_NotNOW and group == 4 and group in result:
#         canVac = True
#     # 마지막 함수로 전달.
#     flu_count_checker(self, fluOld, canVac, OKasEX)

# #- 최종적으로 일일 100명 접종 제한을 확인.
# def flu_count_checker(self, flu_old:bool, can_vacc:bool, ok_as_EX:bool):
#     '''
#     ** 전달 받은 정보를 일일 100명 제한 확인 후 최종 접종여부 판단.
#     1. 전달 받은 노인독감여부, 접종가능여부(카운트) 및 예외접종가능여부(노인)을 분류.
#     2. 현재 총 독감 카운터(예외를 제외한)가 99 또는 그 이하라면 진행.
#     3. 100 또는 100이상(생기면 절대 안되지만..)이라면 중단.
#     4. 물론 노인독감의 예외접종자라면, 진행가능
#     4. 추후를 위해 노인독감여부, 접종가능여부 및 예외접종여부는 같이 전달.
#     '''
#     # 99이하면 진행
#     if can_vacc and Count.Flu_Total_Count <= 99:
#         write_flu_preview(flu_old, can_vacc, ok_as_EX)
#     # 100 또는 그 이상이라면 중단.
#     elif can_vacc and Count.Flu_Total_Count >= 100:
#         eApopup.warning(text = "하루 접종 최대 인원 수를 초과했습니다.")
#         return
#     # 예외접종자라면 진행 가능. ok_as_EX만 확인하면 되지만, 그냥.. 좀 더 확실하게 flu_old까지 확인.
#     elif flu_old and ok_as_EX:
#         write_flu_preview(self, flu_old, can_vacc, ok_as_EX)

# #- Flu 접종의 마지막.. Print Preview 작성.
# def write_flu_preview(self, FluOld:bool, canVac:bool, OKasEX:bool, PaidFlu:bool = False):
#     '''
#     라벨 프린트 폼 작성.
#     1. PaidFlu라면, 카운트 필요없으니 일반 접종처럼 작성.
#     2. 노인독감이면서 접종가능이라면 카운팅 카운터.
#     3. 노인독감이면서 접종불가 하지만 예외접종가능 이라면 예외 카운터.
#     4. 노인독감아니면서 접종가능이라면 소아독감, 카운팅 카운터.
#     5. 2단계도 완료로 해주고.
#     6. 마지막으로 PaidFlu가 아닌경우 Count class 내 selected에 현재 백신종류 지정하기.
#         - 추후 Count.add_counter함수 사용에 필요.
#     '''
#     # 일반 접종의 경우 빠르게 처리해주고.
#     if PaidFlu:
#         vaccine = "유료 독감접종"
#         self.lblr_preview_nocount_vac_lbl.setText(vaccine)
#         self.lblr_preview_count_vac_lbl.setText("")
#         self.lblr_preview_counter_lbl.setText("")
#         Steps.TWO = True
#         return
#     # 접종 종류별, 카운터별 지정.
#     if FluOld and canVac:
#         vaccine = "무료독감:노인"
#         counter = Count.Flu_Old
#         total_counter = 1
#     elif FluOld and OKasEX and not canVac:
#         vaccine = "무료독감:예외"
#         counter = Count.Flu_Ex
#         total_counter = 0
#     elif not FluOld and canVac:
#         vaccine = "무료독감:소아"
#         counter = Count.Flu_Child
#         total_counter = 1

#     self.lblr_preview_nocount_vac_lbl.setText("")
#     self.lblr_preview_count_vac_lbl.setText(vaccine)
#     self.lblr_preview_counter_lbl.setText(
#         f'{str(Count.Flu_Total_Count + total_counter)} ({str(counter +1)})'
#     )

#     Steps.TWO = True
#     Count.Selected = vaccine


# 코로나 접종 분류.
def covid_org(self, vaccine: str):
    '''
    우선 코로나 접종의 일일 100명 제한을 확인하고,
    전달받은 vaccine 종류에 따라, 카운터 지정하고.
    라벨 폼 작성 후 2단계 완료 및 Count.Selected 지정.
    '''
    # 100명 또는 그 이상이라면 중단하기.
    if Count.COVID_Total >= 100:
        eApopup.warning(text="금일 코로나19 접종을 완료했습니다.")
        return
    # 전달 받은 백신의 코드값을 알아내고.
    vac_code = Count.Vaccines[vaccine]
    # 해당 코드값을 이용한 현재 카운터 값을 가져온다.
    counter = getattr(Count, vac_code)
    # 라벨폼에 정보를 기입.
    self.lblr_preview_nocount_vac_lbl.setText("")
    self.lblr_preview_count_vac_lbl.setText(vaccine)
    self.lblr_preview_counter_lbl.setText(f'총 코로나 접종: {str(Count.COVID_Total + 1)} ({str(counter + 1)})')
    # 미리 시스템에 띄우기
    eAwinauto.vaccine_pt(self, 2, self.lblr_preview_ptjmno_lbl.text())
    Steps.TWO = True
    Count.Selected = vaccine


# 프린트와 동시에 필요시 DB에 카운터 정보 저장.
def print_save_it(self, counter: object = None):
    # 스텝1/2를 진행했는지 먼저 확인하고
    if not Steps.ONE:
        eApopup.notify(text="환자정보를 먼저 입력하세요.")
        return
    if not Steps.TWO:
        eApopup.notify(text="백신을 먼저 선택해주세요.")
        return
    # 프린터 설정하고
    printer = QPrinter(QPrinter.HighResolution)
    printer.setPrinterName("4BARCODE 4B-2054L")
    printer.setOutputFormat(QPrinter.NativeFormat)
    printer.setFullPage(True)
    pg_size = QPageSize(QSizeF(80, 40), QPageSize.Millimeter)
    pg_margins = QMarginsF(0, 0, 0, 0)
    printer.setPageSize(pg_size)
    printer.setPageMargins(pg_margins)
    # 페인터 설정하고
    painter = QPainter(printer)
    xscale = printer.pageRect(QPrinter.DevicePixel).width() / self.lblr_preview_frame.width()
    yscale = printer.pageRect(QPrinter.DevicePixel).height() / self.lblr_preview_frame.height()
    scale = min(xscale, yscale)
    # painter.translate(printer.paperRect(QPrinter.Millimeter).center())
    painter.scale(yscale, yscale)
    # 프린트 전송
    self.lblr_preview_frame.render(painter, QPoint(0, 0), painter.viewport())
    # 페인터 끄기
    painter.end()

    # 프린트와 동시에 카운터 올리고
    if Count.Selected != "":
        Count.add_counter()

    # 매번 바로바로 DB에 반영시키기
    write_DB(self)

    # # 자동으로 접종백신에 맞는 시스템에 주민번호까지 입력할까요?
    # ok = eApopup.confirm(text = "접종할 백신에 맞는 시스템으로 이동/입력할까요?")
    # if ok:
    #     if self.lblr_vaccines_cmb.currentText() in Vaccines.COVID:
    #         vacsys = 2
    #     elif self.lblr_vaccines_cmb.currentText() == '인플루엔자' and self.lblr_preview_count_vac_lbl.text() != '':
    #         vacsys = 1
    #     else:
    #         vacsys = 0
    #     eAwinauto.vaccine_pt(self, vacsys, self.lblr_preview_ptjmno_lbl.text())

    # 차팅용 코멘트 복사해놓기.
    if self.lblr_preview_nocount_vac_lbl.text() == "":
        charting_vac = self.lblr_preview_count_vac_lbl.text()
    else:
        charting_vac = self.lblr_preview_nocount_vac_lbl.text()

    charting_txt = f"""# 예방접종 [{charting_vac}]
 - 상기도 감염 증세 포함 발열 여부: 없음.
 - 타 접종 포함 접종 후 부작용 발생여부: 없음. """
    eAinput.copy_it(charting_txt)

    # 그리고 모든 항목을 리셋하기.
    reset_it(self)


# 리셋하기 함수
def reset_it(self):
    # 날짜는 다시 적어주고(혹시 모르니까) 나머지 라벨 폼은 전부 공란으로
    self.lblr_preview_date_lbl.setText(self.infos.date_today.toString("yyyy년MM월dd일(ddd)"))
    self.lblr_preview_nocount_vac_lbl.setText("")
    self.lblr_preview_count_vac_lbl.setText("")
    self.lblr_preview_counter_lbl.setText("")
    self.lblr_vaccines_cmb.setCurrentIndex(0)
    self.lblr_preview_ptname_lbl.setText("")
    self.lblr_preview_ptjmno_lbl.setText("")
    self.lblr_preview_ptphone_lbl.setText("")
    # 단계 확인용 VAR도 초기화해주고
    Steps.ONE = False
    Steps.TWO = False
    # 선택 백신 임시저장값도 초기화해주고
    Count.Selected = ""
    # 확인삼아 카운터 다시 업데이트 해주고.
    counter_update(self)


# 카운터 수정.
def edit_counter(self):
    # 먼저 확인하고
    confirm = eApopup.warning(text="현재 카운트를 수정하시겠습니까?", yes_no=True)
    if confirm == 'NO':
        return
    # 독감접종 / 코로나 중 선택.
    menu_items = ['국가독감접종', '코로나19접종']
    which_type = eApopup.menu(title="수정할 백신 종류는?", buttons=menu_items)
    # 창 닫으라면 그냥 닫아주고
    if which_type == 'CLOSE':
        return
    # 독감 카운터 종류를 선택했거나
    elif which_type == menu_items[0]:
        menu_items = ['무료독감:노인', '무료독감:예외', '무료독감:소아']
    # 코로나 카운터 종류를 선택하고.
    else:
        menu_items = ['화이자XBB.1.5', '모더나XBB.1.5']

    which_vac = eApopup.menu(title="수정할 백신은?", buttons=menu_items)

    if which_vac == 'CLOSE':
        return
    # 현재 수정할 카운터의 값을 미리 띄워주고
    else:
        vac_code = Count.Vaccines[which_vac]
        edit_value = eApopup.get_int(self, content=f'{which_vac} 카운트 수정', default_val=int(getattr(Count, vac_code)))
    # 입력받은 카운터 값을 전달
    Count.edit_counter(vac_code, edit_value)
    # 업데이트하고, DB저장.
    counter_update(self)
    write_DB(self)
