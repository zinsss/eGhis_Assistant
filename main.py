import sys
# 이유는 공부해야함. coinit_flags=2없이는 clipboard copy()가 안됨
sys.coinit_flags = 2

import warnings
# 위 코드 "sys.coinit_flags =2"시 발생하는 UserWarning 무시하기 위함.
warnings.simplefilter("ignore", category=UserWarning)

from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QDate, QTime, QTimer
from PySide6.QtCore import Qt, QThread, QObject, Signal, Slot
import mainUI
from eAmodules import eAsticky, eAquicksaves, eAmdocs, eAstudies, eAlabeler
from eAmodules import eAcalendar, eAreminders, eAmacros
from eAmodules import eAsettings, eAwinauto, eAutils, eApopup, eAinput, eAstr


# General Variables
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
    # Editing MDOCS
    edit_mdocs_title = ""


# Separate Thread for Clock
class Scheduled(QThread):
    def __init__(self, parent):
        super(Scheduled, self).__init__()
        self.parent = parent
        self.parent.alarm.connect(self.check_for_alarm)

    @Slot()
    def check_for_alarm(self):
        auto_backup_time = self.parent.stgn_auto_backup_led.text()
        auto_stats_time = self.parent.stgn_auto_stats_led.text()
        scheduled_tasks = {
            auto_backup_time: [eAwinauto.close_eghis, self],
            auto_stats_time: [eAwinauto.start_stats, self],
            "15:01": [eAmacros.prev_pt]
        }
        time_of_clock = self.parent.clock_led.text()
        time_hour = time_of_clock[:2]
        time_minute = time_of_clock[3:]

        if time_of_clock in list(scheduled_tasks.keys()):
            job = scheduled_tasks[time_of_clock]
            return self.parent.start_worker(*job)
        elif (10 <= int(time_hour) <= 17) and (time_minute == "00"):
            self.start_worker(eAwinauto.vaccine_cont_all, self)
        else:
            return
        pass


# Background Worker
class Worker(QObject):
    finished = Signal()

    def __init__(self):
        super().__init__()

    @Slot()
    def start_working(self, method):
        method()
        self.finished.emit()


