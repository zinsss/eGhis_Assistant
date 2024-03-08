import requests
import sqlite3

from PySide6.QtCore import QTime

from eAmodules import eAlabeler


# DEFAULT_VALUES.
autobackup_time = QTime(19, 30, 00)
autostats_time = QTime(18, 30, 00)
autosync_time = QTime(13, 30, 00)


## General eGhis Assistant Settings

def connect_DB_and_load_settings(self):
    # Load DB
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()    
    # Create table if not exists
    con.execute(
        '''CREATE TABLE if not exists Settings(
        AutoBackup INTEGER,
        AutoBackupTime INTEGER,
        AutoShutdown INTEGER,
        AutoStats INTEGER,
        AutoStatsTime INTEGER,
        AutoSyncBackup INTEGER,
        AutoSyncBackupTime INTEGER,
        DiscordBot INTEGER,
        DiscordWebHook TEXT,
        VacAntiLogout INTEGER)
        '''
    )    
    settingsDB = list(cur.execute(f'SELECT * FROM Settings').fetchall()[0])
    con.close()
    
    self.stng_auto_backup_btn.setChecked(settingsDB[0])
    # self.parent.stng_auto_backup_btn.setChecked(settingsDB[0])
    self.stng_auto_backup_time.setText(str(settingsDB[1]))
    self.stng_auto_shutdown_btn.setChecked(settingsDB[2])
    # self.parent.stng_auto_shutdown_btn.setChecked(settingsDB[2])
    self.stng_auto_stats_btn.setChecked(settingsDB[3])
    # self.parent.stng_auto_stats_btn.setChecked(settingsDB[3])
    self.stng_auto_stats_time.setText(str(settingsDB[4]))
    self.stng_cloud_sync_btn.setChecked(settingsDB[5])
    # self.parent.stng_cloud_sync_btn.setChecked(settingsDB[5])
    self.stng_cloud_sync_time.setText(str(settingsDB[6]))
    self.stng_messenger_btn.setChecked(settingsDB[7])
    # self.parent.stng_messenger_btn.setChecked(settingsDB[7])
    self.stng_messenger_server_pte.setPlainText(settingsDB[8])
    self.stng_vac_sys_log_btn.setChecked(settingsDB[9])
    # self.parent.stng_vac_sys_log_btn.setChecked(settingsDB[9])
    
    global autobackup_time, autostats_time, autosync_time
    # Second까지 지정 안하는 경우 일분내내 반복 작업함.
    autobackup_time = QTime(int(self.stng_auto_backup_time.text()[:2]), int(self.stng_auto_backup_time.text()[2:]), 00)
    autostats_time = QTime(int(self.stng_auto_stats_time.text()[:2]), int(self.stng_auto_stats_time.text()[2:]), 00)
    autosync_time = QTime(int(self.stng_cloud_sync_time.text()[:2]), int(self.stng_cloud_sync_time.text()[2:]), 00)
    
    
def save_to_DB_and_reload(self):
    # DEFAULT SETTINGS
    settings = [
        1,
        '1900',
        1,
        1,
        '1830',
        1,
        '1330',
        1,
        "",
        1
    ]
    settings[0] = int(self.stng_auto_backup_btn.isChecked())
    settings[1] = self.stng_auto_backup_time.text()
    settings[2] = int(self.stng_auto_shutdown_btn.isChecked())
    settings[3] = int(self.stng_auto_stats_btn.isChecked())
    settings[4] = self.stng_auto_stats_time.text()
    settings[5] = int(self.stng_cloud_sync_btn.isChecked())
    settings[6] = self.stng_cloud_sync_time.text()
    settings[7] = int(self.stng_messenger_btn.isChecked())
    settings[8] = self.stng_messenger_server_pte.toPlainText()
    settings[9] = int(self.stng_vac_sys_log_btn.isChecked())

    # DB 연결해서.    
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()
    # DB내 기존 목록을 모두 지우고..
    con.execute('DELETE FROM Settings')
    cur.execute(f'INSERT INTO Settings VALUES {str(tuple(settings))}')
    # DB 저장 후 연결 해제.
    con.commit()
    con.close()
    
    connect_DB_and_load_settings(self)
    
    
## Labeler Settings

