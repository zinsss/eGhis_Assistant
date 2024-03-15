import sqlite3

from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt, QDate

import main
from eAmodules import eApopup, eAreminders


## CalendarWidget, Predefined Styling Formats
WEEKDAYS = QtGui.QTextCharFormat()
WEEKDAYS.setForeground(QtGui.QBrush(QtGui.QColor(193, 198, 216)))
SATURDAYS = QtGui.QTextCharFormat()
SATURDAYS.setForeground(QtGui.QBrush(QtGui.QColor(100, 133, 188)))
SUNDAYS = QtGui.QTextCharFormat()
SUNDAYS.setForeground(QtGui.QBrush(QtGui.QColor(191, 97, 106)))
TASKS_DUE = QtGui.QTextCharFormat()
TASKS_DUE.setForeground(QtGui.QBrush(QtGui.QColor(177, 200, 144)))
HOLIDAYS = QtGui.QTextCharFormat()
HOLIDAYS.setForeground(QtGui.QBrush(QtGui.QColor(255, 90, 100)))
TODAY = QtGui.QTextCharFormat()
TODAY.setForeground(QtGui.QBrush(QtGui.QColor(255, 255, 255)))
SELECTED_DAY = QtGui.QTextCharFormat()
SELECTED_DAY.setForeground(QtGui.QBrush(QtGui.QColor(235, 200, 140)))
EVENT = QtGui.QTextCharFormat()
EVENT.setForeground(QtGui.QBrush(QtGui.QColor(155,122,222)))
LPDOM = QtGui.QTextCharFormat()
LPDOM.setForeground(QtGui.QBrush(QtGui.QColor(222, 133, 100)))


## STYLES FOR CLAIM GUI ALARM ON/OFF
ALRM_ON_STYLE = "color: rgb(222, 133, 100);"
ALRM_OFF_STYLE = "color: rgb(60,65,80);"


## FULLNAMES OF MONTH, BY INDEX IN A LIST
MONTH_NAME = [
    '', # Blanked on purpose. (Easier with python index mechanism, starting with 0)
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]


## DB 연결. DB가 없으면 새로 작성하고, 테이블도 작성함.
def connect_DB_and_load(self, year:int = None, month:int = None):
    # Load DB
    con = sqlite3.connect("./database/eAcalrem.db")
    cur = con.cursor()
    # Create table if not exists
    con.execute(
        '''CREATE TABLE if not exists Calendar(
        Start_Date TEXT,
        End_Date TEXT,
        Not_OPEN INTEGER,
        Event_Title TEXT)
        '''
    )
    # If specified on function call, can get datas of that year/month.
    # Currently not implemented in app for any functionality.
    # Just defaults for now.
    if not year or not month:
        year = self.calendar_wdg.yearShown() 
        month = self.calendar_wdg.monthShown()
    
    first_day_of_month = f'{year}.{str(month).zfill(2)}.01'
    last_day_of_month = f'{year}.{str(month).zfill(2)}.{QDate.fromString(first_day_of_month, "yyyy.MM.dd").daysInMonth()}'
    
    # Get all datas in DB.
    events_for_month = [list(item) for item in list(
        cur.execute(f"""
                    SELECT *
                    FROM Calendar
                    WHERE
                    Start_Date BETWEEN '{first_day_of_month}' AND '{last_day_of_month}'
                    OR
                    End_Date BETWEEN '{first_day_of_month}' AND '{last_day_of_month}'
                    """).fetchall()
    )]
    not_open_events = []
    open_events = []
    LPDoM_date = ""
    for item in events_for_month:
        if item[3] == '청구일':
            LPDoM_date = item[0]
        if item[0] == item[1]:
            if item[2]:
                not_open_events.append(item[0])
            else:
                open_events.append(item[0])
        else:
            start_day = QDate.fromString(item[0], "yyyy.MM.dd")
            end_day = QDate.fromString(item[1], "yyyy.MM.dd")
            period = start_day.daysTo(end_day) +1
            for i in range(period):
                if start_day.addDays(i).month() == month:
                    if item[2]:
                        not_open_events.append(start_day.addDays(i).toString("yyyy.MM.dd"))
                    else:
                        open_events.append(start_day.addDays(i).toString("yyyy.MM.dd"))
    
    # Remove Duplicates
    not_open_events = list(set(not_open_events))
    open_events = list(set(open_events))
    
    # Close DB connection
    con.close()
    return not_open_events, open_events, LPDoM_date


