import sqlite3
from eAmodules import eApopup, eAinput

## DB load/save, Gui Preparations

#: DB 연결. DB가 없으면 새로 작성하고, 테이블도 작성함.
def connect_DB():
    categories = ['DOCS', 'STUD']
    # Load DB
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()
    # Create table if not exists
    con.execute('CREATE TABLE if not exists MedDocs(Cat TEXT UNIQUE, Title TEXT, Contents TEXT)')    
    mdoc_DOCS = dict(cur.execute('SELECT Title, Contents FROM MedDocs WHERE Cat="DOCS"').fetchall())
    mdoc_STUD = dict(cur.execute('SELECT Title, Contents FROM MedDocs WHERE Cat="STUD"').fetchall())
    # Close DB connection
    con.commit()
    con.close()
    return mdoc_DOCS, mdoc_STUD

#: GUI에 적용.
def write_GUI(self):
    # DB에서 목록을 가져와서..
    mdoc_DOCS, mdoc_STUD = connect_DB()
    # 기존 목록을 전부 지우고..
    self.mdoc_docs_lwg.clear()
    self.mdoc_stud_lwg.clear()
    self.mdoc_preview_cat_lbl.setText("")
    self.mdoc_preview_doc_title_lbl.setText("")
    self.mdoc_contents_pte.setPlainText("")
    # 다시 쓰기.
    self.mdoc_docs_lwg.addItems(list(mdoc_DOCS.keys()))
    self.mdoc_stud_lwg.addItems(list(mdoc_STUD.keys()))
    

#: Listwidget item clicked -> load contents to preview.
def load_contents(self, cat:str = None):
    if self.mdoc_edit_btn.isChecked():
        ok = eApopup.warning(text = "편집 모드가 활성화 되어있습니다\n저장 또는 편집모드 해제 후\n다시 시도해 주세요.")
        return
    
    category = {'DOCS':'진단/소견서', 'STUD':'학교 제출용'}
    if cat == None:
        if self.mdoc_preview_cat_lbl.text() == '진단/소견서': cat = "DOCS"
        else: cat = "STUD"
        title = self.mdoc_preview_doc_title_lbl.text()
    elif cat == "DOCS":
        title = self.mdoc_docs_lwg.currentItem().text()
        self.mdoc_stud_lwg.clearSelection()
    else:
        title = self.mdoc_stud_lwg.currentItem().text()
        self.mdoc_docs_lwg.clearSelection()

     # Load DB
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()    
    # Load Dates. And check if today already exist.
    contents = cur.execute(f'SELECT Contents FROM MedDocs WHERE Cat = "{cat}" AND Title = "{title}"').fetchone()
    # Close DB connection
    con.commit()
    con.close()
    # Write note's content to GUI
    self.mdoc_preview_cat_lbl.setText(category[cat])
    self.mdoc_preview_doc_title_lbl.setText(title)
    self.mdoc_contents_pte.setPlainText(contents[0])
    
    
#: DB UPDATE
def update_db(cat:str, column:str, new_value:str, old_value:str):
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()
    # 편집항목 DB내 UPDATE
    con.execute(f'UPDATE MedDocs SET {column} = "{new_value}" WHERE Cat = "{cat}" AND {column} = "{old_value}"')
    # DB 저장 후 연결 해제.
    con.commit()
    con.close()
    

#: GUI에서의 순서변경을 DB에 저장.
def order_change(self, cat:str):
    mdoc_DOCS, mdoc_STUD = connect_DB()
    if cat == "DOCS": target_dict = mdoc_DOCS
    else: target_dict = mdoc_STUD
    target_lwg = getattr(self, f'mdoc_{cat.lower()}_lwg')
    
    items = []
    for i in range(target_lwg.count()):
        item = ["", "", ""]
        item[0] = cat
        item[1] = target_lwg.item(i).text()
        item[2] = target_dict[target_lwg.item(i).text()]
        items.append(item)
    
    # DB 연결해서.    
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()
    # DB내 기존 목록을 모두 지우고..
    con.execute(f'DELETE FROM MedDocs WHERE Cat = "{cat}"')
    for item in items:
        con.execute(f'INSERT INTO MedDocs VALUES (?, ?, ?);', item)
    # DB 저장 후 연결 해제.
    con.commit()
    con.close()

    
#: 타이틀 편집
def title_edit(self, cat:str):
    target_lwg = getattr(self, f'mdoc_{cat.lower()}_lwg')
    old_title = target_lwg.currentItem().text()
    ok = eApopup.confirm_big(text = f"[ {old_title} ]의 제목을 편집합니다.")
    if not ok: return
    
    new_title = eApopup.get_text(
        text = "새로운 문서 제목을 입력하세요.",
        default_text = old_title
        )
    if new_title == None or new_title == old_title: return
    
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()
    # 편집항목 DB내 UPDATE
    con.execute(f'UPDATE MedDocs SET Title = "{new_title}" WHERE Cat = "{cat}" AND Title = "{old_title}"')
    # DB 저장 후 연결 해제.
    con.commit()
    con.close()
    write_GUI(self)
    
    
