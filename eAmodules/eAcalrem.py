import sqlite3

from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt, QDate

import main
from eAmodules import eApopup, eAcalendar, eAreminders


### CalRemAdit, Events and Calendar ###

#: Default styling of calendar widget.
def calrem_calendar_styling(self):
    # First reset all dates in default Styles.
    self.adit_cal_wdg.setDateTextFormat(QDate(), QtGui.QTextCharFormat())
    # Following lines define sytles (font color) of days, weekends, etc.
    self.adit_cal_wdg.setWeekdayTextFormat(Qt.Monday, eAcalendar.WEEKDAYS)
    self.adit_cal_wdg.setWeekdayTextFormat(Qt.Tuesday, eAcalendar.WEEKDAYS)
    self.adit_cal_wdg.setWeekdayTextFormat(Qt.Wednesday, eAcalendar.WEEKDAYS)
    self.adit_cal_wdg.setWeekdayTextFormat(Qt.Thursday, eAcalendar.WEEKDAYS)
    self.adit_cal_wdg.setWeekdayTextFormat(Qt.Friday, eAcalendar.WEEKDAYS)
    self.adit_cal_wdg.setWeekdayTextFormat(Qt.Saturday, eAcalendar.SATURDAYS)
    self.adit_cal_wdg.setWeekdayTextFormat(Qt.Sunday, eAcalendar.SUNDAYS)
    self.adit_cal_wdg.setDateTextFormat(self.parent.infos.date_today, eAcalendar.TODAY)
    
def calendar_page_change(self):
    currentYear = self.adit_cal_wdg.yearShown()
    currentMonth = self.adit_cal_wdg.monthShown()
    
    self.adit_yearmonth_btn.setText(f'{str(currentYear)}.{str(currentMonth).zfill(2)}')


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
    
    self.adit_cal_wdg.setCurrentPage(int(target_ym[:4]), int(target_ym[4:]))
    
#: When selecting date from calendar
# TODO end_date 선택된 후, 즉 시작일부터 종료일까지 style 적용되고, calendar widget의 selectedDate는 end_date인
# 상황에서, end_date가 아닌 다른 날짜를 클릭하면, selectionChanged signal 발동, adit_cal_date_selection이 실행.
# 하지만 다시 선택하되 end_date가 시작일로 하고 싶은경우 end_date를 눌러도 selectionChange가 발동되지 않음.
# 큰건 아니지만... 방법 없을까?
def adit_cal_date_selection(self):
    # Always set to default styling.
    # Needed in case multi-day was selected prior current selection because multi day selection styles.
    calrem_calendar_styling(self)
    # end_date_label will be written from code below if select button was checked. so set to empty here.
    self.event_adit_end_date_lbl.setText("")
    # prior selected date saved. if current selection was end_date select, prior selection as start date.
    prior_selection = QDate.fromString(self.event_adit_start_date_lbl.text(), "yyyy.MM.dd ddd")
    # On date selection, start date label for both event and reminders are set automatically
    # In case of end date select button selection, start date of event page will again be written
    # with prior_selection date.
    selected_date_text = self.adit_cal_wdg.selectedDate().toString("yyyy.MM.dd ddd")
    self.rem_adit_due_date_lbl.setText(selected_date_text)
    self.event_adit_start_date_lbl.setText(selected_date_text)
    # In case end_date select button is checked,
    if self.event_adit_select_btn.isChecked():
        if self.adit_cal_wdg.selectedDate().daysTo(prior_selection) <= 0:
            # prior selection to current selection will be styled as selection.
            for i in range(prior_selection.daysTo(self.adit_cal_wdg.selectedDate())+1):
                self.adit_cal_wdg.setDateTextFormat(prior_selection.addDays(i), eAcalendar.SELECTED_DAY)
            self.event_adit_start_date_lbl.setText(prior_selection.toString("yyyy.MM.dd ddd"))
            self.event_adit_end_date_lbl.setText(selected_date_text)
        else: pass
        # only one click allowed for end_date select button
        self.event_adit_select_btn.setChecked(False)
        
        
#: End_date checkbox를 누를때 발동되는 일련의 작업들.
def end_date_check_toggle(self):
    current_state = self.event_adit_end_date_cbx.isChecked()
    # 체크상태에 맞춰 select버튼도 활성/비활성화
    self.event_adit_select_btn.setEnabled(current_state)
    # 체크 해제상태인 경우 end_date_lbl는 빈칸으로, selectedDate는 start date로 이동.
    if not current_state:
        self.event_adit_end_date_lbl.setText("")
        self.adit_cal_wdg.setSelectedDate(QDate.fromString(self.event_adit_start_date_lbl.text(), "yyyy.MM.dd ddd"))
            

