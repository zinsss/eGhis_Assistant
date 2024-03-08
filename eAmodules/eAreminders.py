from PySide6 import QtGui, QtWidgets, QtCore
from PySide6.QtCore import QDate
import sqlite3

import main
from eAmodules import eApopup


#: Reminders Highlights Color Codes
reminder_status = {
    "[ ]": [(180, 185, 195), "할일", "⚪"],
    "[!]": [(200, 125, 100), "급함", "🟠"],
    "[*]": [(200, 175, 125), "중요", "🟡"],
    "[/]": [(100, 150, 200), "진행", "🔵"],
    "[?]": [(166, 133, 188), "보류", "🟣"],
    "[x]": [(144, 199, 133), "완료", "🟢"],
    "[-]": [(175, 80, 100), "취소", "🔴"],
    "!!!": [(90, 95, 100), "오류", "⚫"]
}

archiving_target = ["[x]", "[-]"]

#################### DB TO GUI (incl. Processing)

## Connect to DB (middle-man)
def connect_DB():
    # Load DB
    con = sqlite3.connect("./database/eAcalrem.db")
    cur = con.cursor()    
    # Create table if not exists
    con.execute('CREATE TABLE if not exists Active(Status TEXT, Reminder TEXT, Sublist TEXT, Due_Date TEXT, Status_Changed TEXT)')
    con.execute('CREATE TABLE if not exists Archive(Status TEXT, Reminder TEXT, Sublist TEXT, Due_Date TEXT, Status_Changed TEXT)')     
    # Load Current Items
    items = [list(item) for item in cur.execute('SELECT * FROM Active').fetchall()]
    # Close DB connection
    con.commit()
    con.close()

    return items


## Load from DB file (middle-man)
def get_db_data(self):
    reminders = connect_DB()
    reminders_gui = []
    
    for reminder in reminders:
        reminder_gui_list = ["", "", "", "\n    ", "", ""]
        # For easier transition to gui.
        # 0 status_color as it is. Will not be written in Gui but will be used for color and checkbox status
        # 1 reminder text as is
        # 2 if there are sublist for the reminder, "..." will be added at last of reminder text
        # 3 for new line,
        # 4 will be due date. written in next line, with 3 as '\n'
        # 5 status change date after due date
        
        # Due date calculation
        if reminder[3] != None and reminder[3] != "":
            due_date = QDate.fromString(reminder[3], "yyyy.MM.dd")
            if reminder[4] != None and reminder[4] != "":
                info = " "
            else:
                to_due_date = self.infos.date_today.daysTo(due_date)
                if to_due_date == 0:
                    info = ", TODAY !!"
                elif to_due_date > 0:
                    info = f", in {to_due_date}d"
                else:
                    info = f", OVERDUE{to_due_date}d"
            due_date_info = f'::DUE {due_date.toString("yyyy.MM.dd(ddd)")}{info}'
            
        if reminder[4] != None and reminder[4] != "":
            if reminder[0] == "[x]":
                status_change_date = f'::DONE {reminder[4]}'
            elif reminder[0] == "[-]":
                status_change_date = f'::CANCELLED {reminder[4]}'
            else:
                status_change_date = ""
            
        reminder_gui_list[0] = reminder[0]
        reminder_gui_list[1] = f' {reminder[1]} '
        reminder_gui_list[2] = "..." if reminder[2] != "" else ""
        reminder_gui_list[4] = due_date_info if reminder[3] != None and reminder[3] != "" else ""
        reminder_gui_list[5] = status_change_date if reminder[4] != None and reminder[4] != "" else ""
        # 만들어진 리스트를 붙이되, due date나 done/cancell date가 없는 경우 2줄짜리 리스트 아이템이 생기지만,
        # rstrip()로 \n까지 지워버림.
        reminder_gui = "".join(reminder_gui_list).rstrip()
        # 하나의 string으로 된 모든 리마인더들을 하나의 리스트에 담아서..
        reminders_gui.append(reminder_gui)

    return reminders_gui

   