#= Calendar Styling, for calendar_wdg and calendar_opt_wdg
def calendar_styling(self, calendar_name:str):
    calendarz = ['calendar_wdg', 'calendar_opt_wdg']
    if calendar_name not in calendarz:
        return
    target = getattr(self, calendar_name)
    # Set Date on Year_Month_Button
    cal_year = target.yearShown()
    cal_month = target.monthShown()
    self.calendar_day_month_lbl.setText(MONTH_NAME[cal_month])
    self.calendar_day_year_lbl.setText(f'{cal_year}')
    
    target.setDateTextFormat(QDate(), QtGui.QTextCharFormat())
    # Following lines define sytles (font color) of days, weekends, etc.
    target.setWeekdayTextFormat(Qt.Monday, WEEKDAYS)
    target.setWeekdayTextFormat(Qt.Tuesday, WEEKDAYS)
    target.setWeekdayTextFormat(Qt.Wednesday, WEEKDAYS)
    target.setWeekdayTextFormat(Qt.Thursday, WEEKDAYS)
    target.setWeekdayTextFormat(Qt.Friday, WEEKDAYS)
    target.setWeekdayTextFormat(Qt.Saturday, SATURDAYS)
    target.setWeekdayTextFormat(Qt.Sunday, SUNDAYS)
    target.setDateTextFormat(self.infos.date_today, TODAY)
    target.setStyleSheet("""
                         QCalendarWidget QTableView{
                             alternate-background-color: rgb(50, 55, 65);
                         }
                         QCalendarWidget QAbstractItemView:!enabled {
                             color:rgb(60, 60, 70);
                         }
                         """)
    

#= Update Calendar_WDG
def calendar_update(self):
    calendar_styling(self, 'calendar_wdg')
    update_LPDoM(self)
    # get DB data
    not_open_events, open_events, LPDoM_date = connect_DB_and_load(self)
    if open_events:
        for event in open_events:
            e_day = QDate.fromString(event, "yyyy.MM.dd")
            self.calendar_wdg.setDateTextFormat(e_day, EVENT)
    if not_open_events:
        for event in not_open_events:
            h_day = QDate.fromString(event, "yyyy.MM.dd")
            self.calendar_wdg.setDateTextFormat(h_day, HOLIDAYS)
    if LPDoM_date:
        LPDoM = QDate.fromString(LPDoM_date, "yyyy.MM.dd")
        self.calendar_wdg.setDateTextFormat(LPDoM, LPDOM)
    # Write day_info_lwg of selected date.            
    date_selected(self)   
            

## Date Selected
def date_selected(self):
    # Just in case, some non completed input was in place. 
    self.calendar_day_info_led.setText("")
    # Selected Date
    selected_date = self.calendar_wdg.selectedDate()
    # GUI writing selected Date info.    
    self.calendar_day_name_lbl.setText(selected_date.toString("dddd"))
    self.calendar_day_date_lbl.setText(selected_date.toString("dd"))
    self.calednar_day_mont_year_lbl.setText(selected_date.toString("MMMM, yyyy"))
    # Clear day_info listwidget
    self.calendar_day_info_lwg.clear()
    # Load DB
    con = sqlite3.connect("./database/eAcalrem.db")
    cur = con.cursor()
    # Create table if not exists
    events_of_day = con.execute(f"""
                                SELECT Event_Title, Not_OPEN FROM Calendar
                                WHERE '{selected_date.toString("yyyy.MM.dd")}'
                                BETWEEN Start_Date AND End_Date
                                """).fetchall()
    # Write NOT_Open_Events to listwidget first for top position 
    for event in events_of_day:
        if event[1]:
            item = QtWidgets.QListWidgetItem(event[0])
            # item.setFlags(
            #     Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled
            # )
            # Set Color of sublist item according to status
            item.setForeground(QtGui.QBrush(QtGui.QColor(225, 90, 100)))
            # Add to QListWidget
            self.calendar_day_info_lwg.addItem(item)
    for event in events_of_day:
        if not event[1]:
            item = QtWidgets.QListWidgetItem(event[0])
            if event[0] == '청구일':
                item.setForeground(QtGui.QBrush(QtGui.QColor(222, 133, 100)))
            self.calendar_day_info_lwg.addItem(item)
            
            
