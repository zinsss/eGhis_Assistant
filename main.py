import sys
# # * 이유는 공부해야함. coinit_flags=2없이는 clipboard copy()가 안됨
sys.coinit_flags = 2

# 위 코드 "sys.coinit_flags =2"시 발생하는 UserWarning 무시하기 위함.
import warnings
warnings.simplefilter("ignore", category=UserWarning)

from PySide6.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QTextEdit
from PySide6.QtCore import QCoreApplication, Qt, QFile, QDate, QTime, QThread, QObject, Signal, Slot, QFileSystemWatcher, QEventLoop, QTimer
from PySide6.QtGui import QClipboard
from PySide6 import QtGui, QtWidgets

import mainUI
from eAmodules import eAcalendar, eAreminders, eAsticky


## General Variables
class Infos():
    # 현재 날짜 및 시간. 여러군데서 씀.
    date_today = QDate.currentDate()
    time_now = QTime.currentTime()
    # Opened Reminder
    opened_reminder_text = ""
    # Opened Event
    opened_event = []
    # 현재 선택된 환자 이름 일시 저장. 매초 확인, 매초 환자 변경여부 확인 위해 사용.
    pt_name_now = ""
    # 오늘이 청구일인지 아닌지 설정해놓기.
    lpdom = False
    