## Write to GUI (middle-man)
# get_db_data에서 return 받은 reminders list를 gui에 상태별 색상으로 write.
def reminders_to_gui(self, reminders:list):
    # archive button, not enabled before processing
    self.reminders_archive_btn.setEnabled(False)    
    # clear the listwidget to prevent duplicates
    self.reminders_lwg.clear()    
    # if there is no active reminder, don't bother running code below.
    if not reminders: return
    
    # Add every reminders to list, set colors by status, turns on archive button if needed.
    for i in range(len(reminders)):
        reminder_item = QtWidgets.QListWidgetItem(reminders[i])
        # if reminder is cancelled, strikeout
        if reminders[i][:3] == "[-]":
            strikeout = reminder_item.font()
            strikeout.setStrikeOut(True)
            reminder_item.setFont(strikeout)
        
        self.reminders_lwg.addItem(reminder_item)            
        
        # set reminders in color by due date (if due today) first, then by status
        self.reminders_lwg.item(i).setForeground(QtGui.QBrush(QtGui.QColor(*reminder_status[reminders[i][:3]][0])))

        # if archiving target is in list, enable archive button
        if reminders[i][:3] in archiving_target: self.reminders_archive_btn.setEnabled(True)

            
## Load and Write Reminders, main
def load_write_reminders(self):
    reminders = get_db_data(self)
    reminders_to_gui(self, reminders)
    

## Get Single Reminder Infos from DB
def get_single_reminder_info(self, reminder_text:str = None):
    if not reminder_text:
        selected = self.reminders_lwg.currentItem()
        reminder_text = selected.text().split('\n')[0][4:].replace("...", "").rstrip()
    
    # DB 연걸.
    con = sqlite3.connect("./database/eAcalrem.db")
    cur = con.cursor()
    # 불러오기.
    reminder_info = list(cur.execute(f'SELECT * FROM Active WHERE Reminder = "{reminder_text}"').fetchone())
    # DB 저장 후 연결 해제.
    con.commit()
    con.close()

    return reminder_info


## Open Reminder in Detail on Reminder Activation(DoubleClick + Return) from QListWidget
def open_reminder_in_detail(self):
    reminder_info = get_single_reminder_info(self)
    #: Writing Reminder Details
    # Status
    status = list(reminder_status.keys())
    # status에서 '!!!' 오류는 제외시키고,
    status.pop()
    # self.reminders_sublist_status_cmb.setCurrentIndex(status.index(reminder_info[0]))
    sublist_page_rem_status_change(self, reminder_info[0])
    # Text
    # 제목을 편집했을 경우, 해당 리마인더를 DB에서 찾기 어려우니, 
    # 편집창을 열때마다, 여는 리마인더를 따로 저장해놓자.
    self.infos.opened_reminder_text = reminder_info[1]
    self.reminders_sublist_reminder_led.setText(reminder_info[1])
    # Sublist?
    self.reminders_sublist_lwg.clear()
    if reminder_info[2]:
        # 원인은 모르겠지만, string literal(\n, \t)등의 구분없이 archive저장시에는 "\n" 자체로 저장됨
        # 해당 string값을 다시 string literal로 변환하고, \n을 기준으로 리스트화. 이후 for loop.
        for sublist_item in reminder_info[2].replace(r'\n', '\n').splitlines():
            item = QtWidgets.QListWidgetItem(sublist_item)
            item.setFlags(
                QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsEnabled
            )
            # Set Color of sublist item according to status
            item.setForeground(QtGui.QBrush(QtGui.QColor(*reminder_status[sublist_item[:3]][0])))
            # Add to QListWidget
            self.reminders_sublist_lwg.addItem(item)

    # Due Date?
    if reminder_info[3] != "":
        self.reminders_sublist_due_cbx.setChecked(True)
        self.reminders_sublist_due_dte.setDate(QDate.fromString(reminder_info[3], "yyyy.MM.dd"))
    
    if reminder_info[4] != "":
        if not reminder_info[0] in archiving_target:
            pass
        elif reminder_info[0] == "[x]":
            self.reminders_sublist_done_canc_lbl.setText("COMPLETED")
            self.reminders_sublist_done_canc_lbl.setStyleSheet("color:rgb(144,199,133);")
            self.reminders_sublist_done_canc_dte.setStyleSheet("color:rgb(144,199,133);")
        else:
            self.reminders_sublist_done_canc_lbl.setText("CANCELLED")
            self.reminders_sublist_done_canc_lbl.setStyleSheet("color:rgb(175, 80, 100);")
            self.reminders_sublist_done_canc_dte.setStyleSheet("color:rgb(175, 80, 100);")
        
        self.reminders_sublist_done_canc_dte.setDate(QDate.fromString(reminder_info[4], "yyyy.MM.dd"))
        self.reminders_sublist_done_canc_lbl.setEnabled(True)
        self.reminders_sublist_done_canc_dte.setEnabled(True)
        
    
    self.reminders_stack.setCurrentIndex(1)
    

