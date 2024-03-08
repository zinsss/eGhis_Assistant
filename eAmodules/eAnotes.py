import sqlite3
from eAmodules import eApopup

#: DB 연결. DB가 없으면 새로 작성하고, 테이블도 작성함.
def connect_DB():
    # Load DB
    con = sqlite3.connect("./database/eGHisAssistant.db")
    cur = con.cursor()    
    # Create table if not exists
    con.execute('CREATE TABLE if not exists Notes(Title TEXT, Contents TEXT)')    
    # Load Dates. And check if today already exist.
    items = [item[0] for item in cur.execute('SELECT Title FROM Notes').fetchall()]
    # Close DB connection
    con.commit()
    con.close()
    return items

#: GUI에 적용.
def write_GUI(self):
    # DB에서 목록을 가져와서..
    items = connect_DB()
    # 기존 목록을 전부 지우고..
    self.notes_title_cmb.clear()
    # 다시 쓰기.
    self.notes_title_cmb.addItem("노트를 선택해주세요.")
    self.notes_title_cmb.addItems(items)
    self.notes_title_cmb.insertSeparator(1)
    # NotesManager에도 써주자.
    self.notes_manager.notes_lwg.clear()
    self.notes_manager.notes_lwg.addItems(items)
    self.notes_manager.notes_title.setText("")

    
#: Load contents of the notes when selected from combobox.    
def load_contents(self, title:str, notes_manager:bool = False):
    global internal_change
    notes = connect_DB()
    
    if title not in notes:
        self.notes_contents_pte.setPlainText("")
        return
    # Load DB
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()    
    # Load Dates. And check if today already exist.
    contents = cur.execute(f'SELECT Contents FROM Notes WHERE Title = "{title}"').fetchone()
    # Close DB connection
    con.commit()
    con.close()
    if not notes_manager:
        self.notes_contents_pte.setPlainText(contents[0])
    else: 
        if self.notes_manager.editing_btn.isChecked() and not internal_change:
            yes = eApopup.warning(text = "현재 노트를 편집 중 입니다.\n편집을 취소할까요?", yes_no = True)
            if not yes: return
            editing_btn_toggle(self.notes_manager)
        self.notes_manager.notes_title.setText(title)
        nm_write_contents_internally(self.notes_manager, contents[0])
        


#################### Notes Manager ####################
internal_change = False

# Opening Notes Manager - (self)
def open_manager(self):
    index_at_cmb = self.notes_title_cmb.currentIndex()
    #! 콤보박스에 추가한 '노트를 선택해주세요', separator 제외.(separator도 index하나 잡아먹음!!!)
    if index_at_cmb <= 1:
        self.notes_manager.notes_lwg.clearSelection()
        self.notes_manager.notes_title.setText("")
        nm_write_contents_internally(self.notes_manager, "")
        self.notes_manager.show()
    else:
        self.notes_manager.notes_lwg.setCurrentItem(self.notes_manager.notes_lwg.item(index_at_cmb - 2))
        load_contents(self, self.notes_manager.notes_lwg.currentItem().text(), notes_manager = True)
        self.notes_manager.show()

# When writing contents internally without editing sign - (self.notes_manager)
def nm_write_contents_internally(self, text:str):
    global internal_change
    internal_change = True
    self.notes_contents.setPlainText(text)


# Editing sign on/off (self.notes_manager)
def editing_btn_toggle(self):
    current = self.editing_btn.isChecked()
    self.editing_btn.setChecked(not current)
    self.reset_btn.setEnabled(not current)
    self.save_btn.setEnabled(not current)


# Checking if content change is internal or by user. - (self.notes_manager)
def editing(self):
    global internal_change
    if internal_change:
        internal_change = False
        return
    if self.editing_btn.isChecked(): return   
    editing_btn_toggle(self)
    
    
# 노트 추가
def add_note(self):
    note_title = eApopup.get_text(text = "새노트의 제목을 입력해주세요.")
    if note_title == "": return    
    self.notes_lwg.addItem(note_title)
    
    DB_insert_list = ["", ""]
    DB_insert_list[0] = (note_title)

    # Load DB
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()    
    # Load Dates. And check if today already exist.
    cur.execute(f'INSERT INTO Notes VALUES (?,?);', DB_insert_list)
    # Close DB connection
    con.commit()
    con.close()
    
    write_GUI(self.parent)
    
    
# 노트 순서 편집
def edit_note_order(self):
    # Load DB
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()
    # Get all items (title, content) in DB.
    all_items = {item[0]:item[1] for item in cur.execute('SELECT * FROM Notes').fetchall()}
    # Make a new order by listwidget index number
    new_items_order = []
    for i in range(self.notes_lwg.count()):
        each_item = ["", ""]
        each_item[0] = self.notes_lwg.item(i).text()
        each_item[1] = all_items[self.notes_lwg.item(i).text()]
        new_items_order.append(each_item)
    # First Delete Everything From Table    
    cur.execute(f'DELETE FROM Notes')
    # Write back each in new order
    for item in new_items_order:
        cur.execute(f'INSERT INTO Notes VALUES (?,?);', item)
    # Close DB connection
    con.commit()
    con.close()
    
    write_GUI(self.parent)
    

