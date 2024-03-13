import sqlite3
from eAmodules import eApopup


def connect_DB():
    # Load DB
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()    
    # Create table if not exists
    con.execute('CREATE TABLE if not exists StickyNotes(Sticky0 TEXT, Sticky1 TEXT, Sticky2 TEXT, Sticky3 TEXT, Sticky4 TEXT, Sticky5 TEXT)')
    # Load Current Items
    try:
        sticky_notes = list(cur.execute('SELECT * FROM StickyNotes').fetchone())
    except TypeError:
        sticky_notes = ["","","","","",""]
    # Close DB connection
    con.commit()
    con.close()

    return sticky_notes


def write_all_to_gui(self, sticky_notes:list):
    for sticky_note in sticky_notes:
        note_numb = sticky_notes.index(sticky_note)
        target_note = getattr(self, f'sticky_note_{str(note_numb)}')
        target_note.setText(sticky_note)


def load_sticky_notes(self):
    sticky_notes = connect_DB()
    write_all_to_gui(self, sticky_notes)


def write_new(self, sticky_note_btn:str):
    # Get target Note Button as attribute.
    target_note = getattr(self, sticky_note_btn)
    # Check if Note is empty. If not, confirm before proceding.
    if target_note.text() != "":
        yes = eApopup.warning(text = "Sticky Note의 내용을 변경할까요?", yes_no = True)
        if not yes: return
    # Get New Note from User Input. If empty, make it "". Or None will be written.    
    note_text = eApopup.get_multiline_text(
        title = "# Sticky Note의 내용을 입력하세요.",
        default_text = f'{target_note.text()}'
    )
    if note_text == None:
        note_text = f'{target_note.text()}'
    # Save text in gui.        
    target_note.setText(note_text)
    # Load DB
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()    
    # Save to DB
    cur.execute(f'UPDATE StickyNotes SET Sticky{sticky_note_btn[-1]} = "{note_text}"')    
    # Close DB connection
    con.commit()
    con.close()


    