## Show and Select TODAY on today button click.
def go_today(self):
    self.calendar_wdg.showToday()
    self.calendar_wdg.setSelectedDate(self.infos.date_today)


## Add Event, from Stack(0)
def add_event_from_main(self):
    """
    Adds event from QLineEdit of calendar_stack index(0).
    Simply Type Event Title and Press Enter.
    IF Event Title STARTS WITH '*', eg. "*Christmas"
    The event title will be Christmas (without preceding '*')
    and the event will be set Not_OPEN True.
    Multi day events must be added from stack index(1).
    """
    event_title = self.calendar_day_info_led.text().rstrip()
    if event_title.startswith("*"):
        event_title = event_title[1:]
        not_open = True
    else:
        not_open = False
    # 사용자는 '청구일'을 일정 제목으로 사용할 수 없음.
    # eGhisAssistant가 자동으로 계산, 관리.
    if event_title == '청구일':
        eApopup.warning(text = '[청구일]은;\n입력할 수 없는 일정 제목입니다.\n자동으로 관리되는 일정 제목입니다.')
        self.calendar_day_info_led.setText("")
        return
    date = self.calendar_wdg.selectedDate().toString("yyyy.MM.dd")
    # Load DB and Verify if Duplicate First
    con = sqlite3.connect("./database/eAcalrem.db")
    cur = con.cursor()
    # Create table if not exists
    duplicate = cur.execute(f"""
                            SELECT * FROM Calendar
                            WHERE
                            Event_Title = '{event_title}'
                            AND
                            (Start_Date = '{date}' OR End_Date = '{date}')
                            """).fetchall()
    if duplicate:
        eApopup.warning(
            text = "같은 일정이 해당 날짜에 이미 존재합니다."
        )
    new_event = [date, date, str(int(not_open)), event_title]
    cur.execute(f"INSERT INTO Calendar VALUES (?, ?, ?, ?);", new_event)
    con.commit()
    con.close()
    
    calendar_update(self)
    self.calendar_day_info_led.setText("")
    

## OPTIONS Page
def options_btn_clicked(self):
    # 버튼을 눌러 들어온 경우, 기 일정을 선택한것은 아니기에,
    # 결국 reset과 같은 역할.
    sel_date = self.calendar_wdg.selectedDate()
    self.calendar_opt_wdg.setSelectedDate(sel_date)
    calendar_opt_page_changed(self)
    self.calendar_event_delete_btn.setEnabled(False)
    self.calendar_event_date_dte.setDate(sel_date)
    self.calendar_opt_event_led.setText("")
    self.calendar_multi_day_cbx.setChecked(False)
    self.calendar_select_end_date_btn.setEnabled(False)
    self.calendar_select_end_date_btn.setChecked(False)    
    self.calendar_start_date_lbl.setText(sel_date.toString("yyyy.MM.dd(ddd)"))
    self.calendar_end_date_lbl.setText("")
    self.calendar_not_open_cbx.setChecked(False)
    self.calendar_stack.setCurrentIndex(1)
    self.infos.opened_event = []
    
    
def event_double_clicked(self):
    event_title = self.calendar_day_info_lwg.currentItem().text()
    if event_title == '청구일':
        eApopup.warning(text = '[청구일]은;\n편집할 수 없는 일정입니다.\n자동으로 관리됩니다.')
        self.calendar_day_info_lwg.setCurrentItem(None)
        return
    target_date = self.calendar_wdg.selectedDate()
    self.calendar_event_delete_btn.setEnabled(True)
    # Load DB
    con = sqlite3.connect("./database/eAcalrem.db")
    cur = con.cursor()
    # Find correct event from DB
    target = cur.execute(f"""
                         SELECT * FROM Calendar
                         WHERE
                         Event_Title = '{event_title}'
                         AND
                         ('{target_date.toString("yyyy.MM.dd")}'
                         BETWEEN
                         Start_Date AND End_Date)
                         """).fetchone()
    # Close Connection
    con.close()
    # Save Opened Event for later
    self.infos.opened_event = list(target)
    # Writing event info to gui
    start_date = QDate.fromString(target[0], "yyyy.MM.dd")
    self.calendar_opt_wdg.setSelectedDate(start_date)
    self.calendar_event_date_dte.setDate(start_date)
    self.calendar_start_date_lbl.setText(start_date.toString("yyyy.MM.dd(ddd)"))
    if target[0] == target[1]:
        self.calendar_multi_day_cbx.setChecked(False)
        self.calendar_end_date_lbl.setText("")
    else:
        self.calendar_multi_day_cbx.setChecked(True)
        end_date = QDate.fromString(target[1], "yyyy.MM.dd")
        self.calendar_end_date_lbl.setText(end_date.toString("yyyy.MM.dd(ddd)"))
    if target[2]:
        self.calendar_not_open_cbx.setChecked(True)
    else:
        self.calendar_not_open_cbx.setChecked(False)
    self.calendar_opt_event_led.setText(target[3])
    print(self.infos.opened_event)
    self.calendar_stack.setCurrentIndex(1)


