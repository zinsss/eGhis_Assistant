from PySide6.QtCore import QDate, QTime

from os import system
import requests, sqlite3

import main
from eAmodules import eAinput, eApopup, eAreminders

## Various Common Functions Used in APP.
#: 주민번호에서 생년월일. 뒷자리로 생년 19 or 20 구분하기.
def jmno_to_birthd(jmno: str):
    # 정확하진 않지만, - 가 있는지, 14자리가 맞는지 확인하기.
    if "-" not in jmno: return
    elif len(jmno) != 14: return
    # 19 또는 20 확인을 위해 먼저 리스트에 분류해놓고.
    year19s = [1, 2, 5, 6]
    year20s = [3, 4, 7, 8]
    # 뒷자리 시작 번호가 어느 년도에 해당하는 숫자인지 확인하고 해당 년도 기입.
    if int(jmno[7]) in year19s: return "19" + jmno[:6]
    elif int(jmno[7]) in year20s: return "20" + jmno[:6]
    else: return
      
#: 최소한의 주민등록번호 validity 검사
def jmno_isValid(jmno_with_dash: str):
    # '-'가 있는 주민번호만 받기로 하고
    if "-" not in jmno_with_dash: return False
    # 7번째 (파이썬에서는 0부터 시작이니 6) 자리에 '-'가 있어야하고
    elif jmno_with_dash[6] != "-": return False
    # '-' 포함 총 14자리여야 하고
    elif len(jmno_with_dash) != 14: return False
    # '-'를 제외 하면 모두 숫자로 구성되어야 하고
    elif jmno_with_dash.replace("-","").isdigit() == False: return False
    # 앞자리는 날짜양식에 맞아야 하며
    elif QDate.fromString(jmno_with_dash[:6], "yyMMdd").isValid() == False: return False
    # 뒷자리 첫번째 숫자는 0이나 9가 아니어야 진행 가능.(생존자 없음 1800년대)
    elif int(jmno_with_dash[7]) not in [1,2,3,4,5,6,7,8]: return False
    else: return True
    
    # # 추가 검증 전, 주민등록 되지 않은 한국인의 경우 뒷자리 첫자리까지만 있고 뒷자리는 모두 0이니 예외시켜주고
    # if jmno_with_dash[:7] == "000000": return True
    
    ##### 주민등록번호 개편으로 사용 시 외국인, 2000년생 이후에서 간헐적 에러남. 사용불가.    
    # # 뒷자리 가장 마지막 검증숫자 확인.
    # # 먼저 '-'를 제외한 모든 숫자를 각각 리스트에 담고
    # each_noDash_noLastDigit = [int(x) for x in jmno_with_dash.replace("-", "")]
    # # 각 숫자를 multipliers 리스트의 숫자로 각각 순서대로 곱해줌 (제시된 번호의 마지막 자리는 제외)
    # multipliers = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    # timed_list = [each_noDash_noLastDigit[i] * multipliers[i] for i in range(len(multipliers))]
    # # 각각의 모든 곱한 값을 더해주고
    # all_added = 0
    # for i in range(len(timed_list)):
    #     all_added = all_added + timed_list[i]
    # # 그 값을 11로 나눈 나머지(remainder)를 다시 11에서 빼주면 나오는 숫자.
    # last_step = 11 - (all_added % 11)
    # # 만약 마지막 계산값이 두자리라면 그 가장 뒷자리 숫자.
    # if last_step >= 10:
    #     last_step = int(str(last_step)[-1])
    # # 계산값이 제시된 주민등록번호의 마지막 숫자와 일치한지 비교.
    # if last_step == each_noDash_noLastDigit[-1]: return True
    # else: return False
        
#: 미성년자 여부 확인
def check_underaged(self, jmno_with_dash:str):
    birthday_yyyyMMdd = jmno_to_birthd(jmno_with_dash)
    target_birth_year = self.infos.date_today.year() - 19
    if int(birthday_yyyyMMdd[:4]) > target_birth_year:
        return True
    elif int(birthday_yyyyMMdd[:4]) == target_birth_year:
        birthday_this_year = QDate.fromString(str(self.infos.date_today.year()) + birthday_yyyyMMdd[4:], "yyyyMMdd")
        today = QDate.currentDate()
        days_to = today.daysTo(birthday_this_year)
        if days_to >= 0: return True
        else: return False        
    else: return False
    
#: 만개월 수 계산하기
def check_age_in_months(jmno_with_dash:str):
    birthday_yyyyMMdd = jmno_to_birthd(jmno_with_dash)
    birthday = QDate.fromString(birthday_yyyyMMdd, "yyyyMMdd")
    # birth_year
    
#= List Widget Manipulation. 
#: 리스트위젯 내 선택 아이템 복사 또는 복붙.
#TODO Soon to be deleted.
def lwg_copy_or_paste(self, listwdg:str, copy_only:bool = False):
    '''
    listwdg: target QListWidget name in string.
    copy_only: default False, only copies to clipboard if True. 
    '''
    lwg = getattr(self, listwdg)
    item = lwg.currentItem().text()
    if copy_only: eAinput.copy_it(item)
    else: eAinput.copy_paste_it(item)

#: 리스트위젯 내 선택 아이템 이동 (위/아래).        
def lwg_move_item(self, listwdg:str, move:str):
    '''
    listwdg: target QListWidget name in string.
    move: 'UP' or 'Down' in string, case insensitive.
    '''
    directions = ["up", "down"]
    if move.lower() not in directions: return    
    lwg = getattr(self, listwdg)
    row = lwg.currentRow()
    item = lwg.takeItem(row)
    if move.lower() == "up":
        lwg.insertItem(row -1, item)
        lwg.setCurrentRow(row-1)
    else:
        lwg.insertItem(row +1, item)
        lwg.setCurrentRow(row+1)
        