# Main GUI Window
class MainWindow(QMainWindow, mainUI.Ui_Main):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Basic Instances to Load---------------------------------------------#
        self.infos = Infos()
        # Load Settings First
        eAsettings.connect_DB_and_load_settings(self)
        eAsettings.connect_DB_and_load_lbler_settings(self)

        # Clock
        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self.update_clock)
        self.clock_timer.start(1000)
        self.update_clock()
        self.clock_led.textChanged.connect(self.scheduled_task)

        # Alarm (Scheduled Tasks)
        # Deselect and Reset Timer
        self.reset_timer = QTimer(self)
        self.reset_timer.timeout.connect(self.reset_widgets)
        self.reset_timer.setSingleShot(True)

        # Getting Threading (separate background worker) ready ---------------#
        self.worker = Worker()
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.worker.finished.connect(self.work_finished)
        # self.thread.started.connect(self.worker.start_working)

        # Collection of UI Updates--------------------------------------------#
        eAsticky.load_sticky_notes(self)

        # Default StackWidgets on Startup-------------------------------------#
        self.calendar_stack.setCurrentIndex(0)
        self.reminders_stack.setCurrentIndex(0)
        # For styling of app_btns, call navigation method instead
        self.apps_buttons('apps_sticky_btn')
        self.studies_stack.setCurrentIndex(0)
        self.settings_stack.setCurrentIndex(0)

        # Calendars-----------------------------------------------------------#
        eAcalendar.calendar_update(self)
        self.calendar_wdg.selectionChanged.connect(
            lambda: eAcalendar.date_selected(self))
        self.calendar_wdg.currentPageChanged.connect(
            lambda: eAcalendar.calendar_update(self))
        self.calendar_prev_month_btn.clicked.connect(
            lambda: self.calendar_wdg.showPreviousMonth())
        self.calendar_today_btn.clicked.connect(
            lambda: eAcalendar.go_today(self))
        self.calendar_next_month_btn.clicked.connect(
            lambda: self.calendar_wdg.showNextMonth())
        self.calendar_yearly_btn.clicked.connect(
            lambda: eAcalendar.yearly_page_toggle(self))
        self.calendar_day_info_lwg.itemActivated.connect(
            lambda: eAcalendar.event_double_clicked(self))
        self.calendar_day_info_led.returnPressed.connect(
            lambda: eAcalendar.add_event_from_main(self))
        self.calendar_day_options_btn.clicked.connect(
            lambda: eAcalendar.options_btn_clicked(self))
        # Calendar OPT View
        eAcalendar.calendar_styling(self, 'calendar_opt_wdg')
        self.calendar_opt_prev_month_btn.clicked.connect(
            lambda: self.calendar_opt_wdg.showPreviousMonth())
        self.calendar_opt_today_btn.clicked.connect(
            lambda: self.calendar_opt_wdg.showToday())
        self.calendar_opt_next_month_btn.clicked.connect(
            lambda: self.calendar_opt_wdg.showNextMonth())
        self.calendar_opt_wdg.currentPageChanged.connect(
            lambda: eAcalendar.calendar_opt_page_changed(self))
        self.calendar_opt_wdg.clicked.connect(
            lambda: eAcalendar.cal_opt_clicked(self))
        self.calendar_event_delete_btn.clicked.connect(
            lambda: eAcalendar.delete_event(self))
        self.calendar_multi_day_cbx.stateChanged.connect(
            lambda: eAcalendar.multi_day_status_toggle(self))
        self.calendar_opt_close_btn.clicked.connect(
            lambda: self.calendar_stack.setCurrentIndex(0))
        self.calendar_opt_write_btn.clicked.connect(
            lambda: eAcalendar.write_btn_clicked(self))
        # Yearly View
        self.calendar_yearly_prev_btn.clicked.connect(
            lambda: eAcalendar.year_navigation_btn(self, prev=True))
        self.calendar_yearly_next_btn.clicked.connect(
            lambda: eAcalendar.year_navigation_btn(self))
        self.calendar_yearly_year_led.returnPressed.connect(
            lambda: eAcalendar.view_yearly(self))
        self.calendar_yearly_done_btn.clicked.connect(
            lambda: eAcalendar.yearly_page_toggle(self))

        # Reminders-----------------------------------------------------------#
        # TODO history to active? what about recurring reminders?
        self.reminders_archive_btn.setEnabled(False)
        eAreminders.load_write_reminders(self)
        # Context Menu for each lists.
        self.reminders_lwg.setContextMenuPolicy(Qt.CustomContextMenu)
        self.reminders_lwg.customContextMenuRequested.connect(
            lambda: eAreminders.reminder_Rmenu(self, "reminders_lwg"))
        self.reminders_sublist_lwg.setContextMenuPolicy(Qt.CustomContextMenu)
        self.reminders_sublist_lwg.customContextMenuRequested.connect(
            lambda: eAreminders.reminder_Rmenu(self, "reminders_sublist_lwg"))
        # Archive Button (not part of reminders_stack)
        self.reminders_history_btn.clicked.connect(
            lambda: self.reminders_stack.setCurrentIndex(2))
        # Reminders Main
        self.reminders_lwg.itemActivated.connect(
            lambda: eAreminders.open_reminder_in_detail(self))
        self.reminders_lwg.model().rowsMoved.connect(
            lambda: self.reminders_lwg.setCurrentItem(None))
        self.reminders_todo_btn.clicked.connect(
            lambda: eAreminders.new_item_status_change(self, "rem", "[ ]"))
        self.reminders_ugnt_btn.clicked.connect(
            lambda: eAreminders.new_item_status_change(self, "rem", "[!]"))
        self.reminders_star_btn.clicked.connect(
            lambda: eAreminders.new_item_status_change(self, "rem", "[*]"))
        self.reminders_prgs_btn.clicked.connect(
            lambda: eAreminders.new_item_status_change(self, "rem", "[/]"))
        self.reminders_dlyd_btn.clicked.connect(
            lambda: eAreminders.new_item_status_change(self, "rem", "[?]"))
        self.reminders_done_btn.clicked.connect(
            lambda: eAreminders.new_item_status_change(self, "rem", "[x]"))
        self.reminders_canc_btn.clicked.connect(
            lambda: eAreminders.new_item_status_change(self, "rem", "[-]"))
        self.reminders_archive_btn.clicked.connect(
            lambda: eAreminders.archive_reminders(self))
        self.reminders_new_led.returnPressed.connect(
            lambda: eAreminders.add_reminder(self))
        self.reminders_clear_btn.clicked.connect(
            lambda: eAreminders.clear_btn_clicked(self))
        # Reminders Detail/Sublist
        self.reminders_sublist_due_cbx.stateChanged.connect(
            lambda: eAreminders.due_date_cbx_toggle(self))
        self.reminders_sublist_reminder_delete_btn.clicked.connect(
            lambda: eAreminders.delete_reminder(self))
        self.reminders_sublist_rem_status_btn.clicked.connect(
            lambda: eAreminders.reminder_Rmenu(self))
        self.reminders_sublist_lwg.itemChanged.connect(
            lambda: eAreminders.sublist_edited(self))
        self.reminders_sublist_ugnt_btn.clicked.connect(
            lambda: eAreminders.new_item_status_change(self, "sub", "[!]"))
        self.reminders_sublist_todo_btn.clicked.connect(
            lambda: eAreminders.new_item_status_change(self, "sub", "[ ]"))
        self.reminders_sublist_star_btn.clicked.connect(
            lambda: eAreminders.new_item_status_change(self, "sub", "[*]"))
        self.reminders_sublist_prgs_btn.clicked.connect(
            lambda: eAreminders.new_item_status_change(self, "sub", "[/]"))
        self.reminders_sublist_dlyd_btn.clicked.connect(
            lambda: eAreminders.new_item_status_change(self, "sub", "[?]"))
        self.reminders_sublist_done_btn.clicked.connect(
            lambda: eAreminders.new_item_status_change(self, "sub", "[x]"))
        self.reminders_sublist_canc_btn.clicked.connect(
            lambda: eAreminders.new_item_status_change(self, "sub", "[-]"))
        self.reminders_sublist_item_led.returnPressed.connect(
            lambda: eAreminders.add_sublist(self))
        self.reminders_sublist_clear_btn.clicked.connect(
            lambda: eAreminders.clear_btn_clicked(self))
        self.reminders_sublist_close_btn.clicked.connect(
            lambda: eAreminders.sublist_close(self))
        self.reminders_sublist_write_btn.clicked.connect(
            lambda: eAreminders.reminder_detail_write(self))
        # Reminders Archive
        self.reminders_archive_done_btn.clicked.connect(
            lambda: eAreminders.close_archive_page(self))
        self.reminders_archive_limit_cmb.currentIndexChanged.connect(
            lambda: eAreminders.show_reminder_history(self))

        # Macros--------------------------------------------------------------#
        # 진료관련
        self.macros_prev_pt_btn.clicked.connect(
            lambda: self.start_worker(eAmacros.prev_pt))
        self.macros_check_ins_btn.clicked.connect(
            lambda: self.start_worker(eAmacros.check_ins))
        self.macros_no_ins_btn.clicked.connect(
            lambda: self.start_worker(eAmacros.no_ins_choice, self))
        self.macros_next_pt_btn.clicked.connect(
            lambda: self.start_worker(eAmacros.next_pt))
        # 코멘트모음
        # self..clicked.connect(lambda:)
        self.macros_fluid_btn.clicked.connect(
            lambda: eAinput.sx_cnp(eAstr.FLUID_LST))
        # self.macros_phytx_btn.clicked.connect(
        #    lambda: eAmacros.physical_tx(self))
        self.macros_phytx_btn.clicked.connect(
            lambda: self.start_worker(eAmacros.physical_tx, self))
        self.macros_chr_btn.clicked.connect(
            lambda: eAinput.sx_cnp(eAstr.CHRMAN_LST))
        self.macros_chr_etc_btn.clicked.connect(
            lambda: eAmacros.chronic_management())
        self.macros_obsv_btn.clicked.connect(
            lambda: eAinput.sx_cnp(eAstr.REPEATS_LST))
        self.macros_lab_studies_btn.clicked.connect(
            lambda: eAmacros.lab_studies())
        self.macros_other_studies_btn.clicked.connect(
            lambda: eAmacros.workups())
        # self.macros_other_comments_btn.clicked.connect(lambda:)
        # 예방접종 관련
        self.macros_labeler_btn.clicked.connect(
            lambda: eAmacros.call_labeler(self))
        self.macros_vac_input_btn.clicked.connect(
            lambda: eAmacros.vac_sys_input(self))
        # self..clicked.connect(lambda:)
        self.macros_vac_log_btn.clicked.connect(
            lambda: eAwinauto.vaccine_cont_all(self))
        # 기타 Macro
        self.macros_flu_btn.clicked.connect(lambda: eAmacros.influenza(self))
        # self..clicked.connect(lambda:)
        # self..clicked.connect(lambda:)
        self.macros_reserve_3_btn.clicked.connect(
            lambda: eAutils.DBsyncDropBox(self))

        # APPS----------------------------------------------------------------#
        # App_Stack Navigation
        self.apps_sticky_btn.clicked.connect(
            lambda: self.apps_buttons('apps_sticky_btn'))
        self.apps_quick_saves_btn.clicked.connect(
            lambda: self.apps_buttons('apps_quick_saves_btn'))
        self.apps_med_docs_btn.clicked.connect(
            lambda: self.apps_buttons('apps_med_docs_btn'))
        self.apps_studies_btn.clicked.connect(
            lambda: self.apps_buttons('apps_studies_btn'))
        self.apps_labeler_btn.clicked.connect(
            lambda: self.apps_buttons('apps_labeler_btn'))
        self.apps_covid_btn.clicked.connect(
            lambda: self.apps_buttons('apps_covid_btn'))
        self.apps_settings_btn.clicked.connect(
            lambda: self.apps_buttons('apps_settings_btn'))
        self.apps_about_btn.clicked.connect(
            lambda: self.apps_buttons('apps_about_btn'))

        # Sticky Notes
        self.sticky_note_0.clicked.connect(
            lambda: eAsticky.write_new(self, 'sticky_note_0'))
        self.sticky_note_1.clicked.connect(
            lambda: eAsticky.write_new(self, 'sticky_note_1'))
        self.sticky_note_2.clicked.connect(
            lambda: eAsticky.write_new(self, 'sticky_note_2'))
        self.sticky_note_3.clicked.connect(
            lambda: eAsticky.write_new(self, 'sticky_note_3'))
        self.sticky_note_4.clicked.connect(
            lambda: eAsticky.write_new(self, 'sticky_note_4'))
        self.sticky_note_5.clicked.connect(
            lambda: eAsticky.write_new(self, 'sticky_note_5'))

        # Quick Saves
        eAquicksaves.write_GUI(self)
        self.qsv_lwg.itemActivated.connect(
            lambda: eAutils.lwg_copy_or_paste(self, "qsv_lwg", copy=True))
        self.qsv_lwg.model().rowsMoved.connect(
            lambda: eAquicksaves.save_DB(self))
        self.qsv_new_btn.clicked.connect(
            lambda: eAquicksaves.write_new(self))
        self.qsv_delete_btn.clicked.connect(
            lambda: eAquicksaves.delete_item(self))
        self.qsv_copypaste_btn.clicked.connect(
            lambda: eAutils.lwg_copy_or_paste(self, "qsv_lwg", copy=True))

        # Medical Documents
        eAmdocs.write_GUI(self)
        self.mdoc_lwg.itemClicked.connect(
            lambda: eAmdocs.load_contents(self))
        self.mdoc_lwg.itemDoubleClicked.connect(
            lambda: eAmdocs.copy_doc(self))
        self.mdoc_lwg.model().rowsMoved.connect(
            lambda: eAmdocs.order_change(self))
        self.mdoc_new_btn.clicked.connect(
            lambda: eAmdocs.add_new_doc(self))
        self.mdoc_edit_btn.clicked.connect(
            lambda: eAmdocs.edit_btn_clicked(self))
        self.mdoc_save_btn.clicked.connect(
            lambda: eAmdocs.edit_doc(self))
        self.mdoc_delete_btn.clicked.connect(
            lambda: eAmdocs.delete_doc(self))
        self.mdoc_copy_btn.clicked.connect(
            lambda: eAmdocs.copy_doc(self))

        # Studies
        eAstudies.reset(self, eAstudies.LAB_TARGETS)
        eAstudies.reset(self, eAstudies.BMD_TARGETS)
        eAstudies.reset(self, eAstudies.ALZ_TARGETS)
        eAstudies.reset(self, eAstudies.IPSS_TARGETS)
        self.studies_lab_btn.clicked.connect(
            lambda: self.studies_buttons('studies_lab_btn'))
        self.studies_bmd_btn.clicked.connect(
            lambda: self.studies_buttons('studies_bmd_btn'))
        self.studies_alz_btn.clicked.connect(
            lambda: self.studies_buttons('studies_alz_btn'))
        self.studies_ipss_btn.clicked.connect(
            lambda: self.studies_buttons('studies_ipss_btn'))
        self.lab_reset_btn.clicked.connect(
            lambda: eAstudies.reset(self, eAstudies.LAB_TARGETS))
        self.bmd_reset_btn.clicked.connect(
            lambda: eAstudies.reset(self, eAstudies.BMD_TARGETS))
        self.alz_reset_btn.clicked.connect(
            lambda: eAstudies.reset(self, eAstudies.ALZ_TARGETS))
        self.ipss_reset_btn.clicked.connect(
            lambda: eAstudies.reset(self, eAstudies.IPSS_TARGETS))
        self.lab_copy_btn.clicked.connect(
            lambda: eAstudies.lab_results_copy(self))
        self.bmd_copy_btn.clicked.connect(
            lambda: eAstudies.bmd_results_copy(self))
        self.alz_copy_btn.clicked.connect(
            lambda: eAstudies.alz_results_copy(self))
        self.ipss_copy_btn.clicked.connect(
            lambda: eAstudies.ipss_results_copy(self))

        # Labeller
        eAlabeler.prepare_labeler(self)
        # self.lblr_count_edit_btn.clicked.connect(lambda:eAlabeler.)
        self.lblr_get_data_btn.clicked.connect(
            lambda: eAlabeler.fetch_and_write_ptinfo(self))
        self.lblr_vaccines_cmb.currentIndexChanged.connect(
            lambda: eAlabeler.vac_combo_selected(self))
        self.lblr_reset_btn.clicked.connect(
            lambda: eAlabeler.reset_it(self))
        self.lblr_print_btn.clicked.connect(
            lambda: eAlabeler.print_save_it(self))
        # self..clicked.connect(lambda:eAlabeler.)
        # self..clicked.connect(lambda:eAlabeler.)
        # self..clicked.connect(lambda:eAlabeler.)
        # self..clicked.connect(lambda:eAlabeler.)
        # self..clicked.connect(lambda:eAlabeler.)
        # self..clicked.connect(lambda:eAlabeler.)

        # Settings
        self.settings_buttons('settings_gen_btn')
        self.settings_gen_btn.clicked.connect(
            lambda: self.settings_buttons('settings_gen_btn'))
        self.settings_lblr_btn.clicked.connect(
            lambda: self.settings_buttons('settings_lblr_btn'))
        # General Settings
        self.stgn_reset_btn.clicked.connect(
            lambda: eAsettings.connect_DB_and_load_lbler_settings(self))
        self.stgn_save_btn.clicked.connect(
            lambda: eAsettings.save_to_DB_and_reload(self))
        # Labeler Settings
        self.stlb_reset_btn.clicked.connect(
            lambda: eAsettings.connect_DB_and_load_lbler_settings(self))
        self.stlb_save_btn.clicked.connect(
            lambda: eAsettings.save_lbler_settings_and_reload(self))

        # ETC
        self.reset_all_btn.clicked.connect(
            lambda: self.reset_widgets())
        # --------------------------------------------------------------------#

    # Clock Updater

    def update_clock(self):
        time_now = QTime.currentTime()
        self.clock_led.setText(time_now.toString('HH:mm'))
        self.pt_alert_checker()

    # Let's Reset Selections of Listwidgets and App Stack after 30 sec?
    def reset_timer_start(self):
        self.reset_timer.start(30000)

    # Working and Planning feature to Reset all selections and stackwidgets to
    # default on certain given time period.
    def reset_widgets(self):
        ok = eApopup.timed_confirm(
            text="GUI 내 Selection을 초기화 합니다.",
            msec=3000
        )
        if not ok:
            return
        else:
            self.calendar_wdg.setSelectedDate(self.infos.date_today)
            self.calendar_day_info_lwg.clearSelection()
            self.calendar_yearly_lwg.clearSelection()
            self.reminders_lwg.clearSelection()
            self.reminders_archive_lwg.clearSelection()
            self.qsv_lwg.clearSelection()
            self.mdoc_lwg.clearSelection()
            self.apps_buttons('apps_sticky_btn')

    # Call Scheduled Tasks at Given Time.
    # Will be called every minute when Clock(lineedit) textChanged.
    def scheduled_task(self):
        scheduled_tasks = {
            self.stgn_auto_backup_led.text(): [eAwinauto.close_eghis, self],
            self.stgn_auto_stats_led.text(): [eAwinauto.start_stats, self],
            self.stgn_cloud_sync_led.text(): [eAutils.DBsyncDropBox, self],
            "18:00": [eAutils.daily_report_discord, self]}
        time_of_clock = self.clock_led.text()
        time_hour = time_of_clock[:2]
        time_minute = time_of_clock[3:]

        if time_of_clock in list(scheduled_tasks.keys()):
            job = scheduled_tasks[time_of_clock]
            return self.start_worker(*job)
        elif (10 <= int(time_hour) <= 17) and (time_minute == "00"):
            self.start_worker(eAwinauto.vaccine_cont_all, self)
        else:
            return

    # = Run Worker with Method as Parameter
    def start_worker(self, method, *args, **kwargs):
        self.thread.start()
        # Create a partial function with the given args and kwargs.
        partial_func = partial(method, *args, **kwargs)
        # Start the worker with the partial function
        self.worker.start_working(partial_func)

    @Slot()
    def work_finished(self):
        self.thread.quit()
        self.thread.wait()
        print("Worker Finished.. Waiting For Next Job.")

    # Patient Alerts
    # Check if '***' is in patient memo of eGhis. And call for alert on/off.
    def pt_alert_checker(self):
        pt_memo = eAwinauto.get_pt_memo()
        if pt_memo is None or pt_memo == "" or "***" not in pt_memo:
            self.pt_alert_toggle(alert=False)
        else:
            self.pt_alert_toggle(alert=True)

    # Toggle on an off
    def pt_alert_toggle(self, alert: bool):
        STYLE_NORMAL = """
        color: rgb(225, 215, 125);
        background-color: rgb(55, 60, 75);
        border: 2px solid rgb(40, 45, 55);
        border-top-right-radius:10px;
        border-bottom-left-radius:10px;
        """
        STYLE_ALERT = """
        color: rgb(225, 215, 125);
        background-color: rgb(150, 75, 100);
        border: 2px solid rgb(40, 45, 55);
        border-top-right-radius:10px;
        border-bottom-left-radius:10px;
        """
        if alert:
            self.clock_led.setStyleSheet(STYLE_ALERT)
        else:
            self.clock_led.setStyleSheet(STYLE_NORMAL)

    # = StackWidget Navigation
    # - App Stack
    def apps_buttons(self, app_btn: str = None):
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
        btn_style_current = """
        QPushButton {
            color:rgb(125,175,225);
            border:none;
        }
        QPushButton:pressed {
            color:rgb(125,175,225);
        }
        """
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
        if app_btn not in app_btns:
            return
        # 각 App page의 index는 위 리스트의 버튼 이름 인덱스와 동일
        index = app_btns.index(app_btn)
        self.apps_stack.setCurrentIndex(index)
        # 매 클릭시마다 현재 페이지는 스타일 다르게 설정하고,
        # 나머지는 모두 default 스타일로 적용.
        for btn in app_btns:
            button = getattr(self, btn)
            if not btn == app_btn:
                button.setStyleSheet(btn_style_default)
            else:
                button.setStyleSheet(btn_style_current)

    # - Studies Stack
    def studies_buttons(self, studies_btn: str):
        studies_btns = ['studies_lab_btn', 'studies_bmd_btn',
                        'studies_alz_btn', 'studies_ipss_btn']
        btn_style_current = """
        QPushButton {
            color:rgb(230,220,144);
            border:none;
        }
        QPushButton:pressed {
            color:rgb(230,220,144);
        }
        """
        btn_style_default = """
        QPushButton {
            color: rgb(165, 170, 180);
            border:none;
        }
        QPushButton:hover {
            color:rgb(230,220,144);
        }
        QPushButton:pressed {
            color:rgb(75,85,100);
        }
        """
        # 각 App page의 index는 위 리스트의 버튼 이름 인덱스와 동일
        index = studies_btns.index(studies_btn)
        self.studies_stack.setCurrentIndex(index)
        # 매 클릭시마다 현재 페이지는 스타일 다르게 설정하고,
        # 나머지는 모두 default 스타일로 적용.
        for btn in studies_btns:
            button = getattr(self, btn)
            if not btn == studies_btn:
                button.setStyleSheet(btn_style_default)
            else:
                button.setStyleSheet(btn_style_current)

    # - Settings Stack
    def settings_buttons(self, setting_btn: str):
        setting_btns = ['settings_gen_btn', 'settings_lblr_btn']
        btn_style_current = """
        QPushButton {
            color:rgb(230,220,144);
            border:none;
        }
        QPushButton:pressed {
            color:rgb(230,220,144);
        }
        """
        btn_style_default = """
        QPushButton {
            color: rgb(165, 170, 180);
            border:none;
        }
        QPushButton:hover {
            color:rgb(230,220,144);
        }
        QPushButton:pressed {
            color:rgb(75,85,100);
        }
        """
        # 각 App page의 index는 위 리스트의 버튼 이름 인덱스와 동일
        index = setting_btns.index(setting_btn)
        self.settings_stack.setCurrentIndex(index)
        # 매 클릭시마다 현재 페이지는 스타일 다르게 설정하고,
        # 나머지는 모두 default 스타일로 적용.
        for btn in setting_btns:
            button = getattr(self, btn)
            if not btn == setting_btn:
                button.setStyleSheet(btn_style_default)
            else:
                button.setStyleSheet(btn_style_current)


# Let's Roll
if __name__ == "__main__":
    app = QApplication(sys.argv)
    clipboard = app.clipboard()
    eA = MainWindow()
    eA.show()
    sys.exit(app.exec())
