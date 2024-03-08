import sqlite3

def connect_DB():
    # Load DB
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()    
    # Create table if not exists 
    # 작업하기 편하도록 TODOs와 TODOsArchive의 index를 동일하게 맞추되, Archived date만 제일 뒤에 추가.
    con.execute('CREATE TABLE if not exists TODOs(Status TEXT, TODO TEXT, Color TEXT, Sublist TEXT, Done_Date TEXT)')
    con.execute('CREATE TABLE if not exists TODOsArchive(Status TEXT, TODO TEXT, Color TEXT, Sublist TEXT, Done_Date TEXT, Archived TEXT)')
    # Load Current Items
    todos = [list(item) for item in cur.execute('SELECT * FROM TODOs').fetchall()]
    # Close DB connection
    con.commit()
    con.close()

    return todos