## Main GUI Window
class MainWindow(QMainWindow, mainUI.Ui_Main):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        # Basic Instances to Load------------------------------------------------------------------#
        self.infos = Infos()
        # self.reminders_Rmenu = eAreminders.reminder_listwidget_Rmenu_create(self)
        
        # Collection of UI Updates-----------------------------------------------------------------#
        self.calendar_clock_lbl.setText(self.infos.time_now.toString("HH:mm"))
        eAsticky.load_sticky_notes(self)
    
        # Default StackWidgets on Startup----------------------------------------------------------#
        self.calendar_stack.setCurrentIndex(0)
        self.reminders_stack.setCurrentIndex(0)
        self.apps_buttons('apps_sticky_btn') # For styling of app_btns, call navigation method instead
        self.studies_stack.setCurrentIndex(0)
        self.settings_stack.setCurrentIndex(0)
                
        # Calendars--------------------------------------------------------------------------------#
        eAcalendar.calendar_update(self)
        self.calendar_wdg.selectionChanged.connect(lambda:eAcalendar.date_selected(self))
        self.calendar_wdg.currentPageChanged.connect(lambda:eAcalendar.calendar_update(self))
        self.calendar_prev_month_btn.clicked.connect(lambda:self.calendar_wdg.showPreviousMonth())
        self.calendar_today_btn.clicked.connect(lambda:eAcalendar.go_today(self))
        self.calendar_next_month_btn.clicked.connect(lambda:self.calendar_wdg.showNextMonth())
        self.calendar_yearly_btn.clicked.connect(lambda:eAcalendar.yearly_page_toggle(self))
        self.calendar_day_info_lwg.itemActivated.connect(lambda:eAcalendar.event_double_clicked(self))
        self.calendar_day_info_led.returnPressed.connect(lambda:eAcalendar.add_event_from_main(self))
        self.calendar_day_options_btn.clicked.connect(lambda:eAcalendar.options_btn_clicked(self))
        # Calendar OPT View
        eAcalendar.calendar_styling(self, 'calendar_opt_wdg')
        self.calendar_opt_prev_month_btn.clicked.connect(lambda:self.calendar_opt_wdg.showPreviousMonth())
        self.calendar_opt_today_btn.clicked.connect(lambda:self.calendar_opt_wdg.showToday())
        self.calendar_opt_next_month_btn.clicked.connect(lambda:self.calendar_opt_wdg.showNextMonth())
        self.calendar_opt_wdg.currentPageChanged.connect(lambda:eAcalendar.calendar_opt_page_changed(self))
        self.calendar_opt_wdg.clicked.connect(lambda:eAcalendar.cal_opt_clicked(self))
        self.calendar_event_delete_btn.clicked.connect(lambda:eAcalendar.delete_event(self))
        self.calendar_multi_day_cbx.stateChanged.connect(lambda:eAcalendar.multi_day_status_toggle(self))
        self.calendar_opt_close_btn.clicked.connect(lambda:self.calendar_stack.setCurrentIndex(0))
        self.calendar_opt_write_btn.clicked.connect(lambda:eAcalendar.write_btn_clicked(self))
        # Yearly View
        self.calendar_yearly_prev_btn.clicked.connect(lambda:eAcalendar.year_navigation_btn(self, prev = True))
        self.calendar_yearly_next_btn.clicked.connect(lambda:eAcalendar.year_navigation_btn(self))
        self.calendar_yearly_year_led.returnPressed.connect(lambda:eAcalendar.view_yearly(self))
        self.calendar_yearly_done_btn.clicked.connect(lambda:eAcalendar.yearly_page_toggle(self))
        
        # Reminders--------------------------------------------------------------------------------#
        #TODO history to active? what about recurring reminders?
        self.reminders_archive_btn.setEnabled(False)
        eAreminders.load_write_reminders(self)
        # Context Menu for each lists.
        self.reminders_lwg.setContextMenuPolicy(Qt.CustomContextMenu)
        self.reminders_lwg.customContextMenuRequested.connect(lambda:eAreminders.reminder_Rmenu(self, "reminders_lwg"))
        self.reminders_sublist_lwg.setContextMenuPolicy(Qt.CustomContextMenu)
        self.reminders_sublist_lwg.customContextMenuRequested.connect(lambda:eAreminders.reminder_Rmenu(self, "reminders_sublist_lwg"))
        # Archive Button (not part of reminders_stack)
        self.reminders_history_btn.clicked.connect(lambda:self.reminders_stack.setCurrentIndex(2))
        # Reminders Main
        self.reminders_lwg.itemActivated.connect(lambda:eAreminders.open_reminder_in_detail(self))
        self.reminders_lwg.model().rowsMoved.connect(lambda:self.reminders_lwg.setCurrentItem(None))
        self.reminders_todo_btn.clicked.connect(lambda:eAreminders.new_item_status_change(self, "reminder", "[ ]"))
        self.reminders_ugnt_btn.clicked.connect(lambda:eAreminders.new_item_status_change(self, "reminder", "[!]"))
        self.reminders_star_btn.clicked.connect(lambda:eAreminders.new_item_status_change(self, "reminder", "[*]"))
        self.reminders_prgs_btn.clicked.connect(lambda:eAreminders.new_item_status_change(self, "reminder", "[/]"))
        self.reminders_dlyd_btn.clicked.connect(lambda:eAreminders.new_item_status_change(self, "reminder", "[?]"))
        self.reminders_done_btn.clicked.connect(lambda:eAreminders.new_item_status_change(self, "reminder", "[x]"))
        self.reminders_canc_btn.clicked.connect(lambda:eAreminders.new_item_status_change(self, "reminder", "[-]"))
        self.reminders_archive_btn.clicked.connect(lambda:eAreminders.archive_reminders(self))
        self.reminders_new_led.returnPressed.connect(lambda:eAreminders.add_reminder(self))
        self.reminders_clear_btn.clicked.connect(lambda:eAreminders.clear_btn_clicked(self))
        # Reminders Detail/Sublist
        self.reminders_sublist_due_cbx.stateChanged.connect(lambda:eAreminders.due_date_cbx_toggle(self))
        self.reminders_sublist_reminder_delete_btn.clicked.connect(lambda:eAreminders.delete_reminder(self))
        self.reminders_sublist_rem_status_btn.clicked.connect(lambda:eAreminders.reminder_Rmenu(self))
        self.reminders_sublist_lwg.itemChanged.connect(lambda:eAreminders.sublist_edited(self))
        self.reminders_sublist_ugnt_btn.clicked.connect(lambda:eAreminders.new_item_status_change(self, "sublist", "[!]"))
        self.reminders_sublist_todo_btn.clicked.connect(lambda:eAreminders.new_item_status_change(self, "sublist", "[ ]"))
        self.reminders_sublist_star_btn.clicked.connect(lambda:eAreminders.new_item_status_change(self, "sublist", "[*]"))
        self.reminders_sublist_prgs_btn.clicked.connect(lambda:eAreminders.new_item_status_change(self, "sublist", "[/]"))
        self.reminders_sublist_dlyd_btn.clicked.connect(lambda:eAreminders.new_item_status_change(self, "sublist", "[?]"))
        self.reminders_sublist_done_btn.clicked.connect(lambda:eAreminders.new_item_status_change(self, "sublist", "[x]"))
        self.reminders_sublist_canc_btn.clicked.connect(lambda:eAreminders.new_item_status_change(self, "sublist", "[-]"))
        self.reminders_sublist_item_led.returnPressed.connect(lambda:eAreminders.add_sublist(self))
        self.reminders_sublist_clear_btn.clicked.connect(lambda:eAreminders.clear_btn_clicked(self))          
        self.reminders_sublist_close_btn.clicked.connect(lambda:eAreminders.sublist_close(self))
        self.reminders_sublist_write_btn.clicked.connect(lambda:eAreminders.reminder_detail_write(self))
        # Reminders Archive
        self.reminders_archive_done_btn.clicked.connect(lambda:self.reminders_stack.setCurrentIndex(0))
        self.reminders_archive_limit_cmb.currentIndexChanged.connect(lambda:eAreminders.show_reminder_history(self))
 
        
        # Macros-----------------------------------------------------------------------------------#
        
        
        # APPS-------------------------------------------------------------------------------------#
        # App_Stack Navigation
        self.apps_sticky_btn.clicked.connect(lambda:self.apps_buttons('apps_sticky_btn'))
        self.apps_quick_saves_btn.clicked.connect(lambda:self.apps_buttons('apps_quick_saves_btn'))
        self.apps_med_docs_btn.clicked.connect(lambda:self.apps_buttons('apps_med_docs_btn'))
        self.apps_studies_btn.clicked.connect(lambda:self.apps_buttons('apps_studies_btn'))
        self.apps_labeler_btn.clicked.connect(lambda:self.apps_buttons('apps_labeler_btn'))
        self.apps_covid_btn.clicked.connect(lambda:self.apps_buttons('apps_covid_btn'))
        self.apps_settings_btn.clicked.connect(lambda:self.apps_buttons('apps_settings_btn'))
        self.apps_about_btn.clicked.connect(lambda:self.apps_buttons('apps_about_btn'))
        
        # Sticky Notes
        self.sticky_note_0.clicked.connect(lambda:eAsticky.write_new(self, 'sticky_note_0'))
        self.sticky_note_1.clicked.connect(lambda:eAsticky.write_new(self, 'sticky_note_1'))
        self.sticky_note_2.clicked.connect(lambda:eAsticky.write_new(self, 'sticky_note_2'))
        self.sticky_note_3.clicked.connect(lambda:eAsticky.write_new(self, 'sticky_note_3'))
        self.sticky_note_4.clicked.connect(lambda:eAsticky.write_new(self, 'sticky_note_4'))
        self.sticky_note_5.clicked.connect(lambda:eAsticky.write_new(self, 'sticky_note_5'))
        
                
    #= App_Stack Navigation     
    def apps_buttons(self, app_btn:str):
        # 각 버튼 이름 저장해놓고.. 버튼 누르면 parameter로 버튼이름 받도록.
        app_btns = [
            'apps_sticky_btn',
            'apps_quick_saves_btn',
            'apps_med_docs_btn',
            'apps_studies_btn',
            'apps_labeler_btn',
            'apps_covid_btn',
            'apps_settings_btn',
            'apps_about_btn'
        ]
        # 현재 페이지 표식 위해 스타일 2가지.
        btn_style_current = "color:rgb(125,175,225);"
        btn_style_default = """
        QPushButton {
            color: rgb(165, 170, 180);
            border:none;
        }
        QPushButton:hover {    
            color:rgb(125,175,225);
        }
        QPushButton:pressed {
            color:rgb(75,75,90);
        }
        """
        # 받은 parameter가 잘못됬다면, 에러내지 말고 그냥 무시하자(일단은)
        if not app_btn in app_btns: return
        # 각 App page의 index는 위 리스트의 버튼 이름 인덱스와 동일하게 맞춰놓음. 
        index = app_btns.index(app_btn)
        self.apps_stack.setCurrentIndex(index)
        # 매 클릭시마다 현재 페이지는 스타일 다르게 설정하고, 나머지는 모두 default 스타일로 적용.
        for btn in app_btns:
            button = getattr(self, btn)
            if not btn == app_btn:
                button.setStyleSheet(btn_style_default)
            else: button.setStyleSheet(btn_style_current)

        
## Let's Roll
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # clipboard = app.clipboard()
    eA = MainWindow()
    eA.show()
    sys.exit(app.exec())