def connect_DB_and_load_lbler_settings(self):
    # Load DB
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()    
    # Create table if not exists
    con.execute(
        '''CREATE TABLE if not exists LblerSettings(
        AutoInput INTEGER,
        ChildFluLotChange INTEGER,
        ChildFluLot TEXT,
        NipFluProcess INTEGER,
        AllowFluOldEx INTEGER,
        FluOldStartDate75over INTEGER,
        FluOldStartDate7074 INTEGER,
        FluOldStartDate6569 INTEGER,
        FluOldEndDate INTEGER,
        FluOldAge75over INTEGER,
        FluOldAge7074From INTEGER,
        FluOldAge7074Until INTEGER,
        FluOldAge6569From INTEGER,
        FluOldAge6569Until INTEGER,
        FluChildTwiceStart INTEGER,
        FluChildTwiceEnd INTEGER,
        FluChildOnceStart INTEGER,
        FluChildOnceEnd INTEGER,
        FluChildAgeFrom INTEGER,
        FluChildAgeUntil INTEGER)
        '''
    )    
    lbler_settingsDB = list(cur.execute(f'SELECT * FROM LblerSettings').fetchall()[0])
    con.commit()
    con.close()
    
    self.stlb_auto_input_cbx.setChecked(lbler_settingsDB[0])
    self.stlb_auto_child_flu_lot_cbx.setChecked(lbler_settingsDB[1])
    self.stlb_child_flu_lot_led.setText(lbler_settingsDB[2])
    self.stlb_flu_auto_sort_cbx.setChecked(lbler_settingsDB[3])
    self.stlb_flu_allow_ex_cbx.setChecked(lbler_settingsDB[4])
    self.stlb_flu_old_over75_start_led.setText(str(lbler_settingsDB[5]))
    self.stlb_flu_old_7074_start_led.setText(str(lbler_settingsDB[6]))
    self.stlb_flu_old_6569_start_led.setText(str(lbler_settingsDB[7]))
    self.stlb_flu_old_end_led.setText(str(lbler_settingsDB[8]))
    self.stlb_flu_age_75over_led.setText(str(lbler_settingsDB[9]))
    self.stlb_flu_age_7074_led1.setText(str(lbler_settingsDB[10]))
    self.stlb_flu_age_7074_led2.setText(str(lbler_settingsDB[11]))
    self.stlb_flu_age_6569_led1.setText(str(lbler_settingsDB[12]))
    self.stlb_flu_age_6569_led2.setText(str(lbler_settingsDB[13]))
    self.stlb_flu_date_child_twice_led1.setText(str(lbler_settingsDB[14]))
    self.stlb_flu_date_child_twice_led2.setText(str(lbler_settingsDB[15]))
    self.stlb_flu_date_child_once_led1.setText(str(lbler_settingsDB[16]))
    self.stlb_flu_date_child_once_led2.setText(str(lbler_settingsDB[17]))
    self.stlb_flu_age_child_led1.setText(str(lbler_settingsDB[18]))
    self.stlb_flu_age_child_led2.setText(str(lbler_settingsDB[19]))
    
    
def save_lbler_settings_and_reload(self):
    lbler_settings = [
        1,
        1,
        "",
        1,
        1,
        20230101,
        20230101,
        20230101,
        20230101,
        20230101,
        20230101,
        20230101,
        20230101,
        20230101,
        20230101,
        20230101,
        20230101,
        20230101,
        20230101,
        20230101,
    ]
    lbler_settings[0] = int(self.stlb_auto_input_cbx.isChecked())
    lbler_settings[1] = int(self.stlb_auto_child_flu_lot_cbx.isChecked())
    lbler_settings[2] = self.stlb_child_flu_lot_led.text()
    lbler_settings[3] = int(self.stlb_flu_auto_sort_cbx.isChecked())
    lbler_settings[4] = int(self.stlb_flu_allow_ex_cbx.isChecked())
    lbler_settings[5] = int(self.stlb_flu_old_over75_start_led.text())
    lbler_settings[6] = int(self.stlb_flu_old_7074_start_led.text())
    lbler_settings[7] = int(self.stlb_flu_old_6569_start_led.text())
    lbler_settings[8] = int(self.stlb_flu_old_end_led.text())
    lbler_settings[9] = int(self.stlb_flu_age_75over_led.text())
    lbler_settings[10] = int(self.stlb_flu_age_7074_led1.text())
    lbler_settings[11] = int(self.stlb_flu_age_7074_led2.text())
    lbler_settings[12] = int(self.stlb_flu_age_6569_led1.text())
    lbler_settings[13] = int(self.stlb_flu_age_6569_led2.text())
    lbler_settings[14] = int(self.stlb_flu_date_child_twice_led1.text())
    lbler_settings[15] = int(self.stlb_flu_date_child_twice_led2.text())
    lbler_settings[16] = int(self.stlb_flu_date_child_once_led1.text())
    lbler_settings[17] = int(self.stlb_flu_date_child_once_led2.text())
    lbler_settings[18] = int(self.stlb_flu_age_child_led1.text())
    lbler_settings[19] = int(self.stlb_flu_age_child_led2.text())
    
    # DB 연결해서.    
    con = sqlite3.connect("./database/eGhisAssistant.db")
    cur = con.cursor()
    # DB내 기존 목록을 모두 지우고..
    con.execute('DELETE FROM LblerSettings')
    cur.execute(f'INSERT INTO LblerSettings VALUES {str(tuple(lbler_settings))}')
    # DB 저장 후 연결 해제.
    con.commit()
    con.close()
    
    connect_DB_and_load_lbler_settings(self)
    eAlabeler.load_FluSettings(self)