#: 현재 입력되어있는 window내의 정보를 DB table에 맞춰 리스트로 작성하기.
def event_current_adit(self):
    # 입력/수정 일정이 multiple day인 경우, 각 일마다 db에 저장되기 때문에..
    # 이에 대비하여 각 일정을 리스트에 저장, 나중에 한번에 입력하기 쉬움.
    new_eventz = []
    # 일단 adit창의 입력된 정보들을 저장해놓고..    
    new_start_date = QDate.fromString(self.event_adit_start_date_lbl.text(), 'yyyy.MM.dd ddd')
    new_day_off = int(self.event_adit_day_off_cbx.isChecked())
    new_multiple_days = int(self.event_adit_end_date_cbx.isChecked())
    new_end_date = QDate.fromString(self.event_adit_end_date_lbl.text(), 'yyyy.MM.dd ddd')
    new_event_detail = self.event_adit_event_led.text()
    new_event_notes = self.event_adit_event_notes_ted.toPlainText()
    
    if not new_multiple_days:
        to_DB_List = [0, 0, 0, 0, 0, 0, 0, "", ""]
        to_DB_List[0] = new_start_date.year()
        to_DB_List[1] = new_start_date.month()
        to_DB_List[2] = new_start_date.day()
        to_DB_List[3] = new_day_off
        to_DB_List[7] = new_event_detail
        to_DB_List[8] = new_event_notes
        new_eventz.append(to_DB_List)
    else:
        for i in range(0, new_start_date.daysTo(new_end_date)+1):
            to_DB_List = [0, 0, 0, 0, 0, 0, 0, "", ""]
            dates = new_start_date.addDays(i)
            to_DB_List[0] = dates.year()
            to_DB_List[1] = dates.month()
            to_DB_List[2] = dates.day()
            to_DB_List[3] = new_day_off
            to_DB_List[4] = new_multiple_days
            to_DB_List[5] = new_start_date.toString("yyyyMMdd")
            to_DB_List[6] = new_end_date.toString("yyyyMMdd")
            to_DB_List[7] = new_event_detail
            to_DB_List[8] = new_event_notes
            new_eventz.append(to_DB_List)
            
    return new_eventz
    

#: 저장버튼 누를때, 상황에 맞게 DB로의 입력 또는 기입력 일정 삭제 후 DB 입력.    
def event_confirm_clicked(self):
    # 일단 편집모드인 경우..
    if self.event_adit_delete_btn.isEnabled():
        # DB저장된 일정을 불러와서
        target_eventz = eAcalendar.get_event_from_DB(self.parent)
        # 1개 이상이면.. 즉 multi day 일정이면,
        if len(target_eventz) > 1:
            # 다 지울꺼라고 경고는 해주고.
            ok = eApopup.warning(text = "편집한 일정은 Multi Day 일정입니다.\n해달 일정의 모든 날짜가 삭제됩니다.")
            if not ok: return
        # 다 지워버려.
        eAcalendar.delete_event(target_eventz)
    
    new_eventz = event_current_adit(self)
    eAcalendar.add_event(new_eventz)
    
    eAcalendar.calendar_update(self.parent)
    eAcalendar.get_event_selected_date(self.parent)
    
    self.reset_it()
    self.hide()
    

def event_delete_clicked(self):
    ok = eApopup.warning(
        text = "해당 일정을 삭제하겠습니까?\n\n- Multi-day 일정은 모든 날짜 동시 삭제\n- 삭제 시 복구 불가.",
        yes_no = True
    )
    if not ok: return
    
    target_eventz = eAcalendar.get_event_from_DB(self.parent)
    eAcalendar.delete_event(target_eventz)
    
    eAcalendar.calendar_update(self.parent)
    eAcalendar.get_event_selected_date(self.parent)
    
    self.reset_it()
    self.hide()
    

###### CalRemAdit, reminders #####
#: Status 변경 시 마다 label미리보기도 같이 변경.
def rem_status_cmb_changed(self):
    current_status_str = self.rem_adit_status_cmb.currentText()[:3]
    self.rem_adit_status_lbl.setText(current_status_str)

#: due_date 체크박스 설정할때마다 label stylesheet 적용하기.
def rem_due_date_clicked(self):
    CHECKED_STYLE = "color: rgb(211, 222, 233);"
    UNCHECKED_STYLE = "color: rgb(88, 99, 122);"
    if self.rem_adit_due_date_cbx.isChecked():
        self.rem_adit_due_date_lbl.setStyleSheet(CHECKED_STYLE)
    else: self.rem_adit_due_date_lbl.setStyleSheet(UNCHECKED_STYLE)