## Load from Archive DB Table and Write to self.popup Reminders History Page
def show_reminder_history(self):
    self.reminders_archive_lwg.clear()
    if not self.reminders_archive_limit_cmb.currentText().isdigit():
        return
    limit = int(self.reminders_archive_limit_cmb.currentText())
    # Load DB
    con = sqlite3.connect("./database/eAcalrem.db")
    cur = con.cursor()    
    # Load Current Items
    items = [list(item) for item in cur.execute(f'SELECT * FROM Archive ORDER BY Status_Changed LIMIT {limit}').fetchall()]
    # Close DB connection
    con.commit()
    con.close()
    
    for item in items:
        gui_content = ""
        if item[0] == "[x]":
            gui_content = "[완료@"
            gui_color = (111, 155, 133)
        else:
            gui_content = "[취소@"
            gui_color = (155, 111, 133)
        gui_content = f'{gui_content}{QDate.fromString(item[4], "yyyy.MM.dd").toString("yyyy.MM.dd(ddd)")}]\n{item[1]}'
        if item[3] != "":
            gui_content = f'{gui_content}\n::DUE {QDate.fromString(item[3], "yyyy.MM.dd").toString("yyyy.MM.dd(ddd)")}'
        if item[2] != "":
            for line in item[2].splitlines():
                gui_content = f'{gui_content}\n - {line}'
        
        archived_reminder = QtWidgets.QListWidgetItem(gui_content)
        archived_reminder.setForeground(QtGui.QBrush(QtGui.QColor(*gui_color)))
        
        self.reminders_archive_lwg.addItem(archived_reminder)
            
   
#     # reversed(list)를 이용한 for loop. 즉, 최근 완료/취소항목이 제일 위로 가도록.
#     for item in reversed(items):
#         # Reminder History ListWidget의 폰트는 Monospace가 아님.
#         # 미적인 효과를 위해 markdown이 아닌 형식으로 변환하자!!
#         if item[1] == "[x]":
#             item[1] = "[완료"
#         else: item[1] = "[취소"
#         # Sublist도 History에서는 모두 한번에 써보자..
#         if item[3]:
#             item[3] = "..."
#             # 원인은 모르겠지만, string literal(\n, \t)등의 구분없이 archive저장시에는 "\n" 자체로 저장됨
#             # 해당 string값을 다시 string literal로 변환하는 작업. 이후 라인별로 리스트화.
#             item[4] = item[4].replace(r'\n', '\n').splitlines()
#         else:
#             item[3] = ""
#             item[4] = ""
#         # Due Date도..
#         if item[5] != "" and item[5] != None: 
#             item[5] = '~'+item[5]
#         else: item[5] = ''
#         # 완료/취소일도..
#         item[6] = '@'+item[6]+']'
        
#         history_gui_format = ""
#         # Sublist가 있다면 다음 줄에 하나씩 더하자. 완료는 *로 시작, 아닌건 -로 시작.
#         if item[3] == "...":
#             history_gui_format = f"{item[1]}{item[6]} {item[2]} {item[3]} {item[5]}"
#             for each in item[4]:
#                 if each.startswith("*"):
#                     history_gui_format = f'{history_gui_format}\n     * {each[1:]}'
#                 else:
#                     history_gui_format = f'{history_gui_format}\n     - {each}'
#         else:
#             history_gui_format = f"{item[1]}{item[6]} {item[2]} {item[5]}"
        
#         self.popup.rem_hist_lwg.addItem(history_gui_format)


## 편집/또는 추가 시 새로 입력될 내용이 기존 DB에 동일하게 입력되어있으면 안되니까!
def verify_reminder(self, reminder:str):
    # DB 연걸.
    con = sqlite3.connect("./database/eAcalrem.db")
    cur = con.cursor()
    # cur.execute는 DB의 값을 tuple로 불러옴. 즉 그냥 하나만 불러오는거니까 [0]추가하면 string값 그대로.
    all_active_reminders = [item[0] for item in cur.execute(f'SELECT Reminder FROM Active').fetchall()]
    # DB 저장 후 연결 해제.
    con.commit()
    con.close()

    if self.infos.opened_reminder_text == reminder:
        return True
    elif reminder in all_active_reminders:
        return False
    else:
        return True
    
    
