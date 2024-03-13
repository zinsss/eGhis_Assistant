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
                    SELECT Start_Date, End_Date, Not_OPEN
                    FROM Calendar
                    WHERE
                    Start_Date BETWEEN '{first_day_of_month}' AND '{last_day_of_month}'
                    OR
                    End_Date BETWEEN '{first_day_of_month}' AND '{last_day_of_month}'
                    """).fetchall()
    )]
    not_open_events = []
    open_events = []
    for item in events_for_month:
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
    return not_open_events, open_events


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
    # get DB data
    not_open_events, open_events = connect_DB_and_load(self)
    if open_events:
        print(open_events)
        for event in open_events:
            e_day = QDate.fromString(event, "yyyy.MM.dd")
            self.calendar_wdg.setDateTextFormat(e_day, EVENT)
    if not_open_events:
        print(not_open_events)
        for event in not_open_events:
            h_day = QDate.fromString(event, "yyyy.MM.dd")
            self.calendar_wdg.setDateTextFormat(h_day, HOLIDAYS)
            
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
            item.setFlags(
                Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled
            )
            # Set Color of sublist item according to status
            item.setForeground(QtGui.QBrush(QtGui.QColor(225, 90, 100)))
            # Add to QListWidget
            self.calendar_day_info_lwg.addItem(item)
    for event in events_of_day:
        if not event[1]:
            self.calendar_day_info_lwg.addItem(event[0])
            
            
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
    self.calendar_event_date_dte.setDate(sel_date)
    self.calendar_multi_day_cbx.setChecked(False)
    self.calendar_select_end_date_btn.setEnabled(False)
    self.calendar_select_end_date_btn.setChecked(False)    
    self.calendar_start_date_lbl.setText(sel_date.toString("yyyy.MM.dd(ddd)"))
    self.calendar_end_date_lbl.setText("")
    self.calendar_stack.setCurrentIndex(1)
    self.infos.opened_event_title = ""
    
    
def event_double_clicked(self):
    event_title = self.calendar_day_info_lwg.currentItem().text()
    target_date = self.calendar_wdg.selectedDate()
    self.infos.opened_event_title = event_title
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
    print(self.infos.opened_event_title)
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


## Add a Event from OPT
def write_btn_clicked(self):
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
    # Event title은 rstrip은 해서 가져오자.
    event_title = self.calendar_opt_event_led.text().rstrip()
    
    event_to_write = [start_date, end_date, not_open, event_title]
    # Load DB
    con = sqlite3.connect("./database/eAcalrem.db")
    cur = con.cursor()
    # Write to DB
    cur.execute(f"INSERT INTO Calendar VALUES (?, ?, ?, ?);", event_to_write)
    # Commit and Close Connection
    con.commit()
    con.close()
    # Reset and Go BACK
    options_btn_clicked(self)
    calendar_update(self)
    self.calendar_stack.setCurrentIndex(0)
    

        
# ## Calendar navigation.
# def go_to(self):
#     target_ym = eApopup.get_text(
#         text = "년.월을 입력하세요.\neg. 202401"
#     )
#     if not target_ym: return
#     if not target_ym.isdigit():
#         eApopup.warning(text = "잘못된 입력입니다.")
#         return
#     if not QDate.fromString(target_ym, "yyyyMM").isValid():
#         eApopup.warning(text = "잘못된 입력입니다.")
#         return
    
#     self.calendar_wdg.setCurrentPage(int(target_ym[:4]), int(target_ym[4:]))


# ## Only on date selection(activated from calendar widget), get that date's events if exist.
# def get_event_selected_date(self):
#     # First clear the day info widget
#     self.calendar_events_lwg.clear()
#     # Get selected date
#     sel_date = self.calendar_wdg.selectedDate()
#     self.calendar_events_lwg.addItem(f'### {sel_date.toString("yyyy.MM.dd ddd")}')
#     # Load and Fetch from DB.
#     con = sqlite3.connect("./database/eAcalrem.db")
#     cur = con.cursor()
#     targetDayEvents = cur.execute(f'SELECT * FROM Calendar WHERE Year={sel_date.year()} AND Month={sel_date.month()} AND Day = {sel_date.day()}').fetchall()
#     # If no event in target date; DO NOTHING
#     if not targetDayEvents: return
#     # If there is, add event's 'Detail' column content to the list;
#     # But if multiple events for specific day, I want Holiday on top.
#     # Maybe easier way exists but separate for loop for now.
#     for event in targetDayEvents:
#         if event[3]:
#             self.calendar_events_lwg.addItem(f'* {event[7]}')
#     for event in targetDayEvents:
#         if not event[3]:
#             self.calendar_events_lwg.addItem(f'- {event[7]}')
#     # After adding all events, if any item has '*' as prefix, style them with given font color
#     for i in range(self.calendar_events_lwg.count()):
#         if "*" in self.calendar_events_lwg.item(i).text():
#             self.calendar_events_lwg.item(i).setForeground(QtGui.QBrush(QtGui.QColor(195, 95, 100)))





# ## Calendar Events
# ######## Working #########

# def get_event_from_DB(self, from_listwdg:bool=False):
#     if not from_listwdg:
#         selectedDate = self.infos.opened_event[0]
#         selectedEvent = self.infos.opened_event[1][2:]
#     else:
#         selectedDate = self.calendar_wdg.selectedDate()
#         selectedEvent = self.calendar_events_lwg.currentItem().text()[2:]
        
#     target_eventz = []
#     # DB 연결
#     con = sqlite3.connect("./database/eAcalrem.db")
#     cur = con.cursor()
#     # 해당 event 불러오기
#     target_event = cur.execute(f'''SELECT * FROM Calendar WHERE
#                                Year = "{selectedDate.toString('yyyy')}" AND
#                                Month = "{selectedDate.toString('MM')}" AND
#                                Day = "{selectedDate.toString('dd')}" AND
#                                Event_Title = "{selectedEvent}"
#                                ''').fetchone()
#     if not target_event[4]:
#         target_eventz.append(list(target_event))
#     else:
#         start_date = QDate.fromString(str(target_event[5]), "yyyyMMdd")
#         end_date = QDate.fromString(str(target_event[6]), "yyyyMMdd")
#         for i in range(start_date.daysTo(end_date)+1):
#             date = start_date.addDays(i)
#             print(date)
#             targetEvent = cur.execute(f'''SELECT * FROM Calendar WHERE
#                                       Year = "{date.toString('yyyy')}" AND
#                                       Month = "{date.toString('MM')}" AND
#                                       Day = "{date.toString('dd')}" AND
#                                       Event_Title = "{selectedEvent}"
#                                       ''').fetchone()
#             target_eventz.append(list(targetEvent))

#     # DB 저장 및 연결해제
#     con.commit()
#     con.close()

#     return target_eventz


# def open_in_window(self):
#     if self.calendar_events_lwg.currentItem().text().startswith("###"): return
#     target_eventz = get_event_from_DB(self, from_listwdg = True)
#     if len(target_eventz) > 1:
#         eApopup.notify(text = "이 일정은 Multi Day 일정입니다.\n모든 날짜에 동일 적용됩니다.")
    
#     self.call_calrem('cal')
#     self.calrem_adit.event_adit_delete_btn.setEnabled(True)
    
#     target = target_eventz[0]
    
#     target_date = QDate(target[0], target[1], target[2])
#     self.calrem_adit.adit_cal_wdg.setSelectedDate(target_date)
#     if target[4] != None and target[4] != "" and target[4] != 0:
#         start_date = QDate.fromString(str(target[5]), "yyyyMMdd")
#         end_date = QDate.fromString(str(target[6]), "yyyyMMdd")
#         self.calrem_adit.event_adit_end_date_cbx.setChecked(True)
#         self.calrem_adit.event_adit_end_date_lbl.setText(end_date.toString("yyyy.MM.dd ddd"))
#         for i in range(start_date.daysTo(end_date)+1):
#             self.calrem_adit.adit_cal_wdg.setDateTextFormat(start_date.addDays(i), SELECTED_DAY)

#     if target[3]:
#         self.calrem_adit.event_adit_day_off_cbx.setChecked(True)
    
#     self.calrem_adit.event_adit_event_led.setText(target[7])
#     self.calrem_adit.event_adit_event_notes_ted.setText(target[8])
    
#     self.open_event_or_reminder('event')


# def add_event(new_eventz:list):
#     con = sqlite3.connect("./database/eAcalrem.db")
#     cur = con.cursor()
#     for new_event in new_eventz:
#         cur.execute(f"INSERT INTO Calendar VALUES {str(tuple(new_event))}")
#     con.commit()
#     con.close()
    

# def delete_event(target_eventz:list):
#     print("delete_event func")
#     print(target_eventz)
#     con = sqlite3.connect("./database/eAcalrem.db")
#     cur = con.cursor()
#     for target_event in target_eventz:
#         print(target_event)
#         cur.execute(f'''DELETE FROM Calendar WHERE
#                     Year = "{target_event[0]}" AND
#                     Month = "{target_event[1]}" AND
#                     Day = "{target_event[2]}" AND
#                     Event_Title = "{target_event[7]}"
#                     ''')
#         print(f'''DELETE FROM Calendar WHERE
#                     Year = "{target_event[0]}" AND
#                     Month = "{target_event[1]}" AND
#                     Day = "{target_event[2]}" AND
#                     Event_Title = "{target_event[7]}"
#                     ''')
#     con.commit()
#     con.close()


# ##########################
# def add_new(self):
#     self.calendar_events_lwg.clearSelection()
#     self.calendar_adit.CalendarAdit.setText("Add NEW Event")
#     self.calendar_adit.reset_it()
#     self.calendar_adit.show()
    
# def edit_current(self):
#     targetDate = self.calendar_wdg.selectedDate()
#     targetEventDetail = self.calendar_events_lwg.currentItem().text()
#     if "*" in targetEventDetail:
#         targetEventDetail = targetEventDetail.replace("*", "")    
    
#     self.calendar_adit.CalendarAdit.setText("Edit Event")
#     self.calendar_adit.caladit_wdg.setSelectedDate(targetDate)
#     self.calendar_adit.caladit_event_detail.setText(targetEventDetail)
#     self.calendar_adit.show()
    

# #= Finding LPDOM
# #- 청구일의 전제 조건. 1) 일요일 아니고, 2) 토요일은 기본적으로 아니되, 장날이 아닌 토요일은 제외. 3) 휴진일/공휴일이 아니어야지..
# def find_LPDOM(self, holidays:list = None, year_month:list = None):
#     holiday_objects = []
#     if holidays != None:
#         for holiday in holidays:
#             holiday_objects.append(QDate(*holiday[:3]))
    
#     if year_month == None:
#         targetYear = self.calendar_wdg.yearShown()
#         targetMonth = self.calendar_wdg.monthShown()
#     else: 
#         targetYear = year_month[0]
#         targetMonth = year_month[1]
    
#     daysInTargetMonth = QDate(targetYear, targetMonth, 1).daysInMonth()
#     lastDayOfMonth = QDate(targetYear, targetMonth, daysInTargetMonth)

#     while True:
#         # 이번달 마지막일이 일요일이면 하루 앞으로..
#         if lastDayOfMonth.dayOfWeek() == 7:
#             lastDayOfMonth = lastDayOfMonth.addDays(-1)
#         # 토요일이면, 장날은 아닌지 확인하고, 아니면 하루 앞으로..
#         elif lastDayOfMonth.dayOfWeek() == 6 and lastDayOfMonth.day() % 5 != 0:
#             lastDayOfMonth = lastDayOfMonth.addDays(-1)
#         # 휴진일/공휴일이라면 하루 앞으로..
#         elif lastDayOfMonth in holiday_objects:
#             lastDayOfMonth = lastDayOfMonth.addDays(-1)
#         else:
#             break
    
#     return lastDayOfMonth

# #- Get LPDOM and Set ALRM_LBL
# def claimAlarm(self):
#     targetYear = self.infos.date_today.year()
#     targetMonth = self.infos.date_today.month()
#     calendar_events = connect_DB_and_load(self, year = targetYear, month = targetMonth)
#     if calendar_events == None:
#         holidays = []
#         schedules = []
#     else:
#         holidays = calendar_events[0]
#         schedules = calendar_events[1]
    
#     # lpdom = Last Practice Day of Month
#     lpdom = find_LPDOM(self, holidays, year_month = [targetYear, targetMonth])
#     if self.infos.date_today == lpdom:
#         self.claim_alarm_lbl.setStyleSheet(ALRM_ON_STYLE)
#         self.infos.lpdom = True
#     else:
#         self.claim_alarm_lbl.setStyleSheet(ALRM_OFF_STYLE)
#         self.infos.lpdom = False



# ####################  Calender Yearly List View  ####################

# def prev_next_year_clicked(self, btn_name:str):
#     btn_names = ['prev', 'next']
#     if btn_name not in btn_names: return
    
#     if not self.popup.events_year_led.text().isdigit():
#         eApopup.warning(text = "년도를 정확히 입력해주세요.")
#         return
    
#     currentYear = int(self.popup.events_year_led.text())
    
#     if btn_name == 'prev':
#         currentYear -= 1
#     else: 
#         currentYear += 1
        
#     self.popup.events_year_led.setText(str(currentYear))
#     calendar_yearly_list_view(self)

# def calendar_yearly_list_view(self):
#     target = self.popup.events_year_led.text()
#     if not target.isdigit(): return
#     else: target_year = int(target)
    
#     # Load DB
#     con = sqlite3.connect("./database/eAcalrem.db")
#     cur = con.cursor()
#     # Get DB Data, Yearly
#     target_events = cur.execute(f'SELECT * FROM Calendar WHERE Year = "{target_year}" ORDER BY "Month" ASC, "Day" ASC').fetchall()
#     # Close DB connection
#     con.close()
    
#     target_events_gui = []
#     for target_event in target_events:
#         target_date = QDate(target_event[0], target_event[1], target_event[2])
#         target_event_gui = f'{target_date.toString("yyyy.MM.dd (ddd)")}'
#         if target_event[4] == 1:
#             start_date = QDate.fromString(str(target_event[5]), "yyyyMMdd")
#             end_date = QDate.fromString(str(target_event[6]), "yyyyMMdd")
#             if target_date == start_date:
#                 target_event_gui = f'{target_event_gui} ~ {end_date.toString("yyyy.MM.dd (ddd)")} - '
#             else: continue
#         else: target_event_gui = f'{target_event_gui} - '
#         target_event_gui = target_event_gui + target_event[7]
#         if target_event[3] == 1:
#             target_event_gui = target_event_gui + " *"
#         target_events_gui.append(target_event_gui)
    
#     self.popup.events_lwg.clear()
#     self.popup.events_lwg.addItems(target_events_gui)
    
#     for i in range(self.popup.events_lwg.count()):
#         if self.popup.events_lwg.item(i).text().endswith("*"):
#             self.popup.events_lwg.item(i).setForeground(QtGui.QBrush(QtGui.QColor(195, 95, 100)))
    
# #########################################################