#: sublist 체크박스 설정때마다 sublist입력 lineedit을 toggle.
# TODO sublist 기 입력상태에서 체크바스 해제 시 기입력 list 삭제??
def sublist_toggle(self):
    if self.rem_adit_sublist_cbx.isChecked():
        self.rem_adit_sublist_led.setEnabled(True)
    else:
        if self.rem_adit_sublist_lwg.count() != 0:
            yes = eApopup.warning(text = "모든 입력된 SubList가 삭제됩니다.\n확실합니까?", yes_no = True)
            if yes:
                self.rem_adit_sublist_lwg.clear()
            else: return
        self.rem_adit_sublist_led.setEnabled(False)
    
#: LineEdit 입력후 엔터 칠때마다,
# 각 내용을 listwidget에 입력하되, 각 리스트 아이템들은;
# checkable, editable, selectable and unchecked의 flag를 설정함. 
# selectable이 필요한 이유는, selected click시 edit가 가능하기 때문.
def sublist_led_entered(self):
    entered_text = self.rem_adit_sublist_led.text()
    item = QtWidgets.QListWidgetItem(entered_text)
            
    item.setFlags(
        Qt.ItemIsEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEditable|Qt.ItemIsSelectable
        )
    item.setCheckState(Qt.Unchecked)
            
    self.rem_adit_sublist_lwg.addItem(item)
    self.rem_adit_sublist_led.clear()
    

#: confirm click 시 진행되는 확인절차 및 실행절차.    
def rem_confirm_clicked(self):
    # 진행 방지 조건 1. 내용은 입력해야지..
    if self.rem_adit_reminder_led.text().rstrip() == "": 
        return
    # 진행 방지 조건 2. 캘린더에도 입력을 하려면, 날짜를 선택해야지..
    if self.rem_adit_also_event_cbx.isChecked():
        if not self.rem_adit_due_date_cbx.isChecked():
            eApopup.warning("날짜가 선택되어 있지 않습니다.\n먼저 'Due Date'를 눌러 체크 한 후,\n날짜를 지정해주세요.")
            return
        else:
            # 캘린더 입력으로 보내기
            pass    
    
    # sublist 체크하고 입력 리스트가 없다면 그냥 체크해제로 변경.
    if self.rem_adit_sublist_cbx.isChecked() and self.rem_adit_sublist_lwg.count() == 0:
        eApopup.warning(text = "Sublist가 입력되지 않았습니다.\nSublist 체크박스가 자동으로 해제됩니다.")
        self.rem_adit_sublist_cbx.setChecked(False)
    
    # 위 방지 조건 1,2가 괜찮아 진행해서.. 현재 윈도우에서 입력된 reminder정보를 받아왔어도..
    reminder, as_event = current_rem_adit(self)
    
    # delete 버튼이 활성화 되어있다면, 편집 저장.
    if self.rem_adit_delete_btn.isEnabled():
        target_reminder = eAreminders.get_single_reminder_info(self.parent, self.parent.infos.opened_reminder)
        if reminder[1] != target_reminder[1]:
            ok = eAreminders.verify_reminder(self, reminder[1])
            if not ok:
                eApopup.notify(text = "방금 편집한 리마인더와\n같은 제목의 항목이 이미 존재합니다.")
                return
        eAreminders.edit_reminder(self.parent, reminder, target_reminder)
    # delete 버튼이 비활성화 되어있다면, 새로 추가하기.
    else:
        # TODO reminder also as calendar event
        if as_event != False:
            print("일단 보류")
        ok = eAreminders.verify_reminder(self, reminder[1])
        if not ok:
            eApopup.notify(text = "추가할 제목의 리마인더가\n이미 DB에 입력되어있습니다.")
            return
        eAreminders.add_reminder(self.parent, reminder)
    # Reset window before closing.
    self.reset_it()
    self.close()