#################### GUI to DB (incl. Processing)
# UPDATE status changes of reminders_lwg item. Save to DB on change.
def update_status_reminders(self, new_status:str):
    target = self.reminders_lwg.currentItem()
    target_status = target.text()[:3]
    if new_status == target_status:
        return
    target_reminder_text = target.text()[4:].split('\n')[0].replace("...", "").rstrip()
    today = self.infos.date_today.toString("yyyy.MM.dd")
    
    if new_status not in archiving_target:
        status_changed = ""
    else:
        status_changed = today
        
    # DB 연결해서.    
    con = sqlite3.connect("./database/eAcalrem.db")
    cur = con.cursor()
    con.execute(f"UPDATE Active SET Status = '{new_status}', Status_Changed = '{status_changed}' WHERE Reminder = '{target_reminder_text}'")
    # DB 저장 후 연결 해제.
    con.commit()
    con.close()
    # reload reminders gui from db
    load_write_reminders(self)


# Sublist item (reminders_sublist_lwg)의 status change.
# Does not save to DB on change.
def sublist_status_change(self, new_status:str):
    target_sublist = self.reminders_sublist_lwg.currentItem()
    target_sublist.setText(f'{new_status} {target_sublist.text()[4:]}')
    target_sublist.setForeground(QtGui.QBrush(QtGui.QColor(*reminder_status[new_status][0])))
    # 색바꿔준 이후 selection은 해제해주자.
    self.reminders_sublist_lwg.setCurrentItem(None)
   
    
def sublist_page_rem_status_change(self, new_status:str):
    btn_style = f"""
    QPushButton {{
        background-color:rgb(55,60,80);
        color: rgb{reminder_status[new_status][0]};
        border:none;
        border-radius:10px;
        border-bottom-left-radius:0px;
        border:1px solid rgb(50,55,70);
    }}
    QPushButton:pressed {{
        background-color:rgb(50,55,65);
    }}
    QPushButton:hover {{
        background-color:rgb(65,70,100);
    }}
    """
    led_style = f"""
    background-color:rgb(42,48,58);
    padding-left: 18px;
    color: rgb{reminder_status[new_status][0]};
    border:1px solid rgb(50,55,70);
    border-right:none;
    border-left:none;
    """
    old_status = self.reminders_sublist_rem_status_btn.text()
    if old_status == new_status:
        return
    elif new_status == "[x]":
        self.reminders_sublist_done_canc_lbl.setText("COMPLETED")
        self.reminders_sublist_done_canc_lbl.setStyleSheet("color:rgb(144,199,133);")
        self.reminders_sublist_done_canc_dte.setDate(self.infos.date_today)
        self.reminders_sublist_done_canc_dte.setStyleSheet("color:rgb(144,199,133);")
    elif new_status == "[-]":
        self.reminders_sublist_done_canc_lbl.setText("CANCELLED")
        self.reminders_sublist_done_canc_lbl.setStyleSheet("color:rgb(175, 80, 100);")
        self.reminders_sublist_done_canc_dte.setStyleSheet("color:rgb(175, 80, 100);")
    else:
        self.reminders_sublist_done_canc_lbl.setText("")
        self.reminders_sublist_done_canc_lbl.setStyleSheet("color:transparent;")
        self.reminders_sublist_done_canc_dte.setDate(self.infos.date_today)
        self.reminders_sublist_done_canc_dte.setStyleSheet("color:transparent;")
        
    self.reminders_sublist_rem_status_btn.setText(new_status)
    self.reminders_sublist_rem_status_btn.setStyleSheet(btn_style)
    self.reminders_sublist_reminder_led.setStyleSheet(led_style)
  

## Add New Reminder to DB (middle-man, parameter from eAcalrem)
def add_reminder(self):
    reminder = ["", "", "", "", ""]
    reminder_status = self.reminders_status_lbl.text()
    reminder_text = self.reminders_new_led.text()
    reminder[0] = reminder_status
    reminder[1] = reminder_text
    # DB 연결해서.    
    con = sqlite3.connect("./database/eAcalrem.db")
    cur = con.cursor()
    # DB에 새로 추가하고.
    con.execute(f'INSERT INTO Active VALUES (?, ?, ?, ?, ?);', reminder)
    # DB 저장 후 연결 해제.
    con.commit()
    con.close()
    # Reset New Reminder LineEdit and Status to Default
    clear_btn_clicked(self)
    # Reload Gui from New DB
    load_write_reminders(self)


