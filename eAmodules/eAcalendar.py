import sqlite3

from PySide6 import QtGui
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
HOLIDAYS.setForeground(QtGui.QBrush(QtGui.QColor(191, 97, 106)))
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
        Year INTEGER,
        Month INTEGER,
        Day INTEGER,
        Not_OPEN INTEGER,
        Multi_Day INTEGER,
        START_DATE INTEGER,
        END_DATE INTEGER,
        Event_Title TEXT,
        Event_Notes TEXT)
        '''
    )
    # If specified on function call, can get datas of that year/month.
    # Currently not implemented in app for any functionality.
    # Just defaults for now.
    if not year: year = self.calendar_wdg.yearShown()
    if not month: month = self.calendar_wdg.monthShown()
    # Get all datas in DB.
    month_events = cur.execute(f'SELECT * FROM Calendar WHERE Year={year} AND Month={month}').fetchall()
    # Close DB connection
    con.close()
    # If there are no event in target year/month; Do NOTHING.
    if not month_events: return
    # But if there is some events, categorize them by holiday/schedule using 'NOT_OPEN' column.
    events = []
    holidays = []
    for event in month_events:
        if event[3]: holidays.append(event)
        else: events.append(event)
    # Return results in list
    return [events, holidays]


## Calendar navigation.
def go_to(self):
    target_ym = eApopup.get_text(
        text = "년.월을 입력하세요.\neg. 202401"
    )
    if not target_ym: return
    if not target_ym.isdigit():
        eApopup.warning(text = "잘못된 입력입니다.")
        return
    if not QDate.fromString(target_ym, "yyyyMM").isValid():
        eApopup.warning(text = "잘못된 입력입니다.")
        return
    
    self.calendar_wdg.setCurrentPage(int(target_ym[:4]), int(target_ym[4:]))


## Only on date selection(activated from calendar widget), get that date's events if exist.
def get_event_selected_date(self):
    # First clear the day info widget
    self.calendar_events_lwg.clear()
    # Get selected date
    sel_date = self.calendar_wdg.selectedDate()
    self.calendar_events_lwg.addItem(f'### {sel_date.toString("yyyy.MM.dd ddd")}')
    # Load and Fetch from DB.
    con = sqlite3.connect("./database/eAcalrem.db")
    cur = con.cursor()
    targetDayEvents = cur.execute(f'SELECT * FROM Calendar WHERE Year={sel_date.year()} AND Month={sel_date.month()} AND Day = {sel_date.day()}').fetchall()
    # If no event in target date; DO NOTHING
    if not targetDayEvents: return
    # If there is, add event's 'Detail' column content to the list;
    # But if multiple events for specific day, I want Holiday on top.
    # Maybe easier way exists but separate for loop for now.
    for event in targetDayEvents:
        if event[3]:
            self.calendar_events_lwg.addItem(f'* {event[7]}')
    for event in targetDayEvents:
        if not event[3]:
            self.calendar_events_lwg.addItem(f'- {event[7]}')
    # After adding all events, if any item has '*' as prefix, style them with given font color
    for i in range(self.calendar_events_lwg.count()):
        if "*" in self.calendar_events_lwg.item(i).text():
            self.calendar_events_lwg.item(i).setForeground(QtGui.QBrush(QtGui.QColor(195, 95, 100)))


#= Update Calendar
def calendar_update(self):
    # reset day info listWdg
    self.calendar_events_lwg.clear()
    # Set Date on Year_Month_Button
    cal_year = self.calendar_wdg.yearShown()
    cal_month = self.calendar_wdg.monthShown()
    self.year_month_btn.setText(f'{cal_year}.{str(cal_month).zfill(2)}')
    # get DB data
    cal_data = connect_DB_and_load(self)
    # get all event days and holiday days for calendar day colors
    events_day = []
    holidays_day = []
    if cal_data != None:
        if cal_data[0] != None:
            for event in cal_data[0]: events_day.append(event[2])
        if cal_data[1] != None:
            for holiday in cal_data[1]: holidays_day.append(holiday[2])
    # First reset all dates in default Styles.
    self.calendar_wdg.setDateTextFormat(QDate(), QtGui.QTextCharFormat())
    # Following lines define sytles (font color) of days, weekends, etc.
    self.calendar_wdg.setWeekdayTextFormat(Qt.Monday, WEEKDAYS)
    self.calendar_wdg.setWeekdayTextFormat(Qt.Tuesday, WEEKDAYS)
    self.calendar_wdg.setWeekdayTextFormat(Qt.Wednesday, WEEKDAYS)
    self.calendar_wdg.setWeekdayTextFormat(Qt.Thursday, WEEKDAYS)
    self.calendar_wdg.setWeekdayTextFormat(Qt.Friday, WEEKDAYS)
    self.calendar_wdg.setWeekdayTextFormat(Qt.Saturday, SATURDAYS)
    self.calendar_wdg.setWeekdayTextFormat(Qt.Sunday, SUNDAYS)
    self.calendar_wdg.setDateTextFormat(self.infos.date_today, TODAY)
    
    if events_day != None:
        for event_day in events_day:
            e_day = QDate(cal_year, cal_month, event_day)
            self.calendar_wdg.setDateTextFormat(e_day, EVENT)
    
    if holidays_day != None:
        for holiday_day in holidays_day:
            h_day = QDate(cal_year, cal_month, holiday_day)
            self.calendar_wdg.setDateTextFormat(h_day, HOLIDAYS)


## Calendar Events
######## Working #########

def get_event_from_DB(self, from_listwdg:bool=False):
    if not from_listwdg:
        selectedDate = self.infos.opened_event[0]
        selectedEvent = self.infos.opened_event[1][2:]
    else:
        selectedDate = self.calendar_wdg.selectedDate()
        selectedEvent = self.calendar_events_lwg.currentItem().text()[2:]
        
    target_eventz = []
    # DB 연결
    con = sqlite3.connect("./database/eAcalrem.db")
    cur = con.cursor()
    # 해당 event 불러오기
    target_event = cur.execute(f'''SELECT * FROM Calendar WHERE
                               Year = "{selectedDate.toString('yyyy')}" AND
                               Month = "{selectedDate.toString('MM')}" AND
                               Day = "{selectedDate.toString('dd')}" AND
                               Event_Title = "{selectedEvent}"
                               ''').fetchone()
    if not target_event[4]:
        target_eventz.append(list(target_event))
    else:
        start_date = QDate.fromString(str(target_event[5]), "yyyyMMdd")
        end_date = QDate.fromString(str(target_event[6]), "yyyyMMdd")
        for i in range(start_date.daysTo(end_date)+1):
            date = start_date.addDays(i)
            print(date)
            targetEvent = cur.execute(f'''SELECT * FROM Calendar WHERE
                                      Year = "{date.toString('yyyy')}" AND
                                      Month = "{date.toString('MM')}" AND
                                      Day = "{date.toString('dd')}" AND
                                      Event_Title = "{selectedEvent}"
                                      ''').fetchone()
            target_eventz.append(list(targetEvent))

    # DB 저장 및 연결해제
    con.commit()
    con.close()

    return target_eventz


def open_in_window(self):
    if self.calendar_events_lwg.currentItem().text().startswith("###"): return
    target_eventz = get_event_from_DB(self, from_listwdg = True)
    if len(target_eventz) > 1:
        eApopup.notify(text = "이 일정은 Multi Day 일정입니다.\n모든 날짜에 동일 적용됩니다.")
    
    self.call_calrem('cal')
    self.calrem_adit.event_adit_delete_btn.setEnabled(True)
    
    target = target_eventz[0]
    
    target_date = QDate(target[0], target[1], target[2])
    self.calrem_adit.adit_cal_wdg.setSelectedDate(target_date)
    if target[4] != None and target[4] != "" and target[4] != 0:
        start_date = QDate.fromString(str(target[5]), "yyyyMMdd")
        end_date = QDate.fromString(str(target[6]), "yyyyMMdd")
        self.calrem_adit.event_adit_end_date_cbx.setChecked(True)
        self.calrem_adit.event_adit_end_date_lbl.setText(end_date.toString("yyyy.MM.dd ddd"))
        for i in range(start_date.daysTo(end_date)+1):
            self.calrem_adit.adit_cal_wdg.setDateTextFormat(start_date.addDays(i), SELECTED_DAY)

    if target[3]:
        self.calrem_adit.event_adit_day_off_cbx.setChecked(True)
    
    self.calrem_adit.event_adit_event_led.setText(target[7])
    self.calrem_adit.event_adit_event_notes_ted.setText(target[8])
    
    self.open_event_or_reminder('event')


def add_event(new_eventz:list):
    con = sqlite3.connect("./database/eAcalrem.db")
    cur = con.cursor()
    for new_event in new_eventz:
        cur.execute(f"INSERT INTO Calendar VALUES {str(tuple(new_event))}")
    con.commit()
    con.close()
    

def delete_event(target_eventz:list):
    print("delete_event func")
    print(target_eventz)
    con = sqlite3.connect("./database/eAcalrem.db")
    cur = con.cursor()
    for target_event in target_eventz:
        print(target_event)
        cur.execute(f'''DELETE FROM Calendar WHERE
                    Year = "{target_event[0]}" AND
                    Month = "{target_event[1]}" AND
                    Day = "{target_event[2]}" AND
                    Event_Title = "{target_event[7]}"
                    ''')
        print(f'''DELETE FROM Calendar WHERE
                    Year = "{target_event[0]}" AND
                    Month = "{target_event[1]}" AND
                    Day = "{target_event[2]}" AND
                    Event_Title = "{target_event[7]}"
                    ''')
    con.commit()
    con.close()


##########################
def add_new(self):
    self.calendar_events_lwg.clearSelection()
    self.calendar_adit.CalendarAdit.setText("Add NEW Event")
    self.calendar_adit.reset_it()
    self.calendar_adit.show()
    
def edit_current(self):
    targetDate = self.calendar_wdg.selectedDate()
    targetEventDetail = self.calendar_events_lwg.currentItem().text()
    if "*" in targetEventDetail:
        targetEventDetail = targetEventDetail.replace("*", "")    
    
    self.calendar_adit.CalendarAdit.setText("Edit Event")
    self.calendar_adit.caladit_wdg.setSelectedDate(targetDate)
    self.calendar_adit.caladit_event_detail.setText(targetEventDetail)
    self.calendar_adit.show()
    

#= Finding LPDOM
#- 청구일의 전제 조건. 1) 일요일 아니고, 2) 토요일은 기본적으로 아니되, 장날이 아닌 토요일은 제외. 3) 휴진일/공휴일이 아니어야지..
def find_LPDOM(self, holidays:list = None, year_month:list = None):
    holiday_objects = []
    if holidays != None:
        for holiday in holidays:
            holiday_objects.append(QDate(*holiday[:3]))
    
    if year_month == None:
        targetYear = self.calendar_wdg.yearShown()
        targetMonth = self.calendar_wdg.monthShown()
    else: 
        targetYear = year_month[0]
        targetMonth = year_month[1]
    
    daysInTargetMonth = QDate(targetYear, targetMonth, 1).daysInMonth()
    lastDayOfMonth = QDate(targetYear, targetMonth, daysInTargetMonth)

    while True:
        # 이번달 마지막일이 일요일이면 하루 앞으로..
        if lastDayOfMonth.dayOfWeek() == 7:
            lastDayOfMonth = lastDayOfMonth.addDays(-1)
        # 토요일이면, 장날은 아닌지 확인하고, 아니면 하루 앞으로..
        elif lastDayOfMonth.dayOfWeek() == 6 and lastDayOfMonth.day() % 5 != 0:
            lastDayOfMonth = lastDayOfMonth.addDays(-1)
        # 휴진일/공휴일이라면 하루 앞으로..
        elif lastDayOfMonth in holiday_objects:
            lastDayOfMonth = lastDayOfMonth.addDays(-1)
        else:
            break
    
    return lastDayOfMonth

#- Get LPDOM and Set ALRM_LBL
def claimAlarm(self):
    targetYear = self.infos.date_today.year()
    targetMonth = self.infos.date_today.month()
    calendar_events = connect_DB_and_load(self, year = targetYear, month = targetMonth)
    if calendar_events == None:
        holidays = []
        schedules = []
    else:
        holidays = calendar_events[0]
        schedules = calendar_events[1]
    
    # lpdom = Last Practice Day of Month
    lpdom = find_LPDOM(self, holidays, year_month = [targetYear, targetMonth])
    if self.infos.date_today == lpdom:
        self.claim_alarm_lbl.setStyleSheet(ALRM_ON_STYLE)
        self.infos.lpdom = True
    else:
        self.claim_alarm_lbl.setStyleSheet(ALRM_OFF_STYLE)
        self.infos.lpdom = False



####################  Calender Yearly List View  ####################

def prev_next_year_clicked(self, btn_name:str):
    btn_names = ['prev', 'next']
    if btn_name not in btn_names: return
    
    if not self.popup.events_year_led.text().isdigit():
        eApopup.warning(text = "년도를 정확히 입력해주세요.")
        return
    
    currentYear = int(self.popup.events_year_led.text())
    
    if btn_name == 'prev':
        currentYear -= 1
    else: 
        currentYear += 1
        
    self.popup.events_year_led.setText(str(currentYear))
    calendar_yearly_list_view(self)

def calendar_yearly_list_view(self):
    target = self.popup.events_year_led.text()
    if not target.isdigit(): return
    else: target_year = int(target)
    
    # Load DB
    con = sqlite3.connect("./database/eAcalrem.db")
    cur = con.cursor()
    # Get DB Data, Yearly
    target_events = cur.execute(f'SELECT * FROM Calendar WHERE Year = "{target_year}" ORDER BY "Month" ASC, "Day" ASC').fetchall()
    # Close DB connection
    con.close()
    
    target_events_gui = []
    for target_event in target_events:
        target_date = QDate(target_event[0], target_event[1], target_event[2])
        target_event_gui = f'{target_date.toString("yyyy.MM.dd (ddd)")}'
        if target_event[4] == 1:
            start_date = QDate.fromString(str(target_event[5]), "yyyyMMdd")
            end_date = QDate.fromString(str(target_event[6]), "yyyyMMdd")
            if target_date == start_date:
                target_event_gui = f'{target_event_gui} ~ {end_date.toString("yyyy.MM.dd (ddd)")} - '
            else: continue
        else: target_event_gui = f'{target_event_gui} - '
        target_event_gui = target_event_gui + target_event[7]
        if target_event[3] == 1:
            target_event_gui = target_event_gui + " *"
        target_events_gui.append(target_event_gui)
    
    self.popup.events_lwg.clear()
    self.popup.events_lwg.addItems(target_events_gui)
    
    for i in range(self.popup.events_lwg.count()):
        if self.popup.events_lwg.item(i).text().endswith("*"):
            self.popup.events_lwg.item(i).setForeground(QtGui.QBrush(QtGui.QColor(195, 95, 100)))
    
#########################################################
