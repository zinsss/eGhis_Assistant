import sqlite3
from eAmodules import eApopup, eAinput

# DB load/save, Gui Preparations


# DB 연결. DB가 없으면 새로 작성하고, 테이블도 작성함.
def connect_DB():
    # Load DB
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()
    # Create table if not exists
    cur.execute('CREATE TABLE if not exists MedDocs(Title TEXT UNIQUE, Contents TEXT)')
    mdocs = dict(cur.execute('SELECT Title, Contents FROM MedDocs').fetchall())
    # Close DB connection
    con.commit()
    con.close()
    return mdocs


# GUI에 적용.
def write_GUI(self):
    # DB에서 목록을 가져와서..
    mdocs = connect_DB()
    # 기존 목록을 전부 지우고..
    self.mdoc_lwg.clear()
    self.mdoc_title_led.setText("")
    self.mdoc_contents_pte.setPlainText("")
    # 다시 쓰기.
    self.mdoc_lwg.addItems(list(mdocs.keys()))


# Listwidget item clicked -> load contents to preview.
def load_contents(self):
    self.reset_timer_start()
    if self.mdoc_edit_btn.isChecked():
        eApopup.warning(text="편집 모드가 활성화 되어있습니다\n저장 또는 편집모드 해제 후\n다시 시도해 주세요.")
        return

    title = self.mdoc_lwg.currentItem().text()

    # Load DB
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()
    # Get Contents for selected title.
    contents = cur.execute(f'SELECT Contents FROM MedDocs WHERE Title = "{title}"').fetchone()
    if not contents:
        contents_text = ""
    else:
        contents_text = contents[0]
    # Close DB connection
    con.commit()
    con.close()
    # Write note's content to GUI
    self.mdoc_title_led.setText(title)
    self.mdoc_title_led.setReadOnly(True)
    self.mdoc_contents_pte.setPlainText(contents_text)
    self.mdoc_contents_pte.setReadOnly(True)


# GUI에서의 순서변경을 DB에 저장.
def order_change(self):
    mdocs = connect_DB()

    items = []
    for i in range(self.mdoc_lwg.count()):
        item = ["", ""]
        item[0] = self.mdoc_lwg.item(i).text()
        item[1] = mdocs[self.mdoc_lwg.item(i).text()]
        items.append(item)

    # DB 연결해서.
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()
    # DB내 기존 목록을 모두 지우고..
    cur.execute('DELETE FROM MedDocs')
    for item in items:
        con.execute('INSERT INTO MedDocs VALUES (?, ?);', item)
    # DB 저장 후 연결 해제.
    con.commit()

    con.close()
    load_contents(self)


# 문서 타이틀 추가
def add_new_doc(self):
    ok = eApopup.confirm_big(text="새로운 문서를 추가할까요?")
    if not ok:
        return

    new_doc_title = eApopup.get_text_big(text="새 문서의 제목을 입력하세요.")
    if new_doc_title is None or new_doc_title == "":
        return

    new_doc = [new_doc_title, ""]

    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()
    # 편집항목 DB내 UPDATE
    cur.execute('INSERT INTO MedDocs VALUES (?, ?);', new_doc)
    # DB 저장 후 연결 해제.
    con.commit()
    con.close()

    write_GUI(self)


# 문서 삭제
def delete_doc(self):
    title = self.mdoc_lwg.currentItem().text()

    if self.mdoc_edit_btn.isChecked():
        eApopup.warning(text="문서를 편집 중 입니다.\n저장 또는 취소 후 진행하세요.")
        return

    ok = eApopup.warning(text="문서를 정말 삭제할까요?", yes_no=True)
    if not ok:
        return
    okok = eApopup.warning(text=f'{title}\n\n정말 삭제할까요? 복구되지 않습니다.', yes_no=True)
    if not okok:
        return

    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()
    # 편집항목 DB내 UPDATE
    cur.execute(f'DELETE FROM MedDocs WHERE Title = "{title}"')
    # DB 저장 후 연결 해제.
    con.commit()
    con.close()

    write_GUI(self)


# 문서 편집모드 확인절차
def check_edit_toggle(self):
    currentMode = self.mdoc_edit_btn.isChecked()
    if currentMode is False:
        ok = eApopup.warning(text="저장 없이 편집모드를 해제할까요? DB에 반영되지 않습니다.")
        if not ok:
            self.mdoc_edit_btn.setChecked(True)
            return
    else:
        if self.mdoc_preview_cat_lbl.text() == "" or self.mdoc_preview_doc_title_lbl.text() == "":
            eApopup.notify(text="편집할 문서를 먼저 선택하세요.")
            return

        ok = eApopup.confirm_big(text=f'[ {self.mdoc_preview_doc_title_lbl.text()} ]을/를 편집하시겠습니까?')
        if not ok:
            self.mdoc_edit_btn.setChecked(False)
            return

    edit_mode_toggler(self)


# 문서 편집모드로 변경
def edit_mode_toggler(self, toggle: bool):
    style_view = "color: rgb(177, 211, 233);"
    style_edit = "color: rgb(180, 150, 185);"

    if toggle:
        style = style_edit
        self.infos.edit_mdocs_title = self.mdoc_title_led.text()
    else:
        style = style_view
        self.infos.edit_mdocs_title = ""

    self.mdoc_contents_pte.setStyleSheet(f"""
                                         background:transparent;
                                         {style}
                                         padding:5px;
                                         border:none;
                                         border-bottom:1px solid rgb(55,60,75);
                                         """)

    self.mdoc_edit_btn.setChecked(toggle)
    self.mdoc_title_led.setReadOnly(not toggle)
    self.mdoc_contents_pte.setReadOnly(not toggle)
    self.mdoc_save_btn.setEnabled(toggle)
    if toggle is False:
        load_contents(self)
    else:
        self.mdoc_contents_pte.setFocus()


def edit_btn_clicked(self):
    edit_mode = self.mdoc_edit_btn.isChecked()
    target_doc = self.mdoc_title_led.text()
    if edit_mode:
        ok = eApopup.confirm_big(text=f"{target_doc}\n\n편집할까요?")
        if not ok:
            self.mdoc_edit_btn.setChecked(False)
            return
    else:
        ok = eApopup.warning(text="저장하지 않고 편집을 취소할까요?")
        if not ok:
            self.mdoc_edit_btn.setChecked(True)
            return
    edit_mode_toggler(self, toggle=edit_mode)


# 편집한 문서 저장하기
def edit_doc(self):
    title_new = self.mdoc_title_led.text()
    contents_new = self.mdoc_contents_pte.toPlainText()
    target_title = self.infos.edit_mdocs_title
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()
    # 편집항목 DB내 UPDATE
    cur.execute(f"UPDATE MedDocs SET Title = '{title_new}', Contents = '{contents_new}' WHERE Title = '{target_title}'")
    # DB 저장 후 연결 해제.
    con.commit()
    con.close()

    edit_mode_toggler(self, False)
    load_contents(self)


#: Copy to Clipboard
def copy_doc(self):
    if not self.mdoc_lwg.currentItem():
        eApopup.notify(text="복사할 문서를 선택하세요.")
        return

    contents = self.mdoc_contents_pte.toPlainText()
    eAinput.copy_it(contents)