def cal_opt_clicked(self):
    # 클릭된 날짜를 우선 저장하고,
    sel_date = self.calendar_opt_wdg.selectedDate()
    # 'select end date'가 체크되어있다면, 즉 end date 선택한 것이라면,
    if self.calendar_select_end_date_btn.isChecked():
        # 시작일로 부터 마지막일까지의 일수가 0보다 적다면
        # >> 시작일과 마지막일의 순서를 변경해 입력할지 물어보자.
        start_date = self.calendar_event_date_dte.date()
        if start_date.daysTo(sel_date) < 0:
            ok = eApopup.warning(
                text = "일정의 시작일이 뒤에 있을 수 없습니다.\nStart와 End Date를 바꿔서 입력할까요?",
                yes_no = True
            )
            # 아니라면 그냥 넘어가고..
            if not ok: return
            self.calendar_end_date_lbl.setText(start_date.toString("yyyy.MM.dd(ddd)"))
            self.calendar_event_date_dte.setDate(sel_date)
            self.calendar_start_date_lbl.setText(sel_date.toString("yyyy.MM.dd(ddd)"))
        # 같은날을 선택했어도 그냥 넘어가고..
        elif start_date.daysTo(sel_date) == 0: return
        # 제대로 입력이 되어있다면, end_date_lbl에 날짜를 저장하고.
        else:
            self.calendar_end_date_lbl.setText(sel_date.toString("yyyy.MM.dd(ddd)"))
        # 혹시나 수정됬을 수 있는 시작일과 마지막일을 다시 불러와서,
        start = QDate.fromString(self.calendar_start_date_lbl.text(), "yyyy.MM.dd(ddd)")
        end = QDate.fromString(self.calendar_end_date_lbl.text(), "yyyy.MM.dd(ddd)")
        # 모든 날짜를 선택된 스타일링으로 바꿔주자.
        for i in range(start.daysTo(end) + 1):
            self.calendar_opt_wdg.setDateTextFormat(start.addDays(i), SELECTED_DAY)
        self.calendar_select_end_date_btn.setChecked(False)
    # 'select end date'가 체크 해제 상태인 경우에는;
    else:
        # 기 선택 후 다시 수정하는 경우 위에서 실행한 스타일링이 남겨져 있을 수 있으니,
        # 원래 기본 스타일링으로 다시 불러온 다음,
        calendar_styling(self, "calendar_opt_wdg")
        # Event_date_dte와 start_date_lbl을 입력해놓자.
        # 노트: 이 상태에는 multi-day event가 체크 또는 해제 되있을 수 있기에,
        # start/end_date_lbl의 스타일이 어떻든, 날짜는 그대로 입력해주고,
        # 이번 선택은 end_date는 아니었으니, end_date_lbl은 바로 setText("")으로 공란으로 만들자.
        self.calendar_event_date_dte.setDate(sel_date)
        self.calendar_start_date_lbl.setText(sel_date.toString("yyyy.MM.dd(ddd)"))
        self.calendar_end_date_lbl.setText("")


def calendar_opt_page_changed(self):
    month = self.calendar_opt_wdg.monthShown()
    year = self.calendar_opt_wdg.yearShown()
    self.calendar_opt_month_year_lbl.setText(f'{year}.{str(month).zfill(2)}')