#: 문서 타이틀 추가
def add_new_doc(self, cat:str):
    category = {'DOCS':'진단/소견서', 'STUD':'학교 제출용'}
    target_lwg = getattr(self, f'mdoc_{cat.lower()}_lwg')
    ok = eApopup.confirm_big(text = f"[ {category[cat]} ]에 새로운 문서를 추가할까요?")
    if not ok: return
    
    new_doc_title = eApopup.get_text(text = "새 문서의 제목을 입력하세요.")
    if new_doc_title == None or new_doc_title == "": return
    
    new_item = ["", "", ""]
    new_item[0] = cat
    new_item[1] = new_doc_title
    
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()
    # 편집항목 DB내 UPDATE
    con.execute(f'INSERT INTO MedDocs VALUES (?, ?, ?);', new_item)
    # DB 저장 후 연결 해제.
    con.commit()
    con.close()
    
    write_GUI(self)


#: 문서 삭제
def delete_doc(self, cat:str):
    target_lwg = getattr(self, f'mdoc_{cat.lower()}_lwg')
    title = target_lwg.currentItem().text()
    
    ok = eApopup.warning(text = "문서를 정말 삭제할까요?", yes_no=True)
    if not ok: return
    okok = eApopup.warning(text = f'[ {title} ]\n\n정말 삭제할까요? 복구되지 않습니다.', yes_no=True)
    if not okok: return
    
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()
    # 편집항목 DB내 UPDATE
    con.execute(f'DELETE FROM MedDocs WHERE Cat = "{cat}" AND Title = "{title}"')
    # DB 저장 후 연결 해제.
    con.commit()
    con.close()
    
    write_GUI(self)   
    
    
#: 문서 편집모드 확인절차
def check_edit_toggle(self):
    currentMode = self.mdoc_edit_btn.isChecked()
    if currentMode == False:
        ok = eApopup.warning(text = "저장 없이 편집모드를 해제할까요? DB에 반영되지 않습니다.")
        if not ok: 
            self.mdoc_edit_btn.setChecked(True)
            return
    else:
        if self.mdoc_preview_cat_lbl.text() == "" or self.mdoc_preview_doc_title_lbl.text() == "":
            eApopup.notify(text = "편집할 문서를 먼저 선택하세요.")
            return
        
        ok = eApopup.confirm_big(text = f'[ {self.mdoc_preview_doc_title_lbl.text()} ]을/를 편집하시겠습니까?')
        if not ok:
            self.mdoc_edit_btn.setChecked(False)
            return
        
    edit_mode_toggler(self)
    

#: 문서 편집모드로 변경
def edit_mode_toggler(self, toggle:bool = None):
    if toggle == None:
        toggle = self.mdoc_edit_btn.isChecked()
    
    self.mdoc_edit_btn.setChecked(toggle) 
    self.mdoc_contents_pte.setReadOnly(not toggle)
    self.mdoc_contents_save_btn.setEnabled(toggle)
    if toggle == False:
        load_contents(self)
        
    
#: 편집한 문서 저장하기
def edit_doc_contents(self):
    category = {'진단/소견서':'DOCS', '학교 제출용':'STUD'}
    cat_lbl = self.mdoc_preview_cat_lbl.text()
    cat = category[cat_lbl]
    doc_title = self.mdoc_preview_doc_title_lbl.text()
    new_contents = self.mdoc_contents_pte.toPlainText()
    
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()
    # 편집항목 DB내 UPDATE
    con.execute(f'UPDATE MedDocs SET Contents = "{new_contents}" WHERE Cat = "{cat}" AND Title = "{doc_title}"')
    # DB 저장 후 연결 해제.
    con.commit()
    con.close()
    
    edit_mode_toggler(self, False)
    load_contents(self, cat)
    
#: Copy or Copy_Paste Docs.
#TODO Soon to be deleted.
def docs_cnp(self, copy_only:bool = False):
    if self.mdoc_preview_cat_lbl.text() == "" or self.mdoc_preview_doc_title_lbl.text() == "":
            eApopup.notify(text = "편집할 문서를 먼저 선택하세요.")
            return
    
    contents = self.mdoc_contents_pte.toPlainText()
    if not copy_only:
        eAinput.copy_paste_it(contents)
    else: eAinput.copy_it(contents)
    
#: Copy or Copy_Paste Docs.
def docs_copy(self, close_window:bool = True):
    if self.mdoc_preview_cat_lbl.text() == "" or self.mdoc_preview_doc_title_lbl.text() == "":
            eApopup.notify(text = "편집할 문서를 먼저 선택하세요.")
            return
    
    contents = self.mdoc_contents_pte.toPlainText()
    eAinput.copy_it(contents)
    if close_window: self.hide()
    else: return
    
     