# 노트 제목 편집
def edit_title(self):
    old_title = self.notes_lwg.currentItem().text()
    
    new_title = eApopup.get_text(text = f"[ {old_title} ]의\n새로운 제목을 입력해주세요.")
    if new_title == "":
        eApopup.notify(text = "제목이 입력되지 않아 취소합니다.")
        return
    ok = eApopup.confirm(text = f'[ {old_title} ]을\n[ {new_title} ]로\n변경/저장 할까요?')
    if not ok: return
    
    # Load DB
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()    
    # Update new title over old title.
    cur.execute(f'UPDATE Notes SET Title = "{new_title}" WHERE Title = "{old_title}"')
    # Close DB connection
    con.commit()
    con.close()
    
    write_GUI(self.parent)
    

# 노트 내용 편집
def edit_content(self):
    current_note = self.notes_lwg.currentItem()
    current_row = self.notes_lwg.currentRow()
    new_content = self.notes_contents.toPlainText()

    if current_note == None:
        ok = eApopup.confirm(text = "작성된 내용으로 새로운 노트를 생성할까요?")
        if not ok: return
        add_note(self)
        self.notes_lwg.setCurrentRow(self.notes_lwg.count()-1)
        current_row = self.notes_lwg.currentRow()
        current_note = self.notes_lwg.currentItem()
    
    note_title = current_note.text()

    # Load DB
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()    
    # Update new title over old title.
    cur.execute(f'UPDATE Notes SET Contents = "{new_content}" WHERE Title = "{note_title}"')
    # Close DB connection
    con.commit()
    con.close()
    
    editing_btn_toggle(self)
    write_GUI(self.parent)
    self.notes_lwg.setCurrentRow(current_row)
            

# 노트 삭제
def delete_note(self):
    current_note = self.notes_lwg.currentItem().text()
    if not current_note: return
    
    yes = eApopup.warning(text = f'[ {current_note} ]을/를\n정말 삭제할까요? (복구 안됨)')
    if not yes: return
    
    # Load DB
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()    
    # Update new title over old title.
    con.execute(f'DELETE FROM Notes WHERE Title = "{current_note}"')
    # Close DB connection
    con.commit()
    con.close()

    write_GUI(self.parent)

#######################################################

    
# #: Edit current loaded notes.
# def edit_current_note(self):
#     sep = "---------------------------------------------------------"
#     notes = connect_DB()
#     title = self.notes_title_cmb.currentText()
#     if title not in list(notes): return
#     contents = self.notes_contents_pte.toPlainText()
#     ok = eApopup.warning(text = f"[ {title} ]의\n내용을 수정하시겠습니까?", yes_no = True)
#     if not ok: return
#     new_contents = eApopup.get_multiline_text(title=f'편집 - {title}', default_text = contents)
#     if new_contents == None: return
#     ok = eApopup.confirm_big(text = f"[ {title} ]의 내용을;\n{sep}\n{new_contents}\n{sep}\n으로 변경할까요?")
#     if not ok: return
#     self.notes_contents_pte.setPlainText(new_contents)
#     notes[title] = new_contents
#     save_DB_with(notes)

# #: Add New Notes.
# def add_new_note(self):
#     sep = "---------------------------------------------------------"
#     notes = connect_DB()
#     ok = eApopup.confirm(text = "Note를 추가하시겠습니까?")
#     if not ok: return
#     title = eApopup.get_text(text = "제목을 입력하세요.")
#     if title in list(notes):
#         eApopup.notify(text = "같은 이름의 Note가 이미 존재합니다.\n다시 작성해주세요.")
#         return
#     contents = eApopup.get_multiline_text(title = f'New Note - {title}')
#     ok = eApopup.confirm_big(text = f"[ {title} ]의 내용을;\n{sep}\n{contents}\n{sep}\n으로 입력할까요?")
#     while not ok:
#         contents = eApopup.get_multiline_text(title = f'New Note - {title}', default_text = {contents})
#     notes[title] = contents
#     save_DB_with(notes)
#     write_GUI(self)

# #: Save to DB with list provided.
# def save_DB_with(notes:dict):
#     # DB연결
#     con = sqlite3.connect("./database/eGHisAssistant.db")
#     cur = con.cursor()
#     # DB내 기존 목록을 모두 지우고..
#     con.execute('DELETE FROM Notes')
#     for k, v in notes.items():
#         con.execute(f"INSERT INTO Notes VALUES (:title, :text)", {'title': k, 'text': v})
#     # DB 저장 후 연결 해제.
#     con.commit()
#     con.close()

# #: Delete current note
# def delete_current_note(self):
#     notes = connect_DB()
#     title = self.notes_title_cmb.currentText()
#     if title not in list(notes): return
#     ok = eApopup.warning(text =f"[ {title} ]을\n정말 삭제하시겠습니까?", yes_no = True)
#     if not ok: return
#     notes.pop(title)
#     save_DB_with(notes)
#     write_GUI(self)
    
    