def multi_day_status_toggle(self):
    toggle = self.calendar_multi_day_cbx.isChecked()
    self.calendar_select_end_date_btn.setEnabled(toggle)
    self.calendar_select_end_date_btn.setChecked(False)
    if toggle:
        self.calendar_start_date_lbl.setStyleSheet("color:rgb(170, 175, 250);")
        self.calendar_from_to_lbl.setStyleSheet("color:rgb(170, 175, 200);")
        self.calendar_end_date_lbl.setStyleSheet("color:rgb(170, 175, 250);")
    else:
        self.calendar_start_date_lbl.setStyleSheet("color:transparent;")
        self.calendar_from_to_lbl.setStyleSheet("color:transparent;")
        self.calendar_end_date_lbl.setStyleSheet("color:transparent;")
        

def not_open_check_toggle(self):
    if self.calendar_not_open_cbx.isChecked():
        self.calendar_day_info_led.setStyleSheet("color:transparent")


## Add a Event from OPT
def write_btn_clicked(self):
    # Event title은 rstrip은 해서 가져오자.
    event_title = self.calendar_opt_event_led.text().rstrip()
    if event_title == "":
        eApopup.warning(text = "일정이 입력되지 않았습니다.")
        return
    elif event_title == "청구일":
        eApopup.warning(text = "[청구일]은\n추가 또는 편집할 수 없습니다.\n자동으로 관리됩니다.")
        return
    
    start_date = self.calendar_event_date_dte.date().toString("yyyy.MM.dd")
    
    # Multi Day 체크 되어있는 경우에는 end_date를 end_date_lbl에서 역으로 다시 가져오고,
    if self.calendar_multi_day_cbx.isChecked():
        end_date = QDate.fromString(self.calendar_end_date_lbl.text(), "yyyy.MM.dd(ddd)").toString("yyyy.MM.dd")
        if not end_date:
            eApopup.warning(text = "일정의 날짜를 확인해주세요.")
            return
        # Selec End Date 버튼 입력 시 이미 MultiDay check시 방지하도록 되어있으나,
        # 혹시 인지못하고 있는 방법등으로 입력이 되어있는 경우를 대비하여 추가적으로
        # Multi Day 체크이나 start/end date가 동일 한 경우를 다시 확인해보자.
        if start_date == end_date:
            ok = eApopup.warning(
                text = "Multi-day Event가 맞나요?\nStart 및 End date이 동일합니다.\n단일 일정으로 입력할까요?",
                yes_no = True
            )
            if not ok: return
            self.calendar_multi_day_cbx.setChecked(False)
            end_date = start_date
    # Multi Day 체크 해제된 경우에는 그냥 start_date와 동일하게 입력.
    else:
        end_date = start_date
    # Not OPEN의 경우 체크박스 체크/해제에 따라 int value로 가져오고.
    if self.calendar_not_open_cbx.isChecked():
        not_open = 1
    else: 
        not_open = 0
    
    event_to_write = [start_date, end_date, not_open, event_title]
    
    # 새로 입력인지, 기일정의 편집인지를 확인해서 각각의 맞는 method로 전달하자.
    if not self.infos.opened_event:
        new_event_save(event_to_write)
    else:
        edit_event(self, event_to_write)
    # Reset and Go BACK
    options_btn_clicked(self)
    calendar_update(self)
    self.calendar_stack.setCurrentIndex(0)


# Called From write_btn_clicked if new item
def new_event_save(event_to_write:list):    
    # Load DB
    con = sqlite3.connect("./database/eAcalrem.db")
    cur = con.cursor()
    # Write to DB
    cur.execute(f"INSERT INTO Calendar VALUES (?, ?, ?, ?);", event_to_write)
    # Commit and Close Connection
    con.commit()
    con.close()


# Called From write_btn_clicked if editing item
def edit_event(self, event_to_write:list):
    target_event = self.infos.opened_event
    # Load DB
    con = sqlite3.connect("./database/eAcalrem.db")
    cur = con.cursor()
    # Find correct event from DB
    cur.execute(f"""UPDATE Calendar 
                SET Start_Date = '{event_to_write[0]}',
                End_Date = '{event_to_write[1]}',
                Not_OPEN = '{event_to_write[2]}',
                Event_Title = '{event_to_write[3]}'
                WHERE Start_Date = '{target_event[0]}' AND
                End_Date = '{target_event[1]}' AND
                Not_OPEN = '{target_event[2]}' AND
                Event_Title = '{target_event[3]}'
                """)
    # Close Connection
    con.commit()
    con.close()
    
    