def add_sublist(self):
    new_sublist = f'{self.reminders_sublist_status_lbl.text()} {self.reminders_sublist_item_led.text()}'
    item = QtWidgets.QListWidgetItem(new_sublist)
    item.setFlags(
        QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsEnabled
        )
    # Set Color of sublist item according to status
    item.setForeground(QtGui.QBrush(QtGui.QColor(*reminder_status[new_sublist[:3]][0])))
    # Add to QListWidget
    self.reminders_sublist_lwg.addItem(item)
    # Reset New Reminder LineEdit and Status to Default
    clear_btn_clicked(self)
    

def reminder_detail_write(self):
    # Look for target reminder to edit from DB.
    target_reminder_text = self.infos.opened_reminder_text
    # Get new status info
    reminder_status = self.reminders_sublist_rem_status_btn.text()
    # Get new reminder text
    reminder_text = self.reminders_sublist_reminder_led.text()
    # Get new sublist of reminder
    reminder_sublist = ""
    for i in range(self.reminders_sublist_lwg.count()):
        reminder_sublist = f'{reminder_sublist}{self.reminders_sublist_lwg.item(i).text().rstrip()}\n'
    reminder_sublist = reminder_sublist.rstrip()
    # Get new due_date if selected.
    if self.reminders_sublist_due_cbx.isChecked():
        reminder_due = self.reminders_sublist_due_dte.date().toString("yyyy.MM.dd")
    else: 
        reminder_due = ""
    # Get new status changed date if needed.
    if reminder_status not in archiving_target:
        reminder_status_change_date = ""
    else:
        reminder_status_change_date = self.infos.date_today.toString("yyyy.MM.dd")
    ok = verify_reminder(self, reminder_text)
    if not ok:
        eApopup.warning(text = "같은 리마인더가 이미 존재합니다.\n확인이 필요합니다.")
        return
    # DB 연결해서.    
    con = sqlite3.connect("./database/eAcalrem.db")
    cur = con.cursor()
    # DB에 새로 추가하고.
    con.execute(f"""
                UPDATE Active SET
                Status = '{reminder_status}',
                Reminder = '{reminder_text}',
                Sublist = '{reminder_sublist}',
                Due_Date = '{reminder_due}',
                Status_Changed = '{reminder_status_change_date}'
                WHERE Reminder = '{target_reminder_text}'
                """)
    # DB 저장 후 연결 해제.
    con.commit()
    con.close()
    # Reset New Reminder LineEdit and Status to Default
    clear_btn_clicked(self)
    self.reminders_stack.setCurrentIndex(0)
    # Reload Gui from New DB
    load_write_reminders(self)    


# ## Delete from active reminders (middle-man)
# def delete_active(self):
#     anws_yes = eApopup.warning(text = "해당 항목을 삭제할까요?\n저장/복구 되지 않습니다.", yes_no = True)
#     if anws_yes:
#         selected = self.reminders_lwg.currentRow()
#         self.reminders_lwg.takeItem(selected)
#     # 저장.
#     save_to_DB(self)
    

## Archive 'Done' or 'Cancelled' reminders
def archive_reminders(self):
    # Gui ListWidget is always in sync with DB.
    # DB 연결해서.    
    con = sqlite3.connect("./database/eAcalrem.db")
    cur = con.cursor()
    # Active에서 대상 리마인더를 가져오고.
    reminders_to_archv = list(cur.execute(f'SELECT * FROM Active WHERE Status = "[x]" OR Status = "[-]"').fetchall())
    # Active에서는 지워주고.
    cur.execute(f'DELETE FROM Active WHERE Status = "[x]" OR Status = "[-]"')
    # 하나 이상 일 수 있으니, for loop으로 Archive에 넣어줌.
    for each in reminders_to_archv:
        cur.execute(f'INSERT INTO Archive VALUES (?, ?, ?, ?, ?);', each)
    # DB 저장 후 연결 해제.
    con.commit()
    con.close()
    # GUI reload
    load_write_reminders(self)
        
    