#: 리스트위젯 내 선택 아이템 삭제.
def lwg_delete_item(self, listwdg:str):
    '''
    listwdg: target QListWidget name in string.
    '''
    ok = eApopup.warning(text = "선택된 항목을 삭제합니다.\n되돌릴 수 없습니다 !!!", yes_no = True)
    if not ok: return
    lwg = getattr(self, listwdg)
    row = lwg.currentRow()
    lwg.takeItem(row)

#: 리스트위젯 아이템 추가
def lwg_add_single_line_item(self, listwdg:str, popup_text:str = ""):
    lwg = getattr(self, listwdg)
    ok = eApopup.confirm(text = f"새로운 항목을 추가할까요?")
    if not ok: return
    else:
        item = eApopup.get_text(text = popup_text)
        if not item: return
        lwg.addItem(item)

#: 리스트위젯 항목 편집(단순 텍스트)
def lwg_item_text_edit(self, listwdg:str, popup_text:str):
    lwg = getattr(self, listwdg)
    ok = eApopup.confirm(text = "선택된 항목을 편집할까요?")
    if not ok: return
    else:
        item = eApopup.get_multiline_text()
        
        
## Other Utilities
def send_discord(self, text:str):
    # 메신저 보내기 설정이 되어있는지 우선 확인하고, 해제됬으면 취소.
    if not self.popup.stng_messenger_btn.isChecked(): return
    # 메신저 설정에 서버(WEBHOOK)가 있는지 확인하고. 
    # TODO 공란이라고 무조건 보내지는 건 아니니까... confirmation 추가하는게..
    if self.popup.stng_messenger_server_pte.toPlainText() == "": return
    # 실제로 메세지 보내기
    message = {"content": f"{str(text)}"}
    requests.post(self.popup.stng_messenger_server_pte.toPlainText(), data=message)
    

## Daily Report.
# TODO work in progress
def daily_report_discord(self):
    if not self.popup.stng_messenger_btn.isChecked(): return
    # Title
    title = f'# Daily Report, {self.infos.date_today.toString("yyyy-MM-dd ddd")}\n'
    
    # Calendar Events in 7 days
    events = f'## Events in 7 days\n'
    
    # Current Active Reminders
    reminders = f'## Active Reminders\n'
    for i in range(self.reminders_lwg.count()):
        status = eAreminders.statuses[self.reminders_lwg.item(i).text()[:3]][2]
        reminder = self.reminders_lwg.item(i).text()[3:]
        reminders = reminders + status + reminder + "\n"
    
    final_report = title + events + reminders
    
    send_discord(self, final_report)
    
    
## DB sync to dropbox.
def DBsyncDropBox(self):
    # 설정을 먼저 확인해주고..
    if not self.popup.stng_cloud_sync_btn.isChecked(): return
    # 파이썬에서 요일을 월요일부터 일요일까지 1~7로 표현하는 것, 그리고 리스트는 0에서 시작해서 인덱스값이 부여되는것 고려!
    folder_name = [None, "mon", "tue", "wed", "thu", "fri", "sat", "sun"]    
    today_date = self.infos.date_today 
    year = today_date.year()
    month = today_date.month()
    
    if month != 1:
        prev_month = month - 1
        prev_month_year = year
    else: 
        prev_month = 12
        prev_month_year = year - 1
    
    target_date = today_date.addDays(-1)
   
    # Load DB
    con = sqlite3.connect("./database/eAcalrem.db")
    cur = con.cursor()
    # Get Data    
    month_events = cur.execute(f'SELECT * FROM Calendar WHERE (Year={year} AND Month={month}) OR (Year = {prev_month_year} AND Month={prev_month})').fetchall()
    # Close DB connection
    con.close()
    
    if month_events:    
        holidays = []
        for event in month_events:
            if event[3]: holidays.append(QDate(*event[:3]))
    
    while True:  
        if target_date.dayOfWeek() == 7:
            target_date = target_date.addDays(-1)
            
        elif target_date in holidays:
            target_date = target_date.addDays(-1)
            
        elif target_date.dayOfWeek() == 6 and target_date.day() % 5 != 0:
            target_date = target_date.addDays(-1)
        
        else:
            break
    
    system(f'cmd /c "xcopy e:\\backup\\{folder_name[target_date.dayOfWeek()]} e:\\MyFiles\\Dropbox\\Sync\\eghis\\{folder_name[target_date.dayOfWeek()]} /E/H/C/I/Y"')
    send_discord(self, text = f"eGhis 백업자료를(\{folder_name[target_date.dayOfWeek()]}) DropBox에 저장했습니다.")


        
        
# def to_snake_case(text:str):
#     temp = [char for char in text]
#     was_upper = False
#     for i in range(len(temp)):
#         if temp[i].islower():
#             was_upper = False
#         elif temp[i] == " ":
#             temp[i] = ""
#             was_upper = False
#         elif temp[i].isupper():
#             if i == 0:
#                 temp[i] = temp[i].lower()
#             elif i == len(temp)-1 and was_upper:
#                 temp[i] = temp[i].lower()
#             elif i == len(temp)-1 and not was_upper:
#                 temp[i] = "_"+temp[i].lower()
#             elif not was_upper:
#                 temp[i] = "_" + temp[i].lower()
#             elif temp[i+1].islower():
#                 temp[i] = "_" + temp[i].lower()
#             elif temp[i+1].isupper():
#                 temp[i] = temp[i].lower()
#             was_upper = True
#     return "".join(temp)