# Delete existing Event
def delete_event(self):
    target_event = self.infos.opened_event
    # Load DB
    con = sqlite3.connect("./database/eAcalrem.db")
    cur = con.cursor()
    # Find correct event from DB
    cur.execute(f"""
                DELETE FROM Calendar
                WHERE Start_Date = '{target_event[0]}' AND
                End_Date = '{target_event[1]}' AND
                Not_OPEN = '{target_event[2]}' AND
                Event_Title = '{target_event[3]}'   
                """)
    # Close Connection
    con.commit()
    con.close()
    # Reset and Go BACK
    options_btn_clicked(self)
    calendar_update(self)
    self.calendar_stack.setCurrentIndex(0)


## Yearly View
# Toggle between yearly and calendar main page.
def yearly_page_toggle(self):
    self.calendar_yearly_year_led.setText(str(self.infos.date_today.year()))
    index = self.calendar_stack.currentIndex()
    if index == 0:
        self.calendar_stack.setCurrentIndex(2)
        view_yearly(self)
    else:
        self.calendar_stack.setCurrentIndex(0)
    

def year_is_valid(target_year:str):
    if not target_year.isdigit():
        eApopup.warning(text="년도를 정확히 입력해주세요.")
        return False
    elif not 2022 <= int(target_year) <= 2042:
        eApopup.warning(text="년도를 확인해주세요.")
        return False
    else:
        return True
    
    
def year_navigation_btn(self, prev:bool = False):
    target_year = self.calendar_yearly_year_led.text().rstrip()
    if not year_is_valid(target_year):
        return
    if prev:
        self.calendar_yearly_year_led.setText(f'{int(target_year)-1}')
    else:
        self.calendar_yearly_year_led.setText(f'{int(target_year)+1}')
    view_yearly(self)
    

def view_yearly(self):
    self.calendar_yearly_lwg.clear()    
    target_year = self.calendar_yearly_year_led.text().rstrip()
    if not year_is_valid(target_year):
        return
    # Load DB
    con = sqlite3.connect("./database/eAcalrem.db")
    cur = con.cursor()
    # Find correct event from DB
    events_in_target = cur.execute(f"""
                                   SELECT * FROM Calendar
                                   WHERE
                                   (Start_Date BETWEEN '{target_year}.01.01' AND '{target_year}.12.31')
                                   OR
                                   (End_Date BETWEEN '{target_year}.01.01' AND '{target_year}.12.31')
                                   ORDER BY Start_Date
                                   """).fetchall()
    # Close Connection
    con.close()
    # GUI에 전용 형식(?)에 맞게 써주면 됨.
    for event in events_in_target:
        start_date = QDate.fromString(event[0], "yyyy.MM.dd").toString("yyyy.MM.dd(ddd)")
        end_date = QDate.fromString(event[1], "yyyy.MM.dd").toString("yyyy.MM.dd(ddd)")
        content = f'## {start_date} | {event[3]}'
        if start_date != end_date:
            content = f'{content}\n ~ {end_date} |'
        
        item = QtWidgets.QListWidgetItem(content)
        # Set Color of sublist item according to status
        if event[2]:
            item.setForeground(QtGui.QBrush(QtGui.QColor(225, 90, 100)))
        self.calendar_yearly_lwg.addItem(item)
        