##### UI Management ##### 
def clear_btn_clicked(self):
    self.reminders_lwg.setCurrentItem(None)
    self.reminders_sublist_lwg.setCurrentItem(None)
    new_item_status_change(self, "reminder", "[ ]")
    new_item_status_change(self, "sublist", "[ ]")
    self.reminders_new_led.setText("")
    self.reminders_sublist_item_led.setText("")
    
    
def reminder_Rmenu(self, listwidget:str = None):
    mouse_pos = QtGui.QCursor.pos()
    if not listwidget:
        self.reminders_sublist_lwg.setCurrentItem(None)
    else:
        target_list = getattr(self, listwidget)
        target_item = target_list.itemAt(target_list.mapFromGlobal(mouse_pos))
        if not target_item:
            self.reminders_lwg.setCurrentItem(None)
            return

    self.reminder_Rmenu = QtWidgets.QMenu(self)
    self.reminder_Rmenu.setTitle("Status 변경")
    
    # '!!!' 오류를 제외한 status항목에 대해 context menu 만들기.
    status = list(reminder_status.keys())
    status.pop()
    for each in status:
        label = QtWidgets.QLabel(f'{each} {reminder_status[each][1]}', self)
        label.setStyleSheet(f"""
                            QLabel{{
                                color: rgb{reminder_status[each][0]};
                                font: 11pt 'D2Coding';
                                padding: 5px;
                            }}
                            QLabel::hover{{
                                background-color: rgb(60, 65, 80);
                            }}
                            """)
        action = QtWidgets.QWidgetAction(self)
        action.setText(each)
        action.setDefaultWidget(label)
        self.reminder_Rmenu.addAction(action)
    
    selected_status = self.reminder_Rmenu.exec(mouse_pos)
    
    if selected_status == None:
        return
    
    if not listwidget:
        sublist_page_rem_status_change(self, selected_status.text())
    elif listwidget == "reminders_lwg":
        update_status_reminders(self, selected_status.text())
    else:
        sublist_status_change(self, selected_status.text())


def new_item_status_change(self, target:str, status:str):
    statuses = list(reminder_status.keys())
    statuses.pop()
    if status not in statuses:
        return
    lbl_style = f"""
    background-color:rgb(42,48,58);
    padding-left: 5px;
    color: rgb{reminder_status[status][0]};
    border:none;
    border-top-left-radius:10px;
    border-bottom-left-radius:10px;
    border:1px solid rgb(50,55,70);
    border-right:none;
    """
    led_style = f"""
    background-color:rgb(42,48,58);
    color: rgb{reminder_status[status][0]};
    border:none;
    border:1px solid rgb(50,55,70);
    border-right:none;
    border-left:none;

    """
    if target == "reminder":
        self.reminders_status_lbl.setText(status)
        self.reminders_status_lbl.setStyleSheet(lbl_style)
        self.reminders_new_led.setStyleSheet(led_style)
        self.reminders_new_led.setFocus()
    else:
        self.reminders_sublist_status_lbl.setText(status)
        self.reminders_sublist_status_lbl.setStyleSheet(lbl_style)
        self.reminders_sublist_item_led.setStyleSheet(led_style)
        self.reminders_sublist_item_led.setFocus()

    
def sublist_reset(self):
    self.reminders_sublist_due_cbx.setChecked(False)
    self.reminders_sublist_due_dte.setDate(self.infos.date_today)
    sublist_page_rem_status_change(self, "[ ]")
    self.reminders_sublist_reminder_led.setText("")
    self.reminders_sublist_lwg.clear()
    self.reminders_sublist_item_led.setText("")
    self.infos.opened_reminder_text = ""
    self.reminders_sublist_done_canc_lbl.setText("")
    self.reminders_sublist_done_canc_lbl.setStyleSheet("color:transparent;")
    self.reminders_sublist_done_canc_dte.setStyleSheet("color:transparent;")


def due_date_cbx_toggle(self):
    status = self.reminders_sublist_due_cbx.isChecked()
    self.reminders_sublist_due_dte.setEnabled(status)


def sublist_edited(self):
    for each in range(self.reminders_sublist_lwg.count()):
        sublist = self.reminders_sublist_lwg.item(each).text()
        status = list(reminder_status.keys())
        status.pop()
        if sublist[:3] not in status:
            if sublist.startswith('!!!'):
                pass
            else:
                sublist = f'!!! {sublist}'               
        elif sublist[:3] in status and sublist[3] != " ":
            sublist = f'{sublist[:3]} {sublist[3:]}'
        else:
            pass
        self.reminders_sublist_lwg.item(each).setText(sublist)


