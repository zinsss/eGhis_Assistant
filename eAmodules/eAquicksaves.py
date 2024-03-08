import sqlite3
from eAmodules import eApopup, eAutils

#: DB 연결. DB가 없으면 새로 작성하고, 테이블도 작성함.
def connect_DB():
    # Load DB
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()    
    # Create table if not exists
    con.execute('CREATE TABLE if not exists Quick(Saves TEXT)')    
    # Load Dates. And check if today already exist.
    items = [item[0] for item in cur.execute('SELECT Saves FROM Quick').fetchall()]
    # Close DB connection
    con.commit()
    con.close()
    return items

#: GUI에 적용.
def write_GUI(self):
    # DB에서 목록을 가져와서..
    items = connect_DB()
    # 기존 목록을 전부 지우고..
    self.qsv_lwg.clear()
    # 다시 쓰기.
    self.qsv_lwg.addItems(items)

# TODO 전부지우고 다시 쓰는것 말고.. 필요부분만 부분변경하는 방법 적용하기!
#: GUI에서의 변경 내용을 DB에 저장.
def save_DB(self):
    # 우선 GUI에서의 목록을 (순서포함) 리스트로 불러오기.
    items = []
    for i in range(self.qsv_lwg.count()):
        items.append(self.qsv_lwg.item(i).text())
    # DB 연결해서.    
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()
    # DB내 기존 목록을 모두 지우고..
    con.execute('DELETE FROM Quick')
    for item in items:
        con.execute(f"INSERT INTO Quick VALUES (:item)", {'item':item})
    # DB 저장 후 연결 해제.
    con.commit()
    con.close()

#: Edit Item
def edit_item(self):
    try:
        to_edit = self.qsv_lwg.currentItem().text()
    except: 
        eApopup.notify(text = "수정할 아이템을 선택하세요.")
        return
        
    ok = eApopup.confirm_big(text = f'{to_edit}\n\n을 수정할까요?' )
    if not ok: return
    
    edited = eApopup.get_multiline_text(title = "Edit Item", default_text = to_edit)
    if edited == None:
        eApopup.notify(text = '취소되었습니다.')
        return
    else:
            # DB 연결해서.    
            con = sqlite3.connect("./database/eGhisAssistant.db")
            cur = con.cursor()
            # DB내 기존 목록을 모두 지우고..
            con.execute(f'UPDATE Quick SET Saves = "{edited}" WHERE Saves = "{to_edit}"')
            # DB 저장 후 연결 해제.
            con.commit()
            con.close()
            # reload
            write_GUI(self)


#: 새로운 Quick Saves 추가하기.
def write_new(self):
    content = eApopup.get_multiline_text(title = "Add to Quick Saves")
    if content != "":
        if '"' in content:
            eApopup.warning(text = "SQLite3 Syntax 활용법을 잘 몰라서..\n현재 \"이 들어가 있는 경우 에러가 납니다.\n\" 제거/수정 후 다시 입력해주세요.")
            return
        self.qsv_lwg.addItem(content)
    else: return