#======= Finding LPDOM
#- 청구일의 전제 조건. 1) 일요일 아니고, 2) 토요일은 기본적으로 아니되, 장날이 아닌 토요일은 제외. 3) 휴진일/공휴일이 아니어야지..
def find_LPDoM(self):
    today_date = self.infos.date_today
    today_year = today_date.year()
    today_month = today_date.month()
    today_month_last_day = today_date.daysInMonth()
    LPDoM = QDate(today_year, today_month, today_month_last_day)
    # Load DB
    con = sqlite3.connect("./database/eAcalrem.db")
    cur = con.cursor()
    # Find correct event from DB
    not_open_days = cur.execute(f"""
                                SELECT * FROM Calendar
                                WHERE Not_Open = '1'
                                AND
                                ((Start_Date BETWEEN
                                '{today_year}.{str(today_month).zfill(2)}.01'
                                AND '{today_year}.{str(today_month).zfill(2)}.{today_month_last_day}')
                                OR
                                (End_Date BETWEEN
                                '{today_year}.{str(today_month).zfill(2)}.01'
                                AND '{today_year}.{str(today_month).zfill(2)}.{today_month_last_day}'))
                                """).fetchall()
    # Close Connection
    con.close()
    # DB에서 불러온 이달의 휴일(일정)을 QDate Object로 변환 및 Multi Day일정이 있는 경우, 모두 단일 항목으로 리스트화.
    not_open_dates = []
    for day in not_open_days:
        if day[0] == day[1]:
            not_open_dates.append(QDate.fromString(day[0], "yyyy.MM.dd"))
        else:
            start = QDate.fromString(day[0], "yyyy.MM.dd")
            end = QDate.fromString(day[1], "yyyy.MM.dd")
            days = start.daysTo(end)
            for i in range(days+1):
                not_open_dates.append(start.addDays(i))
    # 위 언급된 청구일의 전제조건을 기준으로, 합당하지 않는 경우 while loop를 통해 찾아질때까지 돌려~~
    while True:
        # 현재 LPDoM target이 일요일이면 하루 앞으로..
        if LPDoM.dayOfWeek() == 7:
            LPDoM = LPDoM.addDays(-1)
        # 토요일이면, 장날은 아닌지 확인하고, 장날이 아니라면, 노는날..
        elif LPDoM.dayOfWeek() == 6 and LPDoM.day() % 5 != 0:
            LPDoM = LPDoM.addDays(-1)
        # 휴진일/공휴일이라면 하루 앞으로..
        elif LPDoM in not_open_dates:
            LPDoM = LPDoM.addDays(-1)
        # 위 전제 조건이 모두 아니라면, 청구일 당첨~ while loop 탈출~
        else:
            break
    
    return LPDoM


# LPDoM은 eGhisAssistant가 실행될때 마다 이번달의 LPDoM을 계산하고, 입력.
# 기입력된 LPDoM이 있는경우, 삭제하고 새로 입력. (새로운 일정이 수시로 생길 수 있으니까~)
# 마찬가지로 이달에 새로운 일정이 추가될때 마다 확인하자!
def update_LPDoM(self):
    LPDoM = find_LPDoM(self)
    new_LPDoM = (LPDoM.toString("yyyy.MM.dd"), LPDoM.toString("yyyy.MM.dd"), 0, "청구일")
    this_year = self.infos.date_today.toString("yyyy")
    this_month = self.infos.date_today.toString("MM")
    this_month_last_day = self.infos.date_today.daysInMonth()
    # Load DB
    con = sqlite3.connect("./database/eAcalrem.db")
    cur = con.cursor()
    # Find correct event from DB
    existing_lpdom = cur.execute(f"""
                                 SELECT * FROM Calendar
                                 WHERE
                                 Event_Title = '청구일' AND
                                 (Start_Date BETWEEN '{this_year}.{this_month}.01' AND '{this_year}.{this_month}.{this_month_last_day}')
                                 """).fetchone()
    # 입력된 청구일이 없으면 단순히 입력해주고
    if not existing_lpdom:
        cur.execute(f"""
                    INSERT INTO Calendar
                    Values(?, ?, ?, ?);
                    """, new_LPDoM)
    # 기입력 청구일과 정보가 동일하면, 냅두면 되고
    elif new_LPDoM == existing_lpdom:
        return
    # 기입력 청구일과 새로 계산된 청구일의 정보가 다르다면, 기존꺼는 지우고, 새로 입력하자.
    else:
        cur.execute(f"""
                    DELETE FROM Calendar
                    WHERE
                    (Start_Date BETWEEN '{this_year}.{this_month}.01' AND '{this_year}.{this_month}.{this_month_last_day}')
                    AND Event_Title = '청구일'
                    """)
        cur.execute(f"""
                    INSERT INTO Calendar
                    Values(?, ?, ?, ?);
                    """, new_LPDoM)
    # Close Connection
    con.commit()
    con.close()
    # Calendar_Update마다 실행되기때문에 따로 해줄필요는 없음. 