def sublist_close(self):
    yes = eApopup.warning(
        text = "편집된 내용은 삭제됩니다.",
        yes_no = True
    )
    if not yes:
        return
    
    sublist_reset(self)
    self.reminders_lwg.setCurrentItem(None)
    self.reminders_stack.setCurrentIndex(0)
    
    
    
##### UNUSED BUT LEFT FOR FUTURE REFERENCE #####
#= Watch out for DB file changes
# reminders_db_file = pathlib.Path('./database/eGhisAssistant.db')
# reminders_db_mdate = str(datetime.datetime.fromtimestamp(reminders_db_file.stat().st_mtime))

# def save_db_mod_time():
#     global reminders_db_mdate
#     print("print before fx exec" + self.infos.reminders_db_mdate)
#     reminders_db_mdate = str(datetime.datetime.fromtimestamp(reminders_db_file.stat().st_mtime))
    
#= On item double click from gui, status change
# TODO 확인. 취소>>완료 또는 완료>>취소 변경은????
# def status_menu(self):
#     done_cancelled = {
#         'Done' : '완료',
#         'Cancelled' : '취소',
#         'MDsymbols' : ['[x]', '[-]']
#     }
#     selected = self.reminders_lwg.currentItem()
#     # 변경 전 status는 일단 저장해놓고.
#     prev_status = selected.text()[:3]
#     # status 메뉴의 항목들은 위에 정의된 대로...
#     menu_items = [value[0] for key, value in statuses.items()]
#     menu_items.append("DELETE")
#     menu_items.append("EDIT")
#     choice = eApopup.reminders_menu(buttons = menu_items)
#     # close면 취소하고
#     if choice == 'CLOSE': return
#     # delete면 그냥 해당 목록 지우고
#     elif choice == "DELETE": delete_active(self)
#     # edit면 edit 창 열어주고
#     elif choice == "EDIT": edit_reminder(self)
#     else:
#         # 새로운 status의 index를 구하면,
#         status_index = menu_items.index(choice)
#         # statuses dictionary의 key값 리스트(순서 지켜짐)에서 인덱스를 이용하여 값을 구할 수 있고.
#         new_status = list(statuses.keys())[status_index]
#         # 새로운 값으로 변경가능함.
#         reminder = selected.text().replace(selected.text()[:3], new_status)
#         # 끝은 아니고.. 몇가지 추가적인 조건이 있는데.. 
#         # 완료/취소 로의 변경이면 날짜 혹시나 입력되어있으면 일단 지우고, 다시 새로 입력. 
#         if prev_status not in done_cancelled['MDsymbols'] and new_status in done_cancelled['MDsymbols']:
#             if " (@" in reminder:
#                 date_pos = reminder.index(" (@")
#                 reminder = reminder.replace(reminder[date_pos:date_pos + 14], "")
#             reminder = reminder + f' (@{self.infos.date_today.toString("yyyy.MM.dd")})'
#         # 완료/취소에서 완료/취소간 변경이면, 날짜 기입력 없으면 단순추가, 있으면 날짜 변경.
#         elif prev_status in done_cancelled['MDsymbols'] and new_status in done_cancelled['MDsymbols']:
#             if " (@" not in reminder:
#                 reminder = reminder + f' (@{self.infos.date_today.toString("yyyy.MM.dd")})'
#             else:
#                 update_date = eApopup.confirm(text=f"오늘 날짜로 다시 {done_cancelled[choice]} 처리할까요?")
#                 if update_date:
#                     date_pos = reminder.index(" (@")
#                     reminder = reminder.replace(reminder[date_pos:date_pos + 14], f' (@{self.infos.date_today.toString("yyyy.MM.dd")})')
#                 else: return
#         # 완료/취소에서 비완료/취소로의 이동이라면, 날짜 기입력시에는 날짜 삭제.
#         elif prev_status in done_cancelled['MDsymbols'] and new_status not in done_cancelled['MDsymbols']:
#             if " (@" in reminder:
#                 date_pos = reminder.index(" (@")
#                 reminder = reminder.replace(reminder[date_pos:date_pos + 14], "")

#         selected.setText(reminder)
#         selected.setForeground(QtGui.QBrush(QtGui.QColor(*statuses[new_status][1])))
#         selected.setSelected(False)
#     # 마지막에 저장.    
#     save_to_DB(self)