#: Reminder 편집 또는 추가 관련 현재창.
def current_rem_adit(self):    
    # DB Table과 동일한 리스트 형식으로의 작성을 위해.
    rem_status = self.rem_adit_status_lbl.text()
    rem_detail = self.rem_adit_reminder_led.text()
    rem_sublist_bool = 0
    rem_sublist_items = []
    
    if self.rem_adit_due_date_cbx.isChecked():
        # [-4]는 lbl은 yyyy.MM.dd ddd로 표시되어있어서 ' ddd'제거.
        rem_due_date = self.rem_adit_due_date_lbl.text()[:-4]
    else: rem_due_date = ""
    
    # 완료/취소인 경우에는 (@yyyy.MM.dd) 리스트위젯에 표시 및 DB입력을 위해 오늘 날짜 값도 저장해놓고.
    if rem_status in ['[x]', '[-]']:
        rem_done_date = self.parent.infos.date_today.toString("yyyy.MM.dd")
    else: rem_done_date = ""
    
    # List in Reminder 체크박스가 설정되어있으면..
    if self.rem_adit_sublist_cbx.isChecked():
        # DB의 List는 boolean의 int인 1로 설정해주고, 아니면 기본값 0 위에서 이미 설정됨.
        rem_sublist_bool = 1
        # sublist위젯이 기 입력된 항목들 중에서, 체크된 항목은 앞에 *를 붙여서 저장.
        for i in range(self.rem_adit_sublist_lwg.count()):
            sublist_item = self.rem_adit_sublist_lwg.item(i)
            if sublist_item.checkState() == Qt.Unchecked:
                rem_sublist_items.append(sublist_item.text())
            else: rem_sublist_items.append(f'*{sublist_item.text()}')
    # 각 리스트 항목들을 \n으로 구분한 하나의 string으로 저장하자.   
    rem_sublist = "\n".join(rem_sublist_items)

    # DB Table과 같은 형식/순서로 reminder 정보를 저장.
    new_reminder = [rem_status, rem_detail, rem_sublist_bool, rem_sublist, rem_due_date, rem_done_date]
    
    # TODO also as event인 경우 일단 같이 필요할만한 정보를 return.
    # 편집시 이미 입력되어있다면? 중복 입력 방지방법 고려.
    # 편집시 내용(reminder_detail)이 변경됬다면? 중복 입력 방지방법 고려.
    if self.rem_adit_also_event_cbx.isChecked():
        as_event = [rem_due_date, rem_detail]
    else: as_event = False
    
    return new_reminder, as_event


VIEWs = ["cal", "rem"]
TOs = ["prev", "next"]

def showCalRem(self, view:str):
    if view not in VIEWs: return
    
    self.calrem.show()
    # 이유를 모르겠다. setCurrentIndex(1)부터 열면, 0의 tab이 안보임.
    # 일단은 0 갔다가 바로 필요시 1로 옮기자.
    self.calrem.tabWidget.setCurrentIndex(0)
    self.calrem.tabWidget.setCurrentIndex(VIEWs.index(view))
    get_yearly_data(self.calrem, view)

def navigate_year(self, view:str, to:str):
    if view not in VIEWs: return
    if to not in TOs: return
    
    target = getattr(self, f'{view}_year_led')
    if not target.text().isdigit():
        eApopup.warning(text = "년도를 정확히 입력해주세요.")
        return
    if len(target.text()) != 4:
        eApopup.warning(text = "년도를 정확히 입력해주세요.")
        return
    if not target.text().startswith("20"):
        eApopup.warning(text = "년도를 정확히 입력해주세요.")
        return
    
    currentYear = int(target.text())
    if to == "prev": target.setText(str(currentYear - 1))
    else: target.setText(str(currentYear + 1))
    
    get_yearly_data(self, view = view)
    
    
def get_yearly_data(self, view:str):
    if view not in VIEWs: return
    
    if view == "cal":
        currentText = self.cal_year_led.text()
    else:
        currentText = self.rem_year_led.text()
    
    if not currentText.isdigit():
        eApopup.warning(text = "년도를 정확히 입력해주세요.")
        return
    if len(currentText) != 4:
        eApopup.warning(text = "년도를 정확히 입력해주세요.")
        return
    if not currentText.startswith("20"):
        eApopup.warning(text = "년도를 정확히 입력해주세요.")
        return

    currentYear = int(currentText)
    
    if view == "cal": get_data_cal(self, currentYear)
    else: get_data_rem(self, currentYear)
    
    
def get_data_cal(self, year:int):
    self.cal_events_lwg.clear()
    # Load DB
    con = sqlite3.connect("./database/eAcalendar.db")
    cur = con.cursor()
    # Fetch Yearly Events
    yearly_events = cur.execute(f'SELECT * FROM Calendar WHERE Year={year} ORDER BY Year, Month, Day').fetchall()
    # Close DB connection
    con.close()
    
    if not yearly_events: return
    
    events = []
    for event in yearly_events:
        if event[3]:
            holiday = '* '
        else:holiday = "  "
        
        each_event = f'{event[0]}.{event[1]:02d}.{event[2]:02d}{holiday}{event[7]}'
        events.append(each_event)
    
    self.cal_events_lwg.addItems(events)
    

def get_data_rem(self, year:int):
    self.rem_archive_lwg.clear()
    # Load DB
    con = sqlite3.connect("./database/eAreminders.db")
    cur = con.cursor()
    # Fetch Yearly Events
    rem_archives = cur.execute(f'SELECT * FROM Archive WHERE Done_Cancel_Date LIKE "{year}%" ORDER BY Done_Cancel_Date').fetchall()
    # Close DB connection
    con.close()
    
    if not rem_archives: return
    
    archives = []
    for archive in rem_archives:
        if archive[3] != "":
            due_date = f'(~{archive[3]})'
        else: due_date = ""
        
        each_archive = f'@{archive[4]} {archive[1]} {archive[2]} {due_date}'
        archives.append(each_archive)
    
    self.rem_archive_lwg.addItems(archives)
