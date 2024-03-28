# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QCalendarWidget,
    QCheckBox, QComboBox, QDateEdit, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QStackedWidget, QTextEdit, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(590, 2080)
        font = QFont()
        font.setFamilies([u"D2Coding"])
        font.setPointSize(12)
        Main.setFont(font)
        Main.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(50, 55, 70);	\n"
"	color: rgb(180, 185, 194);\n"
"}\n"
"QGroupBox{	\n"
"	background-color: rgb(40, 45, 55);\n"
"	border:1px solid rgb(55, 60, 70);\n"
"	border-radius:10px;\n"
"}\n"
"QStackedWidget{\n"
"	background:transparent;\n"
"}\n"
"QListWidget{\n"
"	background:transparent;\n"
"	alternate-background-color: rgb(43, 48, 60);\n"
"	border:0px;\n"
"	color: rgb(166,177,199);\n"
"	outline:0px;\n"
"}\n"
"QListWidget::item:hover{\n"
"    background-color: rgb(48, 52, 66);\n"
"}\n"
"QListWidget::item:selected{\n"
"    background-color: rgb(52, 57, 75);\n"
"}\n"
"QLabel{\n"
"	background:transparent;\n"
"}\n"
"QPushButton{\n"
"	background:transparent;\n"
"}\n"
"QCheckBox {\n"
"	padding-left:5px;\n"
"	color: rgb(66, 77, 100);\n"
"	background:none;\n"
"}\n"
"QCheckBox:checked {\n"
"	color: rgb(188, 199, 233);\n"
"}\n"
"QCheckBox::indicator {\n"
"	background-color:  rgb(45, 50, 60);\n"
"	border-radius:3px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"	background-color: rgb(70, 85, 120)"
                        ";\n"
"	border:1px solid rgb(50,60,80);\n"
"}\n"
"QDateEdit{\n"
"	color: rgb(188, 199, 233);\n"
"}\n"
"QDateEdit:disabled{\n"
"	color: rgb(66, 77, 100);\n"
"}\n"
"/* VERTICAL SCROLLBAR */\n"
"QScrollBar:vertical {\n"
"    width: 12px;\n"
"    margin: 20px 0px 20px 0px;\n"
"	border-radius: 6px;\n"
"}\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(55, 60, 80);\n"
"	min-height:30px;\n"
"	border-radius: 5px;\n"
"	border:none;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(60, 65, 85);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(50, 55, 75);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	margin-top:3px;\n"
"	background-color: rgb(60, 65, 85);\n"
"	height: 12px;\n"
"	border-radius: 6px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: rgb(65, 70, 90);\n"
"}\n"
"QScrollBar::sub-line:vertical:press"
                        "ed {	\n"
"	background-color: rgb(55, 60, 80);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	margin-bottom:3px;\n"
"	background-color: rgb(60, 65, 85);\n"
"	height: 12px;\n"
"	border-radius: 6px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: rgb(65, 70, 90);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(55, 60, 80);\n"
"}\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background:none;\n"
"}")
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.today_gbx = QGroupBox(self.centralwidget)
        self.today_gbx.setObjectName(u"today_gbx")
        self.today_gbx.setGeometry(QRect(20, 20, 550, 261))
        font1 = QFont()
        font1.setFamilies([u"\uc11c\uc6b8\ub0a8\uc0b0 \uc7a5\uccb4 B"])
        font1.setPointSize(14)
        self.today_gbx.setFont(font1)
        self.today_gbx.setStyleSheet(u"QWidget{	\n"
"	background-color: rgb(40, 45, 55);\n"
"	alternate-background-color: rgb(40, 45, 55);\n"
"	selection-background-color: rgb(40, 45, 55);\n"
"	selection-color: rgb(235, 200, 140);\n"
"}")
        self.calendar_stack = QStackedWidget(self.today_gbx)
        self.calendar_stack.setObjectName(u"calendar_stack")
        self.calendar_stack.setGeometry(QRect(10, 10, 531, 241))
        self.calendar_main = QWidget()
        self.calendar_main.setObjectName(u"calendar_main")
        self.calendar_day_year_lbl = QLabel(self.calendar_main)
        self.calendar_day_year_lbl.setObjectName(u"calendar_day_year_lbl")
        self.calendar_day_year_lbl.setGeometry(QRect(10, 30, 61, 20))
        font2 = QFont()
        font2.setFamilies([u"Lucida Sans"])
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(True)
        self.calendar_day_year_lbl.setFont(font2)
        self.calendar_day_year_lbl.setStyleSheet(u"color: rgb(94, 129, 172);")
        self.calendar_next_month_btn = QPushButton(self.calendar_main)
        self.calendar_next_month_btn.setObjectName(u"calendar_next_month_btn")
        self.calendar_next_month_btn.setGeometry(QRect(150, 30, 30, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendar_next_month_btn.sizePolicy().hasHeightForWidth())
        self.calendar_next_month_btn.setSizePolicy(sizePolicy)
        self.calendar_next_month_btn.setMinimumSize(QSize(0, 0))
        self.calendar_next_month_btn.setMaximumSize(QSize(31, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Lucida Sans"])
        font3.setPointSize(11)
        self.calendar_next_month_btn.setFont(font3)
        self.calendar_next_month_btn.setStyleSheet(u"color: rgb(150, 175, 200);")
        self.calendar_next_month_btn.setAutoDefault(True)
        self.calendar_next_month_btn.setFlat(True)
        self.calendar_day_info_lwg = QListWidget(self.calendar_main)
        self.calendar_day_info_lwg.setObjectName(u"calendar_day_info_lwg")
        self.calendar_day_info_lwg.setGeometry(QRect(260, 59, 261, 151))
        self.calendar_day_info_lwg.setFont(font1)
        self.calendar_day_info_lwg.setStyleSheet(u"border-top:1px solid rgb(60,65,80);\n"
"padding-top:10px;\n"
"padding-left:5px;")
        self.calendar_yearly_btn = QPushButton(self.calendar_main)
        self.calendar_yearly_btn.setObjectName(u"calendar_yearly_btn")
        self.calendar_yearly_btn.setGeometry(QRect(189, 30, 41, 20))
        sizePolicy.setHeightForWidth(self.calendar_yearly_btn.sizePolicy().hasHeightForWidth())
        self.calendar_yearly_btn.setSizePolicy(sizePolicy)
        self.calendar_yearly_btn.setMinimumSize(QSize(0, 20))
        self.calendar_yearly_btn.setMaximumSize(QSize(16777215, 20))
        font4 = QFont()
        font4.setFamilies([u"Lucida Sans"])
        font4.setPointSize(10)
        font4.setItalic(True)
        self.calendar_yearly_btn.setFont(font4)
        self.calendar_yearly_btn.setStyleSheet(u"color: rgb(200, 211, 222);")
        self.calendar_yearly_btn.setAutoDefault(True)
        self.calendar_yearly_btn.setFlat(True)
        self.calendar_wdg = QCalendarWidget(self.calendar_main)
        self.calendar_wdg.setObjectName(u"calendar_wdg")
        self.calendar_wdg.setGeometry(QRect(1, 50, 241, 181))
        sizePolicy.setHeightForWidth(self.calendar_wdg.sizePolicy().hasHeightForWidth())
        self.calendar_wdg.setSizePolicy(sizePolicy)
        font5 = QFont()
        font5.setFamilies([u"\uc11c\uc6b8\ub0a8\uc0b0 \uc7a5\uccb4 M"])
        font5.setPointSize(12)
        self.calendar_wdg.setFont(font5)
        self.calendar_wdg.setFocusPolicy(Qt.NoFocus)
        self.calendar_wdg.setStyleSheet(u"QCalendarWidget QCalendarView{\n"
"	color: rgb(70, 70, 90);\n"
"	selection-color: rgb(235, 200, 140);\n"
"	background-color: rgb(40, 45, 55);\n"
"	selection-background-color: rgb(40, 45, 55);\n"
"	alternate-background-color: rgb(40, 45, 55);\n"
"	border:none;\n"
"	outline:0px;\n"
"}\n"
"QCalendarWidget QTableView{\n"
"	border:0px;\n"
"	outline:0px;\n"
"}")
        self.calendar_wdg.setGridVisible(False)
        self.calendar_wdg.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        self.calendar_wdg.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendar_wdg.setNavigationBarVisible(False)
        self.calendar_day_options_btn = QPushButton(self.calendar_main)
        self.calendar_day_options_btn.setObjectName(u"calendar_day_options_btn")
        self.calendar_day_options_btn.setGeometry(QRect(459, 210, 61, 30))
        sizePolicy.setHeightForWidth(self.calendar_day_options_btn.sizePolicy().hasHeightForWidth())
        self.calendar_day_options_btn.setSizePolicy(sizePolicy)
        self.calendar_day_options_btn.setMinimumSize(QSize(30, 20))
        self.calendar_day_options_btn.setMaximumSize(QSize(80, 16777215))
        font6 = QFont()
        font6.setFamilies([u"Lucida Sans"])
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setItalic(True)
        self.calendar_day_options_btn.setFont(font6)
        self.calendar_day_options_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:rgb(42,48,58);\n"
"	color: rgb(177, 188, 211);\n"
"	border:none;\n"
"	border-radius:none;\n"
"	border-top:1px solid rgb(50,55,70);\n"
"	border-bottom:1px solid rgb(50,55,70);\n"
"}")
        self.calendar_day_options_btn.setAutoDefault(True)
        self.calendar_day_options_btn.setFlat(True)
        self.calendar_day_month_lbl = QPushButton(self.calendar_main)
        self.calendar_day_month_lbl.setObjectName(u"calendar_day_month_lbl")
        self.calendar_day_month_lbl.setGeometry(QRect(0, 0, 161, 31))
        sizePolicy.setHeightForWidth(self.calendar_day_month_lbl.sizePolicy().hasHeightForWidth())
        self.calendar_day_month_lbl.setSizePolicy(sizePolicy)
        self.calendar_day_month_lbl.setMinimumSize(QSize(0, 30))
        self.calendar_day_month_lbl.setMaximumSize(QSize(16777215, 16777215))
        font7 = QFont()
        font7.setFamilies([u"Lucida Sans"])
        font7.setPointSize(16)
        font7.setBold(True)
        font7.setItalic(True)
        self.calendar_day_month_lbl.setFont(font7)
        self.calendar_day_month_lbl.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(143, 188, 187);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}")
        self.calendar_day_month_lbl.setAutoDefault(True)
        self.calendar_day_month_lbl.setFlat(True)
        self.calendar_day_name_lbl = QLabel(self.calendar_main)
        self.calendar_day_name_lbl.setObjectName(u"calendar_day_name_lbl")
        self.calendar_day_name_lbl.setGeometry(QRect(260, 3, 101, 31))
        font8 = QFont()
        font8.setFamilies([u"Lucida Sans"])
        font8.setPointSize(12)
        font8.setBold(True)
        self.calendar_day_name_lbl.setFont(font8)
        self.calendar_day_name_lbl.setStyleSheet(u"color: rgb(180, 185, 194);\n"
"background:transparent;")
        self.calendar_prev_month_btn = QPushButton(self.calendar_main)
        self.calendar_prev_month_btn.setObjectName(u"calendar_prev_month_btn")
        self.calendar_prev_month_btn.setGeometry(QRect(80, 30, 30, 20))
        sizePolicy.setHeightForWidth(self.calendar_prev_month_btn.sizePolicy().hasHeightForWidth())
        self.calendar_prev_month_btn.setSizePolicy(sizePolicy)
        self.calendar_prev_month_btn.setMinimumSize(QSize(0, 20))
        self.calendar_prev_month_btn.setMaximumSize(QSize(30, 20))
        self.calendar_prev_month_btn.setFont(font3)
        self.calendar_prev_month_btn.setStyleSheet(u"color: rgb(150, 175, 200);")
        self.calendar_prev_month_btn.setAutoDefault(True)
        self.calendar_prev_month_btn.setFlat(True)
        self.calendar_today_btn = QPushButton(self.calendar_main)
        self.calendar_today_btn.setObjectName(u"calendar_today_btn")
        self.calendar_today_btn.setGeometry(QRect(110, 30, 40, 20))
        sizePolicy.setHeightForWidth(self.calendar_today_btn.sizePolicy().hasHeightForWidth())
        self.calendar_today_btn.setSizePolicy(sizePolicy)
        self.calendar_today_btn.setMinimumSize(QSize(0, 20))
        self.calendar_today_btn.setMaximumSize(QSize(16777215, 20))
        self.calendar_today_btn.setFont(font4)
        self.calendar_today_btn.setStyleSheet(u"color: rgb(150, 175, 200);")
        self.calendar_today_btn.setAutoDefault(True)
        self.calendar_today_btn.setFlat(True)
        self.calendar_day_info_led = QLineEdit(self.calendar_main)
        self.calendar_day_info_led.setObjectName(u"calendar_day_info_led")
        self.calendar_day_info_led.setGeometry(QRect(260, 210, 201, 30))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.calendar_day_info_led.sizePolicy().hasHeightForWidth())
        self.calendar_day_info_led.setSizePolicy(sizePolicy1)
        self.calendar_day_info_led.setMinimumSize(QSize(0, 30))
        self.calendar_day_info_led.setMaximumSize(QSize(16777215, 30))
        font9 = QFont()
        font9.setFamilies([u"\uc11c\uc6b8\ub0a8\uc0b0 \uc7a5\uccb4 B"])
        font9.setPointSize(11)
        self.calendar_day_info_led.setFont(font9)
        self.calendar_day_info_led.setStyleSheet(u"background-color:rgb(42,48,58);\n"
"padding-left: 3px;\n"
"color: rgb(166,177,199);\n"
"color: rgb(80,85,100);\n"
"border:none;\n"
"border-radius:none;\n"
"border-top:1px solid rgb(50,55,70);\n"
"border-bottom:1px solid rgb(50,55,70);")
        self.calendar_day_info_led.setFrame(False)
        self.calendar_day_date_lbl = QLabel(self.calendar_main)
        self.calendar_day_date_lbl.setObjectName(u"calendar_day_date_lbl")
        self.calendar_day_date_lbl.setGeometry(QRect(260, 28, 41, 31))
        font10 = QFont()
        font10.setFamilies([u"\uc11c\uc6b8\ub0a8\uc0b0\uccb4 EB"])
        font10.setPointSize(22)
        self.calendar_day_date_lbl.setFont(font10)
        self.calendar_day_date_lbl.setFocusPolicy(Qt.NoFocus)
        self.calendar_day_date_lbl.setStyleSheet(u"color: rgb(216, 222, 233);")
        self.calendar_day_date_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.calednar_day_mont_year_lbl = QLabel(self.calendar_main)
        self.calednar_day_mont_year_lbl.setObjectName(u"calednar_day_mont_year_lbl")
        self.calednar_day_mont_year_lbl.setGeometry(QRect(310, 30, 131, 31))
        font11 = QFont()
        font11.setFamilies([u"Lucida Sans"])
        font11.setPointSize(11)
        font11.setItalic(True)
        self.calednar_day_mont_year_lbl.setFont(font11)
        self.calednar_day_mont_year_lbl.setStyleSheet(u"color: rgb(180, 185, 194);\n"
"background:transparent;")
        self.calendar_stack.addWidget(self.calendar_main)
        self.calendar_day_info_lwg.raise_()
        self.calendar_day_year_lbl.raise_()
        self.calendar_next_month_btn.raise_()
        self.calendar_yearly_btn.raise_()
        self.calendar_wdg.raise_()
        self.calendar_day_options_btn.raise_()
        self.calendar_day_month_lbl.raise_()
        self.calendar_day_name_lbl.raise_()
        self.calendar_prev_month_btn.raise_()
        self.calendar_today_btn.raise_()
        self.calendar_day_info_led.raise_()
        self.calendar_day_date_lbl.raise_()
        self.calednar_day_mont_year_lbl.raise_()
        self.calendar_opt = QWidget()
        self.calendar_opt.setObjectName(u"calendar_opt")
        self.calendar_opt_title = QPushButton(self.calendar_opt)
        self.calendar_opt_title.setObjectName(u"calendar_opt_title")
        self.calendar_opt_title.setGeometry(QRect(0, 0, 221, 31))
        sizePolicy.setHeightForWidth(self.calendar_opt_title.sizePolicy().hasHeightForWidth())
        self.calendar_opt_title.setSizePolicy(sizePolicy)
        self.calendar_opt_title.setMinimumSize(QSize(0, 30))
        self.calendar_opt_title.setMaximumSize(QSize(16777215, 16777215))
        self.calendar_opt_title.setFont(font7)
        self.calendar_opt_title.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(143, 188, 187);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}")
        self.calendar_opt_title.setAutoDefault(True)
        self.calendar_opt_title.setFlat(True)
        self.calendar_opt_prev_month_btn = QPushButton(self.calendar_opt)
        self.calendar_opt_prev_month_btn.setObjectName(u"calendar_opt_prev_month_btn")
        self.calendar_opt_prev_month_btn.setGeometry(QRect(140, 30, 30, 20))
        sizePolicy.setHeightForWidth(self.calendar_opt_prev_month_btn.sizePolicy().hasHeightForWidth())
        self.calendar_opt_prev_month_btn.setSizePolicy(sizePolicy)
        self.calendar_opt_prev_month_btn.setMinimumSize(QSize(0, 20))
        self.calendar_opt_prev_month_btn.setMaximumSize(QSize(30, 20))
        font12 = QFont()
        font12.setFamilies([u"Lucida Sans"])
        font12.setPointSize(10)
        self.calendar_opt_prev_month_btn.setFont(font12)
        self.calendar_opt_prev_month_btn.setStyleSheet(u"color: rgb(150, 175, 200);")
        self.calendar_opt_prev_month_btn.setAutoDefault(True)
        self.calendar_opt_prev_month_btn.setFlat(True)
        self.calendar_opt_month_year_lbl = QLabel(self.calendar_opt)
        self.calendar_opt_month_year_lbl.setObjectName(u"calendar_opt_month_year_lbl")
        self.calendar_opt_month_year_lbl.setGeometry(QRect(10, 30, 81, 20))
        self.calendar_opt_month_year_lbl.setFont(font2)
        self.calendar_opt_month_year_lbl.setStyleSheet(u"color: rgb(94, 129, 172);")
        self.calendar_opt_today_btn = QPushButton(self.calendar_opt)
        self.calendar_opt_today_btn.setObjectName(u"calendar_opt_today_btn")
        self.calendar_opt_today_btn.setGeometry(QRect(170, 30, 40, 20))
        sizePolicy.setHeightForWidth(self.calendar_opt_today_btn.sizePolicy().hasHeightForWidth())
        self.calendar_opt_today_btn.setSizePolicy(sizePolicy)
        self.calendar_opt_today_btn.setMinimumSize(QSize(0, 20))
        self.calendar_opt_today_btn.setMaximumSize(QSize(16777215, 20))
        font13 = QFont()
        font13.setFamilies([u"D2Coding"])
        font13.setPointSize(10)
        self.calendar_opt_today_btn.setFont(font13)
        self.calendar_opt_today_btn.setStyleSheet(u"color: rgb(150, 175, 200);")
        self.calendar_opt_today_btn.setAutoDefault(True)
        self.calendar_opt_today_btn.setFlat(True)
        self.calendar_opt_wdg = QCalendarWidget(self.calendar_opt)
        self.calendar_opt_wdg.setObjectName(u"calendar_opt_wdg")
        self.calendar_opt_wdg.setGeometry(QRect(1, 50, 241, 181))
        sizePolicy.setHeightForWidth(self.calendar_opt_wdg.sizePolicy().hasHeightForWidth())
        self.calendar_opt_wdg.setSizePolicy(sizePolicy)
        self.calendar_opt_wdg.setFont(font5)
        self.calendar_opt_wdg.setFocusPolicy(Qt.NoFocus)
        self.calendar_opt_wdg.setStyleSheet(u"QCalendarWidget{\n"
"	color: rgb(70, 70, 90);\n"
"	selection-background-color: rgb(40, 45, 55);\n"
"}\n"
"QCalendarWidget QCalendarView{\n"
"	border:none;\n"
"	outline:0px;\n"
"}\n"
"QCalendarWidget QTableView{\n"
"	color: rgb(70, 70, 90);\n"
"	border:0px;\n"
"	outline:0px;\n"
"	selection-background-color: rgb(40, 45, 55);\n"
"	alternate-background-color: rgb(40, 45, 55);\n"
"	selection-color: rgb(235, 200, 140);\n"
"}\n"
"QCalendarWidget QAbstractItemView:!enabled { \n"
"    color:\"green\"\n"
" }")
        self.calendar_opt_wdg.setGridVisible(False)
        self.calendar_opt_wdg.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        self.calendar_opt_wdg.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendar_opt_wdg.setNavigationBarVisible(False)
        self.calendar_opt_next_month_btn = QPushButton(self.calendar_opt)
        self.calendar_opt_next_month_btn.setObjectName(u"calendar_opt_next_month_btn")
        self.calendar_opt_next_month_btn.setGeometry(QRect(210, 30, 30, 20))
        sizePolicy.setHeightForWidth(self.calendar_opt_next_month_btn.sizePolicy().hasHeightForWidth())
        self.calendar_opt_next_month_btn.setSizePolicy(sizePolicy)
        self.calendar_opt_next_month_btn.setMinimumSize(QSize(0, 0))
        self.calendar_opt_next_month_btn.setMaximumSize(QSize(31, 16777215))
        self.calendar_opt_next_month_btn.setFont(font12)
        self.calendar_opt_next_month_btn.setStyleSheet(u"color: rgb(150, 175, 200);")
        self.calendar_opt_next_month_btn.setAutoDefault(True)
        self.calendar_opt_next_month_btn.setFlat(True)
        self.calendar_opt_event_led = QLineEdit(self.calendar_opt)
        self.calendar_opt_event_led.setObjectName(u"calendar_opt_event_led")
        self.calendar_opt_event_led.setGeometry(QRect(260, 80, 261, 30))
        sizePolicy1.setHeightForWidth(self.calendar_opt_event_led.sizePolicy().hasHeightForWidth())
        self.calendar_opt_event_led.setSizePolicy(sizePolicy1)
        self.calendar_opt_event_led.setMinimumSize(QSize(0, 30))
        self.calendar_opt_event_led.setMaximumSize(QSize(16777215, 30))
        self.calendar_opt_event_led.setFont(font9)
        self.calendar_opt_event_led.setStyleSheet(u"QLineEdit {\n"
"	background-color:rgb(42,48,58);\n"
"	padding-left: 3px;\n"
"	color: rgb(166,177,199);\n"
"	border:none;\n"
"	border-radius:none;\n"
"	border-top:1px solid rgb(50,55,70);\n"
"	border-bottom:1px solid rgb(50,55,70);\n"
"}")
        self.calendar_opt_event_led.setFrame(False)
        self.horizontalLayoutWidget = QWidget(self.calendar_opt)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(260, 50, 261, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.calendar_event_date_title = QLabel(self.horizontalLayoutWidget)
        self.calendar_event_date_title.setObjectName(u"calendar_event_date_title")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.calendar_event_date_title.sizePolicy().hasHeightForWidth())
        self.calendar_event_date_title.setSizePolicy(sizePolicy2)
        font14 = QFont()
        font14.setFamilies([u"Lucida Sans"])
        font14.setPointSize(11)
        font14.setBold(True)
        font14.setItalic(True)
        self.calendar_event_date_title.setFont(font14)
        self.calendar_event_date_title.setStyleSheet(u"padding-left:2px;\n"
"color:rgb(150, 175, 250);")

        self.horizontalLayout.addWidget(self.calendar_event_date_title)

        self.calendar_event_date_dte = QDateEdit(self.horizontalLayoutWidget)
        self.calendar_event_date_dte.setObjectName(u"calendar_event_date_dte")
        font15 = QFont()
        font15.setFamilies([u"D2Coding"])
        font15.setPointSize(11)
        font15.setItalic(False)
        self.calendar_event_date_dte.setFont(font15)
        self.calendar_event_date_dte.setStyleSheet(u"padding-left:5px;\n"
"padding-top:1px;")
        self.calendar_event_date_dte.setFrame(False)
        self.calendar_event_date_dte.setReadOnly(True)
        self.calendar_event_date_dte.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.calendar_event_date_dte.setDateTime(QDateTime(QDate(2024, 1, 31), QTime(0, 0, 0)))
        self.calendar_event_date_dte.setTime(QTime(0, 0, 0))

        self.horizontalLayout.addWidget(self.calendar_event_date_dte)

        self.horizontalLayoutWidget_2 = QWidget(self.calendar_opt)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(260, 110, 261, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.calendar_multi_day_cbx = QCheckBox(self.horizontalLayoutWidget_2)
        self.calendar_multi_day_cbx.setObjectName(u"calendar_multi_day_cbx")
        self.calendar_multi_day_cbx.setFont(font11)
        self.calendar_multi_day_cbx.setStyleSheet(u"padding-top:2px;")

        self.horizontalLayout_2.addWidget(self.calendar_multi_day_cbx)

        self.calendar_select_end_date_btn = QPushButton(self.horizontalLayoutWidget_2)
        self.calendar_select_end_date_btn.setObjectName(u"calendar_select_end_date_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.calendar_select_end_date_btn.sizePolicy().hasHeightForWidth())
        self.calendar_select_end_date_btn.setSizePolicy(sizePolicy3)
        self.calendar_select_end_date_btn.setMinimumSize(QSize(0, 20))
        self.calendar_select_end_date_btn.setMaximumSize(QSize(16777215, 17))
        self.calendar_select_end_date_btn.setFont(font4)
        self.calendar_select_end_date_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:rgb(42,48,58);	\n"
"	color: rgb(200, 211, 222);\n"
"	border:none;\n"
"	border-radius:9px;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:checked {\n"
"	background-color:rgb(50,55,65);	\n"
"	color: rgb(233, 200, 133);\n"
"}\n"
"QPushButton:disabled {\n"
"	color: rgb(66, 77, 100);\n"
"}")
        self.calendar_select_end_date_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.calendar_select_end_date_btn)

        self.horizontalLayoutWidget_4 = QWidget(self.calendar_opt)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(270, 140, 251, 21))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.calendar_start_date_lbl = QLabel(self.horizontalLayoutWidget_4)
        self.calendar_start_date_lbl.setObjectName(u"calendar_start_date_lbl")
        font16 = QFont()
        font16.setFamilies([u"Lucida Sans"])
        font16.setPointSize(9)
        font16.setItalic(True)
        self.calendar_start_date_lbl.setFont(font16)
        self.calendar_start_date_lbl.setStyleSheet(u"color:transparent;")
        self.calendar_start_date_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.calendar_start_date_lbl)

        self.calendar_from_to_lbl = QLabel(self.horizontalLayoutWidget_4)
        self.calendar_from_to_lbl.setObjectName(u"calendar_from_to_lbl")
        sizePolicy2.setHeightForWidth(self.calendar_from_to_lbl.sizePolicy().hasHeightForWidth())
        self.calendar_from_to_lbl.setSizePolicy(sizePolicy2)
        self.calendar_from_to_lbl.setMinimumSize(QSize(15, 0))
        self.calendar_from_to_lbl.setMaximumSize(QSize(15, 16777215))
        font17 = QFont()
        font17.setFamilies([u"Lucida Sans"])
        font17.setPointSize(10)
        font17.setItalic(False)
        self.calendar_from_to_lbl.setFont(font17)
        self.calendar_from_to_lbl.setStyleSheet(u"color:transparent;")
        self.calendar_from_to_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.calendar_from_to_lbl)

        self.calendar_end_date_lbl = QLabel(self.horizontalLayoutWidget_4)
        self.calendar_end_date_lbl.setObjectName(u"calendar_end_date_lbl")
        self.calendar_end_date_lbl.setFont(font16)
        self.calendar_end_date_lbl.setStyleSheet(u"color:transparent;")

        self.horizontalLayout_4.addWidget(self.calendar_end_date_lbl)

        self.calendar_opt_write_btn = QPushButton(self.calendar_opt)
        self.calendar_opt_write_btn.setObjectName(u"calendar_opt_write_btn")
        self.calendar_opt_write_btn.setGeometry(QRect(420, 200, 101, 30))
        sizePolicy.setHeightForWidth(self.calendar_opt_write_btn.sizePolicy().hasHeightForWidth())
        self.calendar_opt_write_btn.setSizePolicy(sizePolicy)
        self.calendar_opt_write_btn.setMinimumSize(QSize(30, 20))
        self.calendar_opt_write_btn.setMaximumSize(QSize(300, 16777215))
        font18 = QFont()
        font18.setFamilies([u"Lucida Sans"])
        font18.setPointSize(10)
        font18.setBold(True)
        font18.setItalic(True)
        self.calendar_opt_write_btn.setFont(font18)
        self.calendar_opt_write_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:rgb(42,48,58);\n"
"	color: rgb(211, 222, 233);\n"
"	border:none;\n"
"	border-radius:10px;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.calendar_opt_write_btn.setAutoDefault(True)
        self.calendar_opt_write_btn.setFlat(True)
        self.calendar_opt_close_btn = QPushButton(self.calendar_opt)
        self.calendar_opt_close_btn.setObjectName(u"calendar_opt_close_btn")
        self.calendar_opt_close_btn.setGeometry(QRect(340, 200, 61, 30))
        sizePolicy.setHeightForWidth(self.calendar_opt_close_btn.sizePolicy().hasHeightForWidth())
        self.calendar_opt_close_btn.setSizePolicy(sizePolicy)
        self.calendar_opt_close_btn.setMinimumSize(QSize(30, 20))
        self.calendar_opt_close_btn.setMaximumSize(QSize(300, 16777215))
        self.calendar_opt_close_btn.setFont(font18)
        self.calendar_opt_close_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:rgb(42,48,58);\n"
"	color: rgb(211, 222, 233);\n"
"	border:none;\n"
"	border-radius:10px;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.calendar_opt_close_btn.setAutoDefault(True)
        self.calendar_opt_close_btn.setFlat(True)
        self.calendar_not_open_cbx = QCheckBox(self.calendar_opt)
        self.calendar_not_open_cbx.setObjectName(u"calendar_not_open_cbx")
        self.calendar_not_open_cbx.setGeometry(QRect(410, 170, 111, 17))
        self.calendar_not_open_cbx.setFont(font11)
        self.calendar_not_open_cbx.setStyleSheet(u"QCheckBox:checked {\n"
"	color: rgb(233, 111, 155);\n"
"}")
        self.calendar_event_delete_btn = QPushButton(self.calendar_opt)
        self.calendar_event_delete_btn.setObjectName(u"calendar_event_delete_btn")
        self.calendar_event_delete_btn.setGeometry(QRect(260, 20, 111, 21))
        sizePolicy.setHeightForWidth(self.calendar_event_delete_btn.sizePolicy().hasHeightForWidth())
        self.calendar_event_delete_btn.setSizePolicy(sizePolicy)
        self.calendar_event_delete_btn.setMinimumSize(QSize(30, 20))
        self.calendar_event_delete_btn.setMaximumSize(QSize(200, 16777215))
        self.calendar_event_delete_btn.setFont(font6)
        self.calendar_event_delete_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:rgb(45,50,60);	\n"
"	color:rgb(70, 75, 100);\n"
"	border:none;\n"
"	border-radius:10px;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:enabled{\n"
"	color: rgb(200, 75, 75);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.calendar_event_delete_btn.setAutoDefault(True)
        self.calendar_event_delete_btn.setFlat(True)
        self.calendar_stack.addWidget(self.calendar_opt)
        self.calendar_opt_title.raise_()
        self.calendar_opt_prev_month_btn.raise_()
        self.calendar_opt_month_year_lbl.raise_()
        self.calendar_opt_today_btn.raise_()
        self.calendar_opt_wdg.raise_()
        self.calendar_opt_next_month_btn.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.horizontalLayoutWidget_4.raise_()
        self.calendar_opt_write_btn.raise_()
        self.calendar_opt_event_led.raise_()
        self.calendar_opt_close_btn.raise_()
        self.calendar_not_open_cbx.raise_()
        self.calendar_event_delete_btn.raise_()
        self.calendar_yearly = QWidget()
        self.calendar_yearly.setObjectName(u"calendar_yearly")
        self.calendar_yearly_lwg = QListWidget(self.calendar_yearly)
        self.calendar_yearly_lwg.setObjectName(u"calendar_yearly_lwg")
        self.calendar_yearly_lwg.setGeometry(QRect(10, 10, 351, 221))
        font19 = QFont()
        font19.setFamilies([u"D2Coding"])
        font19.setPointSize(11)
        font19.setBold(False)
        font19.setItalic(False)
        self.calendar_yearly_lwg.setFont(font19)
        self.calendar_yearly_lwg.setStyleSheet(u"QListWidget{\n"
"	background:transparent;\n"
"	alternate-background-color: rgb(43, 48, 60);\n"
"	border:0px;\n"
"	color: rgb(166,177,199);\n"
"	outline:0px;\n"
"}\n"
"QListWidget::item:hover{\n"
"    background-color: rgb(48, 52, 66);\n"
"}\n"
"QListWidget::item:selected{\n"
"    background-color: rgb(52, 57, 75);\n"
"}")
        self.calendar_yearly_lwg.setEditTriggers(QAbstractItemView.SelectedClicked)
        self.calendar_yearly_lwg.setDragEnabled(True)
        self.calendar_yearly_lwg.setDragDropMode(QAbstractItemView.InternalMove)
        self.calendar_yearly_lwg.setAlternatingRowColors(True)
        self.calendar_yearly_lwg.setLayoutMode(QListView.SinglePass)
        self.calendar_yearly_lwg.setSpacing(1)
        self.calendar_yearly_lwg.setViewMode(QListView.ListMode)
        self.calendar_yearly_lwg.setUniformItemSizes(False)
        self.calendar_yearly_lwg.setSelectionRectVisible(False)
        self.calendar_yearly_done_btn = QPushButton(self.calendar_yearly)
        self.calendar_yearly_done_btn.setObjectName(u"calendar_yearly_done_btn")
        self.calendar_yearly_done_btn.setGeometry(QRect(380, 200, 141, 30))
        sizePolicy.setHeightForWidth(self.calendar_yearly_done_btn.sizePolicy().hasHeightForWidth())
        self.calendar_yearly_done_btn.setSizePolicy(sizePolicy)
        self.calendar_yearly_done_btn.setMinimumSize(QSize(30, 20))
        self.calendar_yearly_done_btn.setMaximumSize(QSize(300, 16777215))
        self.calendar_yearly_done_btn.setFont(font18)
        self.calendar_yearly_done_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:rgb(42,48,58);\n"
"	color: rgb(211, 222, 233);\n"
"	border:none;\n"
"	border-radius:10px;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.calendar_yearly_done_btn.setAutoDefault(True)
        self.calendar_yearly_done_btn.setFlat(True)
        self.calendar_yearly_year = QLabel(self.calendar_yearly)
        self.calendar_yearly_year.setObjectName(u"calendar_yearly_year")
        self.calendar_yearly_year.setGeometry(QRect(410, 100, 41, 30))
        font20 = QFont()
        font20.setFamilies([u"D2Coding ligature"])
        font20.setPointSize(11)
        self.calendar_yearly_year.setFont(font20)
        self.calendar_yearly_year.setStyleSheet(u"background-color:rgb(42,48,58);\n"
"color: rgb(188, 177, 122);\n"
"border-top:1px solid rgb(50,55,70);\n"
"border-bottom:1px solid rgb(50,55,70);\n"
"padding-left:1px;")
        self.calendar_yearly_year.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.calendar_yearly_next_btn = QPushButton(self.calendar_yearly)
        self.calendar_yearly_next_btn.setObjectName(u"calendar_yearly_next_btn")
        self.calendar_yearly_next_btn.setGeometry(QRect(490, 100, 31, 30))
        font21 = QFont()
        font21.setFamilies([u"D2Coding"])
        font21.setPointSize(11)
        self.calendar_yearly_next_btn.setFont(font21)
        self.calendar_yearly_next_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:rgb(42,48,58);\n"
"	color: rgb(166, 155, 133);\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"	border:1px solid rgb(50,55,70);\n"
"	border-right:none;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.calendar_yearly_year_led = QLineEdit(self.calendar_yearly)
        self.calendar_yearly_year_led.setObjectName(u"calendar_yearly_year_led")
        self.calendar_yearly_year_led.setGeometry(QRect(450, 100, 41, 30))
        font22 = QFont()
        font22.setFamilies([u"D2Coding ligature"])
        font22.setPointSize(11)
        font22.setBold(True)
        self.calendar_yearly_year_led.setFont(font22)
        self.calendar_yearly_year_led.setStyleSheet(u"background-color:rgb(42,48,58);\n"
"color: rgb(188, 177, 122);\n"
"border-top:1px solid rgb(50,55,70);\n"
"border-bottom:1px solid rgb(50,55,70);\n"
"padding-left:1px;\n"
"\n"
"")
        self.calendar_yearly_year_led.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.calendar_yearly_prev_btn = QPushButton(self.calendar_yearly)
        self.calendar_yearly_prev_btn.setObjectName(u"calendar_yearly_prev_btn")
        self.calendar_yearly_prev_btn.setGeometry(QRect(380, 100, 31, 30))
        self.calendar_yearly_prev_btn.setFont(font21)
        self.calendar_yearly_prev_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:rgb(42,48,58);	\n"
"	color: rgb(166, 155, 133);\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"	border:1px solid rgb(50,55,70);\n"
"	border-right:none;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.calendar_yearly_title = QLabel(self.calendar_yearly)
        self.calendar_yearly_title.setObjectName(u"calendar_yearly_title")
        self.calendar_yearly_title.setGeometry(QRect(380, 50, 141, 31))
        self.calendar_yearly_title.setFont(font7)
        self.calendar_yearly_title.setStyleSheet(u"color: rgb(143, 188, 187);\n"
"padding-right:2px;")
        self.calendar_yearly_title.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.calendar_stack.addWidget(self.calendar_yearly)
        self.clock_led = QLineEdit(self.today_gbx)
        self.clock_led.setObjectName(u"clock_led")
        self.clock_led.setGeometry(QRect(459, 1, 91, 41))
        font23 = QFont()
        font23.setFamilies([u"Impact"])
        font23.setPointSize(20)
        self.clock_led.setFont(font23)
        self.clock_led.setStyleSheet(u"color: rgb(225, 215, 125);\n"
"background-color: rgb(55, 60, 75);\n"
"border: 2px solid rgb(40, 45, 55);\n"
"border-top-right-radius:10px;\n"
"border-bottom-left-radius:10px;")
        self.clock_led.setAlignment(Qt.AlignCenter)
        self.clock_led.setReadOnly(True)
        self.reminders_gbx = QGroupBox(self.centralwidget)
        self.reminders_gbx.setObjectName(u"reminders_gbx")
        self.reminders_gbx.setGeometry(QRect(20, 300, 550, 431))
        self.reminders_gbx.setStyleSheet(u"QWidget{	\n"
"	background-color: rgb(40, 45, 55);\n"
"}")
        self.reminders_title_lbl = QPushButton(self.reminders_gbx)
        self.reminders_title_lbl.setObjectName(u"reminders_title_lbl")
        self.reminders_title_lbl.setGeometry(QRect(10, 10, 131, 31))
        sizePolicy.setHeightForWidth(self.reminders_title_lbl.sizePolicy().hasHeightForWidth())
        self.reminders_title_lbl.setSizePolicy(sizePolicy)
        self.reminders_title_lbl.setMinimumSize(QSize(0, 30))
        self.reminders_title_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.reminders_title_lbl.setFont(font7)
        self.reminders_title_lbl.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(143, 188, 187);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}")
        self.reminders_title_lbl.setAutoDefault(True)
        self.reminders_title_lbl.setFlat(True)
        self.reminders_stack = QStackedWidget(self.reminders_gbx)
        self.reminders_stack.setObjectName(u"reminders_stack")
        self.reminders_stack.setGeometry(QRect(20, 40, 511, 371))
        self.reminders_main = QWidget()
        self.reminders_main.setObjectName(u"reminders_main")
        self.reminders_lwg = QListWidget(self.reminders_main)
        QListWidgetItem(self.reminders_lwg)
        QListWidgetItem(self.reminders_lwg)
        QListWidgetItem(self.reminders_lwg)
        font24 = QFont()
        font24.setStrikeOut(True)
        __qlistwidgetitem = QListWidgetItem(self.reminders_lwg)
        __qlistwidgetitem.setFont(font24);
        QListWidgetItem(self.reminders_lwg)
        QListWidgetItem(self.reminders_lwg)
        QListWidgetItem(self.reminders_lwg)
        QListWidgetItem(self.reminders_lwg)
        QListWidgetItem(self.reminders_lwg)
        QListWidgetItem(self.reminders_lwg)
        QListWidgetItem(self.reminders_lwg)
        QListWidgetItem(self.reminders_lwg)
        QListWidgetItem(self.reminders_lwg)
        QListWidgetItem(self.reminders_lwg)
        QListWidgetItem(self.reminders_lwg)
        QListWidgetItem(self.reminders_lwg)
        self.reminders_lwg.setObjectName(u"reminders_lwg")
        self.reminders_lwg.setGeometry(QRect(0, 10, 511, 281))
        palette = QPalette()
        brush = QBrush(QColor(166, 177, 199, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(40, 45, 55, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(222, 233, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
        brush3 = QBrush(QColor(43, 48, 60, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush4 = QBrush(QColor(166, 177, 199, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        brush5 = QBrush(QColor(166, 177, 199, 128))
        brush5.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(166, 177, 199, 128))
        brush6.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.reminders_lwg.setPalette(palette)
        self.reminders_lwg.setFont(font19)
        self.reminders_lwg.setStyleSheet(u"QListWidget::item:selected{\n"
"    background-color: rgb(52, 57, 75);\n"
"}\n"
"QListWidget{\n"
"	border-bottom:1px solid rgb(47,52,63);\n"
"}")
        self.reminders_lwg.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.reminders_lwg.setDragEnabled(True)
        self.reminders_lwg.setDragDropMode(QAbstractItemView.InternalMove)
        self.reminders_lwg.setAlternatingRowColors(True)
        self.reminders_lwg.setSelectionMode(QAbstractItemView.SingleSelection)
        self.reminders_lwg.setLayoutMode(QListView.SinglePass)
        self.reminders_lwg.setSpacing(1)
        self.reminders_lwg.setViewMode(QListView.ListMode)
        self.reminders_lwg.setUniformItemSizes(False)
        self.reminders_lwg.setSelectionRectVisible(False)
        self.reminders_lwg.setSortingEnabled(False)
        self.reminders_archive_btn = QPushButton(self.reminders_main)
        self.reminders_archive_btn.setObjectName(u"reminders_archive_btn")
        self.reminders_archive_btn.setGeometry(QRect(440, 310, 71, 21))
        sizePolicy.setHeightForWidth(self.reminders_archive_btn.sizePolicy().hasHeightForWidth())
        self.reminders_archive_btn.setSizePolicy(sizePolicy)
        self.reminders_archive_btn.setMinimumSize(QSize(30, 20))
        self.reminders_archive_btn.setMaximumSize(QSize(80, 16777215))
        self.reminders_archive_btn.setFont(font6)
        self.reminders_archive_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:none;	\n"
"	color:rgb(40, 45, 55);\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:enabled{\n"
"	color: rgb(200, 125, 55);\n"
"	background-color:rgb(45,50,60);	\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.reminders_archive_btn.setAutoDefault(True)
        self.reminders_archive_btn.setFlat(True)
        self.reminders_new_led = QLineEdit(self.reminders_main)
        self.reminders_new_led.setObjectName(u"reminders_new_led")
        self.reminders_new_led.setGeometry(QRect(40, 340, 411, 30))
        sizePolicy1.setHeightForWidth(self.reminders_new_led.sizePolicy().hasHeightForWidth())
        self.reminders_new_led.setSizePolicy(sizePolicy1)
        self.reminders_new_led.setMinimumSize(QSize(0, 30))
        self.reminders_new_led.setMaximumSize(QSize(16777215, 30))
        self.reminders_new_led.setFont(font21)
        self.reminders_new_led.setStyleSheet(u"background-color:rgb(42,48,58);\n"
"color: rgb(180, 185, 195);\n"
"border:none;\n"
"border:1px solid rgb(50,55,70);\n"
"border-right:none;\n"
"border-left:none;\n"
"")
        self.reminders_new_led.setFrame(False)
        self.reminders_clear_btn = QPushButton(self.reminders_main)
        self.reminders_clear_btn.setObjectName(u"reminders_clear_btn")
        self.reminders_clear_btn.setGeometry(QRect(450, 340, 61, 30))
        sizePolicy.setHeightForWidth(self.reminders_clear_btn.sizePolicy().hasHeightForWidth())
        self.reminders_clear_btn.setSizePolicy(sizePolicy)
        self.reminders_clear_btn.setMinimumSize(QSize(30, 20))
        self.reminders_clear_btn.setMaximumSize(QSize(80, 16777215))
        self.reminders_clear_btn.setFont(font6)
        self.reminders_clear_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:rgb(42,48,58);	\n"
"	color: rgb(160, 190, 150);\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"	border:1px solid rgb(50,55,70);\n"
"	border-left:none;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.reminders_clear_btn.setAutoDefault(True)
        self.reminders_clear_btn.setFlat(True)
        self.reminders_star_btn = QPushButton(self.reminders_main)
        self.reminders_star_btn.setObjectName(u"reminders_star_btn")
        self.reminders_star_btn.setGeometry(QRect(50, 310, 20, 20))
        sizePolicy.setHeightForWidth(self.reminders_star_btn.sizePolicy().hasHeightForWidth())
        self.reminders_star_btn.setSizePolicy(sizePolicy)
        self.reminders_star_btn.setMinimumSize(QSize(20, 20))
        self.reminders_star_btn.setMaximumSize(QSize(20, 20))
        font25 = QFont()
        font25.setFamilies([u"D2Coding"])
        font25.setPointSize(12)
        font25.setBold(False)
        self.reminders_star_btn.setFont(font25)
        self.reminders_star_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(225, 200, 125);\n"
"	border:1px solid rgb(50,55,70);	\n"
"	border-radius:10px;\n"
"	color: rgb(60, 65, 80);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(245, 225, 145);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(205, 180, 105);\n"
"}")
        self.reminders_star_btn.setAutoDefault(True)
        self.reminders_star_btn.setFlat(True)
        self.reminders_ugnt_btn = QPushButton(self.reminders_main)
        self.reminders_ugnt_btn.setObjectName(u"reminders_ugnt_btn")
        self.reminders_ugnt_btn.setGeometry(QRect(25, 310, 20, 20))
        sizePolicy.setHeightForWidth(self.reminders_ugnt_btn.sizePolicy().hasHeightForWidth())
        self.reminders_ugnt_btn.setSizePolicy(sizePolicy)
        self.reminders_ugnt_btn.setMinimumSize(QSize(20, 20))
        self.reminders_ugnt_btn.setMaximumSize(QSize(20, 20))
        self.reminders_ugnt_btn.setFont(font25)
        self.reminders_ugnt_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(200, 125, 75);\n"
"	border:1px solid rgb(50,55,70);	\n"
"	border-radius:10px;\n"
"	color: rgb(60, 65, 80);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(220, 145, 95);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(180, 105, 55);\n"
"}")
        self.reminders_ugnt_btn.setAutoDefault(True)
        self.reminders_ugnt_btn.setFlat(True)
        self.reminders_prgs_btn = QPushButton(self.reminders_main)
        self.reminders_prgs_btn.setObjectName(u"reminders_prgs_btn")
        self.reminders_prgs_btn.setGeometry(QRect(75, 310, 20, 20))
        sizePolicy.setHeightForWidth(self.reminders_prgs_btn.sizePolicy().hasHeightForWidth())
        self.reminders_prgs_btn.setSizePolicy(sizePolicy)
        self.reminders_prgs_btn.setMinimumSize(QSize(20, 20))
        self.reminders_prgs_btn.setMaximumSize(QSize(20, 20))
        self.reminders_prgs_btn.setFont(font25)
        self.reminders_prgs_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(100, 125, 175);\n"
"	border:1px solid rgb(50,55,70);	\n"
"	border-radius:10px;\n"
"	color: rgb(60, 65, 80);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(120, 135, 195);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(80, 105, 155);\n"
"}")
        self.reminders_prgs_btn.setAutoDefault(True)
        self.reminders_prgs_btn.setFlat(True)
        self.reminders_dlyd_btn = QPushButton(self.reminders_main)
        self.reminders_dlyd_btn.setObjectName(u"reminders_dlyd_btn")
        self.reminders_dlyd_btn.setGeometry(QRect(100, 310, 20, 20))
        sizePolicy.setHeightForWidth(self.reminders_dlyd_btn.sizePolicy().hasHeightForWidth())
        self.reminders_dlyd_btn.setSizePolicy(sizePolicy)
        self.reminders_dlyd_btn.setMinimumSize(QSize(20, 20))
        self.reminders_dlyd_btn.setMaximumSize(QSize(20, 20))
        self.reminders_dlyd_btn.setFont(font25)
        self.reminders_dlyd_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(150, 125, 175);\n"
"	border:1px solid rgb(50,55,70);	\n"
"	border-radius:10px;\n"
"	color: rgb(60, 65, 80);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(170, 135, 195);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(130, 105, 155);\n"
"}")
        self.reminders_dlyd_btn.setAutoDefault(True)
        self.reminders_dlyd_btn.setFlat(True)
        self.reminders_todo_btn = QPushButton(self.reminders_main)
        self.reminders_todo_btn.setObjectName(u"reminders_todo_btn")
        self.reminders_todo_btn.setGeometry(QRect(0, 310, 20, 20))
        sizePolicy.setHeightForWidth(self.reminders_todo_btn.sizePolicy().hasHeightForWidth())
        self.reminders_todo_btn.setSizePolicy(sizePolicy)
        self.reminders_todo_btn.setMinimumSize(QSize(20, 20))
        self.reminders_todo_btn.setMaximumSize(QSize(20, 20))
        font26 = QFont()
        font26.setFamilies([u"D2Coding"])
        font26.setPointSize(10)
        font26.setBold(False)
        self.reminders_todo_btn.setFont(font26)
        self.reminders_todo_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(180, 185, 195);\n"
"	border:1px solid rgb(50,55,70);	\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(200, 205, 215);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(160, 165, 175);\n"
"}")
        self.reminders_todo_btn.setAutoDefault(True)
        self.reminders_todo_btn.setFlat(True)
        self.reminders_status_lbl = QLabel(self.reminders_main)
        self.reminders_status_lbl.setObjectName(u"reminders_status_lbl")
        self.reminders_status_lbl.setGeometry(QRect(0, 340, 41, 30))
        self.reminders_status_lbl.setFont(font21)
        self.reminders_status_lbl.setStyleSheet(u"background-color:rgb(42,48,58);\n"
"padding-left: 5px;\n"
"color: rgb(180, 185, 195);\n"
"border:none;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border:1px solid rgb(50,55,70);\n"
"border-right:none;")
        self.reminders_done_btn = QPushButton(self.reminders_main)
        self.reminders_done_btn.setObjectName(u"reminders_done_btn")
        self.reminders_done_btn.setGeometry(QRect(140, 310, 20, 20))
        sizePolicy.setHeightForWidth(self.reminders_done_btn.sizePolicy().hasHeightForWidth())
        self.reminders_done_btn.setSizePolicy(sizePolicy)
        self.reminders_done_btn.setMinimumSize(QSize(20, 20))
        self.reminders_done_btn.setMaximumSize(QSize(20, 20))
        self.reminders_done_btn.setFont(font25)
        self.reminders_done_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(140, 175, 100);\n"
"	border:1px solid rgb(50,55,70);	\n"
"	border-radius:10px;\n"
"	color: rgb(60, 65, 80);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(160, 195, 100);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(120, 150, 80);\n"
"}")
        self.reminders_done_btn.setAutoDefault(True)
        self.reminders_done_btn.setFlat(True)
        self.reminders_canc_btn = QPushButton(self.reminders_main)
        self.reminders_canc_btn.setObjectName(u"reminders_canc_btn")
        self.reminders_canc_btn.setGeometry(QRect(165, 310, 20, 20))
        sizePolicy.setHeightForWidth(self.reminders_canc_btn.sizePolicy().hasHeightForWidth())
        self.reminders_canc_btn.setSizePolicy(sizePolicy)
        self.reminders_canc_btn.setMinimumSize(QSize(20, 20))
        self.reminders_canc_btn.setMaximumSize(QSize(20, 20))
        self.reminders_canc_btn.setFont(font25)
        self.reminders_canc_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 75, 75);\n"
"	border:1px solid rgb(50,55,70);	\n"
"	border-radius:10px;\n"
"	color: rgb(60, 65, 80);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(190, 100, 100);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(150, 60, 60);\n"
"}")
        self.reminders_canc_btn.setAutoDefault(True)
        self.reminders_canc_btn.setFlat(True)
        self.reminders_stack.addWidget(self.reminders_main)
        self.reminders_lwg.raise_()
        self.reminders_archive_btn.raise_()
        self.reminders_star_btn.raise_()
        self.reminders_ugnt_btn.raise_()
        self.reminders_prgs_btn.raise_()
        self.reminders_dlyd_btn.raise_()
        self.reminders_todo_btn.raise_()
        self.reminders_new_led.raise_()
        self.reminders_clear_btn.raise_()
        self.reminders_status_lbl.raise_()
        self.reminders_done_btn.raise_()
        self.reminders_canc_btn.raise_()
        self.reminders_sublist = QWidget()
        self.reminders_sublist.setObjectName(u"reminders_sublist")
        self.reminders_sublist_lwg = QListWidget(self.reminders_sublist)
        __qlistwidgetitem1 = QListWidgetItem(self.reminders_sublist_lwg)
        __qlistwidgetitem1.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsEnabled);
        QListWidgetItem(self.reminders_sublist_lwg)
        QListWidgetItem(self.reminders_sublist_lwg)
        self.reminders_sublist_lwg.setObjectName(u"reminders_sublist_lwg")
        self.reminders_sublist_lwg.setGeometry(QRect(10, 60, 501, 211))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush7 = QBrush(QColor(166, 177, 199, 128))
        brush7.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        brush8 = QBrush(QColor(166, 177, 199, 128))
        brush8.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush3)
        brush9 = QBrush(QColor(166, 177, 199, 128))
        brush9.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.reminders_sublist_lwg.setPalette(palette1)
        self.reminders_sublist_lwg.setFont(font19)
        self.reminders_sublist_lwg.setStyleSheet(u"border-left:1px solid rgb(50, 60, 70);\n"
"border-bottom:1px solid rgb(50, 60, 70);\n"
"border-bottom-left-radius:10px;\n"
"padding-left:5px;")
        self.reminders_sublist_lwg.setEditTriggers(QAbstractItemView.SelectedClicked)
        self.reminders_sublist_lwg.setDragEnabled(True)
        self.reminders_sublist_lwg.setDragDropMode(QAbstractItemView.InternalMove)
        self.reminders_sublist_lwg.setAlternatingRowColors(True)
        self.reminders_sublist_lwg.setLayoutMode(QListView.SinglePass)
        self.reminders_sublist_lwg.setSpacing(1)
        self.reminders_sublist_lwg.setViewMode(QListView.ListMode)
        self.reminders_sublist_lwg.setUniformItemSizes(False)
        self.reminders_sublist_lwg.setSelectionRectVisible(False)
        self.reminders_sublist_item_led = QLineEdit(self.reminders_sublist)
        self.reminders_sublist_item_led.setObjectName(u"reminders_sublist_item_led")
        self.reminders_sublist_item_led.setGeometry(QRect(50, 300, 401, 30))
        sizePolicy1.setHeightForWidth(self.reminders_sublist_item_led.sizePolicy().hasHeightForWidth())
        self.reminders_sublist_item_led.setSizePolicy(sizePolicy1)
        self.reminders_sublist_item_led.setMinimumSize(QSize(0, 30))
        self.reminders_sublist_item_led.setMaximumSize(QSize(16777215, 30))
        self.reminders_sublist_item_led.setFont(font21)
        self.reminders_sublist_item_led.setContextMenuPolicy(Qt.CustomContextMenu)
        self.reminders_sublist_item_led.setStyleSheet(u"background-color:rgb(42,48,58);\n"
"padding-left: 5px;\n"
"color: rgb(166,177,199);\n"
"border:none;\n"
"border:1px solid rgb(50,55,70);\n"
"border-right:none;\n"
"border-left:none;\n"
"")
        self.reminders_sublist_item_led.setFrame(False)
        self.reminders_sublist_clear_btn = QPushButton(self.reminders_sublist)
        self.reminders_sublist_clear_btn.setObjectName(u"reminders_sublist_clear_btn")
        self.reminders_sublist_clear_btn.setGeometry(QRect(450, 300, 61, 30))
        sizePolicy.setHeightForWidth(self.reminders_sublist_clear_btn.sizePolicy().hasHeightForWidth())
        self.reminders_sublist_clear_btn.setSizePolicy(sizePolicy)
        self.reminders_sublist_clear_btn.setMinimumSize(QSize(30, 20))
        self.reminders_sublist_clear_btn.setMaximumSize(QSize(80, 16777215))
        self.reminders_sublist_clear_btn.setFont(font6)
        self.reminders_sublist_clear_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:rgb(42,48,58);	\n"
"	color: rgb(160, 190, 150);\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"	border:1px solid rgb(50,55,70);\n"
"	border-left:none;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.reminders_sublist_clear_btn.setAutoDefault(True)
        self.reminders_sublist_clear_btn.setFlat(True)
        self.reminders_sublist_delete_btn = QPushButton(self.reminders_sublist)
        self.reminders_sublist_delete_btn.setObjectName(u"reminders_sublist_delete_btn")
        self.reminders_sublist_delete_btn.setGeometry(QRect(450, 270, 61, 21))
        sizePolicy.setHeightForWidth(self.reminders_sublist_delete_btn.sizePolicy().hasHeightForWidth())
        self.reminders_sublist_delete_btn.setSizePolicy(sizePolicy)
        self.reminders_sublist_delete_btn.setMinimumSize(QSize(30, 20))
        self.reminders_sublist_delete_btn.setMaximumSize(QSize(80, 16777215))
        self.reminders_sublist_delete_btn.setFont(font6)
        self.reminders_sublist_delete_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:rgb(45,50,60);	\n"
"	color: rgb(220, 150, 175);\n"
"	border:none;\n"
"	border-radius:10px;\n"
"	border-top-left-radius:0px;\n"
"	border-top-right-radius:0px;\n"
"	border:1px solid rgb(50,60,70);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.reminders_sublist_delete_btn.setAutoDefault(True)
        self.reminders_sublist_delete_btn.setFlat(True)
        self.reminders_sublist_write_btn = QPushButton(self.reminders_sublist)
        self.reminders_sublist_write_btn.setObjectName(u"reminders_sublist_write_btn")
        self.reminders_sublist_write_btn.setGeometry(QRect(410, 340, 101, 30))
        sizePolicy.setHeightForWidth(self.reminders_sublist_write_btn.sizePolicy().hasHeightForWidth())
        self.reminders_sublist_write_btn.setSizePolicy(sizePolicy)
        self.reminders_sublist_write_btn.setMinimumSize(QSize(30, 20))
        self.reminders_sublist_write_btn.setMaximumSize(QSize(300, 16777215))
        self.reminders_sublist_write_btn.setFont(font18)
        self.reminders_sublist_write_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:rgb(42,48,58);\n"
"	color: rgb(211, 222, 233);\n"
"	border:none;\n"
"	border-radius:10px;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.reminders_sublist_write_btn.setAutoDefault(True)
        self.reminders_sublist_write_btn.setFlat(True)
        self.reminders_sublist_close_btn = QPushButton(self.reminders_sublist)
        self.reminders_sublist_close_btn.setObjectName(u"reminders_sublist_close_btn")
        self.reminders_sublist_close_btn.setGeometry(QRect(330, 340, 61, 30))
        sizePolicy.setHeightForWidth(self.reminders_sublist_close_btn.sizePolicy().hasHeightForWidth())
        self.reminders_sublist_close_btn.setSizePolicy(sizePolicy)
        self.reminders_sublist_close_btn.setMinimumSize(QSize(30, 20))
        self.reminders_sublist_close_btn.setMaximumSize(QSize(300, 16777215))
        self.reminders_sublist_close_btn.setFont(font18)
        self.reminders_sublist_close_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:rgb(42,48,58);\n"
"	color: rgb(211, 222, 233);\n"
"	border:none;\n"
"	border-radius:10px;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.reminders_sublist_close_btn.setAutoDefault(True)
        self.reminders_sublist_close_btn.setFlat(True)
        self.reminders_sublist_reminder_led = QLineEdit(self.reminders_sublist)
        self.reminders_sublist_reminder_led.setObjectName(u"reminders_sublist_reminder_led")
        self.reminders_sublist_reminder_led.setGeometry(QRect(40, 30, 471, 30))
        sizePolicy1.setHeightForWidth(self.reminders_sublist_reminder_led.sizePolicy().hasHeightForWidth())
        self.reminders_sublist_reminder_led.setSizePolicy(sizePolicy1)
        self.reminders_sublist_reminder_led.setMinimumSize(QSize(0, 30))
        self.reminders_sublist_reminder_led.setMaximumSize(QSize(16777215, 30))
        font27 = QFont()
        font27.setFamilies([u"D2Coding"])
        font27.setPointSize(11)
        font27.setBold(False)
        self.reminders_sublist_reminder_led.setFont(font27)
        self.reminders_sublist_reminder_led.setStyleSheet(u"background-color:rgb(42,48,58);\n"
"padding-left: 18px;\n"
"color: rgb(166,177,199);\n"
"border:1px solid rgb(50,55,70);\n"
"border-right:none;\n"
"border-left:none;\n"
"")
        self.reminders_sublist_reminder_led.setFrame(False)
        self.reminders_sublist_due_cbx = QCheckBox(self.reminders_sublist)
        self.reminders_sublist_due_cbx.setObjectName(u"reminders_sublist_due_cbx")
        self.reminders_sublist_due_cbx.setGeometry(QRect(160, 0, 85, 21))
        self.reminders_sublist_due_cbx.setFont(font21)
        self.reminders_sublist_due_dte = QDateEdit(self.reminders_sublist)
        self.reminders_sublist_due_dte.setObjectName(u"reminders_sublist_due_dte")
        self.reminders_sublist_due_dte.setGeometry(QRect(250, 0, 111, 21))
        self.reminders_sublist_due_dte.setFont(font21)
        self.reminders_sublist_due_dte.setStyleSheet(u"border:none;")
        self.reminders_sublist_due_dte.setFrame(False)
        self.reminders_sublist_due_dte.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.reminders_sublist_due_dte.setCalendarPopup(False)
        self.reminders_sublist_todo_btn = QPushButton(self.reminders_sublist)
        self.reminders_sublist_todo_btn.setObjectName(u"reminders_sublist_todo_btn")
        self.reminders_sublist_todo_btn.setGeometry(QRect(10, 275, 20, 20))
        sizePolicy.setHeightForWidth(self.reminders_sublist_todo_btn.sizePolicy().hasHeightForWidth())
        self.reminders_sublist_todo_btn.setSizePolicy(sizePolicy)
        self.reminders_sublist_todo_btn.setMinimumSize(QSize(20, 20))
        self.reminders_sublist_todo_btn.setMaximumSize(QSize(20, 20))
        self.reminders_sublist_todo_btn.setFont(font25)
        self.reminders_sublist_todo_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(180, 185, 195);\n"
"	border:1px solid rgb(50,55,70);	\n"
"	border-radius:10px;\n"
"	color: rgb(60, 65, 80);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(200, 205, 215);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(160, 165, 175);\n"
"}")
        self.reminders_sublist_todo_btn.setAutoDefault(True)
        self.reminders_sublist_todo_btn.setFlat(True)
        self.reminders_sublist_prgs_btn = QPushButton(self.reminders_sublist)
        self.reminders_sublist_prgs_btn.setObjectName(u"reminders_sublist_prgs_btn")
        self.reminders_sublist_prgs_btn.setGeometry(QRect(85, 275, 20, 20))
        sizePolicy.setHeightForWidth(self.reminders_sublist_prgs_btn.sizePolicy().hasHeightForWidth())
        self.reminders_sublist_prgs_btn.setSizePolicy(sizePolicy)
        self.reminders_sublist_prgs_btn.setMinimumSize(QSize(20, 20))
        self.reminders_sublist_prgs_btn.setMaximumSize(QSize(20, 20))
        self.reminders_sublist_prgs_btn.setFont(font25)
        self.reminders_sublist_prgs_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(100, 125, 175);\n"
"	border:1px solid rgb(50,55,70);	\n"
"	border-radius:10px;\n"
"	color: rgb(60, 65, 80);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(120, 135, 195);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(80, 105, 155);\n"
"}")
        self.reminders_sublist_prgs_btn.setAutoDefault(True)
        self.reminders_sublist_prgs_btn.setFlat(True)
        self.reminders_sublist_ugnt_btn = QPushButton(self.reminders_sublist)
        self.reminders_sublist_ugnt_btn.setObjectName(u"reminders_sublist_ugnt_btn")
        self.reminders_sublist_ugnt_btn.setGeometry(QRect(35, 275, 20, 20))
        sizePolicy.setHeightForWidth(self.reminders_sublist_ugnt_btn.sizePolicy().hasHeightForWidth())
        self.reminders_sublist_ugnt_btn.setSizePolicy(sizePolicy)
        self.reminders_sublist_ugnt_btn.setMinimumSize(QSize(20, 20))
        self.reminders_sublist_ugnt_btn.setMaximumSize(QSize(20, 20))
        self.reminders_sublist_ugnt_btn.setFont(font25)
        self.reminders_sublist_ugnt_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(200, 125, 75);\n"
"	border:1px solid rgb(50,55,70);	\n"
"	border-radius:10px;\n"
"	color: rgb(60, 65, 80);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(220, 145, 95);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(180, 105, 55);\n"
"}")
        self.reminders_sublist_ugnt_btn.setAutoDefault(True)
        self.reminders_sublist_ugnt_btn.setFlat(True)
        self.reminders_sublist_star_btn = QPushButton(self.reminders_sublist)
        self.reminders_sublist_star_btn.setObjectName(u"reminders_sublist_star_btn")
        self.reminders_sublist_star_btn.setGeometry(QRect(60, 275, 20, 20))
        sizePolicy.setHeightForWidth(self.reminders_sublist_star_btn.sizePolicy().hasHeightForWidth())
        self.reminders_sublist_star_btn.setSizePolicy(sizePolicy)
        self.reminders_sublist_star_btn.setMinimumSize(QSize(20, 20))
        self.reminders_sublist_star_btn.setMaximumSize(QSize(20, 20))
        self.reminders_sublist_star_btn.setFont(font25)
        self.reminders_sublist_star_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(225, 200, 125);\n"
"	border:1px solid rgb(50,55,70);	\n"
"	border-radius:10px;\n"
"	color: rgb(60, 65, 80);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(245, 225, 145);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(205, 180, 105);\n"
"}")
        self.reminders_sublist_star_btn.setAutoDefault(True)
        self.reminders_sublist_star_btn.setFlat(True)
        self.reminders_sublist_dlyd_btn = QPushButton(self.reminders_sublist)
        self.reminders_sublist_dlyd_btn.setObjectName(u"reminders_sublist_dlyd_btn")
        self.reminders_sublist_dlyd_btn.setGeometry(QRect(110, 275, 20, 20))
        sizePolicy.setHeightForWidth(self.reminders_sublist_dlyd_btn.sizePolicy().hasHeightForWidth())
        self.reminders_sublist_dlyd_btn.setSizePolicy(sizePolicy)
        self.reminders_sublist_dlyd_btn.setMinimumSize(QSize(20, 20))
        self.reminders_sublist_dlyd_btn.setMaximumSize(QSize(20, 20))
        self.reminders_sublist_dlyd_btn.setFont(font25)
        self.reminders_sublist_dlyd_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(150, 125, 175);\n"
"	border:1px solid rgb(50,55,70);	\n"
"	border-radius:10px;\n"
"	color: rgb(60, 65, 80);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(170, 135, 195);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(130, 105, 155);\n"
"}")
        self.reminders_sublist_dlyd_btn.setAutoDefault(True)
        self.reminders_sublist_dlyd_btn.setFlat(True)
        self.reminders_sublist_reminder_delete_btn = QPushButton(self.reminders_sublist)
        self.reminders_sublist_reminder_delete_btn.setObjectName(u"reminders_sublist_reminder_delete_btn")
        self.reminders_sublist_reminder_delete_btn.setGeometry(QRect(359, 0, 151, 21))
        sizePolicy.setHeightForWidth(self.reminders_sublist_reminder_delete_btn.sizePolicy().hasHeightForWidth())
        self.reminders_sublist_reminder_delete_btn.setSizePolicy(sizePolicy)
        self.reminders_sublist_reminder_delete_btn.setMinimumSize(QSize(30, 20))
        self.reminders_sublist_reminder_delete_btn.setMaximumSize(QSize(200, 16777215))
        self.reminders_sublist_reminder_delete_btn.setFont(font6)
        self.reminders_sublist_reminder_delete_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:rgb(45,50,60);	\n"
"	color: rgb(200, 75, 75);\n"
"	border:none;\n"
"	border-radius:10px;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.reminders_sublist_reminder_delete_btn.setAutoDefault(True)
        self.reminders_sublist_reminder_delete_btn.setFlat(True)
        self.reminders_sublist_rem_status_btn = QPushButton(self.reminders_sublist)
        self.reminders_sublist_rem_status_btn.setObjectName(u"reminders_sublist_rem_status_btn")
        self.reminders_sublist_rem_status_btn.setGeometry(QRect(10, 30, 41, 30))
        sizePolicy.setHeightForWidth(self.reminders_sublist_rem_status_btn.sizePolicy().hasHeightForWidth())
        self.reminders_sublist_rem_status_btn.setSizePolicy(sizePolicy)
        self.reminders_sublist_rem_status_btn.setMinimumSize(QSize(30, 20))
        self.reminders_sublist_rem_status_btn.setMaximumSize(QSize(300, 16777215))
        self.reminders_sublist_rem_status_btn.setFont(font19)
        self.reminders_sublist_rem_status_btn.setContextMenuPolicy(Qt.CustomContextMenu)
        self.reminders_sublist_rem_status_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:rgb(55,60,85);\n"
"	color: rgb(211, 222, 233);\n"
"	border:none;\n"
"	border-radius:10px;\n"
"	border-bottom-left-radius:0px;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(65,70,100);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.reminders_sublist_rem_status_btn.setAutoDefault(True)
        self.reminders_sublist_rem_status_btn.setFlat(True)
        self.reminders_sublist_done_btn = QPushButton(self.reminders_sublist)
        self.reminders_sublist_done_btn.setObjectName(u"reminders_sublist_done_btn")
        self.reminders_sublist_done_btn.setGeometry(QRect(145, 275, 20, 20))
        sizePolicy.setHeightForWidth(self.reminders_sublist_done_btn.sizePolicy().hasHeightForWidth())
        self.reminders_sublist_done_btn.setSizePolicy(sizePolicy)
        self.reminders_sublist_done_btn.setMinimumSize(QSize(20, 20))
        self.reminders_sublist_done_btn.setMaximumSize(QSize(20, 20))
        self.reminders_sublist_done_btn.setFont(font25)
        self.reminders_sublist_done_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(140, 175, 100);\n"
"	border:1px solid rgb(50,55,70);	\n"
"	border-radius:10px;\n"
"	color: rgb(60, 65, 80);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(160, 195, 100);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(120, 150, 80);\n"
"}")
        self.reminders_sublist_done_btn.setAutoDefault(True)
        self.reminders_sublist_done_btn.setFlat(True)
        self.reminders_sublist_canc_btn = QPushButton(self.reminders_sublist)
        self.reminders_sublist_canc_btn.setObjectName(u"reminders_sublist_canc_btn")
        self.reminders_sublist_canc_btn.setGeometry(QRect(170, 275, 20, 20))
        sizePolicy.setHeightForWidth(self.reminders_sublist_canc_btn.sizePolicy().hasHeightForWidth())
        self.reminders_sublist_canc_btn.setSizePolicy(sizePolicy)
        self.reminders_sublist_canc_btn.setMinimumSize(QSize(20, 20))
        self.reminders_sublist_canc_btn.setMaximumSize(QSize(20, 20))
        self.reminders_sublist_canc_btn.setFont(font25)
        self.reminders_sublist_canc_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 75, 75);\n"
"	border:1px solid rgb(50,55,70);	\n"
"	border-radius:10px;\n"
"	color: rgb(60, 65, 80);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgb(190, 100, 100);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(150, 60, 60);\n"
"}")
        self.reminders_sublist_canc_btn.setAutoDefault(True)
        self.reminders_sublist_canc_btn.setFlat(True)
        self.reminders_sublist_status_lbl = QLabel(self.reminders_sublist)
        self.reminders_sublist_status_lbl.setObjectName(u"reminders_sublist_status_lbl")
        self.reminders_sublist_status_lbl.setGeometry(QRect(10, 300, 41, 30))
        self.reminders_sublist_status_lbl.setFont(font21)
        self.reminders_sublist_status_lbl.setStyleSheet(u"background-color:rgb(42,48,58);\n"
"padding-left: 5px;\n"
"color: rgb(180, 185, 195);\n"
"border:none;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border:1px solid rgb(50,55,70);\n"
"border-right:none;")
        self.reminders_sublist_done_canc_dte = QDateEdit(self.reminders_sublist)
        self.reminders_sublist_done_canc_dte.setObjectName(u"reminders_sublist_done_canc_dte")
        self.reminders_sublist_done_canc_dte.setGeometry(QRect(80, 349, 111, 21))
        self.reminders_sublist_done_canc_dte.setFont(font21)
        self.reminders_sublist_done_canc_dte.setStyleSheet(u"color: transparent;")
        self.reminders_sublist_done_canc_dte.setFrame(False)
        self.reminders_sublist_done_canc_dte.setReadOnly(True)
        self.reminders_sublist_done_canc_dte.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.reminders_sublist_done_canc_dte.setCalendarPopup(False)
        self.reminders_sublist_done_canc_lbl = QLabel(self.reminders_sublist)
        self.reminders_sublist_done_canc_lbl.setObjectName(u"reminders_sublist_done_canc_lbl")
        self.reminders_sublist_done_canc_lbl.setGeometry(QRect(5, 350, 71, 20))
        self.reminders_sublist_done_canc_lbl.setFont(font21)
        self.reminders_sublist_done_canc_lbl.setStyleSheet(u"color: transparent;")
        self.reminders_sublist_done_canc_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.reminders_stack.addWidget(self.reminders_sublist)
        self.reminders_sublist_done_canc_dte.raise_()
        self.reminders_sublist_lwg.raise_()
        self.reminders_sublist_item_led.raise_()
        self.reminders_sublist_clear_btn.raise_()
        self.reminders_sublist_delete_btn.raise_()
        self.reminders_sublist_write_btn.raise_()
        self.reminders_sublist_close_btn.raise_()
        self.reminders_sublist_reminder_led.raise_()
        self.reminders_sublist_due_cbx.raise_()
        self.reminders_sublist_due_dte.raise_()
        self.reminders_sublist_todo_btn.raise_()
        self.reminders_sublist_prgs_btn.raise_()
        self.reminders_sublist_ugnt_btn.raise_()
        self.reminders_sublist_star_btn.raise_()
        self.reminders_sublist_dlyd_btn.raise_()
        self.reminders_sublist_reminder_delete_btn.raise_()
        self.reminders_sublist_rem_status_btn.raise_()
        self.reminders_sublist_done_btn.raise_()
        self.reminders_sublist_canc_btn.raise_()
        self.reminders_sublist_status_lbl.raise_()
        self.reminders_sublist_done_canc_lbl.raise_()
        self.reminders_archive = QWidget()
        self.reminders_archive.setObjectName(u"reminders_archive")
        self.reminders_archive_done_btn = QPushButton(self.reminders_archive)
        self.reminders_archive_done_btn.setObjectName(u"reminders_archive_done_btn")
        self.reminders_archive_done_btn.setGeometry(QRect(370, 340, 141, 30))
        sizePolicy.setHeightForWidth(self.reminders_archive_done_btn.sizePolicy().hasHeightForWidth())
        self.reminders_archive_done_btn.setSizePolicy(sizePolicy)
        self.reminders_archive_done_btn.setMinimumSize(QSize(30, 20))
        self.reminders_archive_done_btn.setMaximumSize(QSize(300, 16777215))
        self.reminders_archive_done_btn.setFont(font18)
        self.reminders_archive_done_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:rgb(42,48,58);	\n"
"	color: rgb(211, 222, 233);\n"
"	border:none;\n"
"	border-radius:10px;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.reminders_archive_done_btn.setAutoDefault(True)
        self.reminders_archive_done_btn.setFlat(True)
        self.reminders_archive_lwg = QListWidget(self.reminders_archive)
        self.reminders_archive_lwg.setObjectName(u"reminders_archive_lwg")
        self.reminders_archive_lwg.setGeometry(QRect(0, 40, 511, 281))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush10 = QBrush(QColor(166, 177, 199, 128))
        brush10.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        brush11 = QBrush(QColor(166, 177, 199, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush11)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush3)
        brush12 = QBrush(QColor(166, 177, 199, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.reminders_archive_lwg.setPalette(palette2)
        self.reminders_archive_lwg.setFont(font19)
        self.reminders_archive_lwg.setStyleSheet(u"")
        self.reminders_archive_lwg.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.reminders_archive_lwg.setProperty("showDropIndicator", False)
        self.reminders_archive_lwg.setDragEnabled(False)
        self.reminders_archive_lwg.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.reminders_archive_lwg.setAlternatingRowColors(True)
        self.reminders_archive_lwg.setLayoutMode(QListView.SinglePass)
        self.reminders_archive_lwg.setSpacing(1)
        self.reminders_archive_lwg.setViewMode(QListView.ListMode)
        self.reminders_archive_lwg.setUniformItemSizes(False)
        self.reminders_archive_lwg.setSelectionRectVisible(False)
        self.reminders_archive_title = QLabel(self.reminders_archive)
        self.reminders_archive_title.setObjectName(u"reminders_archive_title")
        self.reminders_archive_title.setGeometry(QRect(5, 0, 81, 31))
        self.reminders_archive_title.setFont(font2)
        self.reminders_archive_title.setStyleSheet(u"color: rgb(166, 111, 77);")
        self.reminders_archive_limit_cmb = QComboBox(self.reminders_archive)
        self.reminders_archive_limit_cmb.addItem("")
        self.reminders_archive_limit_cmb.addItem("")
        self.reminders_archive_limit_cmb.addItem("")
        self.reminders_archive_limit_cmb.addItem("")
        self.reminders_archive_limit_cmb.addItem("")
        self.reminders_archive_limit_cmb.setObjectName(u"reminders_archive_limit_cmb")
        self.reminders_archive_limit_cmb.setGeometry(QRect(110, 6, 71, 21))
        self.reminders_archive_limit_cmb.setMinimumSize(QSize(0, 21))
        self.reminders_archive_limit_cmb.setMaximumSize(QSize(16777215, 30))
        self.reminders_archive_limit_cmb.setFont(font14)
        self.reminders_archive_limit_cmb.setStyleSheet(u"QComboBox {\n"
"	background:transparent;\n"
"	selection-background-color: transparent;\n"
"    color: rgb(155, 166, 200);\n"
"	padding-left:3px;\n"
"	margin-right:3px;\n"
"	border:none;\n"
"	border-bottom:1px solid rgb(60, 70, 80);\n"
"	outline:0px;\n"
"}\n"
"QComboBox::drop-down:button{\n"
"	margin-right: 5px;\n"
"    margin-top: 7px;\n"
"	margin-bottom: 6px;\n"
"    height: 8px;\n"
"    width: 8px;\n"
"    border-radius: 4px;\n"
"    background-color: rgb(177, 188, 233);\n"
"}\n"
"QComboBox:drop-down:hover{\n"
"    background-color: rgb(166, 199, 255);;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(60, 65, 80);\n"
"    color: rgb(240, 240, 245);\n"
"    border:1px solid rgb(88, 99, 111);\n"
"    padding:5px;\n"
"	outline:0px;\n"
"	selection-background-color: rgb(60, 65, 80);\n"
"	selection-color:rgb(133, 166, 255);\n"
"}")
        self.reminders_archive_limit_cmb.setMaxVisibleItems(40)
        self.reminders_archive_limit_cmb.setFrame(False)
        self.reminders_archive_limit_lbl = QLabel(self.reminders_archive)
        self.reminders_archive_limit_lbl.setObjectName(u"reminders_archive_limit_lbl")
        self.reminders_archive_limit_lbl.setGeometry(QRect(177, 6, 271, 21))
        self.reminders_archive_limit_lbl.setFont(font4)
        self.reminders_archive_limit_lbl.setStyleSheet(u"border-bottom:1px solid rgb(60, 70, 80);\n"
"padding-left: 7px;")
        self.reminders_stack.addWidget(self.reminders_archive)
        self.reminders_archive_done_btn.raise_()
        self.reminders_archive_lwg.raise_()
        self.reminders_archive_title.raise_()
        self.reminders_archive_limit_lbl.raise_()
        self.reminders_archive_limit_cmb.raise_()
        self.reminders_history_btn = QPushButton(self.reminders_gbx)
        self.reminders_history_btn.setObjectName(u"reminders_history_btn")
        self.reminders_history_btn.setGeometry(QRect(150, 16, 61, 20))
        sizePolicy.setHeightForWidth(self.reminders_history_btn.sizePolicy().hasHeightForWidth())
        self.reminders_history_btn.setSizePolicy(sizePolicy)
        self.reminders_history_btn.setMinimumSize(QSize(30, 20))
        self.reminders_history_btn.setMaximumSize(QSize(200, 16777215))
        self.reminders_history_btn.setFont(font6)
        self.reminders_history_btn.setStyleSheet(u"QPushButton {\n"
"	background-color:rgb(45,50,60);	\n"
"	color: rgb(200, 175, 75);\n"
"	border:none;\n"
"	border-radius:10px;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.reminders_history_btn.setAutoDefault(True)
        self.reminders_history_btn.setFlat(True)
        self.macros_gbx = QGroupBox(self.centralwidget)
        self.macros_gbx.setObjectName(u"macros_gbx")
        self.macros_gbx.setGeometry(QRect(20, 750, 550, 451))
        self.macros_gbx.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(43, 48, 58);\n"
"	border-radius:10%;\n"
"	border:1px solid rgb(45,50,65)\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(38,43,53);\n"
"	border:1px solid rgb(36,41,51)\n"
"}")
        self.macros_title_btn = QPushButton(self.macros_gbx)
        self.macros_title_btn.setObjectName(u"macros_title_btn")
        self.macros_title_btn.setGeometry(QRect(10, 10, 161, 31))
        sizePolicy.setHeightForWidth(self.macros_title_btn.sizePolicy().hasHeightForWidth())
        self.macros_title_btn.setSizePolicy(sizePolicy)
        self.macros_title_btn.setMinimumSize(QSize(0, 30))
        self.macros_title_btn.setMaximumSize(QSize(16777215, 16777215))
        self.macros_title_btn.setFont(font7)
        self.macros_title_btn.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(143, 188, 187);\n"
"	background:none;\n"
"	border:none;\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}")
        self.macros_title_btn.setAutoDefault(True)
        self.macros_title_btn.setFlat(True)
        self.macros_prev_pt_btn = QPushButton(self.macros_gbx)
        self.macros_prev_pt_btn.setObjectName(u"macros_prev_pt_btn")
        self.macros_prev_pt_btn.setGeometry(QRect(20, 50, 120, 30))
        sizePolicy3.setHeightForWidth(self.macros_prev_pt_btn.sizePolicy().hasHeightForWidth())
        self.macros_prev_pt_btn.setSizePolicy(sizePolicy3)
        self.macros_prev_pt_btn.setMinimumSize(QSize(0, 30))
        self.macros_prev_pt_btn.setMaximumSize(QSize(16777215, 16777215))
        font28 = QFont()
        font28.setFamilies([u"\uc11c\uc6b8\ub0a8\uc0b0 \uc7a5\uccb4 B"])
        font28.setPointSize(13)
        self.macros_prev_pt_btn.setFont(font28)
        self.macros_prev_pt_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(77, 111, 177);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(122,155,222);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(77, 111, 177);\n"
"}")
        self.macros_prev_pt_btn.setFlat(True)
        self.macros_check_ins_btn = QPushButton(self.macros_gbx)
        self.macros_check_ins_btn.setObjectName(u"macros_check_ins_btn")
        self.macros_check_ins_btn.setGeometry(QRect(150, 50, 120, 30))
        sizePolicy3.setHeightForWidth(self.macros_check_ins_btn.sizePolicy().hasHeightForWidth())
        self.macros_check_ins_btn.setSizePolicy(sizePolicy3)
        self.macros_check_ins_btn.setMinimumSize(QSize(0, 30))
        self.macros_check_ins_btn.setMaximumSize(QSize(16777215, 16777215))
        font29 = QFont()
        font29.setFamilies([u"\uc11c\uc6b8\ub0a8\uc0b0 \uc7a5\uccb4 B"])
        font29.setPointSize(13)
        font29.setBold(False)
        font29.setItalic(False)
        font29.setStrikeOut(False)
        font29.setKerning(True)
        font29.setStyleStrategy(QFont.PreferDefault)
        self.macros_check_ins_btn.setFont(font29)
        self.macros_check_ins_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(155, 122, 88);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(188,144,111);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(155, 122, 88);\n"
"}")
        self.macros_check_ins_btn.setFlat(True)
        self.macros_no_ins_btn = QPushButton(self.macros_gbx)
        self.macros_no_ins_btn.setObjectName(u"macros_no_ins_btn")
        self.macros_no_ins_btn.setGeometry(QRect(280, 50, 120, 30))
        sizePolicy3.setHeightForWidth(self.macros_no_ins_btn.sizePolicy().hasHeightForWidth())
        self.macros_no_ins_btn.setSizePolicy(sizePolicy3)
        self.macros_no_ins_btn.setMinimumSize(QSize(0, 30))
        self.macros_no_ins_btn.setMaximumSize(QSize(16777215, 16777215))
        self.macros_no_ins_btn.setFont(font28)
        self.macros_no_ins_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(88, 144, 88);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(111,177,111);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(88, 144, 88);\n"
"}")
        self.macros_no_ins_btn.setFlat(True)
        self.macros_next_pt_btn = QPushButton(self.macros_gbx)
        self.macros_next_pt_btn.setObjectName(u"macros_next_pt_btn")
        self.macros_next_pt_btn.setGeometry(QRect(410, 50, 120, 30))
        sizePolicy3.setHeightForWidth(self.macros_next_pt_btn.sizePolicy().hasHeightForWidth())
        self.macros_next_pt_btn.setSizePolicy(sizePolicy3)
        self.macros_next_pt_btn.setMinimumSize(QSize(0, 30))
        self.macros_next_pt_btn.setMaximumSize(QSize(16777215, 16777215))
        self.macros_next_pt_btn.setFont(font28)
        self.macros_next_pt_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(77, 111, 177);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(122,155,222);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(77, 111, 177);\n"
"}")
        self.macros_next_pt_btn.setFlat(True)
        self.macros_phytx_btn = QPushButton(self.macros_gbx)
        self.macros_phytx_btn.setObjectName(u"macros_phytx_btn")
        self.macros_phytx_btn.setGeometry(QRect(410, 130, 120, 30))
        sizePolicy3.setHeightForWidth(self.macros_phytx_btn.sizePolicy().hasHeightForWidth())
        self.macros_phytx_btn.setSizePolicy(sizePolicy3)
        self.macros_phytx_btn.setMinimumSize(QSize(0, 30))
        self.macros_phytx_btn.setMaximumSize(QSize(16777215, 16777215))
        self.macros_phytx_btn.setFont(font28)
        self.macros_phytx_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(122, 88, 155);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(155,100,199);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(122, 88, 155);\n"
"}")
        self.macros_phytx_btn.setFlat(True)
        self.macros_fluid_btn = QPushButton(self.macros_gbx)
        self.macros_fluid_btn.setObjectName(u"macros_fluid_btn")
        self.macros_fluid_btn.setGeometry(QRect(280, 130, 120, 30))
        sizePolicy3.setHeightForWidth(self.macros_fluid_btn.sizePolicy().hasHeightForWidth())
        self.macros_fluid_btn.setSizePolicy(sizePolicy3)
        self.macros_fluid_btn.setMinimumSize(QSize(0, 30))
        self.macros_fluid_btn.setMaximumSize(QSize(16777215, 16777215))
        self.macros_fluid_btn.setFont(font28)
        self.macros_fluid_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(77, 122, 144);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(99,155,199);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(77, 122, 144);\n"
"}")
        self.macros_fluid_btn.setFlat(True)
        self.macros_chr_btn = QPushButton(self.macros_gbx)
        self.macros_chr_btn.setObjectName(u"macros_chr_btn")
        self.macros_chr_btn.setGeometry(QRect(20, 170, 120, 30))
        sizePolicy3.setHeightForWidth(self.macros_chr_btn.sizePolicy().hasHeightForWidth())
        self.macros_chr_btn.setSizePolicy(sizePolicy3)
        self.macros_chr_btn.setMinimumSize(QSize(0, 30))
        self.macros_chr_btn.setMaximumSize(QSize(16777215, 16777215))
        self.macros_chr_btn.setFont(font28)
        self.macros_chr_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(133, 100, 88);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(166,122,100);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(111, 88, 77);\n"
"}")
        self.macros_chr_btn.setFlat(True)
        self.macros_chr_etc_btn = QPushButton(self.macros_gbx)
        self.macros_chr_etc_btn.setObjectName(u"macros_chr_etc_btn")
        self.macros_chr_etc_btn.setGeometry(QRect(150, 170, 120, 30))
        sizePolicy3.setHeightForWidth(self.macros_chr_etc_btn.sizePolicy().hasHeightForWidth())
        self.macros_chr_etc_btn.setSizePolicy(sizePolicy3)
        self.macros_chr_etc_btn.setMinimumSize(QSize(0, 30))
        self.macros_chr_etc_btn.setMaximumSize(QSize(16777215, 16777215))
        self.macros_chr_etc_btn.setFont(font28)
        self.macros_chr_etc_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(122, 100, 88);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(155,133,111);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(122, 100, 88);\n"
"}")
        self.macros_chr_etc_btn.setFlat(True)
        self.macros_lab_studies_btn = QPushButton(self.macros_gbx)
        self.macros_lab_studies_btn.setObjectName(u"macros_lab_studies_btn")
        self.macros_lab_studies_btn.setGeometry(QRect(20, 210, 120, 30))
        sizePolicy3.setHeightForWidth(self.macros_lab_studies_btn.sizePolicy().hasHeightForWidth())
        self.macros_lab_studies_btn.setSizePolicy(sizePolicy3)
        self.macros_lab_studies_btn.setMinimumSize(QSize(0, 30))
        self.macros_lab_studies_btn.setMaximumSize(QSize(16777215, 16777215))
        self.macros_lab_studies_btn.setFont(font28)
        self.macros_lab_studies_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(155, 100, 111);	\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(177,122,133);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(155, 100, 111);	\n"
"}")
        self.macros_lab_studies_btn.setFlat(True)
        self.macros_other_studies_btn = QPushButton(self.macros_gbx)
        self.macros_other_studies_btn.setObjectName(u"macros_other_studies_btn")
        self.macros_other_studies_btn.setGeometry(QRect(150, 210, 120, 30))
        sizePolicy3.setHeightForWidth(self.macros_other_studies_btn.sizePolicy().hasHeightForWidth())
        self.macros_other_studies_btn.setSizePolicy(sizePolicy3)
        self.macros_other_studies_btn.setMinimumSize(QSize(0, 30))
        self.macros_other_studies_btn.setMaximumSize(QSize(16777215, 16777215))
        self.macros_other_studies_btn.setFont(font28)
        self.macros_other_studies_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(122, 100, 177);	\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(144,122,199);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(122, 100, 177);	\n"
"}")
        self.macros_other_studies_btn.setFlat(True)
        self.macros_templates_btn = QPushButton(self.macros_gbx)
        self.macros_templates_btn.setObjectName(u"macros_templates_btn")
        self.macros_templates_btn.setGeometry(QRect(20, 130, 251, 30))
        sizePolicy3.setHeightForWidth(self.macros_templates_btn.sizePolicy().hasHeightForWidth())
        self.macros_templates_btn.setSizePolicy(sizePolicy3)
        self.macros_templates_btn.setMinimumSize(QSize(0, 30))
        self.macros_templates_btn.setMaximumSize(QSize(16777215, 16777215))
        self.macros_templates_btn.setFont(font28)
        self.macros_templates_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(77, 133, 144);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(99,166,177);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(77, 133, 144);\n"
"}")
        self.macros_templates_btn.setFlat(True)
        self.macros_other_comments_btn = QPushButton(self.macros_gbx)
        self.macros_other_comments_btn.setObjectName(u"macros_other_comments_btn")
        self.macros_other_comments_btn.setGeometry(QRect(280, 210, 251, 30))
        sizePolicy3.setHeightForWidth(self.macros_other_comments_btn.sizePolicy().hasHeightForWidth())
        self.macros_other_comments_btn.setSizePolicy(sizePolicy3)
        self.macros_other_comments_btn.setMinimumSize(QSize(0, 30))
        self.macros_other_comments_btn.setMaximumSize(QSize(16777215, 16777215))
        self.macros_other_comments_btn.setFont(font28)
        self.macros_other_comments_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(100, 111, 188);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(111,133,200);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(100, 111, 188);\n"
"}")
        self.macros_other_comments_btn.setFlat(True)
        self.macros_vac_autostart_btn = QPushButton(self.macros_gbx)
        self.macros_vac_autostart_btn.setObjectName(u"macros_vac_autostart_btn")
        self.macros_vac_autostart_btn.setGeometry(QRect(280, 290, 120, 30))
        sizePolicy3.setHeightForWidth(self.macros_vac_autostart_btn.sizePolicy().hasHeightForWidth())
        self.macros_vac_autostart_btn.setSizePolicy(sizePolicy3)
        self.macros_vac_autostart_btn.setMinimumSize(QSize(0, 30))
        self.macros_vac_autostart_btn.setMaximumSize(QSize(16777215, 16777215))
        self.macros_vac_autostart_btn.setFont(font28)
        self.macros_vac_autostart_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(88, 122, 111);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(111,144,133);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(88, 122, 111);\n"
"}")
        self.macros_vac_autostart_btn.setFlat(True)
        self.macros_labeler_btn = QPushButton(self.macros_gbx)
        self.macros_labeler_btn.setObjectName(u"macros_labeler_btn")
        self.macros_labeler_btn.setGeometry(QRect(20, 290, 120, 30))
        sizePolicy3.setHeightForWidth(self.macros_labeler_btn.sizePolicy().hasHeightForWidth())
        self.macros_labeler_btn.setSizePolicy(sizePolicy3)
        self.macros_labeler_btn.setMinimumSize(QSize(0, 30))
        self.macros_labeler_btn.setMaximumSize(QSize(16777215, 16777215))
        self.macros_labeler_btn.setFont(font28)
        self.macros_labeler_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(155, 133, 66);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(177,155,99);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(155, 133, 66);\n"
"}")
        self.macros_labeler_btn.setFlat(True)
        self.macros_vac_input_btn = QPushButton(self.macros_gbx)
        self.macros_vac_input_btn.setObjectName(u"macros_vac_input_btn")
        self.macros_vac_input_btn.setGeometry(QRect(150, 290, 120, 30))
        sizePolicy3.setHeightForWidth(self.macros_vac_input_btn.sizePolicy().hasHeightForWidth())
        self.macros_vac_input_btn.setSizePolicy(sizePolicy3)
        self.macros_vac_input_btn.setMinimumSize(QSize(0, 30))
        self.macros_vac_input_btn.setMaximumSize(QSize(16777215, 16777215))
        self.macros_vac_input_btn.setFont(font28)
        self.macros_vac_input_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(88, 122, 155);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(111,144,177);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(88, 122, 155);\n"
"}")
        self.macros_vac_input_btn.setFlat(True)
        self.macros_practive_title_lbl = QLabel(self.macros_gbx)
        self.macros_practive_title_lbl.setObjectName(u"macros_practive_title_lbl")
        self.macros_practive_title_lbl.setGeometry(QRect(20, 80, 511, 31))
        font30 = QFont()
        font30.setFamilies([u"\uc11c\uc6b8\ub0a8\uc0b0\uccb4 B"])
        font30.setPointSize(12)
        self.macros_practive_title_lbl.setFont(font30)
        self.macros_practive_title_lbl.setStyleSheet(u"color: rgb(180, 185, 194);")
        self.macros_practive_title_lbl.setAlignment(Qt.AlignCenter)
        self.macros_comments_title_lbl = QLabel(self.macros_gbx)
        self.macros_comments_title_lbl.setObjectName(u"macros_comments_title_lbl")
        self.macros_comments_title_lbl.setGeometry(QRect(20, 240, 511, 31))
        self.macros_comments_title_lbl.setFont(font30)
        self.macros_comments_title_lbl.setStyleSheet(u"color: rgb(180, 185, 194);")
        self.macros_comments_title_lbl.setAlignment(Qt.AlignCenter)
        self.macros_vac_title_lbl = QLabel(self.macros_gbx)
        self.macros_vac_title_lbl.setObjectName(u"macros_vac_title_lbl")
        self.macros_vac_title_lbl.setGeometry(QRect(20, 320, 511, 31))
        self.macros_vac_title_lbl.setFont(font30)
        self.macros_vac_title_lbl.setStyleSheet(u"color: rgb(180, 185, 194);")
        self.macros_vac_title_lbl.setAlignment(Qt.AlignCenter)
        self.macros_reserve_2_btn = QPushButton(self.macros_gbx)
        self.macros_reserve_2_btn.setObjectName(u"macros_reserve_2_btn")
        self.macros_reserve_2_btn.setGeometry(QRect(280, 370, 121, 30))
        sizePolicy3.setHeightForWidth(self.macros_reserve_2_btn.sizePolicy().hasHeightForWidth())
        self.macros_reserve_2_btn.setSizePolicy(sizePolicy3)
        self.macros_reserve_2_btn.setMinimumSize(QSize(0, 30))
        self.macros_reserve_2_btn.setMaximumSize(QSize(16777215, 16777215))
        font31 = QFont()
        font31.setFamilies([u"\uc11c\uc6b8\ub0a8\uc0b0 \uc7a5\uccb4 B"])
        font31.setPointSize(12)
        self.macros_reserve_2_btn.setFont(font31)
        self.macros_reserve_2_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(77, 88, 111);\n"
"	border:0px;\n"
"	border-radius:10%;\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(111,122,144);\n"
"}\n"
"QPushButton:pressed {\n"
"	color:rgb(60,70,90);\n"
"}")
        self.macros_reserve_2_btn.setFlat(True)
        self.macros_flu_btn = QPushButton(self.macros_gbx)
        self.macros_flu_btn.setObjectName(u"macros_flu_btn")
        self.macros_flu_btn.setGeometry(QRect(20, 370, 120, 30))
        sizePolicy3.setHeightForWidth(self.macros_flu_btn.sizePolicy().hasHeightForWidth())
        self.macros_flu_btn.setSizePolicy(sizePolicy3)
        self.macros_flu_btn.setMinimumSize(QSize(0, 30))
        self.macros_flu_btn.setMaximumSize(QSize(16777215, 16777215))
        self.macros_flu_btn.setFont(font28)
        self.macros_flu_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(88, 122, 188);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(111,144,200);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(88, 122, 188);\n"
"}")
        self.macros_flu_btn.setFlat(True)
        self.macros_reserve_3_btn = QPushButton(self.macros_gbx)
        self.macros_reserve_3_btn.setObjectName(u"macros_reserve_3_btn")
        self.macros_reserve_3_btn.setGeometry(QRect(410, 370, 120, 30))
        sizePolicy3.setHeightForWidth(self.macros_reserve_3_btn.sizePolicy().hasHeightForWidth())
        self.macros_reserve_3_btn.setSizePolicy(sizePolicy3)
        self.macros_reserve_3_btn.setMinimumSize(QSize(0, 30))
        self.macros_reserve_3_btn.setMaximumSize(QSize(16777215, 16777215))
        self.macros_reserve_3_btn.setFont(font31)
        self.macros_reserve_3_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(77, 88, 111);\n"
"	border:0px;\n"
"	border-radius:10%;\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(111,122,144);\n"
"}\n"
"QPushButton:pressed {\n"
"	color:rgb(60,70,90);\n"
"}")
        self.macros_reserve_3_btn.setFlat(True)
        self.macros_reserve_1_btn = QPushButton(self.macros_gbx)
        self.macros_reserve_1_btn.setObjectName(u"macros_reserve_1_btn")
        self.macros_reserve_1_btn.setGeometry(QRect(150, 370, 120, 30))
        sizePolicy3.setHeightForWidth(self.macros_reserve_1_btn.sizePolicy().hasHeightForWidth())
        self.macros_reserve_1_btn.setSizePolicy(sizePolicy3)
        self.macros_reserve_1_btn.setMinimumSize(QSize(0, 30))
        self.macros_reserve_1_btn.setMaximumSize(QSize(16777215, 16777215))
        self.macros_reserve_1_btn.setFont(font31)
        self.macros_reserve_1_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(155, 111, 133);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(177,133,155);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(155, 111, 133);\n"
"}")
        self.macros_reserve_1_btn.setFlat(True)
        self.macros_others_title_lbl = QLabel(self.macros_gbx)
        self.macros_others_title_lbl.setObjectName(u"macros_others_title_lbl")
        self.macros_others_title_lbl.setGeometry(QRect(20, 400, 511, 31))
        self.macros_others_title_lbl.setFont(font30)
        self.macros_others_title_lbl.setStyleSheet(u"color: rgb(180, 185, 194);")
        self.macros_others_title_lbl.setAlignment(Qt.AlignCenter)
        self.macros_obsv_btn = QPushButton(self.macros_gbx)
        self.macros_obsv_btn.setObjectName(u"macros_obsv_btn")
        self.macros_obsv_btn.setGeometry(QRect(279, 170, 251, 30))
        sizePolicy3.setHeightForWidth(self.macros_obsv_btn.sizePolicy().hasHeightForWidth())
        self.macros_obsv_btn.setSizePolicy(sizePolicy3)
        self.macros_obsv_btn.setMinimumSize(QSize(0, 30))
        self.macros_obsv_btn.setMaximumSize(QSize(16777215, 16777215))
        self.macros_obsv_btn.setFont(font28)
        self.macros_obsv_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(133, 133, 88);	\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(155,155,99);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(144, 144, 100);	\n"
"}")
        self.macros_obsv_btn.setFlat(True)
        self.macros_vac_log_btn = QPushButton(self.macros_gbx)
        self.macros_vac_log_btn.setObjectName(u"macros_vac_log_btn")
        self.macros_vac_log_btn.setGeometry(QRect(410, 290, 120, 30))
        sizePolicy3.setHeightForWidth(self.macros_vac_log_btn.sizePolicy().hasHeightForWidth())
        self.macros_vac_log_btn.setSizePolicy(sizePolicy3)
        self.macros_vac_log_btn.setMinimumSize(QSize(0, 30))
        self.macros_vac_log_btn.setMaximumSize(QSize(16777215, 16777215))
        self.macros_vac_log_btn.setFont(font28)
        self.macros_vac_log_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(122, 88, 88);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(144,111,111);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(122, 88, 88);\n"
"}")
        self.macros_vac_log_btn.setFlat(True)
        self.info_gbx = QGroupBox(self.centralwidget)
        self.info_gbx.setObjectName(u"info_gbx")
        self.info_gbx.setGeometry(QRect(20, 1970, 550, 100))
        self.info_zinsss_lbl = QLabel(self.info_gbx)
        self.info_zinsss_lbl.setObjectName(u"info_zinsss_lbl")
        self.info_zinsss_lbl.setGeometry(QRect(140, 19, 391, 20))
        font32 = QFont()
        font32.setFamilies([u"\uc11c\uc6b8\ud55c\uac15 \uc7a5\uccb4 B"])
        font32.setPointSize(12)
        self.info_zinsss_lbl.setFont(font32)
        self.info_zinsss_lbl.setStyleSheet(u"border:none;\n"
"color: rgb(125, 150, 110);")
        self.info_zinsss_lbl.setAlignment(Qt.AlignCenter)
        self.info_not_for_sale_lbl = QLabel(self.info_gbx)
        self.info_not_for_sale_lbl.setObjectName(u"info_not_for_sale_lbl")
        self.info_not_for_sale_lbl.setGeometry(QRect(140, 60, 390, 20))
        self.info_not_for_sale_lbl.setFont(font11)
        self.info_not_for_sale_lbl.setStyleSheet(u"border:none;\n"
"color: rgb(200, 125, 175);")
        self.info_not_for_sale_lbl.setAlignment(Qt.AlignCenter)
        self.info_title_lbl = QPushButton(self.info_gbx)
        self.info_title_lbl.setObjectName(u"info_title_lbl")
        self.info_title_lbl.setGeometry(QRect(10, 10, 161, 31))
        sizePolicy.setHeightForWidth(self.info_title_lbl.sizePolicy().hasHeightForWidth())
        self.info_title_lbl.setSizePolicy(sizePolicy)
        self.info_title_lbl.setMinimumSize(QSize(0, 30))
        self.info_title_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.info_title_lbl.setFont(font7)
        self.info_title_lbl.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(143, 188, 187);\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"}")
        self.info_title_lbl.setAutoDefault(True)
        self.info_title_lbl.setFlat(True)
        self.info_yhshfm_address_lbl = QLabel(self.info_gbx)
        self.info_yhshfm_address_lbl.setObjectName(u"info_yhshfm_address_lbl")
        self.info_yhshfm_address_lbl.setGeometry(QRect(140, 40, 390, 20))
        self.info_yhshfm_address_lbl.setFont(font32)
        self.info_yhshfm_address_lbl.setStyleSheet(u"border:none;\n"
"color: rgb(111, 111, 122);")
        self.info_yhshfm_address_lbl.setAlignment(Qt.AlignCenter)
        self.apps_gbx = QGroupBox(self.centralwidget)
        self.apps_gbx.setObjectName(u"apps_gbx")
        self.apps_gbx.setGeometry(QRect(20, 1220, 550, 731))
        self.apps_gbx.setStyleSheet(u"QWidget{	\n"
"	background-color: rgb(40, 45, 55);\n"
"}")
        self.apps_med_docs_btn = QPushButton(self.apps_gbx)
        self.apps_med_docs_btn.setObjectName(u"apps_med_docs_btn")
        self.apps_med_docs_btn.setGeometry(QRect(280, 10, 120, 30))
        sizePolicy3.setHeightForWidth(self.apps_med_docs_btn.sizePolicy().hasHeightForWidth())
        self.apps_med_docs_btn.setSizePolicy(sizePolicy3)
        self.apps_med_docs_btn.setMinimumSize(QSize(0, 30))
        self.apps_med_docs_btn.setMaximumSize(QSize(16777215, 16777215))
        self.apps_med_docs_btn.setFont(font2)
        self.apps_med_docs_btn.setStyleSheet(u"QPushButton {\n"
"	font: bold italic 12pt \"Lucida Sans\";\n"
"	color: rgb(165, 170, 180);\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(125,175,225);\n"
"}\n"
"QPushButton:pressed {\n"
"	color:rgb(75,75,90);\n"
"}")
        self.apps_med_docs_btn.setFlat(True)
        self.apps_quick_saves_btn = QPushButton(self.apps_gbx)
        self.apps_quick_saves_btn.setObjectName(u"apps_quick_saves_btn")
        self.apps_quick_saves_btn.setGeometry(QRect(150, 10, 120, 30))
        sizePolicy3.setHeightForWidth(self.apps_quick_saves_btn.sizePolicy().hasHeightForWidth())
        self.apps_quick_saves_btn.setSizePolicy(sizePolicy3)
        self.apps_quick_saves_btn.setMinimumSize(QSize(0, 30))
        self.apps_quick_saves_btn.setMaximumSize(QSize(16777215, 16777215))
        self.apps_quick_saves_btn.setFont(font2)
        self.apps_quick_saves_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(165, 170, 180);\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(125,175,225);\n"
"}\n"
"QPushButton:pressed {\n"
"	color:rgb(75,75,90);\n"
"}")
        self.apps_quick_saves_btn.setFlat(True)
        self.apps_sticky_btn = QPushButton(self.apps_gbx)
        self.apps_sticky_btn.setObjectName(u"apps_sticky_btn")
        self.apps_sticky_btn.setGeometry(QRect(20, 10, 120, 30))
        sizePolicy3.setHeightForWidth(self.apps_sticky_btn.sizePolicy().hasHeightForWidth())
        self.apps_sticky_btn.setSizePolicy(sizePolicy3)
        self.apps_sticky_btn.setMinimumSize(QSize(0, 30))
        self.apps_sticky_btn.setMaximumSize(QSize(16777215, 16777215))
        self.apps_sticky_btn.setFont(font2)
        self.apps_sticky_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(165, 170, 180);\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(125,175,225);\n"
"}\n"
"QPushButton:pressed {\n"
"	color:rgb(75,75,90);\n"
"}")
        self.apps_sticky_btn.setFlat(True)
        self.apps_labeler_btn = QPushButton(self.apps_gbx)
        self.apps_labeler_btn.setObjectName(u"apps_labeler_btn")
        self.apps_labeler_btn.setGeometry(QRect(20, 39, 120, 30))
        sizePolicy3.setHeightForWidth(self.apps_labeler_btn.sizePolicy().hasHeightForWidth())
        self.apps_labeler_btn.setSizePolicy(sizePolicy3)
        self.apps_labeler_btn.setMinimumSize(QSize(0, 30))
        self.apps_labeler_btn.setMaximumSize(QSize(16777215, 16777215))
        self.apps_labeler_btn.setFont(font2)
        self.apps_labeler_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(165, 170, 180);\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(125,175,225);\n"
"}\n"
"QPushButton:pressed {\n"
"	color:rgb(75,75,90);\n"
"}")
        self.apps_labeler_btn.setFlat(True)
        self.apps_settings_btn = QPushButton(self.apps_gbx)
        self.apps_settings_btn.setObjectName(u"apps_settings_btn")
        self.apps_settings_btn.setGeometry(QRect(280, 39, 120, 30))
        sizePolicy3.setHeightForWidth(self.apps_settings_btn.sizePolicy().hasHeightForWidth())
        self.apps_settings_btn.setSizePolicy(sizePolicy3)
        self.apps_settings_btn.setMinimumSize(QSize(0, 30))
        self.apps_settings_btn.setMaximumSize(QSize(16777215, 16777215))
        self.apps_settings_btn.setFont(font2)
        self.apps_settings_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(165, 170, 180);\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(125,175,225);\n"
"}\n"
"QPushButton:pressed {\n"
"	color:rgb(75,75,90);\n"
"}")
        self.apps_settings_btn.setFlat(True)
        self.apps_studies_btn = QPushButton(self.apps_gbx)
        self.apps_studies_btn.setObjectName(u"apps_studies_btn")
        self.apps_studies_btn.setGeometry(QRect(410, 10, 120, 30))
        sizePolicy3.setHeightForWidth(self.apps_studies_btn.sizePolicy().hasHeightForWidth())
        self.apps_studies_btn.setSizePolicy(sizePolicy3)
        self.apps_studies_btn.setMinimumSize(QSize(0, 30))
        self.apps_studies_btn.setMaximumSize(QSize(16777215, 16777215))
        self.apps_studies_btn.setFont(font2)
        self.apps_studies_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(165, 170, 180);\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(125,175,225);\n"
"}\n"
"QPushButton:pressed {\n"
"	color:rgb(75,75,90);\n"
"}")
        self.apps_studies_btn.setFlat(True)
        self.apps_covid_btn = QPushButton(self.apps_gbx)
        self.apps_covid_btn.setObjectName(u"apps_covid_btn")
        self.apps_covid_btn.setGeometry(QRect(150, 39, 120, 30))
        sizePolicy3.setHeightForWidth(self.apps_covid_btn.sizePolicy().hasHeightForWidth())
        self.apps_covid_btn.setSizePolicy(sizePolicy3)
        self.apps_covid_btn.setMinimumSize(QSize(0, 30))
        self.apps_covid_btn.setMaximumSize(QSize(16777215, 16777215))
        self.apps_covid_btn.setFont(font2)
        self.apps_covid_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(165, 170, 180);\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(125,175,225);\n"
"}\n"
"QPushButton:pressed {\n"
"	color:rgb(75,75,90);\n"
"}")
        self.apps_covid_btn.setFlat(True)
        self.apps_stack = QStackedWidget(self.apps_gbx)
        self.apps_stack.setObjectName(u"apps_stack")
        self.apps_stack.setGeometry(QRect(10, 69, 531, 651))
        self.apps_stack.setStyleSheet(u"QWidget{\n"
"	background:transparent;\n"
"}\n"
"QStackedWidget{\n"
"	border-top:1px solid rgb(110,120,140);\n"
"	background:transparent;\n"
"}\n"
"QComboBox {\n"
"	background:transparent;\n"
"	selection-background-color:transparent;\n"
"    color: rgb(133, 166, 255);\n"
"	margin-right:3px;\n"
"	padding-left: 10px;\n"
"	outline:0px;\n"
"}\n"
"QComboBox::drop-down:button{\n"
"	background-color: rgb(166, 177, 200);\n"
"	margin-right:5px;\n"
"    margin-top:9px;\n"
"	margin-bottom:6px;\n"
"    height:10px;\n"
"    width:10px;\n"
"    border-radius:5px;\n"
"}\n"
"QComboBox:drop-down:hover{\n"
"    background-color: rgb(166, 199, 255);;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background: rgb(55, 60, 75);\n"
"    selection-background-color: rgb(55, 60, 75);\n"
"	color: rgb(166, 177, 199);\n"
"	selection-color:rgb(133, 166, 255);\n"
"    border:1px solid rgb(77, 88, 100);\n"
"    padding:5px;\n"
"	outline:0px;\n"
"}")
        self.sticky = QWidget()
        self.sticky.setObjectName(u"sticky")
        self.gridLayoutWidget = QWidget(self.sticky)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 511, 621))
        self.sticky_notes_grd = QGridLayout(self.gridLayoutWidget)
        self.sticky_notes_grd.setSpacing(15)
        self.sticky_notes_grd.setObjectName(u"sticky_notes_grd")
        self.sticky_notes_grd.setContentsMargins(0, 0, 0, 0)
        self.sticky_note_0 = QPushButton(self.gridLayoutWidget)
        self.sticky_note_0.setObjectName(u"sticky_note_0")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.sticky_note_0.sizePolicy().hasHeightForWidth())
        self.sticky_note_0.setSizePolicy(sizePolicy4)
        font33 = QFont()
        font33.setFamilies([u"\uc11c\uc6b8\ub0a8\uc0b0 \uc7a5\uccb4 M"])
        font33.setPointSize(13)
        self.sticky_note_0.setFont(font33)
        self.sticky_note_0.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(38, 43, 53);\n"
"	border: 1px solid rgb(35, 40 ,50);\n"
"	border-radius: 15px;\n"
"	padding: 12px;\n"
"	text-align: top left;\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(42, 47, 57);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(36, 41, 51);\n"
"}")

        self.sticky_notes_grd.addWidget(self.sticky_note_0, 0, 0, 1, 1)

        self.sticky_note_3 = QPushButton(self.gridLayoutWidget)
        self.sticky_note_3.setObjectName(u"sticky_note_3")
        sizePolicy4.setHeightForWidth(self.sticky_note_3.sizePolicy().hasHeightForWidth())
        self.sticky_note_3.setSizePolicy(sizePolicy4)
        self.sticky_note_3.setFont(font33)
        self.sticky_note_3.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(38, 43, 53);\n"
"	border: 1px solid rgb(35, 40 ,50);\n"
"	border-radius: 15px;\n"
"	padding: 12px;\n"
"	text-align: top left;\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(42, 47, 57);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(36, 41, 51);\n"
"}")

        self.sticky_notes_grd.addWidget(self.sticky_note_3, 1, 1, 1, 1)

        self.sticky_note_2 = QPushButton(self.gridLayoutWidget)
        self.sticky_note_2.setObjectName(u"sticky_note_2")
        sizePolicy4.setHeightForWidth(self.sticky_note_2.sizePolicy().hasHeightForWidth())
        self.sticky_note_2.setSizePolicy(sizePolicy4)
        self.sticky_note_2.setFont(font33)
        self.sticky_note_2.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(38, 43, 53);\n"
"	border: 1px solid rgb(35, 40 ,50);\n"
"	border-radius: 15px;\n"
"	padding: 12px;\n"
"	text-align: top left;\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(42, 47, 57);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(36, 41, 51);\n"
"}")

        self.sticky_notes_grd.addWidget(self.sticky_note_2, 1, 0, 1, 1)

        self.sticky_note_1 = QPushButton(self.gridLayoutWidget)
        self.sticky_note_1.setObjectName(u"sticky_note_1")
        sizePolicy4.setHeightForWidth(self.sticky_note_1.sizePolicy().hasHeightForWidth())
        self.sticky_note_1.setSizePolicy(sizePolicy4)
        self.sticky_note_1.setFont(font33)
        self.sticky_note_1.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(38, 43, 53);\n"
"	border: 1px solid rgb(35, 40 ,50);\n"
"	border-radius: 15px;\n"
"	padding: 12px;\n"
"	text-align: top left;\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(42, 47, 57);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(36, 41, 51);\n"
"}")

        self.sticky_notes_grd.addWidget(self.sticky_note_1, 0, 1, 1, 1)

        self.sticky_note_4 = QPushButton(self.gridLayoutWidget)
        self.sticky_note_4.setObjectName(u"sticky_note_4")
        sizePolicy4.setHeightForWidth(self.sticky_note_4.sizePolicy().hasHeightForWidth())
        self.sticky_note_4.setSizePolicy(sizePolicy4)
        self.sticky_note_4.setFont(font33)
        self.sticky_note_4.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(38, 43, 53);\n"
"	border: 1px solid rgb(35, 40 ,50);\n"
"	border-radius: 15px;\n"
"	padding: 12px;\n"
"	text-align: top left;\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(42, 47, 57);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(36, 41, 51);\n"
"}")

        self.sticky_notes_grd.addWidget(self.sticky_note_4, 2, 0, 1, 1)

        self.sticky_note_5 = QPushButton(self.gridLayoutWidget)
        self.sticky_note_5.setObjectName(u"sticky_note_5")
        sizePolicy4.setHeightForWidth(self.sticky_note_5.sizePolicy().hasHeightForWidth())
        self.sticky_note_5.setSizePolicy(sizePolicy4)
        self.sticky_note_5.setFont(font33)
        self.sticky_note_5.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(38, 43, 53);\n"
"	border: 1px solid rgb(35, 40 ,50);\n"
"	border-radius: 15px;\n"
"	padding: 12px;\n"
"	text-align: top left;\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color:rgb(42, 47, 57);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(36, 41, 51);\n"
"}")

        self.sticky_notes_grd.addWidget(self.sticky_note_5, 2, 1, 1, 1)

        self.apps_stack.addWidget(self.sticky)
        self.quick_saves = QWidget()
        self.quick_saves.setObjectName(u"quick_saves")
        self.qsv_lwg = QListWidget(self.quick_saves)
        QListWidgetItem(self.qsv_lwg)
        QListWidgetItem(self.qsv_lwg)
        QListWidgetItem(self.qsv_lwg)
        QListWidgetItem(self.qsv_lwg)
        QListWidgetItem(self.qsv_lwg)
        QListWidgetItem(self.qsv_lwg)
        self.qsv_lwg.setObjectName(u"qsv_lwg")
        self.qsv_lwg.setGeometry(QRect(10, 10, 511, 581))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush13 = QBrush(QColor(0, 0, 0, 0))
        brush13.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush14 = QBrush(QColor(0, 0, 0, 255))
        brush14.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush14)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette3.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush15 = QBrush(QColor(166, 177, 199, 128))
        brush15.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush16 = QBrush(QColor(0, 0, 0, 255))
        brush16.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush16)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette3.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        brush17 = QBrush(QColor(166, 177, 199, 128))
        brush17.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush18 = QBrush(QColor(0, 0, 0, 255))
        brush18.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush18)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush3)
        brush19 = QBrush(QColor(166, 177, 199, 128))
        brush19.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush19)
#endif
        self.qsv_lwg.setPalette(palette3)
        self.qsv_lwg.setFont(font28)
        self.qsv_lwg.setStyleSheet(u"QListWidget::item:selected{\n"
"    background-color: rgb(52, 57, 75);\n"
"}\n"
"QListWidget{\n"
"	border:none;\n"
"	border-bottom:1px solid rgb(55,60,75);\n"
"}")
        self.qsv_lwg.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.qsv_lwg.setEditTriggers(QAbstractItemView.SelectedClicked)
        self.qsv_lwg.setProperty("showDropIndicator", False)
        self.qsv_lwg.setDragEnabled(True)
        self.qsv_lwg.setDragDropMode(QAbstractItemView.InternalMove)
        self.qsv_lwg.setDefaultDropAction(Qt.TargetMoveAction)
        self.qsv_lwg.setAlternatingRowColors(True)
        self.qsv_lwg.setProperty("isWrapping", False)
        self.qsv_lwg.setLayoutMode(QListView.SinglePass)
        self.qsv_lwg.setSpacing(1)
        self.qsv_lwg.setViewMode(QListView.ListMode)
        self.qsv_lwg.setModelColumn(0)
        self.qsv_lwg.setUniformItemSizes(False)
        self.qsv_lwg.setSelectionRectVisible(False)
        self.qsv_lwg.setSortingEnabled(False)
        self.qsv_copypaste_btn = QPushButton(self.quick_saves)
        self.qsv_copypaste_btn.setObjectName(u"qsv_copypaste_btn")
        self.qsv_copypaste_btn.setGeometry(QRect(380, 610, 141, 30))
        sizePolicy3.setHeightForWidth(self.qsv_copypaste_btn.sizePolicy().hasHeightForWidth())
        self.qsv_copypaste_btn.setSizePolicy(sizePolicy3)
        self.qsv_copypaste_btn.setMinimumSize(QSize(0, 30))
        self.qsv_copypaste_btn.setMaximumSize(QSize(16777215, 16777215))
        self.qsv_copypaste_btn.setFont(font4)
        self.qsv_copypaste_btn.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(200, 120, 100);\n"
"	background-color:rgb(45,50,60);\n"
"	border:0px;\n"
"	border-radius:10%;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:hover {    \n"
"	color: rgb(220, 110, 90);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.qsv_copypaste_btn.setFlat(True)
        self.qsv_delete_btn = QPushButton(self.quick_saves)
        self.qsv_delete_btn.setObjectName(u"qsv_delete_btn")
        self.qsv_delete_btn.setGeometry(QRect(80, 610, 61, 30))
        sizePolicy3.setHeightForWidth(self.qsv_delete_btn.sizePolicy().hasHeightForWidth())
        self.qsv_delete_btn.setSizePolicy(sizePolicy3)
        self.qsv_delete_btn.setMinimumSize(QSize(0, 30))
        self.qsv_delete_btn.setMaximumSize(QSize(16777215, 16777215))
        self.qsv_delete_btn.setFont(font4)
        self.qsv_delete_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(200, 150, 175);\n"
"	background-color:rgb(45,50,60);\n"
"	border:0px;\n"
"	border-radius:10%;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:hover {    \n"
"	color: rgb(225, 140, 160);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(75,85,100);\n"
"}")
        self.qsv_delete_btn.setFlat(True)
        self.qsv_new_btn = QPushButton(self.quick_saves)
        self.qsv_new_btn.setObjectName(u"qsv_new_btn")
        self.qsv_new_btn.setGeometry(QRect(10, 610, 50, 30))
        sizePolicy.setHeightForWidth(self.qsv_new_btn.sizePolicy().hasHeightForWidth())
        self.qsv_new_btn.setSizePolicy(sizePolicy)
        self.qsv_new_btn.setMinimumSize(QSize(30, 20))
        self.qsv_new_btn.setMaximumSize(QSize(50, 16777215))
        self.qsv_new_btn.setFont(font6)
        self.qsv_new_btn.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(130, 150, 180);\n"
"	background-color:rgb(45,50,60);\n"
"	border-radius:10%;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(110,130,230);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.qsv_new_btn.setAutoDefault(True)
        self.qsv_new_btn.setFlat(True)
        self.apps_stack.addWidget(self.quick_saves)
        self.med_docs = QWidget()
        self.med_docs.setObjectName(u"med_docs")
        self.mdoc_contents_pte = QPlainTextEdit(self.med_docs)
        self.mdoc_contents_pte.setObjectName(u"mdoc_contents_pte")
        self.mdoc_contents_pte.setGeometry(QRect(0, 340, 531, 251))
        self.mdoc_contents_pte.setFont(font28)
        self.mdoc_contents_pte.setStyleSheet(u"background:transparent;\n"
"color: rgb(177, 211, 233);\n"
"padding:5px;\n"
"border:none;\n"
"border-bottom:1px solid rgb(55,60,75);")
        self.mdoc_new_btn = QPushButton(self.med_docs)
        self.mdoc_new_btn.setObjectName(u"mdoc_new_btn")
        self.mdoc_new_btn.setGeometry(QRect(10, 610, 50, 30))
        sizePolicy3.setHeightForWidth(self.mdoc_new_btn.sizePolicy().hasHeightForWidth())
        self.mdoc_new_btn.setSizePolicy(sizePolicy3)
        self.mdoc_new_btn.setMinimumSize(QSize(0, 30))
        self.mdoc_new_btn.setMaximumSize(QSize(16777215, 16777215))
        self.mdoc_new_btn.setFont(font4)
        self.mdoc_new_btn.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(166, 188, 144);\n"
"	background-color:rgb(45,50,60);\n"
"	border:0px;\n"
"	border-top-left-radius:10%;\n"
"	border-bottom-left-radius:10%;\n"
"	border:1px solid rgb(50,55,70);\n"
"	border-right:none;\n"
"}\n"
"QPushButton:hover {    \n"
"	color: rgb(155, 222, 133);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.mdoc_new_btn.setFlat(True)
        self.mdoc_save_btn = QPushButton(self.med_docs)
        self.mdoc_save_btn.setObjectName(u"mdoc_save_btn")
        self.mdoc_save_btn.setGeometry(QRect(110, 610, 50, 30))
        sizePolicy3.setHeightForWidth(self.mdoc_save_btn.sizePolicy().hasHeightForWidth())
        self.mdoc_save_btn.setSizePolicy(sizePolicy3)
        self.mdoc_save_btn.setMinimumSize(QSize(0, 30))
        self.mdoc_save_btn.setMaximumSize(QSize(16777215, 16777215))
        self.mdoc_save_btn.setFont(font4)
        self.mdoc_save_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(70, 75, 90);\n"
"	background-color:rgb(45,50,60);\n"
"	border:0px;\n"
"	border-top-right-radius:10%;\n"
"	border-bottom-right-radius:10%;\n"
"	border:1px solid rgb(50,55,70);\n"
"	border-left:none;\n"
"}\n"
"QPushButton:enabled{\n"
"	color: rgb(220, 220, 220);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(250,250,255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.mdoc_save_btn.setFlat(True)
        self.mdoc_copy_btn = QPushButton(self.med_docs)
        self.mdoc_copy_btn.setObjectName(u"mdoc_copy_btn")
        self.mdoc_copy_btn.setGeometry(QRect(380, 610, 141, 30))
        sizePolicy3.setHeightForWidth(self.mdoc_copy_btn.sizePolicy().hasHeightForWidth())
        self.mdoc_copy_btn.setSizePolicy(sizePolicy3)
        self.mdoc_copy_btn.setMinimumSize(QSize(0, 30))
        self.mdoc_copy_btn.setMaximumSize(QSize(16777215, 16777215))
        self.mdoc_copy_btn.setFont(font4)
        self.mdoc_copy_btn.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(200, 120, 100);\n"
"	background-color:rgb(45,50,60);\n"
"	border:0px;\n"
"	border-radius:10%;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:hover {    \n"
"	color: rgb(230, 110, 90);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.mdoc_copy_btn.setFlat(True)
        self.mdoc_delete_btn = QPushButton(self.med_docs)
        self.mdoc_delete_btn.setObjectName(u"mdoc_delete_btn")
        self.mdoc_delete_btn.setGeometry(QRect(180, 610, 61, 30))
        sizePolicy3.setHeightForWidth(self.mdoc_delete_btn.sizePolicy().hasHeightForWidth())
        self.mdoc_delete_btn.setSizePolicy(sizePolicy3)
        self.mdoc_delete_btn.setMinimumSize(QSize(0, 30))
        self.mdoc_delete_btn.setMaximumSize(QSize(16777215, 16777215))
        self.mdoc_delete_btn.setFont(font4)
        self.mdoc_delete_btn.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(220, 150, 175);\n"
"	background-color:rgb(45,50,60);\n"
"	border:0px;\n"
"	border-radius:10%;\n"
"	border:1px solid rgb(50,55,70);\n"
"	border-right:none;\n"
"}\n"
"QPushButton:hover {    \n"
"	color: rgb(240, 140, 120);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.mdoc_delete_btn.setFlat(True)
        self.mdoc_lwg = QListWidget(self.med_docs)
        QListWidgetItem(self.mdoc_lwg)
        QListWidgetItem(self.mdoc_lwg)
        QListWidgetItem(self.mdoc_lwg)
        QListWidgetItem(self.mdoc_lwg)
        QListWidgetItem(self.mdoc_lwg)
        QListWidgetItem(self.mdoc_lwg)
        QListWidgetItem(self.mdoc_lwg)
        QListWidgetItem(self.mdoc_lwg)
        QListWidgetItem(self.mdoc_lwg)
        QListWidgetItem(self.mdoc_lwg)
        QListWidgetItem(self.mdoc_lwg)
        QListWidgetItem(self.mdoc_lwg)
        QListWidgetItem(self.mdoc_lwg)
        QListWidgetItem(self.mdoc_lwg)
        self.mdoc_lwg.setObjectName(u"mdoc_lwg")
        self.mdoc_lwg.setGeometry(QRect(10, 10, 511, 271))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush20 = QBrush(QColor(0, 0, 0, 255))
        brush20.setStyle(Qt.NoBrush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush20)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette4.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush21 = QBrush(QColor(166, 177, 199, 128))
        brush21.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush21)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush22 = QBrush(QColor(0, 0, 0, 255))
        brush22.setStyle(Qt.NoBrush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush22)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        brush23 = QBrush(QColor(166, 177, 199, 128))
        brush23.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush23)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush24 = QBrush(QColor(0, 0, 0, 255))
        brush24.setStyle(Qt.NoBrush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush24)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush3)
        brush25 = QBrush(QColor(166, 177, 199, 128))
        brush25.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush25)
#endif
        self.mdoc_lwg.setPalette(palette4)
        self.mdoc_lwg.setFont(font1)
        self.mdoc_lwg.setStyleSheet(u"border:none;\n"
"border-bottom:1px solid rgb(55,60,75);")
        self.mdoc_lwg.setEditTriggers(QAbstractItemView.SelectedClicked)
        self.mdoc_lwg.setDragDropMode(QAbstractItemView.InternalMove)
        self.mdoc_lwg.setAlternatingRowColors(True)
        self.mdoc_lwg.setLayoutMode(QListView.SinglePass)
        self.mdoc_lwg.setSpacing(1)
        self.mdoc_lwg.setViewMode(QListView.ListMode)
        self.mdoc_lwg.setUniformItemSizes(False)
        self.mdoc_lwg.setSelectionRectVisible(False)
        self.mdoc_edit_btn = QPushButton(self.med_docs)
        self.mdoc_edit_btn.setObjectName(u"mdoc_edit_btn")
        self.mdoc_edit_btn.setGeometry(QRect(60, 610, 50, 30))
        sizePolicy3.setHeightForWidth(self.mdoc_edit_btn.sizePolicy().hasHeightForWidth())
        self.mdoc_edit_btn.setSizePolicy(sizePolicy3)
        self.mdoc_edit_btn.setMinimumSize(QSize(0, 30))
        self.mdoc_edit_btn.setMaximumSize(QSize(16777215, 16777215))
        self.mdoc_edit_btn.setFont(font4)
        self.mdoc_edit_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(140, 150, 200);\n"
"	background-color:rgb(45,50,60);\n"
"	border:0px;\n"
"	border:1px solid rgb(50,55,70);\n"
"	border-right:none;\n"
"	border-left:none;\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(100,125,255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.mdoc_edit_btn.setCheckable(True)
        self.mdoc_edit_btn.setFlat(True)
        self.mdoc_title_led = QLineEdit(self.med_docs)
        self.mdoc_title_led.setObjectName(u"mdoc_title_led")
        self.mdoc_title_led.setGeometry(QRect(10, 300, 511, 40))
        sizePolicy1.setHeightForWidth(self.mdoc_title_led.sizePolicy().hasHeightForWidth())
        self.mdoc_title_led.setSizePolicy(sizePolicy1)
        self.mdoc_title_led.setMinimumSize(QSize(0, 40))
        self.mdoc_title_led.setMaximumSize(QSize(16777215, 30))
        font34 = QFont()
        font34.setFamilies([u"Mapo\ub2f9\uc778\ub9ac\ubc1c\uc804\uc18c"])
        font34.setPointSize(14)
        font34.setBold(False)
        self.mdoc_title_led.setFont(font34)
        self.mdoc_title_led.setContextMenuPolicy(Qt.CustomContextMenu)
        self.mdoc_title_led.setStyleSheet(u"background-color:rgb(36,42,55);\n"
"padding-left: 8px;\n"
"color: rgb(133, 166, 199);\n"
"border:none;\n"
"border:1px solid rgb(50,55,70);\n"
"border-radius:10px;\n"
"")
        self.mdoc_title_led.setFrame(False)
        self.apps_stack.addWidget(self.med_docs)
        self.studies = QWidget()
        self.studies.setObjectName(u"studies")
        self.studies_bmd_btn = QPushButton(self.studies)
        self.studies_bmd_btn.setObjectName(u"studies_bmd_btn")
        self.studies_bmd_btn.setGeometry(QRect(140, -2, 120, 30))
        sizePolicy3.setHeightForWidth(self.studies_bmd_btn.sizePolicy().hasHeightForWidth())
        self.studies_bmd_btn.setSizePolicy(sizePolicy3)
        self.studies_bmd_btn.setMinimumSize(QSize(0, 30))
        self.studies_bmd_btn.setMaximumSize(QSize(16777215, 16777215))
        font35 = QFont()
        font35.setFamilies([u"Lucida Sans"])
        font35.setPointSize(11)
        font35.setBold(False)
        font35.setItalic(True)
        self.studies_bmd_btn.setFont(font35)
        self.studies_bmd_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(165, 170, 180);\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(190,200,222);\n"
"	font:bold italic;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(75,85,100);\n"
"}")
        self.studies_bmd_btn.setFlat(True)
        self.studies_ipss_btn = QPushButton(self.studies)
        self.studies_ipss_btn.setObjectName(u"studies_ipss_btn")
        self.studies_ipss_btn.setGeometry(QRect(400, -2, 120, 30))
        sizePolicy3.setHeightForWidth(self.studies_ipss_btn.sizePolicy().hasHeightForWidth())
        self.studies_ipss_btn.setSizePolicy(sizePolicy3)
        self.studies_ipss_btn.setMinimumSize(QSize(0, 30))
        self.studies_ipss_btn.setMaximumSize(QSize(16777215, 16777215))
        self.studies_ipss_btn.setFont(font35)
        self.studies_ipss_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(165, 170, 180);\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(190,200,222);\n"
"	font:bold italic;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(75,85,100);\n"
"}")
        self.studies_ipss_btn.setFlat(True)
        self.studies_alz_btn = QPushButton(self.studies)
        self.studies_alz_btn.setObjectName(u"studies_alz_btn")
        self.studies_alz_btn.setGeometry(QRect(270, -2, 120, 30))
        sizePolicy3.setHeightForWidth(self.studies_alz_btn.sizePolicy().hasHeightForWidth())
        self.studies_alz_btn.setSizePolicy(sizePolicy3)
        self.studies_alz_btn.setMinimumSize(QSize(0, 30))
        self.studies_alz_btn.setMaximumSize(QSize(16777215, 16777215))
        self.studies_alz_btn.setFont(font35)
        self.studies_alz_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(165, 170, 180);\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(190,200,222);\n"
"	font:bold italic;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(75,85,100);\n"
"}")
        self.studies_alz_btn.setFlat(True)
        self.studies_lab_btn = QPushButton(self.studies)
        self.studies_lab_btn.setObjectName(u"studies_lab_btn")
        self.studies_lab_btn.setGeometry(QRect(10, -2, 120, 30))
        sizePolicy3.setHeightForWidth(self.studies_lab_btn.sizePolicy().hasHeightForWidth())
        self.studies_lab_btn.setSizePolicy(sizePolicy3)
        self.studies_lab_btn.setMinimumSize(QSize(0, 30))
        self.studies_lab_btn.setMaximumSize(QSize(16777215, 16777215))
        self.studies_lab_btn.setFont(font35)
        self.studies_lab_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(165, 170, 180);\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(190,200,222);\n"
"	font:bold italic;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(75,85,100);\n"
"}")
        self.studies_lab_btn.setFlat(True)
        self.studies_stack = QStackedWidget(self.studies)
        self.studies_stack.setObjectName(u"studies_stack")
        self.studies_stack.setGeometry(QRect(0, 29, 531, 611))
        self.studies_stack.setStyleSheet(u"QStackedWidget{\n"
"	border-top:1px solid rgb(55,60,75);\n"
"	background:transparent;\n"
"}")
        self.lab_results = QWidget()
        self.lab_results.setObjectName(u"lab_results")
        self.lab_rbc_led = QLineEdit(self.lab_results)
        self.lab_rbc_led.setObjectName(u"lab_rbc_led")
        self.lab_rbc_led.setGeometry(QRect(60, 240, 70, 30))
        self.lab_rbc_led.setMinimumSize(QSize(0, 30))
        self.lab_rbc_led.setMaximumSize(QSize(16777215, 30))
        self.lab_rbc_led.setFont(font11)
        self.lab_rbc_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_rbc_led.setFrame(False)
        self.lab_hct_lbl = QLabel(self.lab_results)
        self.lab_hct_lbl.setObjectName(u"lab_hct_lbl")
        self.lab_hct_lbl.setGeometry(QRect(10, 180, 50, 30))
        self.lab_hct_lbl.setMinimumSize(QSize(45, 30))
        self.lab_hct_lbl.setMaximumSize(QSize(60, 30))
        font36 = QFont()
        font36.setFamilies([u"Lucida Sans"])
        font36.setPointSize(12)
        font36.setItalic(True)
        self.lab_hct_lbl.setFont(font36)
        self.lab_hct_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-left:1px solid rgb(50, 55, 70);\n"
"padding-right:5px;")
        self.lab_hct_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_hb_lbl = QLabel(self.lab_results)
        self.lab_hb_lbl.setObjectName(u"lab_hb_lbl")
        self.lab_hb_lbl.setGeometry(QRect(10, 150, 50, 30))
        self.lab_hb_lbl.setMinimumSize(QSize(45, 30))
        self.lab_hb_lbl.setMaximumSize(QSize(60, 30))
        self.lab_hb_lbl.setFont(font36)
        self.lab_hb_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-left:1px solid rgb(50, 55, 70);\n"
"padding-right:5px;")
        self.lab_hb_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_hct_led = QLineEdit(self.lab_results)
        self.lab_hct_led.setObjectName(u"lab_hct_led")
        self.lab_hct_led.setGeometry(QRect(60, 180, 70, 30))
        self.lab_hct_led.setMinimumSize(QSize(0, 30))
        self.lab_hct_led.setMaximumSize(QSize(16777215, 30))
        self.lab_hct_led.setFont(font11)
        self.lab_hct_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_hct_led.setFrame(False)
        self.lab_plt_led = QLineEdit(self.lab_results)
        self.lab_plt_led.setObjectName(u"lab_plt_led")
        self.lab_plt_led.setGeometry(QRect(60, 270, 70, 30))
        self.lab_plt_led.setMinimumSize(QSize(0, 30))
        self.lab_plt_led.setMaximumSize(QSize(16777215, 30))
        self.lab_plt_led.setFont(font11)
        self.lab_plt_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_plt_led.setFrame(False)
        self.lab_wbc_led = QLineEdit(self.lab_results)
        self.lab_wbc_led.setObjectName(u"lab_wbc_led")
        self.lab_wbc_led.setGeometry(QRect(60, 210, 70, 30))
        self.lab_wbc_led.setMinimumSize(QSize(0, 30))
        self.lab_wbc_led.setMaximumSize(QSize(16777215, 30))
        self.lab_wbc_led.setFont(font11)
        self.lab_wbc_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_wbc_led.setFrame(False)
        self.lab_cbc_title_lbl = QLabel(self.lab_results)
        self.lab_cbc_title_lbl.setObjectName(u"lab_cbc_title_lbl")
        self.lab_cbc_title_lbl.setGeometry(QRect(10, 120, 120, 30))
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lab_cbc_title_lbl.sizePolicy().hasHeightForWidth())
        self.lab_cbc_title_lbl.setSizePolicy(sizePolicy5)
        self.lab_cbc_title_lbl.setMinimumSize(QSize(0, 0))
        self.lab_cbc_title_lbl.setMaximumSize(QSize(16777215, 16777215))
        font37 = QFont()
        font37.setFamilies([u"Lucida Sans"])
        font37.setPointSize(12)
        font37.setBold(False)
        font37.setItalic(True)
        self.lab_cbc_title_lbl.setFont(font37)
        self.lab_cbc_title_lbl.setStyleSheet(u"background-color:rgb(38, 43, 52);\n"
"color: rgb(125, 150, 200);\n"
"border:1px solid rgb(50, 55, 70);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;")
        self.lab_cbc_title_lbl.setAlignment(Qt.AlignCenter)
        self.lab_wbc_lbl = QLabel(self.lab_results)
        self.lab_wbc_lbl.setObjectName(u"lab_wbc_lbl")
        self.lab_wbc_lbl.setGeometry(QRect(10, 210, 50, 30))
        self.lab_wbc_lbl.setMinimumSize(QSize(45, 30))
        self.lab_wbc_lbl.setMaximumSize(QSize(60, 30))
        self.lab_wbc_lbl.setFont(font36)
        self.lab_wbc_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-left:1px solid rgb(50, 55, 70);\n"
"padding-right:5px;")
        self.lab_wbc_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_plt_lbl = QLabel(self.lab_results)
        self.lab_plt_lbl.setObjectName(u"lab_plt_lbl")
        self.lab_plt_lbl.setGeometry(QRect(10, 270, 50, 30))
        self.lab_plt_lbl.setMinimumSize(QSize(45, 30))
        self.lab_plt_lbl.setMaximumSize(QSize(60, 30))
        self.lab_plt_lbl.setFont(font36)
        self.lab_plt_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(50, 55, 70);\n"
"border-left:1px solid rgb(50,55,70);\n"
"border-bottom-left-radius:10px;\n"
"padding-right:5px;")
        self.lab_plt_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_hb_led = QLineEdit(self.lab_results)
        self.lab_hb_led.setObjectName(u"lab_hb_led")
        self.lab_hb_led.setGeometry(QRect(60, 150, 70, 30))
        self.lab_hb_led.setMinimumSize(QSize(0, 30))
        self.lab_hb_led.setMaximumSize(QSize(16777215, 30))
        self.lab_hb_led.setFont(font11)
        self.lab_hb_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_hb_led.setFrame(False)
        self.lab_rbc_lbl = QLabel(self.lab_results)
        self.lab_rbc_lbl.setObjectName(u"lab_rbc_lbl")
        self.lab_rbc_lbl.setGeometry(QRect(10, 240, 50, 30))
        self.lab_rbc_lbl.setMinimumSize(QSize(45, 30))
        self.lab_rbc_lbl.setMaximumSize(QSize(60, 30))
        self.lab_rbc_lbl.setFont(font36)
        self.lab_rbc_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-left:1px solid rgb(50, 55, 70);\n"
"padding-right:5px;")
        self.lab_rbc_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_ft4_led = QLineEdit(self.lab_results)
        self.lab_ft4_led.setObjectName(u"lab_ft4_led")
        self.lab_ft4_led.setGeometry(QRect(450, 180, 70, 30))
        self.lab_ft4_led.setMinimumSize(QSize(0, 30))
        self.lab_ft4_led.setMaximumSize(QSize(16777215, 30))
        self.lab_ft4_led.setFont(font11)
        self.lab_ft4_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_ft4_led.setFrame(False)
        self.lab_tsh_lbl = QLabel(self.lab_results)
        self.lab_tsh_lbl.setObjectName(u"lab_tsh_lbl")
        self.lab_tsh_lbl.setGeometry(QRect(400, 150, 50, 30))
        self.lab_tsh_lbl.setMinimumSize(QSize(45, 30))
        self.lab_tsh_lbl.setMaximumSize(QSize(60, 30))
        self.lab_tsh_lbl.setFont(font36)
        self.lab_tsh_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-left:1px solid rgb(50, 55, 70);\n"
"padding-right:5px;")
        self.lab_tsh_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_ft4_lbl = QLabel(self.lab_results)
        self.lab_ft4_lbl.setObjectName(u"lab_ft4_lbl")
        self.lab_ft4_lbl.setGeometry(QRect(400, 180, 50, 30))
        self.lab_ft4_lbl.setMinimumSize(QSize(45, 30))
        self.lab_ft4_lbl.setMaximumSize(QSize(60, 30))
        self.lab_ft4_lbl.setFont(font36)
        self.lab_ft4_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-left:1px solid rgb(50, 55, 70);\n"
"padding-right:5px;")
        self.lab_ft4_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_tsh_led = QLineEdit(self.lab_results)
        self.lab_tsh_led.setObjectName(u"lab_tsh_led")
        self.lab_tsh_led.setGeometry(QRect(450, 150, 70, 30))
        self.lab_tsh_led.setMinimumSize(QSize(0, 30))
        self.lab_tsh_led.setMaximumSize(QSize(16777215, 30))
        self.lab_tsh_led.setFont(font11)
        self.lab_tsh_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_tsh_led.setFrame(False)
        self.lab_cr_led = QLineEdit(self.lab_results)
        self.lab_cr_led.setObjectName(u"lab_cr_led")
        self.lab_cr_led.setGeometry(QRect(190, 180, 70, 30))
        self.lab_cr_led.setMinimumSize(QSize(0, 30))
        self.lab_cr_led.setMaximumSize(QSize(16777215, 30))
        self.lab_cr_led.setFont(font11)
        self.lab_cr_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_cr_led.setFrame(False)
        self.lab_dm_studies_title_lbl = QLabel(self.lab_results)
        self.lab_dm_studies_title_lbl.setObjectName(u"lab_dm_studies_title_lbl")
        self.lab_dm_studies_title_lbl.setGeometry(QRect(270, 120, 120, 30))
        sizePolicy5.setHeightForWidth(self.lab_dm_studies_title_lbl.sizePolicy().hasHeightForWidth())
        self.lab_dm_studies_title_lbl.setSizePolicy(sizePolicy5)
        self.lab_dm_studies_title_lbl.setMinimumSize(QSize(0, 0))
        self.lab_dm_studies_title_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.lab_dm_studies_title_lbl.setFont(font37)
        self.lab_dm_studies_title_lbl.setStyleSheet(u"background-color:rgb(38, 43, 52);\n"
"color: rgb(125, 150, 200);\n"
"border:1px solid rgb(50, 55, 70);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;")
        self.lab_dm_studies_title_lbl.setAlignment(Qt.AlignCenter)
        self.lab_a1c_lbl = QLabel(self.lab_results)
        self.lab_a1c_lbl.setObjectName(u"lab_a1c_lbl")
        self.lab_a1c_lbl.setGeometry(QRect(270, 180, 50, 30))
        self.lab_a1c_lbl.setMinimumSize(QSize(45, 30))
        self.lab_a1c_lbl.setMaximumSize(QSize(60, 30))
        self.lab_a1c_lbl.setFont(font36)
        self.lab_a1c_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(50, 55, 70);\n"
"border-left:1px solid rgb(50,55,70);\n"
"border-bottom-left-radius:10px;\n"
"padding-right:5px;")
        self.lab_a1c_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_bun_led = QLineEdit(self.lab_results)
        self.lab_bun_led.setObjectName(u"lab_bun_led")
        self.lab_bun_led.setGeometry(QRect(190, 150, 70, 30))
        self.lab_bun_led.setMinimumSize(QSize(0, 30))
        self.lab_bun_led.setMaximumSize(QSize(16777215, 30))
        self.lab_bun_led.setFont(font11)
        self.lab_bun_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_bun_led.setFrame(False)
        self.lab_fbs_led = QLineEdit(self.lab_results)
        self.lab_fbs_led.setObjectName(u"lab_fbs_led")
        self.lab_fbs_led.setGeometry(QRect(320, 150, 70, 30))
        self.lab_fbs_led.setMinimumSize(QSize(0, 30))
        self.lab_fbs_led.setMaximumSize(QSize(16777215, 30))
        self.lab_fbs_led.setFont(font11)
        self.lab_fbs_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_fbs_led.setFrame(False)
        self.lab_a1c_led = QLineEdit(self.lab_results)
        self.lab_a1c_led.setObjectName(u"lab_a1c_led")
        self.lab_a1c_led.setGeometry(QRect(320, 180, 70, 30))
        self.lab_a1c_led.setMinimumSize(QSize(0, 30))
        self.lab_a1c_led.setMaximumSize(QSize(16777215, 30))
        self.lab_a1c_led.setFont(font11)
        self.lab_a1c_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_a1c_led.setFrame(False)
        self.lab_t3_lbl = QLabel(self.lab_results)
        self.lab_t3_lbl.setObjectName(u"lab_t3_lbl")
        self.lab_t3_lbl.setGeometry(QRect(400, 210, 50, 30))
        self.lab_t3_lbl.setMinimumSize(QSize(45, 30))
        self.lab_t3_lbl.setMaximumSize(QSize(60, 30))
        self.lab_t3_lbl.setFont(font36)
        self.lab_t3_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(50, 55, 70);\n"
"border-left:1px solid rgb(50,55,70);\n"
"border-bottom-left-radius:10px;\n"
"padding-right:5px;")
        self.lab_t3_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_fbs_lbl = QLabel(self.lab_results)
        self.lab_fbs_lbl.setObjectName(u"lab_fbs_lbl")
        self.lab_fbs_lbl.setGeometry(QRect(270, 150, 50, 30))
        self.lab_fbs_lbl.setMinimumSize(QSize(45, 30))
        self.lab_fbs_lbl.setMaximumSize(QSize(60, 30))
        self.lab_fbs_lbl.setFont(font36)
        self.lab_fbs_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-left:1px solid rgb(50, 55, 70);\n"
"padding-right:5px;")
        self.lab_fbs_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_tft_title_lbl = QLabel(self.lab_results)
        self.lab_tft_title_lbl.setObjectName(u"lab_tft_title_lbl")
        self.lab_tft_title_lbl.setGeometry(QRect(400, 120, 120, 30))
        sizePolicy5.setHeightForWidth(self.lab_tft_title_lbl.sizePolicy().hasHeightForWidth())
        self.lab_tft_title_lbl.setSizePolicy(sizePolicy5)
        self.lab_tft_title_lbl.setMinimumSize(QSize(0, 0))
        self.lab_tft_title_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.lab_tft_title_lbl.setFont(font37)
        self.lab_tft_title_lbl.setStyleSheet(u"background-color:rgb(38, 43, 52);\n"
"color: rgb(125, 150, 200);\n"
"border:1px solid rgb(50, 55, 70);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;")
        self.lab_tft_title_lbl.setAlignment(Qt.AlignCenter)
        self.lab_renal_title_lbl = QLabel(self.lab_results)
        self.lab_renal_title_lbl.setObjectName(u"lab_renal_title_lbl")
        self.lab_renal_title_lbl.setGeometry(QRect(140, 120, 120, 30))
        sizePolicy5.setHeightForWidth(self.lab_renal_title_lbl.sizePolicy().hasHeightForWidth())
        self.lab_renal_title_lbl.setSizePolicy(sizePolicy5)
        self.lab_renal_title_lbl.setMinimumSize(QSize(0, 0))
        self.lab_renal_title_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.lab_renal_title_lbl.setFont(font37)
        self.lab_renal_title_lbl.setStyleSheet(u"background-color:rgb(38, 43, 52);\n"
"color: rgb(125, 150, 200);\n"
"border:1px solid rgb(50, 55, 70);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;")
        self.lab_renal_title_lbl.setAlignment(Qt.AlignCenter)
        self.lab_cr_lbl = QLabel(self.lab_results)
        self.lab_cr_lbl.setObjectName(u"lab_cr_lbl")
        self.lab_cr_lbl.setGeometry(QRect(140, 180, 50, 30))
        self.lab_cr_lbl.setMinimumSize(QSize(45, 30))
        self.lab_cr_lbl.setMaximumSize(QSize(60, 30))
        self.lab_cr_lbl.setFont(font36)
        self.lab_cr_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(50, 55, 70);\n"
"border-left:1px solid rgb(50,55,70);\n"
"border-bottom-left-radius:10px;\n"
"padding-right:5px;")
        self.lab_cr_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_bun_lbl = QLabel(self.lab_results)
        self.lab_bun_lbl.setObjectName(u"lab_bun_lbl")
        self.lab_bun_lbl.setGeometry(QRect(140, 150, 50, 30))
        self.lab_bun_lbl.setMinimumSize(QSize(45, 30))
        self.lab_bun_lbl.setMaximumSize(QSize(60, 30))
        self.lab_bun_lbl.setFont(font36)
        self.lab_bun_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-left:1px solid rgb(50, 55, 70);\n"
"padding-right:5px;")
        self.lab_bun_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_t3_led = QLineEdit(self.lab_results)
        self.lab_t3_led.setObjectName(u"lab_t3_led")
        self.lab_t3_led.setGeometry(QRect(450, 210, 70, 30))
        self.lab_t3_led.setMinimumSize(QSize(0, 30))
        self.lab_t3_led.setMaximumSize(QSize(16777215, 30))
        self.lab_t3_led.setFont(font11)
        self.lab_t3_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_t3_led.setFrame(False)
        self.lab_tbil_led = QLineEdit(self.lab_results)
        self.lab_tbil_led.setObjectName(u"lab_tbil_led")
        self.lab_tbil_led.setGeometry(QRect(190, 400, 70, 30))
        self.lab_tbil_led.setMinimumSize(QSize(0, 30))
        self.lab_tbil_led.setMaximumSize(QSize(16777215, 30))
        self.lab_tbil_led.setFont(font11)
        self.lab_tbil_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_tbil_led.setFrame(False)
        self.lab_tg_led = QLineEdit(self.lab_results)
        self.lab_tg_led.setObjectName(u"lab_tg_led")
        self.lab_tg_led.setGeometry(QRect(320, 340, 70, 30))
        self.lab_tg_led.setMinimumSize(QSize(0, 30))
        self.lab_tg_led.setMaximumSize(QSize(16777215, 30))
        self.lab_tg_led.setFont(font11)
        self.lab_tg_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_tg_led.setFrame(False)
        self.lab_psa_lbl = QLabel(self.lab_results)
        self.lab_psa_lbl.setObjectName(u"lab_psa_lbl")
        self.lab_psa_lbl.setGeometry(QRect(400, 310, 50, 30))
        self.lab_psa_lbl.setMinimumSize(QSize(45, 30))
        self.lab_psa_lbl.setMaximumSize(QSize(60, 30))
        self.lab_psa_lbl.setFont(font36)
        self.lab_psa_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(50, 55, 70);\n"
"border-left:1px solid rgb(50,55,70);\n"
"border-bottom-left-radius:10px;\n"
"padding-right:5px;")
        self.lab_psa_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_alb_led = QLineEdit(self.lab_results)
        self.lab_alb_led.setObjectName(u"lab_alb_led")
        self.lab_alb_led.setGeometry(QRect(190, 250, 70, 30))
        self.lab_alb_led.setMinimumSize(QSize(0, 30))
        self.lab_alb_led.setMaximumSize(QSize(16777215, 30))
        self.lab_alb_led.setFont(font11)
        self.lab_alb_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_alb_led.setFrame(False)
        self.lab_hdl_lbl = QLabel(self.lab_results)
        self.lab_hdl_lbl.setObjectName(u"lab_hdl_lbl")
        self.lab_hdl_lbl.setGeometry(QRect(270, 280, 50, 30))
        self.lab_hdl_lbl.setMinimumSize(QSize(45, 30))
        self.lab_hdl_lbl.setMaximumSize(QSize(60, 30))
        self.lab_hdl_lbl.setFont(font36)
        self.lab_hdl_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-left:1px solid rgb(50, 55, 70);\n"
"padding-right:5px;")
        self.lab_hdl_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_psa_led = QLineEdit(self.lab_results)
        self.lab_psa_led.setObjectName(u"lab_psa_led")
        self.lab_psa_led.setGeometry(QRect(450, 310, 70, 30))
        self.lab_psa_led.setMinimumSize(QSize(0, 30))
        self.lab_psa_led.setMaximumSize(QSize(16777215, 30))
        self.lab_psa_led.setFont(font11)
        self.lab_psa_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_psa_led.setFrame(False)
        self.lab_alt_lbl = QLabel(self.lab_results)
        self.lab_alt_lbl.setObjectName(u"lab_alt_lbl")
        self.lab_alt_lbl.setGeometry(QRect(140, 340, 50, 30))
        self.lab_alt_lbl.setMinimumSize(QSize(45, 30))
        self.lab_alt_lbl.setMaximumSize(QSize(60, 30))
        self.lab_alt_lbl.setFont(font36)
        self.lab_alt_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-left:1px solid rgb(50, 55, 70);\n"
"padding-right:5px;")
        self.lab_alt_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_lft_title_lbl = QLabel(self.lab_results)
        self.lab_lft_title_lbl.setObjectName(u"lab_lft_title_lbl")
        self.lab_lft_title_lbl.setGeometry(QRect(140, 220, 120, 30))
        sizePolicy5.setHeightForWidth(self.lab_lft_title_lbl.sizePolicy().hasHeightForWidth())
        self.lab_lft_title_lbl.setSizePolicy(sizePolicy5)
        self.lab_lft_title_lbl.setMinimumSize(QSize(0, 0))
        self.lab_lft_title_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.lab_lft_title_lbl.setFont(font37)
        self.lab_lft_title_lbl.setStyleSheet(u"background-color:rgb(38, 43, 52);\n"
"color: rgb(125, 150, 200);\n"
"border:1px solid rgb(50, 55, 70);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;")
        self.lab_lft_title_lbl.setAlignment(Qt.AlignCenter)
        self.lab_esr_led = QLineEdit(self.lab_results)
        self.lab_esr_led.setObjectName(u"lab_esr_led")
        self.lab_esr_led.setGeometry(QRect(60, 370, 70, 30))
        self.lab_esr_led.setMinimumSize(QSize(0, 30))
        self.lab_esr_led.setMaximumSize(QSize(16777215, 30))
        self.lab_esr_led.setFont(font11)
        self.lab_esr_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_esr_led.setFrame(False)
        self.lab_tpr_lbl = QLabel(self.lab_results)
        self.lab_tpr_lbl.setObjectName(u"lab_tpr_lbl")
        self.lab_tpr_lbl.setGeometry(QRect(140, 280, 50, 30))
        self.lab_tpr_lbl.setMinimumSize(QSize(45, 30))
        self.lab_tpr_lbl.setMaximumSize(QSize(60, 30))
        self.lab_tpr_lbl.setFont(font36)
        self.lab_tpr_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-left:1px solid rgb(50, 55, 70);\n"
"padding-right:5px;")
        self.lab_tpr_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_gtp_lbl = QLabel(self.lab_results)
        self.lab_gtp_lbl.setObjectName(u"lab_gtp_lbl")
        self.lab_gtp_lbl.setGeometry(QRect(140, 370, 50, 30))
        self.lab_gtp_lbl.setMinimumSize(QSize(45, 30))
        self.lab_gtp_lbl.setMaximumSize(QSize(60, 30))
        self.lab_gtp_lbl.setFont(font36)
        self.lab_gtp_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-left:1px solid rgb(50, 55, 70);\n"
"padding-right:5px;")
        self.lab_gtp_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_tpr_led = QLineEdit(self.lab_results)
        self.lab_tpr_led.setObjectName(u"lab_tpr_led")
        self.lab_tpr_led.setGeometry(QRect(190, 280, 70, 30))
        self.lab_tpr_led.setMinimumSize(QSize(0, 30))
        self.lab_tpr_led.setMaximumSize(QSize(16777215, 30))
        self.lab_tpr_led.setFont(font11)
        self.lab_tpr_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_tpr_led.setFrame(False)
        self.lab_gtp_led = QLineEdit(self.lab_results)
        self.lab_gtp_led.setObjectName(u"lab_gtp_led")
        self.lab_gtp_led.setGeometry(QRect(190, 370, 70, 30))
        self.lab_gtp_led.setMinimumSize(QSize(0, 30))
        self.lab_gtp_led.setMaximumSize(QSize(16777215, 30))
        self.lab_gtp_led.setFont(font11)
        self.lab_gtp_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_gtp_led.setFrame(False)
        self.lab_crp_led = QLineEdit(self.lab_results)
        self.lab_crp_led.setObjectName(u"lab_crp_led")
        self.lab_crp_led.setGeometry(QRect(60, 340, 70, 30))
        self.lab_crp_led.setMinimumSize(QSize(0, 30))
        self.lab_crp_led.setMaximumSize(QSize(16777215, 30))
        self.lab_crp_led.setFont(font11)
        self.lab_crp_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_crp_led.setFrame(False)
        self.lab_ast_led = QLineEdit(self.lab_results)
        self.lab_ast_led.setObjectName(u"lab_ast_led")
        self.lab_ast_led.setGeometry(QRect(190, 310, 70, 30))
        self.lab_ast_led.setMinimumSize(QSize(0, 30))
        self.lab_ast_led.setMaximumSize(QSize(16777215, 30))
        self.lab_ast_led.setFont(font11)
        self.lab_ast_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_ast_led.setFrame(False)
        self.lab_tbil_lbl = QLabel(self.lab_results)
        self.lab_tbil_lbl.setObjectName(u"lab_tbil_lbl")
        self.lab_tbil_lbl.setGeometry(QRect(140, 400, 50, 30))
        self.lab_tbil_lbl.setMinimumSize(QSize(45, 30))
        self.lab_tbil_lbl.setMaximumSize(QSize(60, 30))
        self.lab_tbil_lbl.setFont(font36)
        self.lab_tbil_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(50, 55, 70);\n"
"border-left:1px solid rgb(50,55,70);\n"
"border-bottom-left-radius:10px;\n"
"padding-right:5px;")
        self.lab_tbil_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_tc_lbl = QLabel(self.lab_results)
        self.lab_tc_lbl.setObjectName(u"lab_tc_lbl")
        self.lab_tc_lbl.setGeometry(QRect(270, 250, 50, 30))
        self.lab_tc_lbl.setMinimumSize(QSize(45, 30))
        self.lab_tc_lbl.setMaximumSize(QSize(60, 30))
        self.lab_tc_lbl.setFont(font36)
        self.lab_tc_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-left:1px solid rgb(50, 55, 70);\n"
"padding-right:5px;")
        self.lab_tc_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_vitd_lbl = QLabel(self.lab_results)
        self.lab_vitd_lbl.setObjectName(u"lab_vitd_lbl")
        self.lab_vitd_lbl.setGeometry(QRect(400, 280, 50, 30))
        self.lab_vitd_lbl.setMinimumSize(QSize(45, 30))
        self.lab_vitd_lbl.setMaximumSize(QSize(60, 30))
        self.lab_vitd_lbl.setFont(font36)
        self.lab_vitd_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-left:1px solid rgb(50, 55, 70);\n"
"padding-right:5px;")
        self.lab_vitd_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_vitd_led = QLineEdit(self.lab_results)
        self.lab_vitd_led.setObjectName(u"lab_vitd_led")
        self.lab_vitd_led.setGeometry(QRect(450, 280, 70, 30))
        self.lab_vitd_led.setMinimumSize(QSize(0, 30))
        self.lab_vitd_led.setMaximumSize(QSize(16777215, 30))
        self.lab_vitd_led.setFont(font11)
        self.lab_vitd_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_vitd_led.setFrame(False)
        self.lab_alb_lbl = QLabel(self.lab_results)
        self.lab_alb_lbl.setObjectName(u"lab_alb_lbl")
        self.lab_alb_lbl.setGeometry(QRect(140, 250, 50, 30))
        self.lab_alb_lbl.setMinimumSize(QSize(45, 30))
        self.lab_alb_lbl.setMaximumSize(QSize(60, 30))
        self.lab_alb_lbl.setFont(font36)
        self.lab_alb_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-left:1px solid rgb(50, 55, 70);\n"
"padding-right:5px;")
        self.lab_alb_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_crp_lbl = QLabel(self.lab_results)
        self.lab_crp_lbl.setObjectName(u"lab_crp_lbl")
        self.lab_crp_lbl.setGeometry(QRect(10, 340, 50, 30))
        self.lab_crp_lbl.setMinimumSize(QSize(45, 30))
        self.lab_crp_lbl.setMaximumSize(QSize(60, 30))
        self.lab_crp_lbl.setFont(font36)
        self.lab_crp_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-left:1px solid rgb(50, 55, 70);\n"
"padding-right:5px;")
        self.lab_crp_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_esr_lbl = QLabel(self.lab_results)
        self.lab_esr_lbl.setObjectName(u"lab_esr_lbl")
        self.lab_esr_lbl.setGeometry(QRect(10, 370, 50, 30))
        self.lab_esr_lbl.setMinimumSize(QSize(45, 30))
        self.lab_esr_lbl.setMaximumSize(QSize(60, 30))
        self.lab_esr_lbl.setFont(font36)
        self.lab_esr_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(50, 55, 70);\n"
"border-left:1px solid rgb(50,55,70);\n"
"border-bottom-left-radius:10px;\n"
"padding-right:5px;")
        self.lab_esr_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_tc_led = QLineEdit(self.lab_results)
        self.lab_tc_led.setObjectName(u"lab_tc_led")
        self.lab_tc_led.setGeometry(QRect(320, 250, 70, 30))
        self.lab_tc_led.setMinimumSize(QSize(0, 30))
        self.lab_tc_led.setMaximumSize(QSize(16777215, 30))
        self.lab_tc_led.setFont(font11)
        self.lab_tc_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_tc_led.setFrame(False)
        self.lab_hdl_led = QLineEdit(self.lab_results)
        self.lab_hdl_led.setObjectName(u"lab_hdl_led")
        self.lab_hdl_led.setGeometry(QRect(320, 280, 70, 30))
        self.lab_hdl_led.setMinimumSize(QSize(0, 30))
        self.lab_hdl_led.setMaximumSize(QSize(16777215, 30))
        self.lab_hdl_led.setFont(font11)
        self.lab_hdl_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_hdl_led.setFrame(False)
        self.lab_tg_lbl = QLabel(self.lab_results)
        self.lab_tg_lbl.setObjectName(u"lab_tg_lbl")
        self.lab_tg_lbl.setGeometry(QRect(270, 340, 50, 30))
        self.lab_tg_lbl.setMinimumSize(QSize(45, 30))
        self.lab_tg_lbl.setMaximumSize(QSize(60, 30))
        self.lab_tg_lbl.setFont(font36)
        self.lab_tg_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(50, 55, 70);\n"
"border-left:1px solid rgb(50,55,70);\n"
"border-bottom-left-radius:10px;\n"
"padding-right:5px;")
        self.lab_tg_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_alt_led = QLineEdit(self.lab_results)
        self.lab_alt_led.setObjectName(u"lab_alt_led")
        self.lab_alt_led.setGeometry(QRect(190, 340, 70, 30))
        self.lab_alt_led.setMinimumSize(QSize(0, 30))
        self.lab_alt_led.setMaximumSize(QSize(16777215, 30))
        self.lab_alt_led.setFont(font11)
        self.lab_alt_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_alt_led.setFrame(False)
        self.lab_ast_lbl = QLabel(self.lab_results)
        self.lab_ast_lbl.setObjectName(u"lab_ast_lbl")
        self.lab_ast_lbl.setGeometry(QRect(140, 310, 50, 30))
        self.lab_ast_lbl.setMinimumSize(QSize(45, 30))
        self.lab_ast_lbl.setMaximumSize(QSize(60, 30))
        self.lab_ast_lbl.setFont(font36)
        self.lab_ast_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-left:1px solid rgb(50, 55, 70);\n"
"padding-right:5px;")
        self.lab_ast_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_lipids_title_lbl = QLabel(self.lab_results)
        self.lab_lipids_title_lbl.setObjectName(u"lab_lipids_title_lbl")
        self.lab_lipids_title_lbl.setGeometry(QRect(270, 220, 120, 30))
        sizePolicy5.setHeightForWidth(self.lab_lipids_title_lbl.sizePolicy().hasHeightForWidth())
        self.lab_lipids_title_lbl.setSizePolicy(sizePolicy5)
        self.lab_lipids_title_lbl.setMinimumSize(QSize(0, 0))
        self.lab_lipids_title_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.lab_lipids_title_lbl.setFont(font37)
        self.lab_lipids_title_lbl.setStyleSheet(u"background-color:rgb(38, 43, 52);\n"
"color: rgb(125, 150, 200);\n"
"border:1px solid rgb(50, 55, 70);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;")
        self.lab_lipids_title_lbl.setAlignment(Qt.AlignCenter)
        self.lab_ldl_lbl = QLabel(self.lab_results)
        self.lab_ldl_lbl.setObjectName(u"lab_ldl_lbl")
        self.lab_ldl_lbl.setGeometry(QRect(270, 310, 50, 30))
        self.lab_ldl_lbl.setMinimumSize(QSize(45, 30))
        self.lab_ldl_lbl.setMaximumSize(QSize(60, 30))
        self.lab_ldl_lbl.setFont(font36)
        self.lab_ldl_lbl.setStyleSheet(u"color: rgb(144, 155, 188);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-left:1px solid rgb(50, 55, 70);\n"
"padding-right:5px;")
        self.lab_ldl_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lab_ldl_led = QLineEdit(self.lab_results)
        self.lab_ldl_led.setObjectName(u"lab_ldl_led")
        self.lab_ldl_led.setGeometry(QRect(320, 310, 70, 30))
        self.lab_ldl_led.setMinimumSize(QSize(0, 30))
        self.lab_ldl_led.setMaximumSize(QSize(16777215, 30))
        self.lab_ldl_led.setFont(font11)
        self.lab_ldl_led.setStyleSheet(u"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(45,50,65);\n"
"border-right:1px solid rgb(50, 55, 70);\n"
"padding-left: 3px;")
        self.lab_ldl_led.setFrame(False)
        self.lab_etc_title_lbl = QLabel(self.lab_results)
        self.lab_etc_title_lbl.setObjectName(u"lab_etc_title_lbl")
        self.lab_etc_title_lbl.setGeometry(QRect(400, 250, 120, 30))
        sizePolicy5.setHeightForWidth(self.lab_etc_title_lbl.sizePolicy().hasHeightForWidth())
        self.lab_etc_title_lbl.setSizePolicy(sizePolicy5)
        self.lab_etc_title_lbl.setMinimumSize(QSize(0, 0))
        self.lab_etc_title_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.lab_etc_title_lbl.setFont(font37)
        self.lab_etc_title_lbl.setStyleSheet(u"background-color:rgb(38, 43, 52);\n"
"color: rgb(125, 150, 200);\n"
"border:1px solid rgb(50, 55, 70);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;")
        self.lab_etc_title_lbl.setAlignment(Qt.AlignCenter)
        self.lab_inflm_title_lbl = QLabel(self.lab_results)
        self.lab_inflm_title_lbl.setObjectName(u"lab_inflm_title_lbl")
        self.lab_inflm_title_lbl.setGeometry(QRect(10, 310, 120, 30))
        sizePolicy5.setHeightForWidth(self.lab_inflm_title_lbl.sizePolicy().hasHeightForWidth())
        self.lab_inflm_title_lbl.setSizePolicy(sizePolicy5)
        self.lab_inflm_title_lbl.setMinimumSize(QSize(0, 0))
        self.lab_inflm_title_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.lab_inflm_title_lbl.setFont(font37)
        self.lab_inflm_title_lbl.setStyleSheet(u"background-color:rgb(38, 43, 52);\n"
"color: rgb(125, 150, 200);\n"
"border:1px solid rgb(50, 55, 70);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;")
        self.lab_inflm_title_lbl.setAlignment(Qt.AlignCenter)
        self.lab_others_title_lbl = QLabel(self.lab_results)
        self.lab_others_title_lbl.setObjectName(u"lab_others_title_lbl")
        self.lab_others_title_lbl.setGeometry(QRect(10, 450, 511, 30))
        sizePolicy5.setHeightForWidth(self.lab_others_title_lbl.sizePolicy().hasHeightForWidth())
        self.lab_others_title_lbl.setSizePolicy(sizePolicy5)
        self.lab_others_title_lbl.setMinimumSize(QSize(0, 0))
        self.lab_others_title_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.lab_others_title_lbl.setFont(font37)
        self.lab_others_title_lbl.setStyleSheet(u"background-color:rgb(38, 43, 52);\n"
"color: rgb(125, 150, 200);\n"
"border:1px solid rgb(50, 55, 70);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;")
        self.lab_others_title_lbl.setAlignment(Qt.AlignCenter)
        self.lab_others_pte = QPlainTextEdit(self.lab_results)
        self.lab_others_pte.setObjectName(u"lab_others_pte")
        self.lab_others_pte.setGeometry(QRect(10, 480, 511, 71))
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.lab_others_pte.sizePolicy().hasHeightForWidth())
        self.lab_others_pte.setSizePolicy(sizePolicy6)
        self.lab_others_pte.setMinimumSize(QSize(0, 0))
        self.lab_others_pte.setMaximumSize(QSize(16777215, 16777215))
        self.lab_others_pte.setFont(font30)
        self.lab_others_pte.setStyleSheet(u"color: rgb(177,188,211);\n"
"border:1px solid rgb(50, 55, 70);\n"
"border-top:0px;\n"
"border-bottom-right-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"padding:5px;\n"
"")
        self.lab_others_pte.setFrameShadow(QFrame.Plain)
        self.lab_others_pte.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lab_others_pte.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lab_others_pte.setReadOnly(False)
        self.lab_others_pte.setTextInteractionFlags(Qt.TextEditorInteraction)
        self.lab_inst_lbl = QLabel(self.lab_results)
        self.lab_inst_lbl.setObjectName(u"lab_inst_lbl")
        self.lab_inst_lbl.setGeometry(QRect(280, 60, 60, 30))
        self.lab_inst_lbl.setMinimumSize(QSize(60, 0))
        self.lab_inst_lbl.setMaximumSize(QSize(60, 16777215))
        self.lab_inst_lbl.setFont(font30)
        self.lab_inst_lbl.setStyleSheet(u"background:transparent;\n"
"color: rgb(133, 155, 200);\n"
"border-top:1px solid rgb(100,110,130);\n"
"border-bottom:1px solid rgb(100,110,130);")
        self.lab_inst_lbl.setAlignment(Qt.AlignCenter)
        self.lab_date_lbl = QLabel(self.lab_results)
        self.lab_date_lbl.setObjectName(u"lab_date_lbl")
        self.lab_date_lbl.setGeometry(QRect(10, 60, 60, 30))
        self.lab_date_lbl.setMinimumSize(QSize(60, 0))
        self.lab_date_lbl.setMaximumSize(QSize(60, 16777215))
        self.lab_date_lbl.setFont(font30)
        self.lab_date_lbl.setStyleSheet(u"background:transparent;\n"
"color: rgb(133, 155, 200);\n"
"border-top:1px solid rgb(100,110,130);\n"
"border-bottom:1px solid rgb(100,110,130);")
        self.lab_date_lbl.setAlignment(Qt.AlignCenter)
        self.lab_date_led = QLineEdit(self.lab_results)
        self.lab_date_led.setObjectName(u"lab_date_led")
        self.lab_date_led.setGeometry(QRect(70, 60, 211, 30))
        self.lab_date_led.setMinimumSize(QSize(0, 0))
        self.lab_date_led.setMaximumSize(QSize(16777215, 31))
        self.lab_date_led.setFont(font30)
        self.lab_date_led.setStyleSheet(u"background:transparent;\n"
"color: rgb(166,177,199);\n"
"border-top:1px solid rgb(100,110,130);\n"
"border-bottom:1px solid rgb(100,110,130);")
        self.lab_date_led.setFrame(False)
        self.lab_inst_led = QLineEdit(self.lab_results)
        self.lab_inst_led.setObjectName(u"lab_inst_led")
        self.lab_inst_led.setGeometry(QRect(340, 60, 181, 30))
        self.lab_inst_led.setMinimumSize(QSize(0, 0))
        self.lab_inst_led.setMaximumSize(QSize(16777215, 31))
        self.lab_inst_led.setFont(font30)
        self.lab_inst_led.setStyleSheet(u"background:transparent;\n"
"color: rgb(166,177,199);\n"
"border-top:1px solid rgb(100,110,130);\n"
"border-bottom:1px solid rgb(100,110,130);")
        self.lab_inst_led.setFrame(False)
        self.lab_title_lbl = QLabel(self.lab_results)
        self.lab_title_lbl.setObjectName(u"lab_title_lbl")
        self.lab_title_lbl.setGeometry(QRect(10, 20, 511, 41))
        font38 = QFont()
        font38.setFamilies([u"Verdana"])
        font38.setPointSize(16)
        font38.setBold(True)
        font38.setItalic(True)
        self.lab_title_lbl.setFont(font38)
        self.lab_title_lbl.setStyleSheet(u"color: rgb(94, 129, 172);")
        self.lab_title_lbl.setAlignment(Qt.AlignCenter)
        self.lab_copy_btn = QPushButton(self.lab_results)
        self.lab_copy_btn.setObjectName(u"lab_copy_btn")
        self.lab_copy_btn.setGeometry(QRect(380, 580, 141, 30))
        sizePolicy3.setHeightForWidth(self.lab_copy_btn.sizePolicy().hasHeightForWidth())
        self.lab_copy_btn.setSizePolicy(sizePolicy3)
        self.lab_copy_btn.setMinimumSize(QSize(0, 30))
        self.lab_copy_btn.setMaximumSize(QSize(16777215, 16777215))
        self.lab_copy_btn.setFont(font4)
        self.lab_copy_btn.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(200, 120, 100);\n"
"	background-color:rgb(45,50,60);\n"
"	border:0px;\n"
"	border-radius:10%;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:hover {    \n"
"	color: rgb(230, 110, 90);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.lab_copy_btn.setFlat(True)
        self.lab_reset_btn = QPushButton(self.lab_results)
        self.lab_reset_btn.setObjectName(u"lab_reset_btn")
        self.lab_reset_btn.setGeometry(QRect(280, 580, 81, 30))
        sizePolicy3.setHeightForWidth(self.lab_reset_btn.sizePolicy().hasHeightForWidth())
        self.lab_reset_btn.setSizePolicy(sizePolicy3)
        self.lab_reset_btn.setMinimumSize(QSize(0, 30))
        self.lab_reset_btn.setMaximumSize(QSize(16777215, 16777215))
        self.lab_reset_btn.setFont(font11)
        self.lab_reset_btn.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(160, 190, 150);\n"
"	background-color:rgb(45,50,60);\n"
"	border-radius:10%;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(140,200,130);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.lab_reset_btn.setFlat(True)
        self.studies_stack.addWidget(self.lab_results)
        self.bmd_results = QWidget()
        self.bmd_results.setObjectName(u"bmd_results")
        self.bmd_lspine_tscore_led = QLineEdit(self.bmd_results)
        self.bmd_lspine_tscore_led.setObjectName(u"bmd_lspine_tscore_led")
        self.bmd_lspine_tscore_led.setGeometry(QRect(130, 150, 131, 30))
        self.bmd_lspine_tscore_led.setMinimumSize(QSize(0, 30))
        self.bmd_lspine_tscore_led.setMaximumSize(QSize(16777215, 25))
        font39 = QFont()
        font39.setFamilies([u"\ub098\ub214\ubc14\ub978\uace0\ub515"])
        font39.setPointSize(12)
        self.bmd_lspine_tscore_led.setFont(font39)
        self.bmd_lspine_tscore_led.setStyleSheet(u"background:transparent;\n"
"color: rgb(177,188,211);\n"
"")
        self.bmd_lspine_tscore_led.setFrame(False)
        self.bmd_inst_lbl = QLabel(self.bmd_results)
        self.bmd_inst_lbl.setObjectName(u"bmd_inst_lbl")
        self.bmd_inst_lbl.setGeometry(QRect(280, 60, 60, 30))
        self.bmd_inst_lbl.setMinimumSize(QSize(60, 0))
        self.bmd_inst_lbl.setMaximumSize(QSize(60, 16777215))
        self.bmd_inst_lbl.setFont(font30)
        self.bmd_inst_lbl.setStyleSheet(u"background:transparent;\n"
"color: rgb(133, 155, 200);\n"
"border-top:1px solid rgb(100,110,130);\n"
"border-bottom:1px solid rgb(100,110,130);")
        self.bmd_inst_lbl.setAlignment(Qt.AlignCenter)
        self.bmd_inst_led = QLineEdit(self.bmd_results)
        self.bmd_inst_led.setObjectName(u"bmd_inst_led")
        self.bmd_inst_led.setGeometry(QRect(340, 60, 181, 30))
        self.bmd_inst_led.setMinimumSize(QSize(0, 0))
        self.bmd_inst_led.setMaximumSize(QSize(16777215, 31))
        self.bmd_inst_led.setFont(font30)
        self.bmd_inst_led.setStyleSheet(u"background:transparent;\n"
"color: rgb(166,177,199);\n"
"border-top:1px solid rgb(100,110,130);\n"
"border-bottom:1px solid rgb(100,110,130);")
        self.bmd_inst_led.setFrame(False)
        self.bmd_dexxa_title_lbl = QLabel(self.bmd_results)
        self.bmd_dexxa_title_lbl.setObjectName(u"bmd_dexxa_title_lbl")
        self.bmd_dexxa_title_lbl.setGeometry(QRect(10, 120, 511, 30))
        sizePolicy5.setHeightForWidth(self.bmd_dexxa_title_lbl.sizePolicy().hasHeightForWidth())
        self.bmd_dexxa_title_lbl.setSizePolicy(sizePolicy5)
        self.bmd_dexxa_title_lbl.setMinimumSize(QSize(0, 0))
        self.bmd_dexxa_title_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.bmd_dexxa_title_lbl.setFont(font37)
        self.bmd_dexxa_title_lbl.setStyleSheet(u"background-color:rgb(38, 43, 52);\n"
"color: rgb(125, 150, 200);\n"
"border:1px solid rgb(50, 55, 70);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;")
        self.bmd_dexxa_title_lbl.setAlignment(Qt.AlignCenter)
        self.bmd_femur_tscore_led = QLineEdit(self.bmd_results)
        self.bmd_femur_tscore_led.setObjectName(u"bmd_femur_tscore_led")
        self.bmd_femur_tscore_led.setGeometry(QRect(380, 150, 131, 30))
        self.bmd_femur_tscore_led.setMinimumSize(QSize(0, 30))
        self.bmd_femur_tscore_led.setMaximumSize(QSize(16777215, 25))
        self.bmd_femur_tscore_led.setFont(font39)
        self.bmd_femur_tscore_led.setStyleSheet(u"background:transparent;\n"
"color: rgb(177,188,211);")
        self.bmd_femur_tscore_led.setFrame(False)
        self.bmd_date_led = QLineEdit(self.bmd_results)
        self.bmd_date_led.setObjectName(u"bmd_date_led")
        self.bmd_date_led.setGeometry(QRect(70, 60, 211, 30))
        self.bmd_date_led.setMinimumSize(QSize(0, 0))
        self.bmd_date_led.setMaximumSize(QSize(16777215, 31))
        self.bmd_date_led.setFont(font30)
        self.bmd_date_led.setStyleSheet(u"background:transparent;\n"
"color: rgb(166,177,199);\n"
"border-top:1px solid rgb(100,110,130);\n"
"border-bottom:1px solid rgb(100,110,130);")
        self.bmd_date_led.setFrame(False)
        self.bmd_others_title_lbl = QLabel(self.bmd_results)
        self.bmd_others_title_lbl.setObjectName(u"bmd_others_title_lbl")
        self.bmd_others_title_lbl.setGeometry(QRect(10, 210, 511, 30))
        sizePolicy5.setHeightForWidth(self.bmd_others_title_lbl.sizePolicy().hasHeightForWidth())
        self.bmd_others_title_lbl.setSizePolicy(sizePolicy5)
        self.bmd_others_title_lbl.setMinimumSize(QSize(0, 0))
        self.bmd_others_title_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.bmd_others_title_lbl.setFont(font37)
        self.bmd_others_title_lbl.setStyleSheet(u"background-color:rgb(38, 43, 52);\n"
"color: rgb(125, 150, 200);\n"
"border:1px solid rgb(50, 55, 70);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;")
        self.bmd_others_title_lbl.setAlignment(Qt.AlignCenter)
        self.bmd_femur_cmb = QComboBox(self.bmd_results)
        self.bmd_femur_cmb.addItem("")
        self.bmd_femur_cmb.addItem("")
        self.bmd_femur_cmb.setObjectName(u"bmd_femur_cmb")
        self.bmd_femur_cmb.setGeometry(QRect(260, 150, 120, 30))
        sizePolicy5.setHeightForWidth(self.bmd_femur_cmb.sizePolicy().hasHeightForWidth())
        self.bmd_femur_cmb.setSizePolicy(sizePolicy5)
        self.bmd_femur_cmb.setMinimumSize(QSize(120, 30))
        self.bmd_femur_cmb.setMaximumSize(QSize(120, 31))
        self.bmd_femur_cmb.setFont(font36)
        self.bmd_femur_cmb.setStyleSheet(u"color: rgb(144, 155, 188);")
        self.bmd_femur_cmb.setFrame(False)
        self.bmd_date_lbl = QLabel(self.bmd_results)
        self.bmd_date_lbl.setObjectName(u"bmd_date_lbl")
        self.bmd_date_lbl.setGeometry(QRect(10, 60, 60, 30))
        self.bmd_date_lbl.setMinimumSize(QSize(60, 0))
        self.bmd_date_lbl.setMaximumSize(QSize(60, 16777215))
        self.bmd_date_lbl.setFont(font30)
        self.bmd_date_lbl.setStyleSheet(u"background:transparent;\n"
"color: rgb(133, 155, 200);\n"
"border-top:1px solid rgb(100,110,130);\n"
"border-bottom:1px solid rgb(100,110,130);")
        self.bmd_date_lbl.setAlignment(Qt.AlignCenter)
        self.bmd_lspine_lbl = QLabel(self.bmd_results)
        self.bmd_lspine_lbl.setObjectName(u"bmd_lspine_lbl")
        self.bmd_lspine_lbl.setGeometry(QRect(10, 150, 120, 30))
        self.bmd_lspine_lbl.setMinimumSize(QSize(120, 30))
        self.bmd_lspine_lbl.setMaximumSize(QSize(120, 25))
        self.bmd_lspine_lbl.setFont(font36)
        self.bmd_lspine_lbl.setStyleSheet(u"background:transparent;\n"
"color: rgb(144, 155, 188);\n"
"padding-left:10px;")
        self.bmd_lspine_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.bmd_others_pte = QPlainTextEdit(self.bmd_results)
        self.bmd_others_pte.setObjectName(u"bmd_others_pte")
        self.bmd_others_pte.setGeometry(QRect(10, 240, 511, 151))
        font40 = QFont()
        font40.setFamilies([u"\ub098\ub214\ubc14\ub978\uace0\ub515"])
        font40.setPointSize(10)
        self.bmd_others_pte.setFont(font40)
        self.bmd_others_pte.setStyleSheet(u"color: rgb(177,188,211);\n"
"border:1px solid rgb(50, 55, 70);\n"
"border-top:0px;\n"
"border-bottom-right-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"padding:5px;")
        self.bmd_others_pte.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.bmd_others_pte.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.bmd_others_pte.setReadOnly(False)
        self.bmd_box_lbl = QLabel(self.bmd_results)
        self.bmd_box_lbl.setObjectName(u"bmd_box_lbl")
        self.bmd_box_lbl.setGeometry(QRect(10, 150, 511, 31))
        self.bmd_box_lbl.setMinimumSize(QSize(60, 30))
        self.bmd_box_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.bmd_box_lbl.setFont(font39)
        self.bmd_box_lbl.setStyleSheet(u"color: rgb(177,188,211);\n"
"border:1px solid rgb(50, 55, 70);\n"
"border-top:0px;\n"
"border-bottom-right-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"padding:5px;\n"
"")
        self.bmd_box_lbl.setAlignment(Qt.AlignCenter)
        self.bmd_title_lbl = QLabel(self.bmd_results)
        self.bmd_title_lbl.setObjectName(u"bmd_title_lbl")
        self.bmd_title_lbl.setGeometry(QRect(10, 20, 511, 41))
        self.bmd_title_lbl.setFont(font38)
        self.bmd_title_lbl.setStyleSheet(u"color: rgb(94, 129, 172);")
        self.bmd_title_lbl.setAlignment(Qt.AlignCenter)
        self.bmd_copy_btn = QPushButton(self.bmd_results)
        self.bmd_copy_btn.setObjectName(u"bmd_copy_btn")
        self.bmd_copy_btn.setGeometry(QRect(380, 580, 141, 30))
        sizePolicy3.setHeightForWidth(self.bmd_copy_btn.sizePolicy().hasHeightForWidth())
        self.bmd_copy_btn.setSizePolicy(sizePolicy3)
        self.bmd_copy_btn.setMinimumSize(QSize(0, 30))
        self.bmd_copy_btn.setMaximumSize(QSize(16777215, 16777215))
        self.bmd_copy_btn.setFont(font4)
        self.bmd_copy_btn.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(200, 120, 100);\n"
"	background-color:rgb(45,50,60);\n"
"	border:0px;\n"
"	border-radius:10%;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:hover {    \n"
"	color: rgb(230, 110, 90);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.bmd_copy_btn.setFlat(True)
        self.bmd_reset_btn = QPushButton(self.bmd_results)
        self.bmd_reset_btn.setObjectName(u"bmd_reset_btn")
        self.bmd_reset_btn.setGeometry(QRect(280, 580, 81, 30))
        sizePolicy3.setHeightForWidth(self.bmd_reset_btn.sizePolicy().hasHeightForWidth())
        self.bmd_reset_btn.setSizePolicy(sizePolicy3)
        self.bmd_reset_btn.setMinimumSize(QSize(0, 30))
        self.bmd_reset_btn.setMaximumSize(QSize(16777215, 16777215))
        self.bmd_reset_btn.setFont(font11)
        self.bmd_reset_btn.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(160, 190, 150);\n"
"	background-color:rgb(45,50,60);\n"
"	border-radius:10%;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(140,200,130);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.bmd_reset_btn.setFlat(True)
        self.studies_stack.addWidget(self.bmd_results)
        self.bmd_box_lbl.raise_()
        self.bmd_lspine_tscore_led.raise_()
        self.bmd_inst_lbl.raise_()
        self.bmd_inst_led.raise_()
        self.bmd_dexxa_title_lbl.raise_()
        self.bmd_femur_tscore_led.raise_()
        self.bmd_date_led.raise_()
        self.bmd_others_title_lbl.raise_()
        self.bmd_femur_cmb.raise_()
        self.bmd_date_lbl.raise_()
        self.bmd_lspine_lbl.raise_()
        self.bmd_others_pte.raise_()
        self.bmd_title_lbl.raise_()
        self.bmd_copy_btn.raise_()
        self.bmd_reset_btn.raise_()
        self.alz_results = QWidget()
        self.alz_results.setObjectName(u"alz_results")
        self.alz_inst_led = QLineEdit(self.alz_results)
        self.alz_inst_led.setObjectName(u"alz_inst_led")
        self.alz_inst_led.setGeometry(QRect(340, 60, 181, 30))
        self.alz_inst_led.setMinimumSize(QSize(0, 0))
        self.alz_inst_led.setMaximumSize(QSize(16777215, 31))
        self.alz_inst_led.setFont(font30)
        self.alz_inst_led.setStyleSheet(u"background:transparent;\n"
"color: rgb(166,177,199);\n"
"border-top:1px solid rgb(100,110,130);\n"
"border-bottom:1px solid rgb(100,110,130);")
        self.alz_inst_led.setFrame(False)
        self.alz_mmse_led = QLineEdit(self.alz_results)
        self.alz_mmse_led.setObjectName(u"alz_mmse_led")
        self.alz_mmse_led.setGeometry(QRect(80, 150, 80, 30))
        self.alz_mmse_led.setMinimumSize(QSize(0, 30))
        self.alz_mmse_led.setMaximumSize(QSize(16777215, 25))
        self.alz_mmse_led.setFont(font39)
        self.alz_mmse_led.setStyleSheet(u"background:transparent;\n"
"color: rgb(177,188,211);")
        self.alz_mmse_led.setFrame(False)
        self.alz_fx_studies_title_lbl = QLabel(self.alz_results)
        self.alz_fx_studies_title_lbl.setObjectName(u"alz_fx_studies_title_lbl")
        self.alz_fx_studies_title_lbl.setGeometry(QRect(10, 120, 511, 30))
        sizePolicy5.setHeightForWidth(self.alz_fx_studies_title_lbl.sizePolicy().hasHeightForWidth())
        self.alz_fx_studies_title_lbl.setSizePolicy(sizePolicy5)
        self.alz_fx_studies_title_lbl.setMinimumSize(QSize(0, 0))
        self.alz_fx_studies_title_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.alz_fx_studies_title_lbl.setFont(font37)
        self.alz_fx_studies_title_lbl.setStyleSheet(u"background-color:rgb(38, 43, 52);\n"
"color: rgb(125, 150, 200);\n"
"border:1px solid rgb(50, 55, 70);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;")
        self.alz_fx_studies_title_lbl.setAlignment(Qt.AlignCenter)
        self.alz_cdr_lbl = QLabel(self.alz_results)
        self.alz_cdr_lbl.setObjectName(u"alz_cdr_lbl")
        self.alz_cdr_lbl.setGeometry(QRect(200, 150, 60, 30))
        self.alz_cdr_lbl.setMinimumSize(QSize(60, 30))
        self.alz_cdr_lbl.setMaximumSize(QSize(60, 30))
        self.alz_cdr_lbl.setFont(font36)
        self.alz_cdr_lbl.setStyleSheet(u"background:transparent;\n"
"color: rgb(144, 155, 188);")
        self.alz_cdr_lbl.setAlignment(Qt.AlignCenter)
        self.alz_date_led = QLineEdit(self.alz_results)
        self.alz_date_led.setObjectName(u"alz_date_led")
        self.alz_date_led.setGeometry(QRect(70, 60, 211, 30))
        self.alz_date_led.setMinimumSize(QSize(0, 0))
        self.alz_date_led.setMaximumSize(QSize(16777215, 31))
        self.alz_date_led.setFont(font30)
        self.alz_date_led.setStyleSheet(u"background:transparent;\n"
"color: rgb(166,177,199);\n"
"border-top:1px solid rgb(100,110,130);\n"
"border-bottom:1px solid rgb(100,110,130);")
        self.alz_date_led.setFrame(False)
        self.alz_cdr_led = QLineEdit(self.alz_results)
        self.alz_cdr_led.setObjectName(u"alz_cdr_led")
        self.alz_cdr_led.setGeometry(QRect(260, 150, 80, 30))
        self.alz_cdr_led.setMinimumSize(QSize(0, 30))
        self.alz_cdr_led.setMaximumSize(QSize(16777215, 25))
        self.alz_cdr_led.setFont(font39)
        self.alz_cdr_led.setStyleSheet(u"background:transparent;\n"
"color: rgb(177,188,211);")
        self.alz_cdr_led.setFrame(False)
        self.alz_comm_title_lbl = QLabel(self.alz_results)
        self.alz_comm_title_lbl.setObjectName(u"alz_comm_title_lbl")
        self.alz_comm_title_lbl.setGeometry(QRect(10, 210, 511, 30))
        sizePolicy5.setHeightForWidth(self.alz_comm_title_lbl.sizePolicy().hasHeightForWidth())
        self.alz_comm_title_lbl.setSizePolicy(sizePolicy5)
        self.alz_comm_title_lbl.setMinimumSize(QSize(0, 0))
        self.alz_comm_title_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.alz_comm_title_lbl.setFont(font37)
        self.alz_comm_title_lbl.setStyleSheet(u"background-color:rgb(38, 43, 52);\n"
"color: rgb(125, 150, 200);\n"
"border:1px solid rgb(50, 55, 70);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;")
        self.alz_comm_title_lbl.setAlignment(Qt.AlignCenter)
        self.alz_date_lbl = QLabel(self.alz_results)
        self.alz_date_lbl.setObjectName(u"alz_date_lbl")
        self.alz_date_lbl.setGeometry(QRect(10, 60, 60, 30))
        self.alz_date_lbl.setMinimumSize(QSize(60, 0))
        self.alz_date_lbl.setMaximumSize(QSize(60, 16777215))
        self.alz_date_lbl.setFont(font30)
        self.alz_date_lbl.setStyleSheet(u"background:transparent;\n"
"color: rgb(133, 155, 200);\n"
"border-top:1px solid rgb(100,110,130);\n"
"border-bottom:1px solid rgb(100,110,130);")
        self.alz_date_lbl.setAlignment(Qt.AlignCenter)
        self.alz_box_lbl = QLabel(self.alz_results)
        self.alz_box_lbl.setObjectName(u"alz_box_lbl")
        self.alz_box_lbl.setGeometry(QRect(10, 150, 511, 31))
        self.alz_box_lbl.setMinimumSize(QSize(60, 30))
        self.alz_box_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.alz_box_lbl.setFont(font39)
        self.alz_box_lbl.setStyleSheet(u"color: rgb(177,188,211);\n"
"border:1px solid rgb(50, 55, 70);\n"
"border-top:0px;\n"
"border-bottom-right-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"padding:5px;")
        self.alz_box_lbl.setAlignment(Qt.AlignCenter)
        self.alz_inst_lbl = QLabel(self.alz_results)
        self.alz_inst_lbl.setObjectName(u"alz_inst_lbl")
        self.alz_inst_lbl.setGeometry(QRect(280, 60, 60, 30))
        self.alz_inst_lbl.setMinimumSize(QSize(60, 0))
        self.alz_inst_lbl.setMaximumSize(QSize(60, 16777215))
        self.alz_inst_lbl.setFont(font30)
        self.alz_inst_lbl.setStyleSheet(u"background:transparent;\n"
"color: rgb(133, 155, 200);\n"
"border-top:1px solid rgb(100,110,130);\n"
"border-bottom:1px solid rgb(100,110,130);")
        self.alz_inst_lbl.setAlignment(Qt.AlignCenter)
        self.alz_mmse_lbl = QLabel(self.alz_results)
        self.alz_mmse_lbl.setObjectName(u"alz_mmse_lbl")
        self.alz_mmse_lbl.setGeometry(QRect(20, 150, 60, 30))
        self.alz_mmse_lbl.setMinimumSize(QSize(60, 30))
        self.alz_mmse_lbl.setMaximumSize(QSize(60, 30))
        self.alz_mmse_lbl.setFont(font36)
        self.alz_mmse_lbl.setStyleSheet(u"background:transparent;\n"
"color: rgb(144, 155, 188);")
        self.alz_mmse_lbl.setAlignment(Qt.AlignCenter)
        self.alz_comm_pte = QPlainTextEdit(self.alz_results)
        self.alz_comm_pte.setObjectName(u"alz_comm_pte")
        self.alz_comm_pte.setGeometry(QRect(10, 240, 511, 151))
        self.alz_comm_pte.setFont(font31)
        self.alz_comm_pte.setStyleSheet(u"color: rgb(177,188,211);\n"
"border:1px solid rgb(50, 55, 70);\n"
"border-top:0px;\n"
"border-bottom-right-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"padding:5px;")
        self.alz_comm_pte.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.alz_comm_pte.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.alz_comm_pte.setReadOnly(False)
        self.alz_comm_pte.setTextInteractionFlags(Qt.TextEditorInteraction)
        self.alz_gds_led = QLineEdit(self.alz_results)
        self.alz_gds_led.setObjectName(u"alz_gds_led")
        self.alz_gds_led.setGeometry(QRect(430, 150, 80, 30))
        self.alz_gds_led.setMinimumSize(QSize(0, 30))
        self.alz_gds_led.setMaximumSize(QSize(16777215, 25))
        self.alz_gds_led.setFont(font39)
        self.alz_gds_led.setStyleSheet(u"background:transparent;\n"
"color: rgb(177,188,211);")
        self.alz_gds_led.setFrame(False)
        self.alz_gds_lbl = QLabel(self.alz_results)
        self.alz_gds_lbl.setObjectName(u"alz_gds_lbl")
        self.alz_gds_lbl.setGeometry(QRect(370, 150, 60, 30))
        self.alz_gds_lbl.setMinimumSize(QSize(60, 30))
        self.alz_gds_lbl.setMaximumSize(QSize(60, 30))
        self.alz_gds_lbl.setFont(font36)
        self.alz_gds_lbl.setStyleSheet(u"background:transparent;\n"
"color: rgb(144, 155, 188);")
        self.alz_gds_lbl.setAlignment(Qt.AlignCenter)
        self.alz_title_lbl = QLabel(self.alz_results)
        self.alz_title_lbl.setObjectName(u"alz_title_lbl")
        self.alz_title_lbl.setGeometry(QRect(10, 20, 511, 41))
        self.alz_title_lbl.setFont(font38)
        self.alz_title_lbl.setStyleSheet(u"color: rgb(94, 129, 172);")
        self.alz_title_lbl.setAlignment(Qt.AlignCenter)
        self.alz_reset_btn = QPushButton(self.alz_results)
        self.alz_reset_btn.setObjectName(u"alz_reset_btn")
        self.alz_reset_btn.setGeometry(QRect(280, 580, 81, 30))
        sizePolicy3.setHeightForWidth(self.alz_reset_btn.sizePolicy().hasHeightForWidth())
        self.alz_reset_btn.setSizePolicy(sizePolicy3)
        self.alz_reset_btn.setMinimumSize(QSize(0, 30))
        self.alz_reset_btn.setMaximumSize(QSize(16777215, 16777215))
        self.alz_reset_btn.setFont(font11)
        self.alz_reset_btn.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(160, 190, 150);\n"
"	background-color:rgb(45,50,60);\n"
"	border-radius:10%;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(140,200,130);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.alz_reset_btn.setFlat(True)
        self.alz_copy_btn = QPushButton(self.alz_results)
        self.alz_copy_btn.setObjectName(u"alz_copy_btn")
        self.alz_copy_btn.setGeometry(QRect(380, 580, 141, 30))
        sizePolicy3.setHeightForWidth(self.alz_copy_btn.sizePolicy().hasHeightForWidth())
        self.alz_copy_btn.setSizePolicy(sizePolicy3)
        self.alz_copy_btn.setMinimumSize(QSize(0, 30))
        self.alz_copy_btn.setMaximumSize(QSize(16777215, 16777215))
        self.alz_copy_btn.setFont(font4)
        self.alz_copy_btn.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(200, 120, 100);\n"
"	background-color:rgb(45,50,60);\n"
"	border:0px;\n"
"	border-radius:10%;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:hover {    \n"
"	color: rgb(230, 110, 90);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.alz_copy_btn.setFlat(True)
        self.studies_stack.addWidget(self.alz_results)
        self.alz_box_lbl.raise_()
        self.alz_inst_led.raise_()
        self.alz_mmse_led.raise_()
        self.alz_fx_studies_title_lbl.raise_()
        self.alz_cdr_lbl.raise_()
        self.alz_date_led.raise_()
        self.alz_cdr_led.raise_()
        self.alz_comm_title_lbl.raise_()
        self.alz_date_lbl.raise_()
        self.alz_inst_lbl.raise_()
        self.alz_mmse_lbl.raise_()
        self.alz_comm_pte.raise_()
        self.alz_gds_led.raise_()
        self.alz_gds_lbl.raise_()
        self.alz_title_lbl.raise_()
        self.alz_reset_btn.raise_()
        self.alz_copy_btn.raise_()
        self.ipss_results = QWidget()
        self.ipss_results.setObjectName(u"ipss_results")
        self.ipss_scr_2 = QWidget(self.ipss_results)
        self.ipss_scr_2.setObjectName(u"ipss_scr_2")
        self.ipss_scr_2.setGeometry(QRect(10, 400, 511, 61))
        self.ipss_scr_2.setStyleSheet(u"border:1px solid rgb(70,75,90);\n"
"border-radius:10px;")
        self.gridLayout_13 = QGridLayout(self.ipss_scr_2)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(3, 3, 3, 3)
        self.ipss_scr_2_5i = QLabel(self.ipss_scr_2)
        self.ipss_scr_2_5i.setObjectName(u"ipss_scr_2_5i")
        self.ipss_scr_2_5i.setMinimumSize(QSize(0, 25))
        self.ipss_scr_2_5i.setMaximumSize(QSize(16777215, 25))
        self.ipss_scr_2_5i.setFont(font5)
        self.ipss_scr_2_5i.setStyleSheet(u"color: rgb(177, 188, 211);\n"
"border:none;\n"
"border-radius:15px;")
        self.ipss_scr_2_5i.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.ipss_scr_2_5i, 1, 5, 1, 1)

        self.ipss_scr_2_2i = QLabel(self.ipss_scr_2)
        self.ipss_scr_2_2i.setObjectName(u"ipss_scr_2_2i")
        self.ipss_scr_2_2i.setMinimumSize(QSize(0, 25))
        self.ipss_scr_2_2i.setMaximumSize(QSize(16777215, 25))
        self.ipss_scr_2_2i.setFont(font5)
        self.ipss_scr_2_2i.setStyleSheet(u"color: rgb(177, 188, 211);\n"
"border:none;")
        self.ipss_scr_2_2i.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.ipss_scr_2_2i, 1, 2, 1, 1)

        self.ipss_scr_2_5 = QLabel(self.ipss_scr_2)
        self.ipss_scr_2_5.setObjectName(u"ipss_scr_2_5")
        self.ipss_scr_2_5.setMinimumSize(QSize(0, 30))
        self.ipss_scr_2_5.setMaximumSize(QSize(16777215, 30))
        font41 = QFont()
        font41.setFamilies([u"Impact"])
        font41.setPointSize(20)
        font41.setBold(False)
        self.ipss_scr_2_5.setFont(font41)
        self.ipss_scr_2_5.setStyleSheet(u"color: rgb(133, 166, 233);\n"
"background:none;\n"
"border:none;\n"
"\n"
"")
        self.ipss_scr_2_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.ipss_scr_2_5, 0, 5, 1, 1)

        self.ipss_scr_2_3i = QLabel(self.ipss_scr_2)
        self.ipss_scr_2_3i.setObjectName(u"ipss_scr_2_3i")
        self.ipss_scr_2_3i.setMinimumSize(QSize(0, 25))
        self.ipss_scr_2_3i.setMaximumSize(QSize(16777215, 25))
        self.ipss_scr_2_3i.setFont(font5)
        self.ipss_scr_2_3i.setStyleSheet(u"color: rgb(177, 188, 211);\n"
"border:none;")
        self.ipss_scr_2_3i.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.ipss_scr_2_3i, 1, 3, 1, 1)

        self.ipss_scr_2_1 = QLabel(self.ipss_scr_2)
        self.ipss_scr_2_1.setObjectName(u"ipss_scr_2_1")
        self.ipss_scr_2_1.setMinimumSize(QSize(0, 30))
        self.ipss_scr_2_1.setMaximumSize(QSize(16777215, 30))
        self.ipss_scr_2_1.setFont(font41)
        self.ipss_scr_2_1.setStyleSheet(u"color: rgb(133, 166, 233);\n"
"background:none;\n"
"border:none;\n"
"\n"
"")
        self.ipss_scr_2_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.ipss_scr_2_1, 0, 1, 1, 1)

        self.ipss_scr_2_0i = QLabel(self.ipss_scr_2)
        self.ipss_scr_2_0i.setObjectName(u"ipss_scr_2_0i")
        self.ipss_scr_2_0i.setMinimumSize(QSize(0, 25))
        self.ipss_scr_2_0i.setMaximumSize(QSize(16777215, 25))
        self.ipss_scr_2_0i.setFont(font5)
        self.ipss_scr_2_0i.setStyleSheet(u"color: rgb(177, 188, 211);\n"
"border:none;\n"
"border-radius:15px;")
        self.ipss_scr_2_0i.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.ipss_scr_2_0i, 1, 0, 1, 1)

        self.ipss_scr_2_2 = QLabel(self.ipss_scr_2)
        self.ipss_scr_2_2.setObjectName(u"ipss_scr_2_2")
        self.ipss_scr_2_2.setMinimumSize(QSize(0, 30))
        self.ipss_scr_2_2.setMaximumSize(QSize(16777215, 30))
        self.ipss_scr_2_2.setFont(font41)
        self.ipss_scr_2_2.setStyleSheet(u"color: rgb(133, 166, 233);\n"
"background:none;\n"
"border:none;\n"
"\n"
"")
        self.ipss_scr_2_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.ipss_scr_2_2, 0, 2, 1, 1)

        self.ipss_scr_2_1i = QLabel(self.ipss_scr_2)
        self.ipss_scr_2_1i.setObjectName(u"ipss_scr_2_1i")
        self.ipss_scr_2_1i.setMinimumSize(QSize(0, 25))
        self.ipss_scr_2_1i.setMaximumSize(QSize(16777215, 25))
        self.ipss_scr_2_1i.setFont(font5)
        self.ipss_scr_2_1i.setStyleSheet(u"color: rgb(177, 188, 211);\n"
"border:none;")
        self.ipss_scr_2_1i.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.ipss_scr_2_1i, 1, 1, 1, 1)

        self.ipss_scr_2_3 = QLabel(self.ipss_scr_2)
        self.ipss_scr_2_3.setObjectName(u"ipss_scr_2_3")
        self.ipss_scr_2_3.setMinimumSize(QSize(0, 30))
        self.ipss_scr_2_3.setMaximumSize(QSize(16777215, 30))
        self.ipss_scr_2_3.setFont(font41)
        self.ipss_scr_2_3.setStyleSheet(u"color: rgb(133, 166, 233);\n"
"background:none;\n"
"border:none;\n"
"\n"
"")
        self.ipss_scr_2_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.ipss_scr_2_3, 0, 3, 1, 1)

        self.ipss_scr_2_0 = QLabel(self.ipss_scr_2)
        self.ipss_scr_2_0.setObjectName(u"ipss_scr_2_0")
        self.ipss_scr_2_0.setMinimumSize(QSize(0, 30))
        self.ipss_scr_2_0.setMaximumSize(QSize(16777215, 30))
        self.ipss_scr_2_0.setFont(font41)
        self.ipss_scr_2_0.setStyleSheet(u"color: rgb(133, 166, 233);\n"
"background:none;\n"
"border:none;\n"
"\n"
"")
        self.ipss_scr_2_0.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.ipss_scr_2_0, 0, 0, 1, 1)

        self.ipss_scr_2_4i = QLabel(self.ipss_scr_2)
        self.ipss_scr_2_4i.setObjectName(u"ipss_scr_2_4i")
        self.ipss_scr_2_4i.setMinimumSize(QSize(0, 25))
        self.ipss_scr_2_4i.setMaximumSize(QSize(16777215, 25))
        self.ipss_scr_2_4i.setFont(font5)
        self.ipss_scr_2_4i.setStyleSheet(u"color: rgb(177, 188, 211);\n"
"border:none;")
        self.ipss_scr_2_4i.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.ipss_scr_2_4i, 1, 4, 1, 1)

        self.ipss_scr_2_4 = QLabel(self.ipss_scr_2)
        self.ipss_scr_2_4.setObjectName(u"ipss_scr_2_4")
        self.ipss_scr_2_4.setMinimumSize(QSize(0, 30))
        self.ipss_scr_2_4.setMaximumSize(QSize(16777215, 30))
        self.ipss_scr_2_4.setFont(font41)
        self.ipss_scr_2_4.setStyleSheet(u"color: rgb(133, 166, 233);\n"
"background:none;\n"
"border:none;\n"
"\n"
"")
        self.ipss_scr_2_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.ipss_scr_2_4, 0, 4, 1, 1)

        self.ipss_date_lbl = QLabel(self.ipss_results)
        self.ipss_date_lbl.setObjectName(u"ipss_date_lbl")
        self.ipss_date_lbl.setGeometry(QRect(10, 60, 60, 30))
        self.ipss_date_lbl.setMinimumSize(QSize(60, 0))
        self.ipss_date_lbl.setMaximumSize(QSize(60, 16777215))
        self.ipss_date_lbl.setFont(font30)
        self.ipss_date_lbl.setStyleSheet(u"background:transparent;\n"
"color: rgb(133, 155, 200);\n"
"border-top:1px solid rgb(100,110,130);\n"
"border-bottom:1px solid rgb(100,110,130);")
        self.ipss_date_lbl.setAlignment(Qt.AlignCenter)
        self.ipss_1_cmb = QComboBox(self.ipss_results)
        self.ipss_1_cmb.addItem("")
        self.ipss_1_cmb.addItem("")
        self.ipss_1_cmb.addItem("")
        self.ipss_1_cmb.addItem("")
        self.ipss_1_cmb.addItem("")
        self.ipss_1_cmb.addItem("")
        self.ipss_1_cmb.addItem("")
        self.ipss_1_cmb.setObjectName(u"ipss_1_cmb")
        self.ipss_1_cmb.setGeometry(QRect(460, 200, 50, 30))
        self.ipss_1_cmb.setMinimumSize(QSize(0, 0))
        self.ipss_1_cmb.setMaximumSize(QSize(16777215, 30))
        palette5 = QPalette()
        brush26 = QBrush(QColor(133, 166, 255, 255))
        brush26.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush26)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush26)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush26)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette5.setBrush(QPalette.Active, QPalette.Highlight, brush13)
        brush27 = QBrush(QColor(133, 166, 255, 128))
        brush27.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush27)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush26)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush26)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush26)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette5.setBrush(QPalette.Inactive, QPalette.Highlight, brush13)
        brush28 = QBrush(QColor(133, 166, 255, 128))
        brush28.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush28)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush26)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush26)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush26)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        brush29 = QBrush(QColor(133, 166, 255, 128))
        brush29.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush29)
#endif
        self.ipss_1_cmb.setPalette(palette5)
        self.ipss_1_cmb.setFont(font1)
        self.ipss_1_cmb.setStyleSheet(u"border:none;\n"
"border-bottom:1px solid rgb(44,55,77);")
        self.ipss_1_cmb.setFrame(False)
        self.ipss_inst_led = QLineEdit(self.ipss_results)
        self.ipss_inst_led.setObjectName(u"ipss_inst_led")
        self.ipss_inst_led.setGeometry(QRect(340, 60, 181, 30))
        self.ipss_inst_led.setMinimumSize(QSize(0, 0))
        self.ipss_inst_led.setMaximumSize(QSize(16777215, 31))
        self.ipss_inst_led.setFont(font30)
        self.ipss_inst_led.setStyleSheet(u"background:transparent;\n"
"color: rgb(166,177,199);\n"
"border-top:1px solid rgb(100,110,130);\n"
"border-bottom:1px solid rgb(100,110,130);")
        self.ipss_inst_led.setFrame(False)
        self.ipss_3_cmb = QComboBox(self.ipss_results)
        self.ipss_3_cmb.addItem("")
        self.ipss_3_cmb.addItem("")
        self.ipss_3_cmb.addItem("")
        self.ipss_3_cmb.addItem("")
        self.ipss_3_cmb.addItem("")
        self.ipss_3_cmb.addItem("")
        self.ipss_3_cmb.addItem("")
        self.ipss_3_cmb.setObjectName(u"ipss_3_cmb")
        self.ipss_3_cmb.setGeometry(QRect(460, 260, 50, 30))
        self.ipss_3_cmb.setMinimumSize(QSize(0, 0))
        self.ipss_3_cmb.setMaximumSize(QSize(16777215, 30))
        self.ipss_3_cmb.setFont(font1)
        self.ipss_3_cmb.setStyleSheet(u"border:none;\n"
"border-bottom:1px solid rgb(44,55,77);")
        self.ipss_3_cmb.setFrame(False)
        self.ipss_6_lbl = QLabel(self.ipss_results)
        self.ipss_6_lbl.setObjectName(u"ipss_6_lbl")
        self.ipss_6_lbl.setGeometry(QRect(20, 350, 440, 30))
        self.ipss_6_lbl.setMinimumSize(QSize(0, 30))
        self.ipss_6_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.ipss_6_lbl.setFont(font9)
        self.ipss_6_lbl.setStyleSheet(u"background:none;\n"
"color: rgb(155, 166, 200);\n"
"border:none;\n"
"border-bottom:1px solid rgb(44,55,77);\n"
"")
        self.ipss_6_lbl.setWordWrap(True)
        self.ipss_2_cmb = QComboBox(self.ipss_results)
        self.ipss_2_cmb.addItem("")
        self.ipss_2_cmb.addItem("")
        self.ipss_2_cmb.addItem("")
        self.ipss_2_cmb.addItem("")
        self.ipss_2_cmb.addItem("")
        self.ipss_2_cmb.addItem("")
        self.ipss_2_cmb.addItem("")
        self.ipss_2_cmb.setObjectName(u"ipss_2_cmb")
        self.ipss_2_cmb.setGeometry(QRect(460, 230, 50, 30))
        self.ipss_2_cmb.setMinimumSize(QSize(0, 0))
        self.ipss_2_cmb.setMaximumSize(QSize(16777215, 30))
        self.ipss_2_cmb.setFont(font1)
        self.ipss_2_cmb.setStyleSheet(u"border:none;\n"
"border-bottom:1px solid rgb(44,55,77);")
        self.ipss_2_cmb.setFrame(False)
        self.ipss_7_lbl = QLabel(self.ipss_results)
        self.ipss_7_lbl.setObjectName(u"ipss_7_lbl")
        self.ipss_7_lbl.setGeometry(QRect(20, 480, 440, 30))
        sizePolicy6.setHeightForWidth(self.ipss_7_lbl.sizePolicy().hasHeightForWidth())
        self.ipss_7_lbl.setSizePolicy(sizePolicy6)
        self.ipss_7_lbl.setMinimumSize(QSize(0, 30))
        self.ipss_7_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.ipss_7_lbl.setFont(font9)
        self.ipss_7_lbl.setStyleSheet(u"background:none;\n"
"color: rgb(155, 166, 200);\n"
"border:none;\n"
"border-bottom:1px solid rgb(44,55,77);\n"
"")
        self.ipss_7_lbl.setWordWrap(True)
        self.ipss_3_lbl = QLabel(self.ipss_results)
        self.ipss_3_lbl.setObjectName(u"ipss_3_lbl")
        self.ipss_3_lbl.setGeometry(QRect(20, 260, 440, 30))
        self.ipss_3_lbl.setMinimumSize(QSize(0, 30))
        self.ipss_3_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.ipss_3_lbl.setFont(font9)
        self.ipss_3_lbl.setStyleSheet(u"background:none;\n"
"color: rgb(155, 166, 200);\n"
"border:none;\n"
"border-bottom:1px solid rgb(44,55,77);\n"
"")
        self.ipss_3_lbl.setWordWrap(True)
        self.ipss_4_cmb = QComboBox(self.ipss_results)
        self.ipss_4_cmb.addItem("")
        self.ipss_4_cmb.addItem("")
        self.ipss_4_cmb.addItem("")
        self.ipss_4_cmb.addItem("")
        self.ipss_4_cmb.addItem("")
        self.ipss_4_cmb.addItem("")
        self.ipss_4_cmb.addItem("")
        self.ipss_4_cmb.setObjectName(u"ipss_4_cmb")
        self.ipss_4_cmb.setGeometry(QRect(460, 290, 50, 30))
        self.ipss_4_cmb.setMinimumSize(QSize(0, 0))
        self.ipss_4_cmb.setMaximumSize(QSize(16777215, 30))
        self.ipss_4_cmb.setFont(font1)
        self.ipss_4_cmb.setStyleSheet(u"border:none;\n"
"border-bottom:1px solid rgb(44,55,77);")
        self.ipss_4_cmb.setFrame(False)
        self.ipss_5_cmb = QComboBox(self.ipss_results)
        self.ipss_5_cmb.addItem("")
        self.ipss_5_cmb.addItem("")
        self.ipss_5_cmb.addItem("")
        self.ipss_5_cmb.addItem("")
        self.ipss_5_cmb.addItem("")
        self.ipss_5_cmb.addItem("")
        self.ipss_5_cmb.addItem("")
        self.ipss_5_cmb.setObjectName(u"ipss_5_cmb")
        self.ipss_5_cmb.setGeometry(QRect(460, 320, 50, 30))
        self.ipss_5_cmb.setMinimumSize(QSize(0, 0))
        self.ipss_5_cmb.setMaximumSize(QSize(16777215, 30))
        self.ipss_5_cmb.setFont(font1)
        self.ipss_5_cmb.setStyleSheet(u"border:none;\n"
"border-bottom:1px solid rgb(44,55,77);")
        self.ipss_5_cmb.setFrame(False)
        self.ipss_7_cmb = QComboBox(self.ipss_results)
        self.ipss_7_cmb.addItem("")
        self.ipss_7_cmb.addItem("")
        self.ipss_7_cmb.addItem("")
        self.ipss_7_cmb.addItem("")
        self.ipss_7_cmb.addItem("")
        self.ipss_7_cmb.addItem("")
        self.ipss_7_cmb.addItem("")
        self.ipss_7_cmb.setObjectName(u"ipss_7_cmb")
        self.ipss_7_cmb.setGeometry(QRect(460, 480, 50, 30))
        self.ipss_7_cmb.setMinimumSize(QSize(0, 0))
        self.ipss_7_cmb.setMaximumSize(QSize(16777215, 30))
        self.ipss_7_cmb.setFont(font1)
        self.ipss_7_cmb.setStyleSheet(u"border:none;\n"
"border-bottom:1px solid rgb(44,55,77);")
        self.ipss_7_cmb.setFrame(False)
        self.ipss_inst_lbl = QLabel(self.ipss_results)
        self.ipss_inst_lbl.setObjectName(u"ipss_inst_lbl")
        self.ipss_inst_lbl.setGeometry(QRect(280, 60, 60, 30))
        self.ipss_inst_lbl.setMinimumSize(QSize(60, 0))
        self.ipss_inst_lbl.setMaximumSize(QSize(60, 16777215))
        self.ipss_inst_lbl.setFont(font30)
        self.ipss_inst_lbl.setStyleSheet(u"background:transparent;\n"
"color: rgb(133, 155, 200);\n"
"border-top:1px solid rgb(100,110,130);\n"
"border-bottom:1px solid rgb(100,110,130);")
        self.ipss_inst_lbl.setAlignment(Qt.AlignCenter)
        self.ipss_5_lbl = QLabel(self.ipss_results)
        self.ipss_5_lbl.setObjectName(u"ipss_5_lbl")
        self.ipss_5_lbl.setGeometry(QRect(20, 320, 440, 30))
        self.ipss_5_lbl.setMinimumSize(QSize(0, 30))
        self.ipss_5_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.ipss_5_lbl.setFont(font9)
        self.ipss_5_lbl.setStyleSheet(u"background:none;\n"
"color: rgb(155, 166, 200);\n"
"border:none;\n"
"border-bottom:1px solid rgb(44,55,77);\n"
"")
        self.ipss_5_lbl.setWordWrap(True)
        self.ipss_date_led = QLineEdit(self.ipss_results)
        self.ipss_date_led.setObjectName(u"ipss_date_led")
        self.ipss_date_led.setGeometry(QRect(70, 60, 211, 30))
        self.ipss_date_led.setMinimumSize(QSize(0, 0))
        self.ipss_date_led.setMaximumSize(QSize(16777215, 31))
        self.ipss_date_led.setFont(font30)
        self.ipss_date_led.setStyleSheet(u"background:transparent;\n"
"color: rgb(166,177,199);\n"
"border-top:1px solid rgb(100,110,130);\n"
"border-bottom:1px solid rgb(100,110,130);")
        self.ipss_date_led.setFrame(False)
        self.ipss_6_cmb = QComboBox(self.ipss_results)
        self.ipss_6_cmb.addItem("")
        self.ipss_6_cmb.addItem("")
        self.ipss_6_cmb.addItem("")
        self.ipss_6_cmb.addItem("")
        self.ipss_6_cmb.addItem("")
        self.ipss_6_cmb.addItem("")
        self.ipss_6_cmb.addItem("")
        self.ipss_6_cmb.setObjectName(u"ipss_6_cmb")
        self.ipss_6_cmb.setGeometry(QRect(460, 350, 50, 30))
        self.ipss_6_cmb.setMinimumSize(QSize(0, 0))
        self.ipss_6_cmb.setMaximumSize(QSize(16777215, 30))
        self.ipss_6_cmb.setFont(font1)
        self.ipss_6_cmb.setStyleSheet(u"border:none;\n"
"border-bottom:1px solid rgb(44,55,77);")
        self.ipss_6_cmb.setFrame(False)
        self.ipss_2_lbl = QLabel(self.ipss_results)
        self.ipss_2_lbl.setObjectName(u"ipss_2_lbl")
        self.ipss_2_lbl.setGeometry(QRect(20, 230, 440, 30))
        self.ipss_2_lbl.setMinimumSize(QSize(0, 30))
        self.ipss_2_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.ipss_2_lbl.setFont(font9)
        self.ipss_2_lbl.setStyleSheet(u"background:none;\n"
"color: rgb(155, 166, 200);\n"
"border:none;\n"
"border-bottom:1px solid rgb(44,55,77);\n"
"")
        self.ipss_2_lbl.setWordWrap(True)
        self.ipss_1_lbl = QLabel(self.ipss_results)
        self.ipss_1_lbl.setObjectName(u"ipss_1_lbl")
        self.ipss_1_lbl.setGeometry(QRect(20, 200, 440, 30))
        sizePolicy6.setHeightForWidth(self.ipss_1_lbl.sizePolicy().hasHeightForWidth())
        self.ipss_1_lbl.setSizePolicy(sizePolicy6)
        self.ipss_1_lbl.setMinimumSize(QSize(0, 30))
        self.ipss_1_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.ipss_1_lbl.setFont(font9)
        self.ipss_1_lbl.setStyleSheet(u"background:none;\n"
"color: rgb(155, 166, 200);\n"
"border:none;\n"
"border-bottom:1px solid rgb(44,55,77);\n"
"")
        self.ipss_1_lbl.setWordWrap(True)
        self.ipss_4_lbl = QLabel(self.ipss_results)
        self.ipss_4_lbl.setObjectName(u"ipss_4_lbl")
        self.ipss_4_lbl.setGeometry(QRect(20, 290, 440, 30))
        self.ipss_4_lbl.setMinimumSize(QSize(0, 30))
        self.ipss_4_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.ipss_4_lbl.setFont(font9)
        self.ipss_4_lbl.setStyleSheet(u"background:none;\n"
"color: rgb(155, 166, 200);\n"
"border:none;\n"
"border-bottom:1px solid rgb(44,55,77);\n"
"")
        self.ipss_4_lbl.setWordWrap(True)
        self.ipss_scr_1 = QWidget(self.ipss_results)
        self.ipss_scr_1.setObjectName(u"ipss_scr_1")
        self.ipss_scr_1.setGeometry(QRect(10, 120, 511, 61))
        self.ipss_scr_1.setStyleSheet(u"border:1px solid rgb(70,75,90);\n"
"border-radius:10px;")
        self.gridLayout_14 = QGridLayout(self.ipss_scr_1)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(3, 3, 3, 3)
        self.ipss_scr_1_2i = QLabel(self.ipss_scr_1)
        self.ipss_scr_1_2i.setObjectName(u"ipss_scr_1_2i")
        self.ipss_scr_1_2i.setMinimumSize(QSize(0, 30))
        self.ipss_scr_1_2i.setMaximumSize(QSize(16777215, 30))
        self.ipss_scr_1_2i.setFont(font5)
        self.ipss_scr_1_2i.setStyleSheet(u"color: rgb(177, 188, 211);\n"
"border:none;")
        self.ipss_scr_1_2i.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.ipss_scr_1_2i, 1, 2, 1, 1)

        self.ipss_scr_1_1 = QLabel(self.ipss_scr_1)
        self.ipss_scr_1_1.setObjectName(u"ipss_scr_1_1")
        self.ipss_scr_1_1.setMinimumSize(QSize(0, 30))
        self.ipss_scr_1_1.setMaximumSize(QSize(16777215, 30))
        self.ipss_scr_1_1.setFont(font41)
        self.ipss_scr_1_1.setStyleSheet(u"color: rgb(133, 166, 233);\n"
"background:none;\n"
"border:none;\n"
"\n"
"")
        self.ipss_scr_1_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.ipss_scr_1_1, 0, 1, 1, 1)

        self.ipss_scr_1_2 = QLabel(self.ipss_scr_1)
        self.ipss_scr_1_2.setObjectName(u"ipss_scr_1_2")
        self.ipss_scr_1_2.setMinimumSize(QSize(0, 30))
        self.ipss_scr_1_2.setMaximumSize(QSize(16777215, 30))
        self.ipss_scr_1_2.setFont(font41)
        self.ipss_scr_1_2.setStyleSheet(u"color: rgb(133, 166, 233);\n"
"background:none;\n"
"border:none;\n"
"\n"
"")
        self.ipss_scr_1_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.ipss_scr_1_2, 0, 2, 1, 1)

        self.ipss_scr_1_0 = QLabel(self.ipss_scr_1)
        self.ipss_scr_1_0.setObjectName(u"ipss_scr_1_0")
        self.ipss_scr_1_0.setMinimumSize(QSize(0, 30))
        self.ipss_scr_1_0.setMaximumSize(QSize(16777215, 30))
        self.ipss_scr_1_0.setFont(font41)
        self.ipss_scr_1_0.setStyleSheet(u"color: rgb(133, 166, 233);\n"
"background:none;\n"
"border:none;\n"
"\n"
"")
        self.ipss_scr_1_0.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.ipss_scr_1_0, 0, 0, 1, 1)

        self.ipss_scr_1_5 = QLabel(self.ipss_scr_1)
        self.ipss_scr_1_5.setObjectName(u"ipss_scr_1_5")
        self.ipss_scr_1_5.setMinimumSize(QSize(0, 30))
        self.ipss_scr_1_5.setMaximumSize(QSize(16777215, 30))
        self.ipss_scr_1_5.setFont(font41)
        self.ipss_scr_1_5.setStyleSheet(u"color: rgb(133, 166, 233);\n"
"background:none;\n"
"border:none;\n"
"\n"
"")
        self.ipss_scr_1_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.ipss_scr_1_5, 0, 5, 1, 1)

        self.ipss_scr_1_0i = QLabel(self.ipss_scr_1)
        self.ipss_scr_1_0i.setObjectName(u"ipss_scr_1_0i")
        self.ipss_scr_1_0i.setMinimumSize(QSize(0, 30))
        self.ipss_scr_1_0i.setMaximumSize(QSize(16777215, 30))
        self.ipss_scr_1_0i.setFont(font5)
        self.ipss_scr_1_0i.setStyleSheet(u"color: rgb(177, 188, 211);\n"
"border:none;")
        self.ipss_scr_1_0i.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.ipss_scr_1_0i, 1, 0, 1, 1)

        self.ipss_scr_1_4i = QLabel(self.ipss_scr_1)
        self.ipss_scr_1_4i.setObjectName(u"ipss_scr_1_4i")
        self.ipss_scr_1_4i.setMinimumSize(QSize(0, 30))
        self.ipss_scr_1_4i.setMaximumSize(QSize(16777215, 30))
        self.ipss_scr_1_4i.setFont(font5)
        self.ipss_scr_1_4i.setStyleSheet(u"color: rgb(177, 188, 211);\n"
"border:none;")
        self.ipss_scr_1_4i.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.ipss_scr_1_4i, 1, 4, 1, 1)

        self.ipss_scr_1_5i = QLabel(self.ipss_scr_1)
        self.ipss_scr_1_5i.setObjectName(u"ipss_scr_1_5i")
        self.ipss_scr_1_5i.setMinimumSize(QSize(0, 30))
        self.ipss_scr_1_5i.setMaximumSize(QSize(16777215, 30))
        self.ipss_scr_1_5i.setFont(font5)
        self.ipss_scr_1_5i.setStyleSheet(u"color: rgb(177, 188, 211);\n"
"border:none;")
        self.ipss_scr_1_5i.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.ipss_scr_1_5i, 1, 5, 1, 1)

        self.ipss_scr_1_3i = QLabel(self.ipss_scr_1)
        self.ipss_scr_1_3i.setObjectName(u"ipss_scr_1_3i")
        self.ipss_scr_1_3i.setMinimumSize(QSize(0, 30))
        self.ipss_scr_1_3i.setMaximumSize(QSize(16777215, 30))
        self.ipss_scr_1_3i.setFont(font5)
        self.ipss_scr_1_3i.setStyleSheet(u"color: rgb(177, 188, 211);\n"
"border:none;")
        self.ipss_scr_1_3i.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.ipss_scr_1_3i, 1, 3, 1, 1)

        self.ipss_scr_1_3 = QLabel(self.ipss_scr_1)
        self.ipss_scr_1_3.setObjectName(u"ipss_scr_1_3")
        self.ipss_scr_1_3.setMinimumSize(QSize(0, 30))
        self.ipss_scr_1_3.setMaximumSize(QSize(16777215, 30))
        self.ipss_scr_1_3.setFont(font41)
        self.ipss_scr_1_3.setStyleSheet(u"color: rgb(133, 166, 233);\n"
"background:none;\n"
"border:none;\n"
"\n"
"")
        self.ipss_scr_1_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.ipss_scr_1_3, 0, 3, 1, 1)

        self.ipss_scr_1_1i = QLabel(self.ipss_scr_1)
        self.ipss_scr_1_1i.setObjectName(u"ipss_scr_1_1i")
        self.ipss_scr_1_1i.setMinimumSize(QSize(0, 30))
        self.ipss_scr_1_1i.setMaximumSize(QSize(16777215, 30))
        self.ipss_scr_1_1i.setFont(font5)
        self.ipss_scr_1_1i.setStyleSheet(u"color: rgb(177, 188, 211);\n"
"border:none;")
        self.ipss_scr_1_1i.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.ipss_scr_1_1i, 1, 1, 1, 1)

        self.ipss_scr_1_4 = QLabel(self.ipss_scr_1)
        self.ipss_scr_1_4.setObjectName(u"ipss_scr_1_4")
        self.ipss_scr_1_4.setMinimumSize(QSize(0, 30))
        self.ipss_scr_1_4.setMaximumSize(QSize(16777215, 30))
        self.ipss_scr_1_4.setFont(font41)
        self.ipss_scr_1_4.setStyleSheet(u"color: rgb(133, 166, 233);\n"
"background:none;\n"
"border:none;\n"
"\n"
"")
        self.ipss_scr_1_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.ipss_scr_1_4, 0, 4, 1, 1)

        self.ipss_title_lbl = QLabel(self.ipss_results)
        self.ipss_title_lbl.setObjectName(u"ipss_title_lbl")
        self.ipss_title_lbl.setGeometry(QRect(10, 20, 511, 41))
        self.ipss_title_lbl.setFont(font38)
        self.ipss_title_lbl.setStyleSheet(u"color: rgb(94, 129, 172);")
        self.ipss_title_lbl.setAlignment(Qt.AlignCenter)
        self.ipss_reset_btn = QPushButton(self.ipss_results)
        self.ipss_reset_btn.setObjectName(u"ipss_reset_btn")
        self.ipss_reset_btn.setGeometry(QRect(280, 580, 81, 30))
        sizePolicy3.setHeightForWidth(self.ipss_reset_btn.sizePolicy().hasHeightForWidth())
        self.ipss_reset_btn.setSizePolicy(sizePolicy3)
        self.ipss_reset_btn.setMinimumSize(QSize(0, 30))
        self.ipss_reset_btn.setMaximumSize(QSize(16777215, 16777215))
        self.ipss_reset_btn.setFont(font11)
        self.ipss_reset_btn.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(160, 190, 150);\n"
"	background-color:rgb(45,50,60);\n"
"	border-radius:10%;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(140,200,130);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.ipss_reset_btn.setFlat(True)
        self.ipss_copy_btn = QPushButton(self.ipss_results)
        self.ipss_copy_btn.setObjectName(u"ipss_copy_btn")
        self.ipss_copy_btn.setGeometry(QRect(380, 580, 141, 30))
        sizePolicy3.setHeightForWidth(self.ipss_copy_btn.sizePolicy().hasHeightForWidth())
        self.ipss_copy_btn.setSizePolicy(sizePolicy3)
        self.ipss_copy_btn.setMinimumSize(QSize(0, 30))
        self.ipss_copy_btn.setMaximumSize(QSize(16777215, 16777215))
        self.ipss_copy_btn.setFont(font4)
        self.ipss_copy_btn.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(200, 120, 100);\n"
"	background-color:rgb(45,50,60);\n"
"	border:0px;\n"
"	border-radius:10%;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:hover {    \n"
"	color: rgb(230, 110, 90);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.ipss_copy_btn.setFlat(True)
        self.studies_stack.addWidget(self.ipss_results)
        self.apps_stack.addWidget(self.studies)
        self.labeler = QWidget()
        self.labeler.setObjectName(u"labeler")
        self.lblr_count_gbx = QGroupBox(self.labeler)
        self.lblr_count_gbx.setObjectName(u"lblr_count_gbx")
        self.lblr_count_gbx.setGeometry(QRect(10, 20, 151, 271))
        self.lblr_count_gbx.setStyleSheet(u"QGroupBox{\n"
"	color: rgb(190, 200, 240);\n"
"	border:1px solid rgb(50, 55, 70);\n"
"	border-radius:10px;\n"
"}")
        self.lblr_count_total_covid_led = QLineEdit(self.lblr_count_gbx)
        self.lblr_count_total_covid_led.setObjectName(u"lblr_count_total_covid_led")
        self.lblr_count_total_covid_led.setGeometry(QRect(90, 50, 51, 30))
        self.lblr_count_total_covid_led.setMinimumSize(QSize(0, 30))
        self.lblr_count_total_covid_led.setMaximumSize(QSize(16777215, 30))
        self.lblr_count_total_covid_led.setFont(font28)
        self.lblr_count_total_covid_led.setStyleSheet(u"background:transparent;\n"
"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(70,80,100);")
        self.lblr_count_total_covid_led.setFrame(False)
        self.lblr_count_old_flu_ex_led = QLineEdit(self.lblr_count_gbx)
        self.lblr_count_old_flu_ex_led.setObjectName(u"lblr_count_old_flu_ex_led")
        self.lblr_count_old_flu_ex_led.setGeometry(QRect(90, 230, 51, 30))
        self.lblr_count_old_flu_ex_led.setMinimumSize(QSize(0, 30))
        self.lblr_count_old_flu_ex_led.setMaximumSize(QSize(16777215, 30))
        self.lblr_count_old_flu_ex_led.setFont(font31)
        self.lblr_count_old_flu_ex_led.setStyleSheet(u"background:transparent;\n"
"color: rgb(177,188,211);\n"
"padding-left:5px;")
        self.lblr_count_old_flu_ex_led.setFrame(False)
        self.lblr_count_total_covid_lbl = QLabel(self.lblr_count_gbx)
        self.lblr_count_total_covid_lbl.setObjectName(u"lblr_count_total_covid_lbl")
        self.lblr_count_total_covid_lbl.setGeometry(QRect(19, 50, 71, 30))
        self.lblr_count_total_covid_lbl.setMinimumSize(QSize(0, 30))
        self.lblr_count_total_covid_lbl.setMaximumSize(QSize(16777215, 30))
        self.lblr_count_total_covid_lbl.setFont(font28)
        self.lblr_count_total_covid_lbl.setStyleSheet(u"background:transparent;\n"
"color: rgb(155, 166, 200);\n"
"border-bottom:1px solid rgb(70,80,100);")
        self.lblr_count_total_covid_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lblr_count_child_flu_lbl = QLabel(self.lblr_count_gbx)
        self.lblr_count_child_flu_lbl.setObjectName(u"lblr_count_child_flu_lbl")
        self.lblr_count_child_flu_lbl.setGeometry(QRect(10, 200, 80, 30))
        self.lblr_count_child_flu_lbl.setMinimumSize(QSize(0, 30))
        self.lblr_count_child_flu_lbl.setMaximumSize(QSize(16777215, 30))
        self.lblr_count_child_flu_lbl.setFont(font31)
        self.lblr_count_child_flu_lbl.setStyleSheet(u"background:transparent;\n"
"color: rgb(133, 155, 200);")
        self.lblr_count_child_flu_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lblr_count_child_flu_led = QLineEdit(self.lblr_count_gbx)
        self.lblr_count_child_flu_led.setObjectName(u"lblr_count_child_flu_led")
        self.lblr_count_child_flu_led.setGeometry(QRect(90, 200, 51, 30))
        self.lblr_count_child_flu_led.setMinimumSize(QSize(0, 30))
        self.lblr_count_child_flu_led.setMaximumSize(QSize(16777215, 30))
        self.lblr_count_child_flu_led.setFont(font31)
        self.lblr_count_child_flu_led.setStyleSheet(u"background:transparent;\n"
"color: rgb(177,188,211);\n"
"padding-left:5px;")
        self.lblr_count_child_flu_led.setFrame(False)
        self.lblr_count_old_flu_lbl = QLabel(self.lblr_count_gbx)
        self.lblr_count_old_flu_lbl.setObjectName(u"lblr_count_old_flu_lbl")
        self.lblr_count_old_flu_lbl.setGeometry(QRect(10, 170, 80, 30))
        self.lblr_count_old_flu_lbl.setMinimumSize(QSize(0, 30))
        self.lblr_count_old_flu_lbl.setMaximumSize(QSize(16777215, 30))
        self.lblr_count_old_flu_lbl.setFont(font31)
        self.lblr_count_old_flu_lbl.setStyleSheet(u"background:transparent;\n"
"color: rgb(133, 155, 200);")
        self.lblr_count_old_flu_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lblr_count_total_flu_led = QLineEdit(self.lblr_count_gbx)
        self.lblr_count_total_flu_led.setObjectName(u"lblr_count_total_flu_led")
        self.lblr_count_total_flu_led.setGeometry(QRect(90, 140, 51, 30))
        self.lblr_count_total_flu_led.setMinimumSize(QSize(0, 30))
        self.lblr_count_total_flu_led.setMaximumSize(QSize(16777215, 30))
        self.lblr_count_total_flu_led.setFont(font28)
        self.lblr_count_total_flu_led.setStyleSheet(u"background:transparent;\n"
"color: rgb(177,188,211);\n"
"border-bottom:1px solid rgb(70,80,100);")
        self.lblr_count_total_flu_led.setFrame(False)
        self.lblr_count_md_led = QLineEdit(self.lblr_count_gbx)
        self.lblr_count_md_led.setObjectName(u"lblr_count_md_led")
        self.lblr_count_md_led.setGeometry(QRect(90, 110, 51, 30))
        self.lblr_count_md_led.setMinimumSize(QSize(0, 30))
        self.lblr_count_md_led.setMaximumSize(QSize(16777215, 30))
        self.lblr_count_md_led.setFont(font9)
        self.lblr_count_md_led.setStyleSheet(u"background:transparent;\n"
"color: rgb(177,188,211);\n"
"padding-left:5px;")
        self.lblr_count_md_led.setFrame(False)
        self.lblr_count_old_flu_ex_lbl = QLabel(self.lblr_count_gbx)
        self.lblr_count_old_flu_ex_lbl.setObjectName(u"lblr_count_old_flu_ex_lbl")
        self.lblr_count_old_flu_ex_lbl.setGeometry(QRect(10, 230, 80, 30))
        self.lblr_count_old_flu_ex_lbl.setMinimumSize(QSize(0, 30))
        self.lblr_count_old_flu_ex_lbl.setMaximumSize(QSize(16777215, 30))
        self.lblr_count_old_flu_ex_lbl.setFont(font31)
        self.lblr_count_old_flu_ex_lbl.setStyleSheet(u"background:transparent;\n"
"color: rgb(133, 155, 200);")
        self.lblr_count_old_flu_ex_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lblr_count_pf_lbl = QLabel(self.lblr_count_gbx)
        self.lblr_count_pf_lbl.setObjectName(u"lblr_count_pf_lbl")
        self.lblr_count_pf_lbl.setGeometry(QRect(10, 80, 80, 30))
        self.lblr_count_pf_lbl.setMinimumSize(QSize(0, 30))
        self.lblr_count_pf_lbl.setMaximumSize(QSize(16777215, 30))
        self.lblr_count_pf_lbl.setFont(font9)
        self.lblr_count_pf_lbl.setStyleSheet(u"background:transparent;\n"
"color: rgb(133, 155, 200);")
        self.lblr_count_pf_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lblr_count_total_flu_lbl = QLabel(self.lblr_count_gbx)
        self.lblr_count_total_flu_lbl.setObjectName(u"lblr_count_total_flu_lbl")
        self.lblr_count_total_flu_lbl.setGeometry(QRect(19, 140, 71, 30))
        self.lblr_count_total_flu_lbl.setMinimumSize(QSize(0, 30))
        self.lblr_count_total_flu_lbl.setMaximumSize(QSize(16777215, 30))
        self.lblr_count_total_flu_lbl.setFont(font28)
        self.lblr_count_total_flu_lbl.setStyleSheet(u"background:transparent;\n"
"color: rgb(155, 166, 200);\n"
"border-bottom:1px solid rgb(70,80,100);")
        self.lblr_count_total_flu_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lblr_count_md_lbl = QLabel(self.lblr_count_gbx)
        self.lblr_count_md_lbl.setObjectName(u"lblr_count_md_lbl")
        self.lblr_count_md_lbl.setGeometry(QRect(10, 110, 80, 30))
        self.lblr_count_md_lbl.setMinimumSize(QSize(0, 30))
        self.lblr_count_md_lbl.setMaximumSize(QSize(16777215, 30))
        self.lblr_count_md_lbl.setFont(font9)
        self.lblr_count_md_lbl.setStyleSheet(u"background:transparent;\n"
"color: rgb(133, 155, 200);")
        self.lblr_count_md_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lblr_count_old_flu_led = QLineEdit(self.lblr_count_gbx)
        self.lblr_count_old_flu_led.setObjectName(u"lblr_count_old_flu_led")
        self.lblr_count_old_flu_led.setGeometry(QRect(90, 170, 51, 30))
        self.lblr_count_old_flu_led.setMinimumSize(QSize(0, 30))
        self.lblr_count_old_flu_led.setMaximumSize(QSize(16777215, 30))
        self.lblr_count_old_flu_led.setFont(font31)
        self.lblr_count_old_flu_led.setStyleSheet(u"background:transparent;\n"
"color: rgb(177,188,211);\n"
"padding-left:5px;")
        self.lblr_count_old_flu_led.setFrame(False)
        self.lblr_count_pf_led = QLineEdit(self.lblr_count_gbx)
        self.lblr_count_pf_led.setObjectName(u"lblr_count_pf_led")
        self.lblr_count_pf_led.setGeometry(QRect(90, 80, 51, 30))
        self.lblr_count_pf_led.setMinimumSize(QSize(0, 30))
        self.lblr_count_pf_led.setMaximumSize(QSize(16777215, 30))
        self.lblr_count_pf_led.setFont(font9)
        self.lblr_count_pf_led.setStyleSheet(u"background:transparent;\n"
"color: rgb(177,188,211);\n"
"padding-left:5px;")
        self.lblr_count_pf_led.setFrame(False)
        self.lblr_count_edit_btn = QPushButton(self.lblr_count_gbx)
        self.lblr_count_edit_btn.setObjectName(u"lblr_count_edit_btn")
        self.lblr_count_edit_btn.setGeometry(QRect(99, 10, 41, 30))
        sizePolicy3.setHeightForWidth(self.lblr_count_edit_btn.sizePolicy().hasHeightForWidth())
        self.lblr_count_edit_btn.setSizePolicy(sizePolicy3)
        self.lblr_count_edit_btn.setMinimumSize(QSize(0, 30))
        self.lblr_count_edit_btn.setMaximumSize(QSize(16777215, 16777215))
        self.lblr_count_edit_btn.setFont(font11)
        self.lblr_count_edit_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(140, 150, 200);\n"
"	background-color:rgb(45,50,60);\n"
"	border-radius:10%;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(120,130,255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.lblr_count_edit_btn.setFlat(True)
        self.lblr_count_title_lbl = QLabel(self.lblr_count_gbx)
        self.lblr_count_title_lbl.setObjectName(u"lblr_count_title_lbl")
        self.lblr_count_title_lbl.setGeometry(QRect(10, 10, 81, 30))
        self.lblr_count_title_lbl.setMinimumSize(QSize(0, 30))
        self.lblr_count_title_lbl.setMaximumSize(QSize(16777215, 30))
        font42 = QFont()
        font42.setFamilies([u"\uc57c\ub180\uc790 \uc57c\uccb4 B"])
        font42.setPointSize(18)
        font42.setItalic(False)
        self.lblr_count_title_lbl.setFont(font42)
        self.lblr_count_title_lbl.setStyleSheet(u"background:transparent;\n"
"color: rgb(175, 180, 200);")
        self.lblr_count_title_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lblr_info_lbl = QTextEdit(self.labeler)
        self.lblr_info_lbl.setObjectName(u"lblr_info_lbl")
        self.lblr_info_lbl.setGeometry(QRect(10, 460, 511, 181))
        font43 = QFont()
        font43.setFamilies([u"\uc11c\uc6b8\ud55c\uac15 \uc7a5\uccb4 M"])
        font43.setPointSize(12)
        self.lblr_info_lbl.setFont(font43)
        self.lblr_info_lbl.setStyleSheet(u"background:transparent;\n"
"border:none;")
        self.lblr_info_lbl.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lblr_info_lbl.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.lblr_info_lbl.setUndoRedoEnabled(False)
        self.lblr_info_lbl.setReadOnly(True)
        self.lblr_main_gbx = QGroupBox(self.labeler)
        self.lblr_main_gbx.setObjectName(u"lblr_main_gbx")
        self.lblr_main_gbx.setGeometry(QRect(180, 20, 341, 421))
        self.lblr_main_gbx.setStyleSheet(u"QGroupBox{\n"
"	color: rgb(190, 200, 240);\n"
"	border:1px solid rgb(50, 55, 70);\n"
"	border-radius:10px;\n"
"}")
        self.lblr_vaccines_cmb = QComboBox(self.lblr_main_gbx)
        self.lblr_vaccines_cmb.setObjectName(u"lblr_vaccines_cmb")
        self.lblr_vaccines_cmb.setGeometry(QRect(40, 120, 211, 30))
        self.lblr_vaccines_cmb.setMinimumSize(QSize(0, 25))
        self.lblr_vaccines_cmb.setMaximumSize(QSize(16777215, 30))
        self.lblr_vaccines_cmb.setFont(font1)
        self.lblr_vaccines_cmb.setStyleSheet(u"QComboBox {\n"
"	background:transparent;\n"
"	selection-background-color: transparent;\n"
"    color: rgb(155, 166, 200);\n"
"	margin-right:3px;\n"
"	outline:0px;\n"
"}\n"
"QComboBox::drop-down:button{\n"
"	margin-right:5px;\n"
"    margin-top:10px;\n"
"	margin-bottom:6px;\n"
"    height:10px;\n"
"    width:10px;\n"
"    border-radius:5px;\n"
"    background-color: rgb(177, 188, 233);\n"
"}\n"
"QComboBox:drop-down:hover{\n"
"    background-color: rgb(166, 199, 255);;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(60, 65, 80);\n"
"    color: rgb(240, 240, 245);\n"
"    border:1px solid rgb(88, 99, 111);\n"
"    padding:5px;\n"
"	outline:0px;\n"
"	selection-background-color: rgb(60, 65, 80);\n"
"	selection-color:rgb(133, 166, 255);\n"
"}")
        self.lblr_vaccines_cmb.setMaxVisibleItems(40)
        self.lblr_vaccines_cmb.setFrame(False)
        self.lblr_step3_lbl = QLabel(self.lblr_main_gbx)
        self.lblr_step3_lbl.setObjectName(u"lblr_step3_lbl")
        self.lblr_step3_lbl.setGeometry(QRect(20, 170, 301, 30))
        self.lblr_step3_lbl.setMinimumSize(QSize(0, 30))
        self.lblr_step3_lbl.setMaximumSize(QSize(16777215, 30))
        font44 = QFont()
        font44.setFamilies([u"\uc11c\uc6b8\ud55c\uac15 \uc7a5\uccb4 B"])
        font44.setPointSize(14)
        font44.setItalic(True)
        self.lblr_step3_lbl.setFont(font44)
        self.lblr_step3_lbl.setStyleSheet(u"border-bottom:1px solid rgb(75,80,100);\n"
"background:transparent;\n"
"color: rgb(133, 155, 200);")
        self.lblr_step3_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lblr_print_btn = QPushButton(self.lblr_main_gbx)
        self.lblr_print_btn.setObjectName(u"lblr_print_btn")
        self.lblr_print_btn.setGeometry(QRect(215, 370, 101, 30))
        sizePolicy3.setHeightForWidth(self.lblr_print_btn.sizePolicy().hasHeightForWidth())
        self.lblr_print_btn.setSizePolicy(sizePolicy3)
        self.lblr_print_btn.setMinimumSize(QSize(0, 30))
        self.lblr_print_btn.setMaximumSize(QSize(16777215, 16777215))
        self.lblr_print_btn.setFont(font14)
        self.lblr_print_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(200, 180, 25);\n"
"	background-color:rgb(45,50,60);\n"
"	border-radius:10%;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:hover {    \n"
"	color: rgb(220, 200, 25);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.lblr_print_btn.setFlat(True)
        self.lblr_preview_frame = QFrame(self.lblr_main_gbx)
        self.lblr_preview_frame.setObjectName(u"lblr_preview_frame")
        self.lblr_preview_frame.setGeometry(QRect(20, 210, 300, 150))
        sizePolicy5.setHeightForWidth(self.lblr_preview_frame.sizePolicy().hasHeightForWidth())
        self.lblr_preview_frame.setSizePolicy(sizePolicy5)
        self.lblr_preview_frame.setMinimumSize(QSize(300, 150))
        self.lblr_preview_frame.setMaximumSize(QSize(300, 150))
        self.lblr_preview_frame.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"	color: rgb(0,0,0);\n"
"}")
        self.lblr_preview_frame.setFrameShape(QFrame.StyledPanel)
        self.lblr_preview_frame.setFrameShadow(QFrame.Raised)
        self.lblr_preview_count_vac_lbl = QLabel(self.lblr_preview_frame)
        self.lblr_preview_count_vac_lbl.setObjectName(u"lblr_preview_count_vac_lbl")
        self.lblr_preview_count_vac_lbl.setGeometry(QRect(10, 34, 281, 51))
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.lblr_preview_count_vac_lbl.sizePolicy().hasHeightForWidth())
        self.lblr_preview_count_vac_lbl.setSizePolicy(sizePolicy7)
        self.lblr_preview_count_vac_lbl.setMinimumSize(QSize(0, 0))
        self.lblr_preview_count_vac_lbl.setMaximumSize(QSize(16777215, 16777215))
        font45 = QFont()
        font45.setFamilies([u"\uc11c\uc6b8\ub0a8\uc0b0 \uc7a5\uccb4 EB"])
        font45.setPointSize(32)
        font45.setBold(False)
        self.lblr_preview_count_vac_lbl.setFont(font45)
        self.lblr_preview_count_vac_lbl.setStyleSheet(u"QWidget{\n"
"	background:none;\n"
"	border:none;\n"
"}\n"
"")
        self.lblr_preview_count_vac_lbl.setAlignment(Qt.AlignCenter)
        self.lblr_preview_line2 = QFrame(self.lblr_preview_frame)
        self.lblr_preview_line2.setObjectName(u"lblr_preview_line2")
        self.lblr_preview_line2.setGeometry(QRect(20, 102, 261, 2))
        self.lblr_preview_line2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.lblr_preview_line2.setFrameShadow(QFrame.Plain)
        self.lblr_preview_line2.setFrameShape(QFrame.HLine)
        self.lblr_preview_line1 = QFrame(self.lblr_preview_frame)
        self.lblr_preview_line1.setObjectName(u"lblr_preview_line1")
        self.lblr_preview_line1.setGeometry(QRect(20, 27, 261, 2))
        self.lblr_preview_line1.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.lblr_preview_line1.setFrameShadow(QFrame.Plain)
        self.lblr_preview_line1.setFrameShape(QFrame.HLine)
        self.lblr_preview_ptphone_lbl = QLabel(self.lblr_preview_frame)
        self.lblr_preview_ptphone_lbl.setObjectName(u"lblr_preview_ptphone_lbl")
        self.lblr_preview_ptphone_lbl.setGeometry(QRect(160, 125, 121, 16))
        sizePolicy7.setHeightForWidth(self.lblr_preview_ptphone_lbl.sizePolicy().hasHeightForWidth())
        self.lblr_preview_ptphone_lbl.setSizePolicy(sizePolicy7)
        self.lblr_preview_ptphone_lbl.setMinimumSize(QSize(0, 0))
        self.lblr_preview_ptphone_lbl.setMaximumSize(QSize(16777215, 16777215))
        font46 = QFont()
        font46.setFamilies([u"D2Coding ligature"])
        font46.setPointSize(12)
        font46.setBold(False)
        self.lblr_preview_ptphone_lbl.setFont(font46)
        self.lblr_preview_ptphone_lbl.setStyleSheet(u"QWidget{\n"
"	background:none;\n"
"	border:none;\n"
"}\n"
"")
        self.lblr_preview_ptphone_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lblr_preview_ptjmno_lbl = QLabel(self.lblr_preview_frame)
        self.lblr_preview_ptjmno_lbl.setObjectName(u"lblr_preview_ptjmno_lbl")
        self.lblr_preview_ptjmno_lbl.setGeometry(QRect(160, 106, 121, 20))
        sizePolicy7.setHeightForWidth(self.lblr_preview_ptjmno_lbl.sizePolicy().hasHeightForWidth())
        self.lblr_preview_ptjmno_lbl.setSizePolicy(sizePolicy7)
        self.lblr_preview_ptjmno_lbl.setMinimumSize(QSize(0, 0))
        self.lblr_preview_ptjmno_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.lblr_preview_ptjmno_lbl.setFont(font46)
        self.lblr_preview_ptjmno_lbl.setStyleSheet(u"QWidget{\n"
"	background:none;\n"
"	border:none;\n"
"}\n"
"")
        self.lblr_preview_ptjmno_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lblr_preview_date_lbl = QLabel(self.lblr_preview_frame)
        self.lblr_preview_date_lbl.setObjectName(u"lblr_preview_date_lbl")
        self.lblr_preview_date_lbl.setGeometry(QRect(20, 9, 141, 16))
        sizePolicy7.setHeightForWidth(self.lblr_preview_date_lbl.sizePolicy().hasHeightForWidth())
        self.lblr_preview_date_lbl.setSizePolicy(sizePolicy7)
        self.lblr_preview_date_lbl.setMinimumSize(QSize(0, 0))
        self.lblr_preview_date_lbl.setMaximumSize(QSize(16777215, 16777215))
        font47 = QFont()
        font47.setFamilies([u"\uc11c\uc6b8\ub0a8\uc0b0 \uc7a5\uccb4 B"])
        font47.setPointSize(12)
        font47.setBold(False)
        self.lblr_preview_date_lbl.setFont(font47)
        self.lblr_preview_date_lbl.setStyleSheet(u"QWidget{\n"
"	background:none;\n"
"	border:none;\n"
"}\n"
"")
        self.lblr_preview_date_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lblr_preview_ptname_lbl = QLabel(self.lblr_preview_frame)
        self.lblr_preview_ptname_lbl.setObjectName(u"lblr_preview_ptname_lbl")
        self.lblr_preview_ptname_lbl.setGeometry(QRect(20, 109, 121, 31))
        sizePolicy7.setHeightForWidth(self.lblr_preview_ptname_lbl.sizePolicy().hasHeightForWidth())
        self.lblr_preview_ptname_lbl.setSizePolicy(sizePolicy7)
        self.lblr_preview_ptname_lbl.setMinimumSize(QSize(0, 0))
        self.lblr_preview_ptname_lbl.setMaximumSize(QSize(16777215, 16777215))
        font48 = QFont()
        font48.setFamilies([u"\uc11c\uc6b8\ub0a8\uc0b0 \uc7a5\uccb4 B"])
        font48.setPointSize(14)
        font48.setBold(False)
        self.lblr_preview_ptname_lbl.setFont(font48)
        self.lblr_preview_ptname_lbl.setStyleSheet(u"QWidget{\n"
"	background:none;\n"
"	border:none;\n"
"}\n"
"")
        self.lblr_preview_ptname_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lblr_preview_lot_lbl = QLabel(self.lblr_preview_frame)
        self.lblr_preview_lot_lbl.setObjectName(u"lblr_preview_lot_lbl")
        self.lblr_preview_lot_lbl.setGeometry(QRect(170, 9, 111, 20))
        sizePolicy7.setHeightForWidth(self.lblr_preview_lot_lbl.sizePolicy().hasHeightForWidth())
        self.lblr_preview_lot_lbl.setSizePolicy(sizePolicy7)
        self.lblr_preview_lot_lbl.setMinimumSize(QSize(0, 0))
        self.lblr_preview_lot_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.lblr_preview_lot_lbl.setFont(font46)
        self.lblr_preview_lot_lbl.setStyleSheet(u"QWidget{\n"
"	background:none;\n"
"	border:none;\n"
"}\n"
"")
        self.lblr_preview_lot_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lblr_preview_counter_lbl = QLabel(self.lblr_preview_frame)
        self.lblr_preview_counter_lbl.setObjectName(u"lblr_preview_counter_lbl")
        self.lblr_preview_counter_lbl.setGeometry(QRect(20, 80, 261, 21))
        sizePolicy7.setHeightForWidth(self.lblr_preview_counter_lbl.sizePolicy().hasHeightForWidth())
        self.lblr_preview_counter_lbl.setSizePolicy(sizePolicy7)
        self.lblr_preview_counter_lbl.setMinimumSize(QSize(0, 0))
        self.lblr_preview_counter_lbl.setMaximumSize(QSize(16777215, 16777215))
        font49 = QFont()
        font49.setFamilies([u"\ub098\ub214\ubc14\ub978\uace0\ub515"])
        font49.setPointSize(14)
        font49.setBold(True)
        self.lblr_preview_counter_lbl.setFont(font49)
        self.lblr_preview_counter_lbl.setStyleSheet(u"QWidget{\n"
"	background:none;\n"
"	border:none;\n"
"}\n"
"")
        self.lblr_preview_counter_lbl.setAlignment(Qt.AlignCenter)
        self.lblr_preview_nocount_vac_lbl = QLabel(self.lblr_preview_frame)
        self.lblr_preview_nocount_vac_lbl.setObjectName(u"lblr_preview_nocount_vac_lbl")
        self.lblr_preview_nocount_vac_lbl.setGeometry(QRect(10, 30, 281, 81))
        sizePolicy7.setHeightForWidth(self.lblr_preview_nocount_vac_lbl.sizePolicy().hasHeightForWidth())
        self.lblr_preview_nocount_vac_lbl.setSizePolicy(sizePolicy7)
        self.lblr_preview_nocount_vac_lbl.setMinimumSize(QSize(0, 0))
        self.lblr_preview_nocount_vac_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.lblr_preview_nocount_vac_lbl.setFont(font45)
        self.lblr_preview_nocount_vac_lbl.setStyleSheet(u"QWidget{\n"
"	background:none;\n"
"	border:none;\n"
"}\n"
"")
        self.lblr_preview_nocount_vac_lbl.setAlignment(Qt.AlignCenter)
        self.lblr_get_data_btn = QPushButton(self.lblr_main_gbx)
        self.lblr_get_data_btn.setObjectName(u"lblr_get_data_btn")
        self.lblr_get_data_btn.setGeometry(QRect(40, 40, 121, 30))
        sizePolicy5.setHeightForWidth(self.lblr_get_data_btn.sizePolicy().hasHeightForWidth())
        self.lblr_get_data_btn.setSizePolicy(sizePolicy5)
        self.lblr_get_data_btn.setMinimumSize(QSize(0, 0))
        self.lblr_get_data_btn.setMaximumSize(QSize(16777215, 16777215))
        self.lblr_get_data_btn.setFont(font14)
        self.lblr_get_data_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(160, 170, 200);\n"
"	background:transparent;\n"
"	border:none;\n"
"	text-align:left;\n"
"}\n"
"QPushButton::hover {	\n"
"	color: rgb(200, 220, 240);\n"
"}\n"
"QPushButton::pressed {	\n"
"	color: rgb(100, 111, 144);\n"
"}")
        self.lblr_get_data_btn.setAutoDefault(True)
        self.lblr_get_data_btn.setFlat(True)
        self.lblr_step2_lbl = QLabel(self.lblr_main_gbx)
        self.lblr_step2_lbl.setObjectName(u"lblr_step2_lbl")
        self.lblr_step2_lbl.setGeometry(QRect(20, 90, 301, 30))
        self.lblr_step2_lbl.setMinimumSize(QSize(0, 30))
        self.lblr_step2_lbl.setMaximumSize(QSize(16777215, 30))
        self.lblr_step2_lbl.setFont(font44)
        self.lblr_step2_lbl.setStyleSheet(u"border-bottom:1px solid rgb(75,80,100);\n"
"background:transparent;\n"
"color: rgb(133, 155, 200);")
        self.lblr_step2_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lblr_step1_lbl = QLabel(self.lblr_main_gbx)
        self.lblr_step1_lbl.setObjectName(u"lblr_step1_lbl")
        self.lblr_step1_lbl.setGeometry(QRect(20, 10, 301, 30))
        self.lblr_step1_lbl.setMinimumSize(QSize(0, 30))
        self.lblr_step1_lbl.setMaximumSize(QSize(16777215, 30))
        self.lblr_step1_lbl.setFont(font44)
        self.lblr_step1_lbl.setStyleSheet(u"border-bottom:1px solid rgb(75,80,100);\n"
"background:transparent;\n"
"color: rgb(133, 155, 200);")
        self.lblr_step1_lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lblr_reset_btn = QPushButton(self.lblr_main_gbx)
        self.lblr_reset_btn.setObjectName(u"lblr_reset_btn")
        self.lblr_reset_btn.setGeometry(QRect(140, 370, 61, 30))
        sizePolicy3.setHeightForWidth(self.lblr_reset_btn.sizePolicy().hasHeightForWidth())
        self.lblr_reset_btn.setSizePolicy(sizePolicy3)
        self.lblr_reset_btn.setMinimumSize(QSize(0, 30))
        self.lblr_reset_btn.setMaximumSize(QSize(16777215, 16777215))
        self.lblr_reset_btn.setFont(font11)
        self.lblr_reset_btn.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(160, 190, 150);\n"
"	background-color:rgb(45,50,60);\n"
"	border-radius:10%;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(140,200,130);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.lblr_reset_btn.setFlat(True)
        self.lblr_flu_date_ckecker_gbx = QGroupBox(self.labeler)
        self.lblr_flu_date_ckecker_gbx.setObjectName(u"lblr_flu_date_ckecker_gbx")
        self.lblr_flu_date_ckecker_gbx.setGeometry(QRect(10, 310, 151, 131))
        self.lblr_flu_date_ckecker_gbx.setStyleSheet(u"QGroupBox{\n"
"	border:1px solid rgb(55, 66, 55);\n"
"	border-radius:10px;\n"
"}")
        self.lblr_flu_date_checker_title = QLabel(self.lblr_flu_date_ckecker_gbx)
        self.lblr_flu_date_checker_title.setObjectName(u"lblr_flu_date_checker_title")
        self.lblr_flu_date_checker_title.setGeometry(QRect(0, 0, 151, 41))
        self.lblr_flu_date_checker_title.setMinimumSize(QSize(0, 0))
        self.lblr_flu_date_checker_title.setMaximumSize(QSize(16777215, 16777215))
        self.lblr_flu_date_checker_title.setFont(font42)
        self.lblr_flu_date_checker_title.setStyleSheet(u"border:1px solid rgb(55, 66, 55);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"color: rgb(66, 122, 99);\n"
"padding-left:6px;\n"
"")
        self.lblr_flu_date_checker_title.setAlignment(Qt.AlignCenter)
        self.lblr_flu_date_checker_old_lbl = QLabel(self.lblr_flu_date_ckecker_gbx)
        self.lblr_flu_date_checker_old_lbl.setObjectName(u"lblr_flu_date_checker_old_lbl")
        self.lblr_flu_date_checker_old_lbl.setGeometry(QRect(10, 50, 81, 30))
        self.lblr_flu_date_checker_old_lbl.setMinimumSize(QSize(0, 30))
        self.lblr_flu_date_checker_old_lbl.setMaximumSize(QSize(16777215, 30))
        self.lblr_flu_date_checker_old_lbl.setFont(font47)
        self.lblr_flu_date_checker_old_lbl.setStyleSheet(u"background:transparent;\n"
"color: rgb(100, 133, 122);\n"
"border-bottom:1px solid rgb(66, 88, 77);")
        self.lblr_flu_date_checker_old_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lblr_flu_date_checker_old = QLineEdit(self.lblr_flu_date_ckecker_gbx)
        self.lblr_flu_date_checker_old.setObjectName(u"lblr_flu_date_checker_old")
        self.lblr_flu_date_checker_old.setGeometry(QRect(90, 50, 51, 30))
        self.lblr_flu_date_checker_old.setMinimumSize(QSize(0, 30))
        self.lblr_flu_date_checker_old.setMaximumSize(QSize(16777215, 30))
        font50 = QFont()
        font50.setFamilies([u"D2Coding ligature"])
        font50.setPointSize(12)
        font50.setBold(True)
        self.lblr_flu_date_checker_old.setFont(font50)
        self.lblr_flu_date_checker_old.setStyleSheet(u"background:transparent;\n"
"color: rgb(188, 155, 100);\n"
"border-bottom:1px solid rgb(66, 88, 77);")
        self.lblr_flu_date_checker_old.setFrame(False)
        self.lblr_flu_date_checker_old.setAlignment(Qt.AlignCenter)
        self.lblr_flu_date_checker_old.setReadOnly(True)
        self.lblr_flu_date_checker_chile_lbl = QLabel(self.lblr_flu_date_ckecker_gbx)
        self.lblr_flu_date_checker_chile_lbl.setObjectName(u"lblr_flu_date_checker_chile_lbl")
        self.lblr_flu_date_checker_chile_lbl.setGeometry(QRect(10, 80, 81, 30))
        self.lblr_flu_date_checker_chile_lbl.setMinimumSize(QSize(0, 30))
        self.lblr_flu_date_checker_chile_lbl.setMaximumSize(QSize(16777215, 30))
        self.lblr_flu_date_checker_chile_lbl.setFont(font47)
        self.lblr_flu_date_checker_chile_lbl.setStyleSheet(u"background:transparent;\n"
"color: rgb(100, 133, 122);\n"
"border-bottom:1px solid rgb(66, 88, 77);")
        self.lblr_flu_date_checker_chile_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lblr_flu_date_checker_child = QLineEdit(self.lblr_flu_date_ckecker_gbx)
        self.lblr_flu_date_checker_child.setObjectName(u"lblr_flu_date_checker_child")
        self.lblr_flu_date_checker_child.setGeometry(QRect(90, 80, 51, 30))
        self.lblr_flu_date_checker_child.setMinimumSize(QSize(0, 30))
        self.lblr_flu_date_checker_child.setMaximumSize(QSize(16777215, 30))
        self.lblr_flu_date_checker_child.setFont(font50)
        self.lblr_flu_date_checker_child.setStyleSheet(u"background:transparent;\n"
"color: rgb(188, 155, 100);\n"
"border-bottom:1px solid rgb(66, 88, 77);")
        self.lblr_flu_date_checker_child.setFrame(False)
        self.lblr_flu_date_checker_child.setAlignment(Qt.AlignCenter)
        self.lblr_flu_date_checker_child.setReadOnly(True)
        self.apps_stack.addWidget(self.labeler)
        self.covid_report = QWidget()
        self.covid_report.setObjectName(u"covid_report")
        self.c19r_address1_lbl = QLabel(self.covid_report)
        self.c19r_address1_lbl.setObjectName(u"c19r_address1_lbl")
        self.c19r_address1_lbl.setGeometry(QRect(30, 190, 70, 30))
        self.c19r_address1_lbl.setMinimumSize(QSize(0, 0))
        self.c19r_address1_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.c19r_address1_lbl.setFont(font31)
        self.c19r_address1_lbl.setStyleSheet(u"border-bottom:1px solid rgb(60,65,80);\n"
"background:transparent;\n"
"color: rgb(133, 155, 200);\n"
"")
        self.c19r_address1_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.c19r_sxsince_led = QLineEdit(self.covid_report)
        self.c19r_sxsince_led.setObjectName(u"c19r_sxsince_led")
        self.c19r_sxsince_led.setGeometry(QRect(100, 310, 111, 30))
        self.c19r_sxsince_led.setMinimumSize(QSize(0, 30))
        self.c19r_sxsince_led.setMaximumSize(QSize(16777215, 25))
        self.c19r_sxsince_led.setFont(font31)
        self.c19r_sxsince_led.setStyleSheet(u"border-bottom:1px solid rgb(60,65,80);\n"
"background:transparent;\n"
"padding-left:10px;\n"
"color: rgb(166,177,199);")
        self.c19r_sxsince_led.setFrame(False)
        self.c19r_sxsince_led.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.c19r_underaged_cbx = QCheckBox(self.covid_report)
        self.c19r_underaged_cbx.setObjectName(u"c19r_underaged_cbx")
        self.c19r_underaged_cbx.setGeometry(QRect(270, 120, 190, 30))
        self.c19r_underaged_cbx.setMinimumSize(QSize(0, 30))
        self.c19r_underaged_cbx.setFont(font31)
        self.c19r_underaged_cbx.setStyleSheet(u"")
        self.c19r_underaged_cbx.setCheckable(False)
        self.c19r_ptphone_led = QLineEdit(self.covid_report)
        self.c19r_ptphone_led.setObjectName(u"c19r_ptphone_led")
        self.c19r_ptphone_led.setGeometry(QRect(100, 160, 120, 30))
        self.c19r_ptphone_led.setMinimumSize(QSize(0, 0))
        self.c19r_ptphone_led.setMaximumSize(QSize(16777215, 30))
        self.c19r_ptphone_led.setFont(font31)
        self.c19r_ptphone_led.setStyleSheet(u"border-bottom:1px solid rgb(60,65,80);\n"
"background:transparent;\n"
"padding-left:10px;\n"
"color: rgb(166,177,199);")
        self.c19r_ptphone_led.setFrame(False)
        self.c19r_address1_led = QLineEdit(self.covid_report)
        self.c19r_address1_led.setObjectName(u"c19r_address1_led")
        self.c19r_address1_led.setGeometry(QRect(100, 190, 391, 30))
        self.c19r_address1_led.setMinimumSize(QSize(0, 0))
        self.c19r_address1_led.setMaximumSize(QSize(16777215, 30))
        self.c19r_address1_led.setFont(font31)
        self.c19r_address1_led.setStyleSheet(u"border-bottom:1px solid rgb(60,65,80);\n"
"background:transparent;\n"
"padding-left:10px;\n"
"color: rgb(166,177,199);")
        self.c19r_address1_led.setFrame(False)
        self.c19r_ptjmno_led = QLineEdit(self.covid_report)
        self.c19r_ptjmno_led.setObjectName(u"c19r_ptjmno_led")
        self.c19r_ptjmno_led.setGeometry(QRect(100, 130, 120, 30))
        self.c19r_ptjmno_led.setMinimumSize(QSize(0, 0))
        self.c19r_ptjmno_led.setMaximumSize(QSize(16777215, 30))
        self.c19r_ptjmno_led.setFont(font31)
        self.c19r_ptjmno_led.setStyleSheet(u"border-bottom:1px solid rgb(60,65,80);\n"
"background:transparent;\n"
"padding-left:10px;\n"
"color: rgb(166,177,199);")
        self.c19r_ptjmno_led.setFrame(False)
        self.c19r_ptphone_lbl = QLabel(self.covid_report)
        self.c19r_ptphone_lbl.setObjectName(u"c19r_ptphone_lbl")
        self.c19r_ptphone_lbl.setGeometry(QRect(30, 160, 70, 30))
        self.c19r_ptphone_lbl.setMinimumSize(QSize(0, 0))
        self.c19r_ptphone_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.c19r_ptphone_lbl.setFont(font31)
        self.c19r_ptphone_lbl.setStyleSheet(u"border-bottom:1px solid rgb(60,65,80);\n"
"background:transparent;\n"
"color: rgb(133, 155, 200);\n"
"")
        self.c19r_ptphone_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.c19r_sxsince_lbl = QLabel(self.covid_report)
        self.c19r_sxsince_lbl.setObjectName(u"c19r_sxsince_lbl")
        self.c19r_sxsince_lbl.setGeometry(QRect(30, 310, 70, 30))
        self.c19r_sxsince_lbl.setMinimumSize(QSize(0, 30))
        self.c19r_sxsince_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.c19r_sxsince_lbl.setFont(font31)
        self.c19r_sxsince_lbl.setStyleSheet(u"border-bottom:1px solid rgb(60,65,80);\n"
"background:transparent;\n"
"color: rgb(133, 155, 200);\n"
"")
        self.c19r_sxsince_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.c19r_notes_pte = QPlainTextEdit(self.covid_report)
        self.c19r_notes_pte.setObjectName(u"c19r_notes_pte")
        self.c19r_notes_pte.setGeometry(QRect(100, 430, 411, 60))
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.c19r_notes_pte.sizePolicy().hasHeightForWidth())
        self.c19r_notes_pte.setSizePolicy(sizePolicy8)
        self.c19r_notes_pte.setMaximumSize(QSize(16777215, 16777215))
        self.c19r_notes_pte.setFont(font31)
        self.c19r_notes_pte.setStyleSheet(u"border-top:1px solid rgb(60,65,80);\n"
"border-bottom:1px solid rgb(60,65,80);\n"
"background:transparent;\n"
"padding-left:10px;\n"
"color: rgb(166,177,199);")
        self.c19r_notes_pte.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.c19r_notes_pte.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.c19r_notes_pte.setReadOnly(True)
        self.c19r_dx_date_lbl = QLabel(self.covid_report)
        self.c19r_dx_date_lbl.setObjectName(u"c19r_dx_date_lbl")
        self.c19r_dx_date_lbl.setGeometry(QRect(30, 340, 70, 30))
        self.c19r_dx_date_lbl.setMinimumSize(QSize(0, 30))
        self.c19r_dx_date_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.c19r_dx_date_lbl.setFont(font31)
        self.c19r_dx_date_lbl.setStyleSheet(u"background:transparent;\n"
"color: rgb(133, 155, 200);\n"
"")
        self.c19r_dx_date_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.c19r_address2_led = QLineEdit(self.covid_report)
        self.c19r_address2_led.setObjectName(u"c19r_address2_led")
        self.c19r_address2_led.setGeometry(QRect(100, 220, 391, 30))
        self.c19r_address2_led.setMinimumSize(QSize(0, 0))
        self.c19r_address2_led.setMaximumSize(QSize(16777215, 30))
        self.c19r_address2_led.setFont(font31)
        self.c19r_address2_led.setStyleSheet(u"border-bottom:1px solid rgb(60,65,80);\n"
"background:transparent;\n"
"padding-left:10px;\n"
"color: rgb(166,177,199);")
        self.c19r_address2_led.setFrame(False)
        self.c19r_doctor_led = QLineEdit(self.covid_report)
        self.c19r_doctor_led.setObjectName(u"c19r_doctor_led")
        self.c19r_doctor_led.setGeometry(QRect(100, 490, 71, 30))
        self.c19r_doctor_led.setMinimumSize(QSize(0, 30))
        self.c19r_doctor_led.setMaximumSize(QSize(16777215, 25))
        self.c19r_doctor_led.setFont(font31)
        self.c19r_doctor_led.setStyleSheet(u"border-bottom:1px solid rgb(60,65,80);\n"
"background:transparent;\n"
"padding-left:10px;\n"
"color: rgb(166,177,199);")
        self.c19r_doctor_led.setFrame(False)
        self.c19r_symp_lbl = QLabel(self.covid_report)
        self.c19r_symp_lbl.setObjectName(u"c19r_symp_lbl")
        self.c19r_symp_lbl.setGeometry(QRect(30, 370, 70, 30))
        self.c19r_symp_lbl.setMinimumSize(QSize(0, 30))
        self.c19r_symp_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.c19r_symp_lbl.setFont(font31)
        self.c19r_symp_lbl.setStyleSheet(u"border-top:1px solid rgb(60,65,80);\n"
"background:transparent;\n"
"color: rgb(133, 155, 200);\n"
"")
        self.c19r_symp_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.c19r_subtitle2_lbl = QLabel(self.covid_report)
        self.c19r_subtitle2_lbl.setObjectName(u"c19r_subtitle2_lbl")
        self.c19r_subtitle2_lbl.setGeometry(QRect(20, 280, 157, 30))
        font51 = QFont()
        font51.setFamilies([u"\uc11c\uc6b8\ud55c\uac15 \uc7a5\uccb4 B"])
        font51.setPointSize(14)
        font51.setBold(False)
        font51.setItalic(True)
        self.c19r_subtitle2_lbl.setFont(font51)
        self.c19r_subtitle2_lbl.setStyleSheet(u"padding-left:5px;\n"
"color: rgb(188, 199, 233);\n"
"background:none;")
        self.c19r_notes_lbl = QLabel(self.covid_report)
        self.c19r_notes_lbl.setObjectName(u"c19r_notes_lbl")
        self.c19r_notes_lbl.setGeometry(QRect(30, 430, 70, 30))
        self.c19r_notes_lbl.setMinimumSize(QSize(0, 30))
        self.c19r_notes_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.c19r_notes_lbl.setFont(font31)
        self.c19r_notes_lbl.setStyleSheet(u"border-top:1px solid rgb(60,65,80);\n"
"background:transparent;\n"
"color: rgb(133, 155, 200);\n"
"")
        self.c19r_notes_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.c19r_ptname_lbl = QLabel(self.covid_report)
        self.c19r_ptname_lbl.setObjectName(u"c19r_ptname_lbl")
        self.c19r_ptname_lbl.setGeometry(QRect(30, 100, 70, 30))
        self.c19r_ptname_lbl.setMinimumSize(QSize(0, 0))
        self.c19r_ptname_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.c19r_ptname_lbl.setFont(font31)
        self.c19r_ptname_lbl.setStyleSheet(u"border-bottom:1px solid rgb(60,65,80);\n"
"background:transparent;\n"
"color: rgb(133, 155, 200);\n"
"")
        self.c19r_ptname_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.c19r_symp_pte = QPlainTextEdit(self.covid_report)
        self.c19r_symp_pte.setObjectName(u"c19r_symp_pte")
        self.c19r_symp_pte.setGeometry(QRect(100, 370, 411, 60))
        sizePolicy8.setHeightForWidth(self.c19r_symp_pte.sizePolicy().hasHeightForWidth())
        self.c19r_symp_pte.setSizePolicy(sizePolicy8)
        self.c19r_symp_pte.setMaximumSize(QSize(16777215, 60))
        font52 = QFont()
        font52.setFamilies([u"\uc11c\uc6b8\ub0a8\uc0b0 \uc7a5\uccb4 B"])
        font52.setPointSize(10)
        self.c19r_symp_pte.setFont(font52)
        self.c19r_symp_pte.setStyleSheet(u"border-top:1px solid rgb(60,65,80);\n"
"background:transparent;\n"
"padding-left:10px;\n"
"color: rgb(166,177,199);")
        self.c19r_symp_pte.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.c19r_symp_pte.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.c19r_symp_pte.setReadOnly(True)
        self.c19r_subtitle1_lbl = QLabel(self.covid_report)
        self.c19r_subtitle1_lbl.setObjectName(u"c19r_subtitle1_lbl")
        self.c19r_subtitle1_lbl.setGeometry(QRect(20, 70, 85, 30))
        self.c19r_subtitle1_lbl.setMinimumSize(QSize(0, 30))
        self.c19r_subtitle1_lbl.setFont(font51)
        self.c19r_subtitle1_lbl.setStyleSheet(u"padding-left:5px;\n"
"color: rgb(188, 199, 233);\n"
"background:none;")
        self.c19r_ptname_led = QLineEdit(self.covid_report)
        self.c19r_ptname_led.setObjectName(u"c19r_ptname_led")
        self.c19r_ptname_led.setGeometry(QRect(100, 100, 120, 30))
        self.c19r_ptname_led.setMinimumSize(QSize(0, 0))
        self.c19r_ptname_led.setMaximumSize(QSize(16777215, 30))
        self.c19r_ptname_led.setFont(font31)
        self.c19r_ptname_led.setStyleSheet(u"border-bottom:1px solid rgb(60,65,80);\n"
"background:transparent;\n"
"padding-left:10px;\n"
"color: rgb(166,177,199);")
        self.c19r_ptname_led.setFrame(False)
        self.c19r_dx_date_led = QLineEdit(self.covid_report)
        self.c19r_dx_date_led.setObjectName(u"c19r_dx_date_led")
        self.c19r_dx_date_led.setGeometry(QRect(100, 340, 111, 30))
        self.c19r_dx_date_led.setMinimumSize(QSize(0, 30))
        self.c19r_dx_date_led.setMaximumSize(QSize(16777215, 30))
        self.c19r_dx_date_led.setFont(font31)
        self.c19r_dx_date_led.setStyleSheet(u"background:transparent;\n"
"padding-left:10px;\n"
"color: rgb(166,177,199);")
        self.c19r_dx_date_led.setFrame(False)
        self.c19r_dx_date_led.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.c19r_adult_name_lbl = QLabel(self.covid_report)
        self.c19r_adult_name_lbl.setObjectName(u"c19r_adult_name_lbl")
        self.c19r_adult_name_lbl.setGeometry(QRect(270, 150, 80, 30))
        self.c19r_adult_name_lbl.setMinimumSize(QSize(75, 30))
        self.c19r_adult_name_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.c19r_adult_name_lbl.setFont(font31)
        self.c19r_adult_name_lbl.setStyleSheet(u"border-bottom:1px solid rgb(60,65,80);\n"
"background:transparent;\n"
"color: rgb(133, 155, 200);\n"
"color: rgb(66, 77, 100);\n"
"")
        self.c19r_adult_name_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.c19r_address2_lbl = QLabel(self.covid_report)
        self.c19r_address2_lbl.setObjectName(u"c19r_address2_lbl")
        self.c19r_address2_lbl.setGeometry(QRect(30, 220, 70, 30))
        self.c19r_address2_lbl.setMinimumSize(QSize(0, 0))
        self.c19r_address2_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.c19r_address2_lbl.setFont(font31)
        self.c19r_address2_lbl.setStyleSheet(u"border-bottom:1px solid rgb(60,65,80);\n"
"background:transparent;\n"
"color: rgb(133, 155, 200);\n"
"")
        self.c19r_address2_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.c19r_ptjmno_lbl = QLabel(self.covid_report)
        self.c19r_ptjmno_lbl.setObjectName(u"c19r_ptjmno_lbl")
        self.c19r_ptjmno_lbl.setGeometry(QRect(30, 130, 70, 30))
        self.c19r_ptjmno_lbl.setMinimumSize(QSize(0, 0))
        self.c19r_ptjmno_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.c19r_ptjmno_lbl.setFont(font31)
        self.c19r_ptjmno_lbl.setStyleSheet(u"border-bottom:1px solid rgb(60,65,80);\n"
"background:transparent;\n"
"color: rgb(133, 155, 200);\n"
"")
        self.c19r_ptjmno_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.c19r_doctor_lbl = QLabel(self.covid_report)
        self.c19r_doctor_lbl.setObjectName(u"c19r_doctor_lbl")
        self.c19r_doctor_lbl.setGeometry(QRect(30, 489, 70, 31))
        self.c19r_doctor_lbl.setMinimumSize(QSize(0, 31))
        self.c19r_doctor_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.c19r_doctor_lbl.setFont(font31)
        self.c19r_doctor_lbl.setStyleSheet(u"border-top:1px solid rgb(60,65,80);\n"
"border-bottom:1px solid rgb(60,65,80);\n"
"background:transparent;\n"
"color: rgb(133, 155, 200);\n"
"")
        self.c19r_doctor_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.c19r_adult_name_led = QLineEdit(self.covid_report)
        self.c19r_adult_name_led.setObjectName(u"c19r_adult_name_led")
        self.c19r_adult_name_led.setGeometry(QRect(350, 150, 110, 30))
        self.c19r_adult_name_led.setMinimumSize(QSize(0, 30))
        self.c19r_adult_name_led.setMaximumSize(QSize(16777215, 25))
        self.c19r_adult_name_led.setFont(font31)
        self.c19r_adult_name_led.setStyleSheet(u"border-bottom:1px solid rgb(60,65,80);\n"
"background:transparent;\n"
"padding-left:10px;\n"
"color: rgb(166,177,199);")
        self.c19r_adult_name_led.setFrame(False)
        self.c19r_report_btn = QPushButton(self.covid_report)
        self.c19r_report_btn.setObjectName(u"c19r_report_btn")
        self.c19r_report_btn.setGeometry(QRect(429, 610, 91, 30))
        sizePolicy3.setHeightForWidth(self.c19r_report_btn.sizePolicy().hasHeightForWidth())
        self.c19r_report_btn.setSizePolicy(sizePolicy3)
        self.c19r_report_btn.setMinimumSize(QSize(0, 30))
        self.c19r_report_btn.setMaximumSize(QSize(16777215, 16777215))
        self.c19r_report_btn.setFont(font11)
        self.c19r_report_btn.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(150, 150, 250);\n"
"	background-color:rgb(45,50,60);\n"
"	border-radius:10%;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(120,120,255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.c19r_report_btn.setFlat(True)
        self.c19r_system_login_btn = QPushButton(self.covid_report)
        self.c19r_system_login_btn.setObjectName(u"c19r_system_login_btn")
        self.c19r_system_login_btn.setGeometry(QRect(270, 610, 61, 30))
        sizePolicy3.setHeightForWidth(self.c19r_system_login_btn.sizePolicy().hasHeightForWidth())
        self.c19r_system_login_btn.setSizePolicy(sizePolicy3)
        self.c19r_system_login_btn.setMinimumSize(QSize(0, 30))
        self.c19r_system_login_btn.setMaximumSize(QSize(16777215, 16777215))
        self.c19r_system_login_btn.setFont(font11)
        self.c19r_system_login_btn.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(130, 150, 180);\n"
"	background-color:rgb(45,50,60);\n"
"	border-radius:10%;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(110,130,230);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.c19r_system_login_btn.setFlat(True)
        self.c19r_title_lbl = QLabel(self.covid_report)
        self.c19r_title_lbl.setObjectName(u"c19r_title_lbl")
        self.c19r_title_lbl.setGeometry(QRect(20, 19, 491, 41))
        self.c19r_title_lbl.setMinimumSize(QSize(0, 30))
        font53 = QFont()
        font53.setFamilies([u"Lucida Sans"])
        font53.setPointSize(14)
        font53.setBold(True)
        font53.setItalic(True)
        self.c19r_title_lbl.setFont(font53)
        self.c19r_title_lbl.setStyleSheet(u"color: rgb(94, 129, 172);\n"
"background-color:rgb(38, 43, 52);\n"
"border:1px solid rgb(50, 55, 70);\n"
"border-radius:10px;")
        self.c19r_title_lbl.setAlignment(Qt.AlignCenter)
        self.c19r_warning_lbl = QLabel(self.covid_report)
        self.c19r_warning_lbl.setObjectName(u"c19r_warning_lbl")
        self.c19r_warning_lbl.setGeometry(QRect(10, 540, 511, 101))
        self.c19r_warning_lbl.setMinimumSize(QSize(0, 30))
        font54 = QFont()
        font54.setFamilies([u"\uc11c\uc6b8\ud55c\uac15 \uc7a5\uccb4 M"])
        font54.setPointSize(14)
        font54.setBold(True)
        font54.setItalic(True)
        self.c19r_warning_lbl.setFont(font54)
        self.c19r_warning_lbl.setStyleSheet(u"color: rgb(233, 100, 133);\n"
"background-color:rgb(38, 43, 52);\n"
"border:1px solid rgb(50, 55, 70);\n"
"border-radius:10px;")
        self.c19r_warning_lbl.setAlignment(Qt.AlignCenter)
        self.c19r_reset_btn = QPushButton(self.covid_report)
        self.c19r_reset_btn.setObjectName(u"c19r_reset_btn")
        self.c19r_reset_btn.setGeometry(QRect(340, 610, 61, 30))
        sizePolicy3.setHeightForWidth(self.c19r_reset_btn.sizePolicy().hasHeightForWidth())
        self.c19r_reset_btn.setSizePolicy(sizePolicy3)
        self.c19r_reset_btn.setMinimumSize(QSize(0, 30))
        self.c19r_reset_btn.setMaximumSize(QSize(16777215, 16777215))
        self.c19r_reset_btn.setFont(font11)
        self.c19r_reset_btn.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(160, 190, 150);\n"
"	background-color:rgb(45,50,60);\n"
"	border-radius:10%;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(140,200,130);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.c19r_reset_btn.setFlat(True)
        self.apps_stack.addWidget(self.covid_report)
        self.c19r_address1_lbl.raise_()
        self.c19r_sxsince_led.raise_()
        self.c19r_underaged_cbx.raise_()
        self.c19r_ptphone_led.raise_()
        self.c19r_address1_led.raise_()
        self.c19r_ptjmno_led.raise_()
        self.c19r_ptphone_lbl.raise_()
        self.c19r_sxsince_lbl.raise_()
        self.c19r_notes_pte.raise_()
        self.c19r_dx_date_lbl.raise_()
        self.c19r_address2_led.raise_()
        self.c19r_doctor_led.raise_()
        self.c19r_symp_lbl.raise_()
        self.c19r_subtitle2_lbl.raise_()
        self.c19r_notes_lbl.raise_()
        self.c19r_ptname_lbl.raise_()
        self.c19r_symp_pte.raise_()
        self.c19r_subtitle1_lbl.raise_()
        self.c19r_ptname_led.raise_()
        self.c19r_dx_date_led.raise_()
        self.c19r_adult_name_lbl.raise_()
        self.c19r_address2_lbl.raise_()
        self.c19r_ptjmno_lbl.raise_()
        self.c19r_doctor_lbl.raise_()
        self.c19r_adult_name_led.raise_()
        self.c19r_report_btn.raise_()
        self.c19r_system_login_btn.raise_()
        self.c19r_title_lbl.raise_()
        self.c19r_reset_btn.raise_()
        self.c19r_warning_lbl.raise_()
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.settings_reserve_2_btn = QPushButton(self.settings)
        self.settings_reserve_2_btn.setObjectName(u"settings_reserve_2_btn")
        self.settings_reserve_2_btn.setGeometry(QRect(400, -2, 120, 30))
        sizePolicy3.setHeightForWidth(self.settings_reserve_2_btn.sizePolicy().hasHeightForWidth())
        self.settings_reserve_2_btn.setSizePolicy(sizePolicy3)
        self.settings_reserve_2_btn.setMinimumSize(QSize(0, 30))
        self.settings_reserve_2_btn.setMaximumSize(QSize(16777215, 16777215))
        self.settings_reserve_2_btn.setFont(font35)
        self.settings_reserve_2_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(165, 170, 180);\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(230,220,144);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(75,85,100);\n"
"}")
        self.settings_reserve_2_btn.setFlat(True)
        self.settings_reserve_1_btn = QPushButton(self.settings)
        self.settings_reserve_1_btn.setObjectName(u"settings_reserve_1_btn")
        self.settings_reserve_1_btn.setGeometry(QRect(270, -2, 120, 30))
        sizePolicy3.setHeightForWidth(self.settings_reserve_1_btn.sizePolicy().hasHeightForWidth())
        self.settings_reserve_1_btn.setSizePolicy(sizePolicy3)
        self.settings_reserve_1_btn.setMinimumSize(QSize(0, 30))
        self.settings_reserve_1_btn.setMaximumSize(QSize(16777215, 16777215))
        self.settings_reserve_1_btn.setFont(font35)
        self.settings_reserve_1_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(165, 170, 180);\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(230,220,144);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(75,85,100);\n"
"}")
        self.settings_reserve_1_btn.setFlat(True)
        self.settings_gen_btn = QPushButton(self.settings)
        self.settings_gen_btn.setObjectName(u"settings_gen_btn")
        self.settings_gen_btn.setGeometry(QRect(10, -2, 120, 30))
        sizePolicy3.setHeightForWidth(self.settings_gen_btn.sizePolicy().hasHeightForWidth())
        self.settings_gen_btn.setSizePolicy(sizePolicy3)
        self.settings_gen_btn.setMinimumSize(QSize(0, 30))
        self.settings_gen_btn.setMaximumSize(QSize(16777215, 16777215))
        self.settings_gen_btn.setFont(font35)
        self.settings_gen_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(165, 170, 180);\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(230,220,144);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(75,85,100);\n"
"}")
        self.settings_gen_btn.setFlat(True)
        self.settings_lblr_btn = QPushButton(self.settings)
        self.settings_lblr_btn.setObjectName(u"settings_lblr_btn")
        self.settings_lblr_btn.setGeometry(QRect(140, -2, 120, 30))
        sizePolicy3.setHeightForWidth(self.settings_lblr_btn.sizePolicy().hasHeightForWidth())
        self.settings_lblr_btn.setSizePolicy(sizePolicy3)
        self.settings_lblr_btn.setMinimumSize(QSize(0, 30))
        self.settings_lblr_btn.setMaximumSize(QSize(16777215, 16777215))
        self.settings_lblr_btn.setFont(font35)
        self.settings_lblr_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(165, 170, 180);\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(230,220,144);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(75,85,100);\n"
"}")
        self.settings_lblr_btn.setFlat(True)
        self.settings_stack = QStackedWidget(self.settings)
        self.settings_stack.setObjectName(u"settings_stack")
        self.settings_stack.setGeometry(QRect(0, 29, 531, 611))
        self.settings_stack.setStyleSheet(u"QStackedWidget{\n"
"	border-top:1px solid rgb(55,60,75);\n"
"	background:transparent;\n"
"}")
        self.general_settings = QWidget()
        self.general_settings.setObjectName(u"general_settings")
        self.stgn_auto_backup_btn = QPushButton(self.general_settings)
        self.stgn_auto_backup_btn.setObjectName(u"stgn_auto_backup_btn")
        self.stgn_auto_backup_btn.setGeometry(QRect(20, 80, 151, 20))
        sizePolicy5.setHeightForWidth(self.stgn_auto_backup_btn.sizePolicy().hasHeightForWidth())
        self.stgn_auto_backup_btn.setSizePolicy(sizePolicy5)
        self.stgn_auto_backup_btn.setMinimumSize(QSize(0, 0))
        self.stgn_auto_backup_btn.setMaximumSize(QSize(16777215, 16777215))
        self.stgn_auto_backup_btn.setFont(font37)
        self.stgn_auto_backup_btn.setStyleSheet(u"QPushButton{\n"
"	text-align:left;\n"
"}\n"
"QPushButton::checked {\n"
"	color: rgb(233, 111, 122);\n"
"}")
        self.stgn_auto_backup_btn.setCheckable(True)
        self.stgn_auto_backup_btn.setChecked(True)
        self.stgn_auto_backup_btn.setAutoDefault(True)
        self.stgn_auto_backup_btn.setFlat(True)
        self.stgn_messenger_btn = QPushButton(self.general_settings)
        self.stgn_messenger_btn.setObjectName(u"stgn_messenger_btn")
        self.stgn_messenger_btn.setGeometry(QRect(20, 300, 111, 20))
        sizePolicy5.setHeightForWidth(self.stgn_messenger_btn.sizePolicy().hasHeightForWidth())
        self.stgn_messenger_btn.setSizePolicy(sizePolicy5)
        self.stgn_messenger_btn.setMinimumSize(QSize(0, 0))
        self.stgn_messenger_btn.setMaximumSize(QSize(16777215, 16777215))
        self.stgn_messenger_btn.setFont(font37)
        self.stgn_messenger_btn.setStyleSheet(u"QPushButton{\n"
"	text-align:left;\n"
"}\n"
"QPushButton::checked {\n"
"	color: rgb(100, 155, 244);\n"
"}\n"
"\n"
"\n"
"")
        self.stgn_messenger_btn.setCheckable(True)
        self.stgn_messenger_btn.setChecked(True)
        self.stgn_messenger_btn.setAutoDefault(True)
        self.stgn_messenger_btn.setFlat(True)
        self.stgn_auto_shutdown_btn = QPushButton(self.general_settings)
        self.stgn_auto_shutdown_btn.setObjectName(u"stgn_auto_shutdown_btn")
        self.stgn_auto_shutdown_btn.setGeometry(QRect(40, 130, 151, 20))
        sizePolicy5.setHeightForWidth(self.stgn_auto_shutdown_btn.sizePolicy().hasHeightForWidth())
        self.stgn_auto_shutdown_btn.setSizePolicy(sizePolicy5)
        self.stgn_auto_shutdown_btn.setMinimumSize(QSize(0, 0))
        self.stgn_auto_shutdown_btn.setMaximumSize(QSize(16777215, 16777215))
        self.stgn_auto_shutdown_btn.setFont(font37)
        self.stgn_auto_shutdown_btn.setStyleSheet(u"QPushButton{\n"
"	text-align:left;\n"
"}\n"
"QPushButton::checked {\n"
"	color: rgb(200, 133, 100);\n"
"}")
        self.stgn_auto_shutdown_btn.setCheckable(True)
        self.stgn_auto_shutdown_btn.setChecked(True)
        self.stgn_auto_shutdown_btn.setAutoDefault(True)
        self.stgn_auto_shutdown_btn.setFlat(True)
        self.stgn_auto_stats_btn = QPushButton(self.general_settings)
        self.stgn_auto_stats_btn.setObjectName(u"stgn_auto_stats_btn")
        self.stgn_auto_stats_btn.setGeometry(QRect(20, 180, 151, 20))
        sizePolicy5.setHeightForWidth(self.stgn_auto_stats_btn.sizePolicy().hasHeightForWidth())
        self.stgn_auto_stats_btn.setSizePolicy(sizePolicy5)
        self.stgn_auto_stats_btn.setMinimumSize(QSize(0, 0))
        self.stgn_auto_stats_btn.setMaximumSize(QSize(16777215, 16777215))
        self.stgn_auto_stats_btn.setFont(font37)
        self.stgn_auto_stats_btn.setStyleSheet(u"QPushButton{\n"
"	text-align:left;\n"
"}\n"
"QPushButton::checked {\n"
"	color: rgb(200, 188, 133);\n"
"}\n"
"\n"
"\n"
"")
        self.stgn_auto_stats_btn.setCheckable(True)
        self.stgn_auto_stats_btn.setChecked(True)
        self.stgn_auto_stats_btn.setAutoDefault(True)
        self.stgn_auto_stats_btn.setFlat(True)
        self.stgn_cloud_sync_btn = QPushButton(self.general_settings)
        self.stgn_cloud_sync_btn.setObjectName(u"stgn_cloud_sync_btn")
        self.stgn_cloud_sync_btn.setGeometry(QRect(20, 250, 161, 20))
        sizePolicy5.setHeightForWidth(self.stgn_cloud_sync_btn.sizePolicy().hasHeightForWidth())
        self.stgn_cloud_sync_btn.setSizePolicy(sizePolicy5)
        self.stgn_cloud_sync_btn.setMinimumSize(QSize(0, 0))
        self.stgn_cloud_sync_btn.setMaximumSize(QSize(16777215, 16777215))
        self.stgn_cloud_sync_btn.setFont(font37)
        self.stgn_cloud_sync_btn.setStyleSheet(u"QPushButton{\n"
"	text-align:left;\n"
"}\n"
"QPushButton::checked {\n"
"	color: rgb(133, 211, 133);\n"
"}\n"
"\n"
"\n"
"")
        self.stgn_cloud_sync_btn.setCheckable(True)
        self.stgn_cloud_sync_btn.setChecked(True)
        self.stgn_cloud_sync_btn.setAutoDefault(True)
        self.stgn_cloud_sync_btn.setFlat(True)
        self.stgn_vac_sys_log_btn = QPushButton(self.general_settings)
        self.stgn_vac_sys_log_btn.setObjectName(u"stgn_vac_sys_log_btn")
        self.stgn_vac_sys_log_btn.setGeometry(QRect(20, 440, 151, 20))
        sizePolicy5.setHeightForWidth(self.stgn_vac_sys_log_btn.sizePolicy().hasHeightForWidth())
        self.stgn_vac_sys_log_btn.setSizePolicy(sizePolicy5)
        self.stgn_vac_sys_log_btn.setMinimumSize(QSize(0, 0))
        self.stgn_vac_sys_log_btn.setMaximumSize(QSize(16777215, 16777215))
        self.stgn_vac_sys_log_btn.setFont(font37)
        self.stgn_vac_sys_log_btn.setStyleSheet(u"QPushButton{\n"
"	text-align:left;\n"
"}\n"
"QPushButton::checked {\n"
"	color: rgb(211, 144, 222);\n"
"}\n"
"\n"
"\n"
"")
        self.stgn_vac_sys_log_btn.setCheckable(True)
        self.stgn_vac_sys_log_btn.setChecked(True)
        self.stgn_vac_sys_log_btn.setAutoDefault(True)
        self.stgn_vac_sys_log_btn.setFlat(True)
        self.stgn_auto_backup_lbl = QLabel(self.general_settings)
        self.stgn_auto_backup_lbl.setObjectName(u"stgn_auto_backup_lbl")
        self.stgn_auto_backup_lbl.setGeometry(QRect(30, 100, 271, 20))
        self.stgn_auto_backup_lbl.setFont(font5)
        self.stgn_auto_shutdown_lbl = QLabel(self.general_settings)
        self.stgn_auto_shutdown_lbl.setObjectName(u"stgn_auto_shutdown_lbl")
        self.stgn_auto_shutdown_lbl.setGeometry(QRect(50, 150, 291, 20))
        self.stgn_auto_shutdown_lbl.setFont(font5)
        self.stgn_auto_stats_1_lbl = QLabel(self.general_settings)
        self.stgn_auto_stats_1_lbl.setObjectName(u"stgn_auto_stats_1_lbl")
        self.stgn_auto_stats_1_lbl.setGeometry(QRect(30, 200, 291, 20))
        self.stgn_auto_stats_1_lbl.setFont(font5)
        self.stgn_auto_stats_2_lbl = QLabel(self.general_settings)
        self.stgn_auto_stats_2_lbl.setObjectName(u"stgn_auto_stats_2_lbl")
        self.stgn_auto_stats_2_lbl.setGeometry(QRect(30, 220, 281, 20))
        self.stgn_auto_stats_2_lbl.setFont(font5)
        self.stgn_cloud_sync_lbl = QLabel(self.general_settings)
        self.stgn_cloud_sync_lbl.setObjectName(u"stgn_cloud_sync_lbl")
        self.stgn_cloud_sync_lbl.setGeometry(QRect(30, 270, 341, 20))
        self.stgn_cloud_sync_lbl.setFont(font5)
        self.stgn_messenger_1_lbl = QLabel(self.general_settings)
        self.stgn_messenger_1_lbl.setObjectName(u"stgn_messenger_1_lbl")
        self.stgn_messenger_1_lbl.setGeometry(QRect(30, 320, 201, 20))
        self.stgn_messenger_1_lbl.setFont(font5)
        self.stgn_messenger_2_lbl = QLabel(self.general_settings)
        self.stgn_messenger_2_lbl.setObjectName(u"stgn_messenger_2_lbl")
        self.stgn_messenger_2_lbl.setGeometry(QRect(40, 340, 391, 20))
        self.stgn_messenger_2_lbl.setFont(font5)
        self.stgn_messenger_3_lbl = QLabel(self.general_settings)
        self.stgn_messenger_3_lbl.setObjectName(u"stgn_messenger_3_lbl")
        self.stgn_messenger_3_lbl.setGeometry(QRect(40, 360, 391, 20))
        self.stgn_messenger_3_lbl.setFont(font5)
        self.stgn_auto_backup_led = QLineEdit(self.general_settings)
        self.stgn_auto_backup_led.setObjectName(u"stgn_auto_backup_led")
        self.stgn_auto_backup_led.setGeometry(QRect(300, 100, 50, 20))
        self.stgn_auto_backup_led.setMinimumSize(QSize(0, 0))
        self.stgn_auto_backup_led.setMaximumSize(QSize(16777215, 30))
        self.stgn_auto_backup_led.setFont(font1)
        self.stgn_auto_backup_led.setStyleSheet(u"color: rgb(166,177,199);\n"
"border-bottom:1px solid rgb(50, 55, 70);")
        self.stgn_auto_backup_led.setFrame(False)
        self.stgn_auto_backup_led.setAlignment(Qt.AlignCenter)
        self.stgn_auto_stats_led = QLineEdit(self.general_settings)
        self.stgn_auto_stats_led.setObjectName(u"stgn_auto_stats_led")
        self.stgn_auto_stats_led.setGeometry(QRect(310, 220, 50, 20))
        self.stgn_auto_stats_led.setMinimumSize(QSize(0, 0))
        self.stgn_auto_stats_led.setMaximumSize(QSize(16777215, 30))
        self.stgn_auto_stats_led.setFont(font1)
        self.stgn_auto_stats_led.setStyleSheet(u"color: rgb(166,177,199);\n"
"border-bottom:1px solid rgb(50, 55, 70);")
        self.stgn_auto_stats_led.setFrame(False)
        self.stgn_auto_stats_led.setAlignment(Qt.AlignCenter)
        self.stgn_cloud_sync_led = QLineEdit(self.general_settings)
        self.stgn_cloud_sync_led.setObjectName(u"stgn_cloud_sync_led")
        self.stgn_cloud_sync_led.setGeometry(QRect(370, 270, 50, 20))
        self.stgn_cloud_sync_led.setMinimumSize(QSize(0, 0))
        self.stgn_cloud_sync_led.setMaximumSize(QSize(16777215, 30))
        self.stgn_cloud_sync_led.setFont(font1)
        self.stgn_cloud_sync_led.setStyleSheet(u"color: rgb(166,177,199);\n"
"border-bottom:1px solid rgb(50, 55, 70);")
        self.stgn_cloud_sync_led.setFrame(False)
        self.stgn_cloud_sync_led.setAlignment(Qt.AlignCenter)
        self.stgn_vac_sys_log_lbl = QLabel(self.general_settings)
        self.stgn_vac_sys_log_lbl.setObjectName(u"stgn_vac_sys_log_lbl")
        self.stgn_vac_sys_log_lbl.setGeometry(QRect(30, 460, 481, 20))
        self.stgn_vac_sys_log_lbl.setFont(font5)
        self.stgn_messenger_server_pte = QPlainTextEdit(self.general_settings)
        self.stgn_messenger_server_pte.setObjectName(u"stgn_messenger_server_pte")
        self.stgn_messenger_server_pte.setGeometry(QRect(90, 383, 411, 51))
        sizePolicy8.setHeightForWidth(self.stgn_messenger_server_pte.sizePolicy().hasHeightForWidth())
        self.stgn_messenger_server_pte.setSizePolicy(sizePolicy8)
        self.stgn_messenger_server_pte.setMaximumSize(QSize(16777215, 555555))
        self.stgn_messenger_server_pte.setFont(font52)
        self.stgn_messenger_server_pte.setStyleSheet(u"background-color:rgb(39, 44, 54);\n"
"color: rgb(166,177,199);\n"
"border:1px solid rgb(45, 50, 65);\n"
"border-radius:5px;\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"")
        self.stgn_messenger_server_pte.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.stgn_messenger_server_pte.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.stgn_messenger_server_pte.setReadOnly(True)
        self.stgn_messenger_server_lbl = QLabel(self.general_settings)
        self.stgn_messenger_server_lbl.setObjectName(u"stgn_messenger_server_lbl")
        self.stgn_messenger_server_lbl.setGeometry(QRect(40, 380, 41, 20))
        self.stgn_messenger_server_lbl.setFont(font5)
        self.stgn_title_lbl = QLabel(self.general_settings)
        self.stgn_title_lbl.setObjectName(u"stgn_title_lbl")
        self.stgn_title_lbl.setGeometry(QRect(20, 20, 491, 41))
        self.stgn_title_lbl.setMinimumSize(QSize(0, 30))
        self.stgn_title_lbl.setFont(font53)
        self.stgn_title_lbl.setStyleSheet(u"color: rgb(94, 129, 172);\n"
"background-color:rgb(38, 43, 52);\n"
"border:1px solid rgb(45, 50, 65);\n"
"border-radius:10px;")
        self.stgn_title_lbl.setAlignment(Qt.AlignCenter)
        self.stgn_info_lbl = QLabel(self.general_settings)
        self.stgn_info_lbl.setObjectName(u"stgn_info_lbl")
        self.stgn_info_lbl.setGeometry(QRect(20, 500, 491, 41))
        self.stgn_info_lbl.setMinimumSize(QSize(0, 30))
        font55 = QFont()
        font55.setFamilies([u"\uc11c\uc6b8\ub0a8\uc0b0 \uc7a5\uccb4 M"])
        font55.setPointSize(12)
        font55.setBold(False)
        font55.setItalic(True)
        font55.setStyleStrategy(QFont.PreferAntialias)
        self.stgn_info_lbl.setFont(font55)
        self.stgn_info_lbl.setStyleSheet(u"color: rgb(100, 120, 150);\n"
"background-color:rgb(38, 43, 52);\n"
"border:1px solid rgb(45, 50, 65);\n"
"border-radius:10px;")
        self.stgn_info_lbl.setAlignment(Qt.AlignCenter)
        self.stgn_save_btn = QPushButton(self.general_settings)
        self.stgn_save_btn.setObjectName(u"stgn_save_btn")
        self.stgn_save_btn.setGeometry(QRect(380, 580, 141, 30))
        sizePolicy3.setHeightForWidth(self.stgn_save_btn.sizePolicy().hasHeightForWidth())
        self.stgn_save_btn.setSizePolicy(sizePolicy3)
        self.stgn_save_btn.setMinimumSize(QSize(0, 30))
        self.stgn_save_btn.setMaximumSize(QSize(16777215, 16777215))
        self.stgn_save_btn.setFont(font11)
        self.stgn_save_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(200, 200, 200);\n"
"	background-color:rgb(45,50,60);\n"
"	border-radius:10%;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(240,240,250);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.stgn_save_btn.setFlat(True)
        self.stgn_reset_btn = QPushButton(self.general_settings)
        self.stgn_reset_btn.setObjectName(u"stgn_reset_btn")
        self.stgn_reset_btn.setGeometry(QRect(290, 580, 81, 30))
        sizePolicy3.setHeightForWidth(self.stgn_reset_btn.sizePolicy().hasHeightForWidth())
        self.stgn_reset_btn.setSizePolicy(sizePolicy3)
        self.stgn_reset_btn.setMinimumSize(QSize(0, 30))
        self.stgn_reset_btn.setMaximumSize(QSize(16777215, 16777215))
        self.stgn_reset_btn.setFont(font11)
        self.stgn_reset_btn.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(160, 190, 150);\n"
"	background-color:rgb(45,50,60);\n"
"	border-radius:10%;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(140,200,130);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.stgn_reset_btn.setFlat(True)
        self.settings_stack.addWidget(self.general_settings)
        self.labeler_settings = QWidget()
        self.labeler_settings.setObjectName(u"labeler_settings")
        self.stlb_flu_age_75over_lbl1 = QLabel(self.labeler_settings)
        self.stlb_flu_age_75over_lbl1.setObjectName(u"stlb_flu_age_75over_lbl1")
        self.stlb_flu_age_75over_lbl1.setGeometry(QRect(370, 260, 31, 30))
        self.stlb_flu_age_75over_lbl1.setMinimumSize(QSize(0, 30))
        self.stlb_flu_age_75over_lbl1.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_age_75over_lbl1.setFont(font47)
        self.stlb_flu_age_75over_lbl1.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);")
        self.stlb_flu_age_75over_lbl1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.stlb_flu_old_over75_start_lbl = QLabel(self.labeler_settings)
        self.stlb_flu_old_over75_start_lbl.setObjectName(u"stlb_flu_old_over75_start_lbl")
        self.stlb_flu_old_over75_start_lbl.setGeometry(QRect(19, 260, 70, 30))
        self.stlb_flu_old_over75_start_lbl.setMinimumSize(QSize(70, 30))
        self.stlb_flu_old_over75_start_lbl.setMaximumSize(QSize(70, 30))
        self.stlb_flu_old_over75_start_lbl.setFont(font31)
        self.stlb_flu_old_over75_start_lbl.setStyleSheet(u"color: rgb(133, 155, 200);\n"
"border-bottom:1px solid rgb(70,75,100);\n"
"background:transparent")
        self.stlb_flu_old_over75_start_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.stlb_flu_old_over75_start_led = QLineEdit(self.labeler_settings)
        self.stlb_flu_old_over75_start_led.setObjectName(u"stlb_flu_old_over75_start_led")
        self.stlb_flu_old_over75_start_led.setGeometry(QRect(89, 260, 81, 30))
        self.stlb_flu_old_over75_start_led.setMinimumSize(QSize(0, 30))
        self.stlb_flu_old_over75_start_led.setMaximumSize(QSize(16777215, 30))
        font56 = QFont()
        font56.setFamilies([u"\uc11c\uc6b8\ub0a8\uc0b0 \uc7a5\uccb4 M"])
        font56.setPointSize(13)
        font56.setBold(False)
        self.stlb_flu_old_over75_start_led.setFont(font56)
        self.stlb_flu_old_over75_start_led.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);\n"
"padding-left:6px;")
        self.stlb_flu_old_over75_start_led.setFrame(False)
        self.stlb_flu_age_child_lbl = QLabel(self.labeler_settings)
        self.stlb_flu_age_child_lbl.setObjectName(u"stlb_flu_age_child_lbl")
        self.stlb_flu_age_child_lbl.setGeometry(QRect(20, 480, 70, 30))
        self.stlb_flu_age_child_lbl.setMinimumSize(QSize(70, 30))
        self.stlb_flu_age_child_lbl.setMaximumSize(QSize(70, 30))
        self.stlb_flu_age_child_lbl.setFont(font31)
        self.stlb_flu_age_child_lbl.setStyleSheet(u"color: rgb(133, 155, 200);\n"
"border-bottom:1px solid rgb(70,75,100);\n"
"background:transparent")
        self.stlb_flu_age_child_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.stlb_flu_allow_ex_cbx = QCheckBox(self.labeler_settings)
        self.stlb_flu_allow_ex_cbx.setObjectName(u"stlb_flu_allow_ex_cbx")
        self.stlb_flu_allow_ex_cbx.setGeometry(QRect(10, 200, 271, 30))
        self.stlb_flu_allow_ex_cbx.setMinimumSize(QSize(0, 30))
        self.stlb_flu_allow_ex_cbx.setFont(font31)
        self.stlb_flu_allow_ex_cbx.setStyleSheet(u"")
        self.stlb_flu_allow_ex_cbx.setChecked(True)
        self.stlb_flu_auto_sort_cbx = QCheckBox(self.labeler_settings)
        self.stlb_flu_auto_sort_cbx.setObjectName(u"stlb_flu_auto_sort_cbx")
        self.stlb_flu_auto_sort_cbx.setGeometry(QRect(10, 170, 251, 30))
        self.stlb_flu_auto_sort_cbx.setMinimumSize(QSize(0, 30))
        self.stlb_flu_auto_sort_cbx.setFont(font31)
        self.stlb_flu_auto_sort_cbx.setStyleSheet(u"")
        self.stlb_flu_auto_sort_cbx.setChecked(True)
        self.stlb_flu_age_7074_lbl = QLabel(self.labeler_settings)
        self.stlb_flu_age_7074_lbl.setObjectName(u"stlb_flu_age_7074_lbl")
        self.stlb_flu_age_7074_lbl.setGeometry(QRect(220, 290, 70, 30))
        self.stlb_flu_age_7074_lbl.setMinimumSize(QSize(70, 30))
        self.stlb_flu_age_7074_lbl.setMaximumSize(QSize(70, 30))
        self.stlb_flu_age_7074_lbl.setFont(font31)
        self.stlb_flu_age_7074_lbl.setStyleSheet(u"color: rgb(133, 155, 200);\n"
"border-bottom:1px solid rgb(70,75,100);\n"
"background:transparent")
        self.stlb_flu_age_7074_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.stlb_flu_old_7074_start_led = QLineEdit(self.labeler_settings)
        self.stlb_flu_old_7074_start_led.setObjectName(u"stlb_flu_old_7074_start_led")
        self.stlb_flu_old_7074_start_led.setGeometry(QRect(89, 290, 81, 30))
        self.stlb_flu_old_7074_start_led.setMinimumSize(QSize(0, 30))
        self.stlb_flu_old_7074_start_led.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_old_7074_start_led.setFont(font56)
        self.stlb_flu_old_7074_start_led.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);\n"
"padding-left:6px;")
        self.stlb_flu_old_7074_start_led.setFrame(False)
        self.stlb_flu_old_6569_start_led = QLineEdit(self.labeler_settings)
        self.stlb_flu_old_6569_start_led.setObjectName(u"stlb_flu_old_6569_start_led")
        self.stlb_flu_old_6569_start_led.setGeometry(QRect(89, 320, 81, 30))
        self.stlb_flu_old_6569_start_led.setMinimumSize(QSize(0, 30))
        self.stlb_flu_old_6569_start_led.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_old_6569_start_led.setFont(font56)
        self.stlb_flu_old_6569_start_led.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);\n"
"padding-left:6px;")
        self.stlb_flu_old_6569_start_led.setFrame(False)
        self.stlb_flu_old_7074_start_lbl = QLabel(self.labeler_settings)
        self.stlb_flu_old_7074_start_lbl.setObjectName(u"stlb_flu_old_7074_start_lbl")
        self.stlb_flu_old_7074_start_lbl.setGeometry(QRect(19, 290, 70, 30))
        self.stlb_flu_old_7074_start_lbl.setMinimumSize(QSize(70, 30))
        self.stlb_flu_old_7074_start_lbl.setMaximumSize(QSize(70, 30))
        self.stlb_flu_old_7074_start_lbl.setFont(font31)
        self.stlb_flu_old_7074_start_lbl.setStyleSheet(u"color: rgb(133, 155, 200);\n"
"border-bottom:1px solid rgb(70,75,100);\n"
"background:transparent")
        self.stlb_flu_old_7074_start_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.stlb_child_flu_lot_led = QLineEdit(self.labeler_settings)
        self.stlb_child_flu_lot_led.setObjectName(u"stlb_child_flu_lot_led")
        self.stlb_child_flu_lot_led.setGeometry(QRect(69, 140, 150, 30))
        self.stlb_child_flu_lot_led.setMinimumSize(QSize(0, 30))
        self.stlb_child_flu_lot_led.setMaximumSize(QSize(16777215, 30))
        font57 = QFont()
        font57.setFamilies([u"\uc11c\uc6b8\ub0a8\uc0b0 \uc7a5\uccb4 M"])
        font57.setPointSize(12)
        font57.setBold(False)
        self.stlb_child_flu_lot_led.setFont(font57)
        self.stlb_child_flu_lot_led.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);")
        self.stlb_child_flu_lot_led.setFrame(False)
        self.stlb_flu_old_6569_start_lbl = QLabel(self.labeler_settings)
        self.stlb_flu_old_6569_start_lbl.setObjectName(u"stlb_flu_old_6569_start_lbl")
        self.stlb_flu_old_6569_start_lbl.setGeometry(QRect(19, 320, 70, 30))
        self.stlb_flu_old_6569_start_lbl.setMinimumSize(QSize(70, 30))
        self.stlb_flu_old_6569_start_lbl.setMaximumSize(QSize(70, 30))
        self.stlb_flu_old_6569_start_lbl.setFont(font31)
        self.stlb_flu_old_6569_start_lbl.setStyleSheet(u"color: rgb(133, 155, 200);\n"
"border-bottom:1px solid rgb(70,75,100);\n"
"background:transparent")
        self.stlb_flu_old_6569_start_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.stlb_subtitle_flu_old_age_lbl = QLabel(self.labeler_settings)
        self.stlb_subtitle_flu_old_age_lbl.setObjectName(u"stlb_subtitle_flu_old_age_lbl")
        self.stlb_subtitle_flu_old_age_lbl.setGeometry(QRect(210, 230, 281, 30))
        font58 = QFont()
        font58.setFamilies([u"\uc11c\uc6b8\ub0a8\uc0b0 \uc7a5\uccb4 B"])
        font58.setPointSize(12)
        font58.setBold(True)
        self.stlb_subtitle_flu_old_age_lbl.setFont(font58)
        self.stlb_subtitle_flu_old_age_lbl.setStyleSheet(u"padding-left:10px;\n"
"color: rgb(155, 188, 222);\n"
"border:none;\n"
"background:none;")
        self.stlb_flu_age_6569_lbl = QLabel(self.labeler_settings)
        self.stlb_flu_age_6569_lbl.setObjectName(u"stlb_flu_age_6569_lbl")
        self.stlb_flu_age_6569_lbl.setGeometry(QRect(220, 320, 70, 30))
        self.stlb_flu_age_6569_lbl.setMinimumSize(QSize(70, 30))
        self.stlb_flu_age_6569_lbl.setMaximumSize(QSize(70, 30))
        self.stlb_flu_age_6569_lbl.setFont(font31)
        self.stlb_flu_age_6569_lbl.setStyleSheet(u"color: rgb(133, 155, 200);\n"
"border-bottom:1px solid rgb(70,75,100);\n"
"background:transparent")
        self.stlb_flu_age_6569_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.stlb_flu_old_over75_start_lbl1 = QLabel(self.labeler_settings)
        self.stlb_flu_old_over75_start_lbl1.setObjectName(u"stlb_flu_old_over75_start_lbl1")
        self.stlb_flu_old_over75_start_lbl1.setGeometry(QRect(170, 260, 31, 30))
        self.stlb_flu_old_over75_start_lbl1.setMinimumSize(QSize(0, 30))
        self.stlb_flu_old_over75_start_lbl1.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_old_over75_start_lbl1.setFont(font47)
        self.stlb_flu_old_over75_start_lbl1.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);")
        self.stlb_flu_old_over75_start_lbl1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.stlb_flu_date_child_once_led1 = QLineEdit(self.labeler_settings)
        self.stlb_flu_date_child_once_led1.setObjectName(u"stlb_flu_date_child_once_led1")
        self.stlb_flu_date_child_once_led1.setGeometry(QRect(90, 450, 81, 30))
        self.stlb_flu_date_child_once_led1.setMinimumSize(QSize(0, 30))
        self.stlb_flu_date_child_once_led1.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_date_child_once_led1.setFont(font56)
        self.stlb_flu_date_child_once_led1.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);\n"
"padding-left:6px;")
        self.stlb_flu_date_child_once_led1.setFrame(False)
        self.stlb_subtitle_flu_old_date_lbl = QLabel(self.labeler_settings)
        self.stlb_subtitle_flu_old_date_lbl.setObjectName(u"stlb_subtitle_flu_old_date_lbl")
        self.stlb_subtitle_flu_old_date_lbl.setGeometry(QRect(9, 230, 181, 30))
        self.stlb_subtitle_flu_old_date_lbl.setFont(font58)
        self.stlb_subtitle_flu_old_date_lbl.setStyleSheet(u"padding-left:10px;\n"
"color: rgb(155, 188, 222);\n"
"border:none;\n"
"background:none;")
        self.stlb_flu_age_75over_led = QLineEdit(self.labeler_settings)
        self.stlb_flu_age_75over_led.setObjectName(u"stlb_flu_age_75over_led")
        self.stlb_flu_age_75over_led.setGeometry(QRect(290, 260, 81, 30))
        self.stlb_flu_age_75over_led.setMinimumSize(QSize(0, 30))
        self.stlb_flu_age_75over_led.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_age_75over_led.setFont(font56)
        self.stlb_flu_age_75over_led.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);\n"
"padding-left:6px;")
        self.stlb_flu_age_75over_led.setFrame(False)
        self.stlb_child_flu_lot_lbl = QLabel(self.labeler_settings)
        self.stlb_child_flu_lot_lbl.setObjectName(u"stlb_child_flu_lot_lbl")
        self.stlb_child_flu_lot_lbl.setGeometry(QRect(29, 140, 40, 30))
        self.stlb_child_flu_lot_lbl.setMinimumSize(QSize(40, 30))
        self.stlb_child_flu_lot_lbl.setMaximumSize(QSize(16777215, 30))
        self.stlb_child_flu_lot_lbl.setFont(font31)
        self.stlb_child_flu_lot_lbl.setStyleSheet(u"color: rgb(133, 155, 200);\n"
"border-bottom:1px solid rgb(70,75,100);")
        self.stlb_child_flu_lot_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.stlb_auto_input_cbx = QCheckBox(self.labeler_settings)
        self.stlb_auto_input_cbx.setObjectName(u"stlb_auto_input_cbx")
        self.stlb_auto_input_cbx.setGeometry(QRect(10, 80, 300, 30))
        self.stlb_auto_input_cbx.setMinimumSize(QSize(0, 30))
        self.stlb_auto_input_cbx.setFont(font31)
        self.stlb_auto_input_cbx.setStyleSheet(u"")
        self.stlb_auto_input_cbx.setChecked(True)
        self.stlb_flu_date_child_twice_led1 = QLineEdit(self.labeler_settings)
        self.stlb_flu_date_child_twice_led1.setObjectName(u"stlb_flu_date_child_twice_led1")
        self.stlb_flu_date_child_twice_led1.setGeometry(QRect(90, 420, 81, 30))
        self.stlb_flu_date_child_twice_led1.setMinimumSize(QSize(0, 30))
        self.stlb_flu_date_child_twice_led1.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_date_child_twice_led1.setFont(font56)
        self.stlb_flu_date_child_twice_led1.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);\n"
"padding-left:6px;")
        self.stlb_flu_date_child_twice_led1.setFrame(False)
        self.stlb_flu_old_6569_start_lbl1 = QLabel(self.labeler_settings)
        self.stlb_flu_old_6569_start_lbl1.setObjectName(u"stlb_flu_old_6569_start_lbl1")
        self.stlb_flu_old_6569_start_lbl1.setGeometry(QRect(170, 320, 31, 30))
        self.stlb_flu_old_6569_start_lbl1.setMinimumSize(QSize(0, 30))
        self.stlb_flu_old_6569_start_lbl1.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_old_6569_start_lbl1.setFont(font47)
        self.stlb_flu_old_6569_start_lbl1.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);")
        self.stlb_flu_old_6569_start_lbl1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.stlb_flu_date_child_twice_lbl = QLabel(self.labeler_settings)
        self.stlb_flu_date_child_twice_lbl.setObjectName(u"stlb_flu_date_child_twice_lbl")
        self.stlb_flu_date_child_twice_lbl.setGeometry(QRect(20, 420, 70, 30))
        self.stlb_flu_date_child_twice_lbl.setMinimumSize(QSize(70, 30))
        self.stlb_flu_date_child_twice_lbl.setMaximumSize(QSize(70, 30))
        self.stlb_flu_date_child_twice_lbl.setFont(font31)
        self.stlb_flu_date_child_twice_lbl.setStyleSheet(u"color: rgb(133, 155, 200);\n"
"border-bottom:1px solid rgb(70,75,100);\n"
"background:transparent")
        self.stlb_flu_date_child_twice_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.stlb_flu_age_child_led1 = QLineEdit(self.labeler_settings)
        self.stlb_flu_age_child_led1.setObjectName(u"stlb_flu_age_child_led1")
        self.stlb_flu_age_child_led1.setGeometry(QRect(90, 480, 81, 30))
        self.stlb_flu_age_child_led1.setMinimumSize(QSize(0, 30))
        self.stlb_flu_age_child_led1.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_age_child_led1.setFont(font56)
        self.stlb_flu_age_child_led1.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);\n"
"padding-left:6px;")
        self.stlb_flu_age_child_led1.setFrame(False)
        self.stlb_flu_age_75over_lbl = QLabel(self.labeler_settings)
        self.stlb_flu_age_75over_lbl.setObjectName(u"stlb_flu_age_75over_lbl")
        self.stlb_flu_age_75over_lbl.setGeometry(QRect(220, 260, 70, 30))
        self.stlb_flu_age_75over_lbl.setMinimumSize(QSize(70, 30))
        self.stlb_flu_age_75over_lbl.setMaximumSize(QSize(70, 30))
        self.stlb_flu_age_75over_lbl.setFont(font31)
        self.stlb_flu_age_75over_lbl.setStyleSheet(u"color: rgb(133, 155, 200);\n"
"border-bottom:1px solid rgb(70,75,100);\n"
"background:transparent")
        self.stlb_flu_age_75over_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.stlb_auto_child_flu_lot_cbx = QCheckBox(self.labeler_settings)
        self.stlb_auto_child_flu_lot_cbx.setObjectName(u"stlb_auto_child_flu_lot_cbx")
        self.stlb_auto_child_flu_lot_cbx.setGeometry(QRect(10, 110, 268, 30))
        self.stlb_auto_child_flu_lot_cbx.setMinimumSize(QSize(0, 30))
        self.stlb_auto_child_flu_lot_cbx.setFont(font31)
        self.stlb_auto_child_flu_lot_cbx.setStyleSheet(u"")
        self.stlb_auto_child_flu_lot_cbx.setChecked(True)
        self.stlb_flu_old_7074_start_lbl1 = QLabel(self.labeler_settings)
        self.stlb_flu_old_7074_start_lbl1.setObjectName(u"stlb_flu_old_7074_start_lbl1")
        self.stlb_flu_old_7074_start_lbl1.setGeometry(QRect(170, 290, 31, 30))
        self.stlb_flu_old_7074_start_lbl1.setMinimumSize(QSize(0, 30))
        self.stlb_flu_old_7074_start_lbl1.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_old_7074_start_lbl1.setFont(font47)
        self.stlb_flu_old_7074_start_lbl1.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);")
        self.stlb_flu_old_7074_start_lbl1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.stlb_flu_age_child_led2 = QLineEdit(self.labeler_settings)
        self.stlb_flu_age_child_led2.setObjectName(u"stlb_flu_age_child_led2")
        self.stlb_flu_age_child_led2.setGeometry(QRect(200, 480, 81, 30))
        self.stlb_flu_age_child_led2.setMinimumSize(QSize(0, 30))
        self.stlb_flu_age_child_led2.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_age_child_led2.setFont(font56)
        self.stlb_flu_age_child_led2.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);\n"
"padding-left:6px;")
        self.stlb_flu_age_child_led2.setFrame(False)
        self.stlb_flu_date_child_once_lbl1 = QLabel(self.labeler_settings)
        self.stlb_flu_date_child_once_lbl1.setObjectName(u"stlb_flu_date_child_once_lbl1")
        self.stlb_flu_date_child_once_lbl1.setGeometry(QRect(170, 450, 31, 30))
        self.stlb_flu_date_child_once_lbl1.setMinimumSize(QSize(0, 30))
        self.stlb_flu_date_child_once_lbl1.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_date_child_once_lbl1.setFont(font57)
        self.stlb_flu_date_child_once_lbl1.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);")
        self.stlb_flu_date_child_once_lbl1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.stlb_subtitle_flu_child_lbl = QLabel(self.labeler_settings)
        self.stlb_subtitle_flu_child_lbl.setObjectName(u"stlb_subtitle_flu_child_lbl")
        self.stlb_subtitle_flu_child_lbl.setGeometry(QRect(10, 400, 244, 18))
        self.stlb_subtitle_flu_child_lbl.setFont(font58)
        self.stlb_subtitle_flu_child_lbl.setStyleSheet(u"padding-left:10px;\n"
"color: rgb(155, 188, 222);\n"
"border:none;\n"
"background:none;")
        self.stlb_flu_date_child_twice_lbl1 = QLabel(self.labeler_settings)
        self.stlb_flu_date_child_twice_lbl1.setObjectName(u"stlb_flu_date_child_twice_lbl1")
        self.stlb_flu_date_child_twice_lbl1.setGeometry(QRect(170, 420, 31, 30))
        self.stlb_flu_date_child_twice_lbl1.setMinimumSize(QSize(0, 30))
        self.stlb_flu_date_child_twice_lbl1.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_date_child_twice_lbl1.setFont(font57)
        self.stlb_flu_date_child_twice_lbl1.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);")
        self.stlb_flu_date_child_twice_lbl1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.stlb_flu_date_child_once_lbl = QLabel(self.labeler_settings)
        self.stlb_flu_date_child_once_lbl.setObjectName(u"stlb_flu_date_child_once_lbl")
        self.stlb_flu_date_child_once_lbl.setGeometry(QRect(20, 450, 70, 30))
        self.stlb_flu_date_child_once_lbl.setMinimumSize(QSize(70, 30))
        self.stlb_flu_date_child_once_lbl.setMaximumSize(QSize(70, 30))
        self.stlb_flu_date_child_once_lbl.setFont(font31)
        self.stlb_flu_date_child_once_lbl.setStyleSheet(u"color: rgb(133, 155, 200);\n"
"border-bottom:1px solid rgb(70,75,100);\n"
"background:transparent")
        self.stlb_flu_date_child_once_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.stlb_flu_date_child_once_led2 = QLineEdit(self.labeler_settings)
        self.stlb_flu_date_child_once_led2.setObjectName(u"stlb_flu_date_child_once_led2")
        self.stlb_flu_date_child_once_led2.setGeometry(QRect(200, 450, 81, 30))
        self.stlb_flu_date_child_once_led2.setMinimumSize(QSize(0, 30))
        self.stlb_flu_date_child_once_led2.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_date_child_once_led2.setFont(font56)
        self.stlb_flu_date_child_once_led2.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);\n"
"padding-left:6px;")
        self.stlb_flu_date_child_once_led2.setFrame(False)
        self.stlb_flu_date_child_once_lbl2 = QLabel(self.labeler_settings)
        self.stlb_flu_date_child_once_lbl2.setObjectName(u"stlb_flu_date_child_once_lbl2")
        self.stlb_flu_date_child_once_lbl2.setGeometry(QRect(280, 450, 31, 30))
        self.stlb_flu_date_child_once_lbl2.setMinimumSize(QSize(0, 30))
        self.stlb_flu_date_child_once_lbl2.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_date_child_once_lbl2.setFont(font57)
        self.stlb_flu_date_child_once_lbl2.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);")
        self.stlb_flu_date_child_once_lbl2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.stlb_flu_date_child_twice_lbl2 = QLabel(self.labeler_settings)
        self.stlb_flu_date_child_twice_lbl2.setObjectName(u"stlb_flu_date_child_twice_lbl2")
        self.stlb_flu_date_child_twice_lbl2.setGeometry(QRect(280, 420, 31, 30))
        self.stlb_flu_date_child_twice_lbl2.setMinimumSize(QSize(0, 30))
        self.stlb_flu_date_child_twice_lbl2.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_date_child_twice_lbl2.setFont(font57)
        self.stlb_flu_date_child_twice_lbl2.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);")
        self.stlb_flu_date_child_twice_lbl2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.stlb_flu_date_child_twice_led2 = QLineEdit(self.labeler_settings)
        self.stlb_flu_date_child_twice_led2.setObjectName(u"stlb_flu_date_child_twice_led2")
        self.stlb_flu_date_child_twice_led2.setGeometry(QRect(200, 420, 81, 30))
        self.stlb_flu_date_child_twice_led2.setMinimumSize(QSize(0, 30))
        self.stlb_flu_date_child_twice_led2.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_date_child_twice_led2.setFont(font56)
        self.stlb_flu_date_child_twice_led2.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);\n"
"padding-left:6px;")
        self.stlb_flu_date_child_twice_led2.setFrame(False)
        self.stlb_flu_old_end_lbl = QLabel(self.labeler_settings)
        self.stlb_flu_old_end_lbl.setObjectName(u"stlb_flu_old_end_lbl")
        self.stlb_flu_old_end_lbl.setGeometry(QRect(20, 350, 70, 30))
        self.stlb_flu_old_end_lbl.setMinimumSize(QSize(70, 30))
        self.stlb_flu_old_end_lbl.setMaximumSize(QSize(70, 30))
        self.stlb_flu_old_end_lbl.setFont(font31)
        self.stlb_flu_old_end_lbl.setStyleSheet(u"color: rgb(133, 155, 200);\n"
"border-bottom:1px solid rgb(70,75,100);\n"
"background:transparent")
        self.stlb_flu_old_end_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.stlb_flu_old_end_lbl1 = QLabel(self.labeler_settings)
        self.stlb_flu_old_end_lbl1.setObjectName(u"stlb_flu_old_end_lbl1")
        self.stlb_flu_old_end_lbl1.setGeometry(QRect(170, 350, 31, 30))
        self.stlb_flu_old_end_lbl1.setMinimumSize(QSize(0, 30))
        self.stlb_flu_old_end_lbl1.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_old_end_lbl1.setFont(font57)
        self.stlb_flu_old_end_lbl1.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);")
        self.stlb_flu_old_end_lbl1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.stlb_flu_old_end_led = QLineEdit(self.labeler_settings)
        self.stlb_flu_old_end_led.setObjectName(u"stlb_flu_old_end_led")
        self.stlb_flu_old_end_led.setGeometry(QRect(90, 350, 81, 30))
        self.stlb_flu_old_end_led.setMinimumSize(QSize(0, 30))
        self.stlb_flu_old_end_led.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_old_end_led.setFont(font56)
        self.stlb_flu_old_end_led.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);\n"
"padding-left:6px;")
        self.stlb_flu_old_end_led.setFrame(False)
        self.stlb_title_lbl = QLabel(self.labeler_settings)
        self.stlb_title_lbl.setObjectName(u"stlb_title_lbl")
        self.stlb_title_lbl.setGeometry(QRect(20, 20, 491, 41))
        self.stlb_title_lbl.setMinimumSize(QSize(0, 30))
        self.stlb_title_lbl.setFont(font53)
        self.stlb_title_lbl.setStyleSheet(u"color: rgb(94, 129, 172);\n"
"background-color:rgb(38, 43, 52);\n"
"border:1px solid rgb(45, 50, 65);\n"
"border-radius:10px;")
        self.stlb_title_lbl.setAlignment(Qt.AlignCenter)
        self.stlb_flu_age_child_lbl1 = QLabel(self.labeler_settings)
        self.stlb_flu_age_child_lbl1.setObjectName(u"stlb_flu_age_child_lbl1")
        self.stlb_flu_age_child_lbl1.setGeometry(QRect(170, 480, 31, 30))
        self.stlb_flu_age_child_lbl1.setMinimumSize(QSize(0, 30))
        self.stlb_flu_age_child_lbl1.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_age_child_lbl1.setFont(font57)
        self.stlb_flu_age_child_lbl1.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);")
        self.stlb_flu_age_child_lbl1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.stlb_flu_age_child_lbl2 = QLabel(self.labeler_settings)
        self.stlb_flu_age_child_lbl2.setObjectName(u"stlb_flu_age_child_lbl2")
        self.stlb_flu_age_child_lbl2.setGeometry(QRect(280, 480, 31, 30))
        self.stlb_flu_age_child_lbl2.setMinimumSize(QSize(0, 30))
        self.stlb_flu_age_child_lbl2.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_age_child_lbl2.setFont(font57)
        self.stlb_flu_age_child_lbl2.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);")
        self.stlb_flu_age_child_lbl2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.stlb_flu_age_7074_lbl2 = QLabel(self.labeler_settings)
        self.stlb_flu_age_7074_lbl2.setObjectName(u"stlb_flu_age_7074_lbl2")
        self.stlb_flu_age_7074_lbl2.setGeometry(QRect(480, 290, 31, 30))
        self.stlb_flu_age_7074_lbl2.setMinimumSize(QSize(0, 30))
        self.stlb_flu_age_7074_lbl2.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_age_7074_lbl2.setFont(font57)
        self.stlb_flu_age_7074_lbl2.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);")
        self.stlb_flu_age_7074_lbl2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.stlb_flu_age_7074_lbl1 = QLabel(self.labeler_settings)
        self.stlb_flu_age_7074_lbl1.setObjectName(u"stlb_flu_age_7074_lbl1")
        self.stlb_flu_age_7074_lbl1.setGeometry(QRect(370, 290, 31, 30))
        self.stlb_flu_age_7074_lbl1.setMinimumSize(QSize(0, 30))
        self.stlb_flu_age_7074_lbl1.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_age_7074_lbl1.setFont(font57)
        self.stlb_flu_age_7074_lbl1.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);")
        self.stlb_flu_age_7074_lbl1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.stlb_flu_age_7074_led1 = QLineEdit(self.labeler_settings)
        self.stlb_flu_age_7074_led1.setObjectName(u"stlb_flu_age_7074_led1")
        self.stlb_flu_age_7074_led1.setGeometry(QRect(290, 290, 81, 30))
        self.stlb_flu_age_7074_led1.setMinimumSize(QSize(0, 30))
        self.stlb_flu_age_7074_led1.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_age_7074_led1.setFont(font56)
        self.stlb_flu_age_7074_led1.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);\n"
"padding-left:6px;")
        self.stlb_flu_age_7074_led1.setFrame(False)
        self.stlb_flu_age_7074_led2 = QLineEdit(self.labeler_settings)
        self.stlb_flu_age_7074_led2.setObjectName(u"stlb_flu_age_7074_led2")
        self.stlb_flu_age_7074_led2.setGeometry(QRect(400, 290, 81, 30))
        self.stlb_flu_age_7074_led2.setMinimumSize(QSize(0, 30))
        self.stlb_flu_age_7074_led2.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_age_7074_led2.setFont(font56)
        self.stlb_flu_age_7074_led2.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);\n"
"padding-left:6px;")
        self.stlb_flu_age_7074_led2.setFrame(False)
        self.stlb_flu_age_6569_lbl2 = QLabel(self.labeler_settings)
        self.stlb_flu_age_6569_lbl2.setObjectName(u"stlb_flu_age_6569_lbl2")
        self.stlb_flu_age_6569_lbl2.setGeometry(QRect(480, 320, 31, 30))
        self.stlb_flu_age_6569_lbl2.setMinimumSize(QSize(0, 30))
        self.stlb_flu_age_6569_lbl2.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_age_6569_lbl2.setFont(font57)
        self.stlb_flu_age_6569_lbl2.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);")
        self.stlb_flu_age_6569_lbl2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.stlb_flu_age_6569_lbl1 = QLabel(self.labeler_settings)
        self.stlb_flu_age_6569_lbl1.setObjectName(u"stlb_flu_age_6569_lbl1")
        self.stlb_flu_age_6569_lbl1.setGeometry(QRect(370, 320, 31, 30))
        self.stlb_flu_age_6569_lbl1.setMinimumSize(QSize(0, 30))
        self.stlb_flu_age_6569_lbl1.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_age_6569_lbl1.setFont(font57)
        self.stlb_flu_age_6569_lbl1.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);")
        self.stlb_flu_age_6569_lbl1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.stlb_flu_age_6569_led1 = QLineEdit(self.labeler_settings)
        self.stlb_flu_age_6569_led1.setObjectName(u"stlb_flu_age_6569_led1")
        self.stlb_flu_age_6569_led1.setGeometry(QRect(290, 320, 81, 30))
        self.stlb_flu_age_6569_led1.setMinimumSize(QSize(0, 30))
        self.stlb_flu_age_6569_led1.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_age_6569_led1.setFont(font56)
        self.stlb_flu_age_6569_led1.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);\n"
"padding-left:6px;")
        self.stlb_flu_age_6569_led1.setFrame(False)
        self.stlb_flu_age_6569_led2 = QLineEdit(self.labeler_settings)
        self.stlb_flu_age_6569_led2.setObjectName(u"stlb_flu_age_6569_led2")
        self.stlb_flu_age_6569_led2.setGeometry(QRect(400, 320, 81, 30))
        self.stlb_flu_age_6569_led2.setMinimumSize(QSize(0, 30))
        self.stlb_flu_age_6569_led2.setMaximumSize(QSize(16777215, 30))
        self.stlb_flu_age_6569_led2.setFont(font56)
        self.stlb_flu_age_6569_led2.setStyleSheet(u"color: rgb(130, 135, 175);\n"
"background:transparent;\n"
"border-bottom:1px solid rgb(70,75,100);\n"
"padding-left:6px;")
        self.stlb_flu_age_6569_led2.setFrame(False)
        self.stlb_save_btn = QPushButton(self.labeler_settings)
        self.stlb_save_btn.setObjectName(u"stlb_save_btn")
        self.stlb_save_btn.setGeometry(QRect(380, 580, 141, 30))
        sizePolicy3.setHeightForWidth(self.stlb_save_btn.sizePolicy().hasHeightForWidth())
        self.stlb_save_btn.setSizePolicy(sizePolicy3)
        self.stlb_save_btn.setMinimumSize(QSize(0, 30))
        self.stlb_save_btn.setMaximumSize(QSize(16777215, 16777215))
        self.stlb_save_btn.setFont(font11)
        self.stlb_save_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(200, 200, 200);\n"
"	background-color:rgb(45,50,60);\n"
"	border-radius:10%;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(240,240,250);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.stlb_save_btn.setFlat(True)
        self.stlb_reset_btn = QPushButton(self.labeler_settings)
        self.stlb_reset_btn.setObjectName(u"stlb_reset_btn")
        self.stlb_reset_btn.setGeometry(QRect(290, 580, 81, 30))
        sizePolicy3.setHeightForWidth(self.stlb_reset_btn.sizePolicy().hasHeightForWidth())
        self.stlb_reset_btn.setSizePolicy(sizePolicy3)
        self.stlb_reset_btn.setMinimumSize(QSize(0, 30))
        self.stlb_reset_btn.setMaximumSize(QSize(16777215, 16777215))
        self.stlb_reset_btn.setFont(font11)
        self.stlb_reset_btn.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(160, 190, 150);\n"
"	background-color:rgb(45,50,60);\n"
"	border-radius:10%;\n"
"	border:1px solid rgb(50,55,70);\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(140,200,130);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(50,55,65);\n"
"}")
        self.stlb_reset_btn.setFlat(True)
        self.settings_stack.addWidget(self.labeler_settings)
        self.apps_stack.addWidget(self.settings)
        self.about = QWidget()
        self.about.setObjectName(u"about")
        self.about_te = QTextEdit(self.about)
        self.about_te.setObjectName(u"about_te")
        self.about_te.setGeometry(QRect(10, 20, 511, 611))
        self.about_te.setFont(font31)
        self.about_te.setStyleSheet(u"border:none;\n"
"border-bottom:1px solid rgb(50,55,60);")
        self.about_te.setReadOnly(True)
        self.apps_stack.addWidget(self.about)
        self.apps_about_btn = QPushButton(self.apps_gbx)
        self.apps_about_btn.setObjectName(u"apps_about_btn")
        self.apps_about_btn.setGeometry(QRect(410, 39, 120, 30))
        sizePolicy3.setHeightForWidth(self.apps_about_btn.sizePolicy().hasHeightForWidth())
        self.apps_about_btn.setSizePolicy(sizePolicy3)
        self.apps_about_btn.setMinimumSize(QSize(0, 30))
        self.apps_about_btn.setMaximumSize(QSize(16777215, 16777215))
        self.apps_about_btn.setFont(font2)
        self.apps_about_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(165, 170, 180);\n"
"	border:none;\n"
"}\n"
"QPushButton:hover {    \n"
"	color:rgb(125,175,225);\n"
"}\n"
"QPushButton:pressed {\n"
"	color:rgb(75,75,90);\n"
"}")
        self.apps_about_btn.setFlat(True)
        Main.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.lab_hb_led, self.lab_hct_led)
        QWidget.setTabOrder(self.lab_hct_led, self.lab_wbc_led)
        QWidget.setTabOrder(self.lab_wbc_led, self.lab_rbc_led)
        QWidget.setTabOrder(self.lab_rbc_led, self.lab_plt_led)
        QWidget.setTabOrder(self.lab_plt_led, self.lab_crp_led)
        QWidget.setTabOrder(self.lab_crp_led, self.lab_esr_led)
        QWidget.setTabOrder(self.lab_esr_led, self.lab_bun_led)
        QWidget.setTabOrder(self.lab_bun_led, self.lab_cr_led)
        QWidget.setTabOrder(self.lab_cr_led, self.lab_alb_led)
        QWidget.setTabOrder(self.lab_alb_led, self.lab_tpr_led)
        QWidget.setTabOrder(self.lab_tpr_led, self.lab_ast_led)
        QWidget.setTabOrder(self.lab_ast_led, self.lab_alt_led)
        QWidget.setTabOrder(self.lab_alt_led, self.lab_gtp_led)
        QWidget.setTabOrder(self.lab_gtp_led, self.lab_tbil_led)
        QWidget.setTabOrder(self.lab_tbil_led, self.lab_fbs_led)
        QWidget.setTabOrder(self.lab_fbs_led, self.lab_a1c_led)
        QWidget.setTabOrder(self.lab_a1c_led, self.lab_tc_led)
        QWidget.setTabOrder(self.lab_tc_led, self.lab_hdl_led)
        QWidget.setTabOrder(self.lab_hdl_led, self.lab_ldl_led)
        QWidget.setTabOrder(self.lab_ldl_led, self.lab_tg_led)
        QWidget.setTabOrder(self.lab_tg_led, self.lab_tsh_led)
        QWidget.setTabOrder(self.lab_tsh_led, self.lab_ft4_led)
        QWidget.setTabOrder(self.lab_ft4_led, self.lab_t3_led)
        QWidget.setTabOrder(self.lab_t3_led, self.lab_vitd_led)
        QWidget.setTabOrder(self.lab_vitd_led, self.lab_psa_led)
        QWidget.setTabOrder(self.lab_psa_led, self.lab_others_pte)
        QWidget.setTabOrder(self.lab_others_pte, self.lab_copy_btn)
        QWidget.setTabOrder(self.lab_copy_btn, self.bmd_date_led)
        QWidget.setTabOrder(self.bmd_date_led, self.bmd_inst_led)
        QWidget.setTabOrder(self.bmd_inst_led, self.bmd_lspine_tscore_led)
        QWidget.setTabOrder(self.bmd_lspine_tscore_led, self.bmd_femur_cmb)
        QWidget.setTabOrder(self.bmd_femur_cmb, self.bmd_femur_tscore_led)
        QWidget.setTabOrder(self.bmd_femur_tscore_led, self.bmd_others_pte)
        QWidget.setTabOrder(self.bmd_others_pte, self.bmd_copy_btn)
        QWidget.setTabOrder(self.bmd_copy_btn, self.alz_date_led)
        QWidget.setTabOrder(self.alz_date_led, self.alz_inst_led)
        QWidget.setTabOrder(self.alz_inst_led, self.alz_mmse_led)
        QWidget.setTabOrder(self.alz_mmse_led, self.alz_cdr_led)
        QWidget.setTabOrder(self.alz_cdr_led, self.alz_gds_led)
        QWidget.setTabOrder(self.alz_gds_led, self.alz_comm_pte)
        QWidget.setTabOrder(self.alz_comm_pte, self.alz_copy_btn)
        QWidget.setTabOrder(self.alz_copy_btn, self.ipss_date_led)
        QWidget.setTabOrder(self.ipss_date_led, self.ipss_inst_led)
        QWidget.setTabOrder(self.ipss_inst_led, self.ipss_1_cmb)
        QWidget.setTabOrder(self.ipss_1_cmb, self.ipss_2_cmb)
        QWidget.setTabOrder(self.ipss_2_cmb, self.ipss_3_cmb)
        QWidget.setTabOrder(self.ipss_3_cmb, self.ipss_4_cmb)
        QWidget.setTabOrder(self.ipss_4_cmb, self.ipss_5_cmb)
        QWidget.setTabOrder(self.ipss_5_cmb, self.ipss_6_cmb)
        QWidget.setTabOrder(self.ipss_6_cmb, self.ipss_7_cmb)
        QWidget.setTabOrder(self.ipss_7_cmb, self.ipss_copy_btn)
        QWidget.setTabOrder(self.ipss_copy_btn, self.lab_date_led)
        QWidget.setTabOrder(self.lab_date_led, self.lab_inst_led)
        QWidget.setTabOrder(self.lab_inst_led, self.macros_labeler_btn)
        QWidget.setTabOrder(self.macros_labeler_btn, self.macros_vac_input_btn)
        QWidget.setTabOrder(self.macros_vac_input_btn, self.macros_reserve_2_btn)
        QWidget.setTabOrder(self.macros_reserve_2_btn, self.macros_flu_btn)
        QWidget.setTabOrder(self.macros_flu_btn, self.macros_reserve_3_btn)
        QWidget.setTabOrder(self.macros_reserve_3_btn, self.macros_reserve_1_btn)
        QWidget.setTabOrder(self.macros_reserve_1_btn, self.macros_obsv_btn)
        QWidget.setTabOrder(self.macros_obsv_btn, self.macros_vac_log_btn)
        QWidget.setTabOrder(self.macros_vac_log_btn, self.info_title_lbl)
        QWidget.setTabOrder(self.info_title_lbl, self.apps_med_docs_btn)
        QWidget.setTabOrder(self.apps_med_docs_btn, self.apps_quick_saves_btn)
        QWidget.setTabOrder(self.apps_quick_saves_btn, self.apps_sticky_btn)
        QWidget.setTabOrder(self.apps_sticky_btn, self.apps_labeler_btn)
        QWidget.setTabOrder(self.apps_labeler_btn, self.apps_settings_btn)
        QWidget.setTabOrder(self.apps_settings_btn, self.apps_studies_btn)
        QWidget.setTabOrder(self.apps_studies_btn, self.apps_covid_btn)
        QWidget.setTabOrder(self.apps_covid_btn, self.qsv_lwg)
        QWidget.setTabOrder(self.qsv_lwg, self.qsv_copypaste_btn)
        QWidget.setTabOrder(self.qsv_copypaste_btn, self.qsv_delete_btn)
        QWidget.setTabOrder(self.qsv_delete_btn, self.qsv_new_btn)
        QWidget.setTabOrder(self.qsv_new_btn, self.mdoc_contents_pte)
        QWidget.setTabOrder(self.mdoc_contents_pte, self.mdoc_new_btn)
        QWidget.setTabOrder(self.mdoc_new_btn, self.mdoc_save_btn)
        QWidget.setTabOrder(self.mdoc_save_btn, self.mdoc_copy_btn)
        QWidget.setTabOrder(self.mdoc_copy_btn, self.mdoc_delete_btn)
        QWidget.setTabOrder(self.mdoc_delete_btn, self.mdoc_lwg)
        QWidget.setTabOrder(self.mdoc_lwg, self.studies_bmd_btn)
        QWidget.setTabOrder(self.studies_bmd_btn, self.studies_ipss_btn)
        QWidget.setTabOrder(self.studies_ipss_btn, self.studies_alz_btn)
        QWidget.setTabOrder(self.studies_alz_btn, self.studies_lab_btn)
        QWidget.setTabOrder(self.studies_lab_btn, self.calendar_day_options_btn)
        QWidget.setTabOrder(self.calendar_day_options_btn, self.calendar_day_info_lwg)
        QWidget.setTabOrder(self.calendar_day_info_lwg, self.calendar_day_month_lbl)
        QWidget.setTabOrder(self.calendar_day_month_lbl, self.calendar_yearly_btn)
        QWidget.setTabOrder(self.calendar_yearly_btn, self.calendar_next_month_btn)
        QWidget.setTabOrder(self.calendar_next_month_btn, self.calendar_opt_title)
        QWidget.setTabOrder(self.calendar_opt_title, self.calendar_day_info_led)
        QWidget.setTabOrder(self.calendar_day_info_led, self.reminders_title_lbl)
        QWidget.setTabOrder(self.reminders_title_lbl, self.reminders_lwg)
        QWidget.setTabOrder(self.reminders_lwg, self.calendar_select_end_date_btn)
        QWidget.setTabOrder(self.calendar_select_end_date_btn, self.calendar_opt_prev_month_btn)
        QWidget.setTabOrder(self.calendar_opt_prev_month_btn, self.calendar_today_btn)
        QWidget.setTabOrder(self.calendar_today_btn, self.calendar_opt_today_btn)
        QWidget.setTabOrder(self.calendar_opt_today_btn, self.calendar_multi_day_cbx)
        QWidget.setTabOrder(self.calendar_multi_day_cbx, self.calendar_prev_month_btn)
        QWidget.setTabOrder(self.calendar_prev_month_btn, self.calendar_opt_next_month_btn)
        QWidget.setTabOrder(self.calendar_opt_next_month_btn, self.reminders_archive_btn)
        QWidget.setTabOrder(self.reminders_archive_btn, self.reminders_new_led)
        QWidget.setTabOrder(self.reminders_new_led, self.calendar_opt_event_led)
        QWidget.setTabOrder(self.calendar_opt_event_led, self.reminders_clear_btn)
        QWidget.setTabOrder(self.reminders_clear_btn, self.macros_other_comments_btn)
        QWidget.setTabOrder(self.macros_other_comments_btn, self.macros_vac_autostart_btn)
        QWidget.setTabOrder(self.macros_vac_autostart_btn, self.reminders_sublist_clear_btn)
        QWidget.setTabOrder(self.reminders_sublist_clear_btn, self.reminders_sublist_delete_btn)
        QWidget.setTabOrder(self.reminders_sublist_delete_btn, self.reminders_sublist_item_led)
        QWidget.setTabOrder(self.reminders_sublist_item_led, self.reminders_archive_done_btn)
        QWidget.setTabOrder(self.reminders_archive_done_btn, self.reminders_archive_lwg)
        QWidget.setTabOrder(self.reminders_archive_lwg, self.macros_title_btn)
        QWidget.setTabOrder(self.macros_title_btn, self.reminders_archive_limit_cmb)
        QWidget.setTabOrder(self.reminders_archive_limit_cmb, self.macros_next_pt_btn)
        QWidget.setTabOrder(self.macros_next_pt_btn, self.macros_no_ins_btn)
        QWidget.setTabOrder(self.macros_no_ins_btn, self.macros_fluid_btn)
        QWidget.setTabOrder(self.macros_fluid_btn, self.macros_phytx_btn)
        QWidget.setTabOrder(self.macros_phytx_btn, self.macros_chr_btn)
        QWidget.setTabOrder(self.macros_chr_btn, self.macros_chr_etc_btn)
        QWidget.setTabOrder(self.macros_chr_etc_btn, self.macros_other_studies_btn)
        QWidget.setTabOrder(self.macros_other_studies_btn, self.macros_check_ins_btn)
        QWidget.setTabOrder(self.macros_check_ins_btn, self.macros_lab_studies_btn)
        QWidget.setTabOrder(self.macros_lab_studies_btn, self.lblr_count_total_covid_led)
        QWidget.setTabOrder(self.lblr_count_total_covid_led, self.lblr_count_old_flu_ex_led)
        QWidget.setTabOrder(self.lblr_count_old_flu_ex_led, self.lblr_count_child_flu_led)
        QWidget.setTabOrder(self.lblr_count_child_flu_led, self.lblr_count_total_flu_led)
        QWidget.setTabOrder(self.lblr_count_total_flu_led, self.lblr_count_md_led)
        QWidget.setTabOrder(self.lblr_count_md_led, self.lblr_count_old_flu_led)
        QWidget.setTabOrder(self.lblr_count_old_flu_led, self.lblr_count_pf_led)
        QWidget.setTabOrder(self.lblr_count_pf_led, self.lblr_count_edit_btn)
        QWidget.setTabOrder(self.lblr_count_edit_btn, self.lblr_info_lbl)
        QWidget.setTabOrder(self.lblr_info_lbl, self.lblr_vaccines_cmb)
        QWidget.setTabOrder(self.lblr_vaccines_cmb, self.lblr_print_btn)
        QWidget.setTabOrder(self.lblr_print_btn, self.lblr_get_data_btn)
        QWidget.setTabOrder(self.lblr_get_data_btn, self.lblr_reset_btn)
        QWidget.setTabOrder(self.lblr_reset_btn, self.c19r_sxsince_led)
        QWidget.setTabOrder(self.c19r_sxsince_led, self.c19r_underaged_cbx)
        QWidget.setTabOrder(self.c19r_underaged_cbx, self.c19r_ptphone_led)
        QWidget.setTabOrder(self.c19r_ptphone_led, self.c19r_address1_led)
        QWidget.setTabOrder(self.c19r_address1_led, self.c19r_ptjmno_led)
        QWidget.setTabOrder(self.c19r_ptjmno_led, self.c19r_notes_pte)
        QWidget.setTabOrder(self.c19r_notes_pte, self.c19r_address2_led)
        QWidget.setTabOrder(self.c19r_address2_led, self.c19r_doctor_led)
        QWidget.setTabOrder(self.c19r_doctor_led, self.c19r_symp_pte)
        QWidget.setTabOrder(self.c19r_symp_pte, self.c19r_ptname_led)
        QWidget.setTabOrder(self.c19r_ptname_led, self.c19r_dx_date_led)
        QWidget.setTabOrder(self.c19r_dx_date_led, self.c19r_adult_name_led)
        QWidget.setTabOrder(self.c19r_adult_name_led, self.c19r_report_btn)
        QWidget.setTabOrder(self.c19r_report_btn, self.c19r_system_login_btn)
        QWidget.setTabOrder(self.c19r_system_login_btn, self.c19r_reset_btn)
        QWidget.setTabOrder(self.c19r_reset_btn, self.settings_reserve_2_btn)
        QWidget.setTabOrder(self.settings_reserve_2_btn, self.settings_reserve_1_btn)
        QWidget.setTabOrder(self.settings_reserve_1_btn, self.settings_gen_btn)
        QWidget.setTabOrder(self.settings_gen_btn, self.settings_lblr_btn)
        QWidget.setTabOrder(self.settings_lblr_btn, self.stgn_auto_backup_btn)
        QWidget.setTabOrder(self.stgn_auto_backup_btn, self.stgn_messenger_btn)
        QWidget.setTabOrder(self.stgn_messenger_btn, self.stgn_auto_shutdown_btn)
        QWidget.setTabOrder(self.stgn_auto_shutdown_btn, self.stgn_auto_stats_btn)
        QWidget.setTabOrder(self.stgn_auto_stats_btn, self.stgn_cloud_sync_btn)
        QWidget.setTabOrder(self.stgn_cloud_sync_btn, self.stgn_vac_sys_log_btn)
        QWidget.setTabOrder(self.stgn_vac_sys_log_btn, self.stgn_auto_backup_led)
        QWidget.setTabOrder(self.stgn_auto_backup_led, self.stgn_auto_stats_led)
        QWidget.setTabOrder(self.stgn_auto_stats_led, self.stgn_cloud_sync_led)
        QWidget.setTabOrder(self.stgn_cloud_sync_led, self.stgn_messenger_server_pte)
        QWidget.setTabOrder(self.stgn_messenger_server_pte, self.stgn_save_btn)
        QWidget.setTabOrder(self.stgn_save_btn, self.stgn_reset_btn)
        QWidget.setTabOrder(self.stgn_reset_btn, self.stlb_flu_old_over75_start_led)
        QWidget.setTabOrder(self.stlb_flu_old_over75_start_led, self.stlb_flu_allow_ex_cbx)
        QWidget.setTabOrder(self.stlb_flu_allow_ex_cbx, self.stlb_flu_auto_sort_cbx)
        QWidget.setTabOrder(self.stlb_flu_auto_sort_cbx, self.stlb_flu_old_7074_start_led)
        QWidget.setTabOrder(self.stlb_flu_old_7074_start_led, self.stlb_flu_old_6569_start_led)
        QWidget.setTabOrder(self.stlb_flu_old_6569_start_led, self.stlb_child_flu_lot_led)
        QWidget.setTabOrder(self.stlb_child_flu_lot_led, self.stlb_flu_date_child_once_led1)
        QWidget.setTabOrder(self.stlb_flu_date_child_once_led1, self.stlb_flu_age_75over_led)
        QWidget.setTabOrder(self.stlb_flu_age_75over_led, self.stlb_auto_input_cbx)
        QWidget.setTabOrder(self.stlb_auto_input_cbx, self.stlb_flu_date_child_twice_led1)
        QWidget.setTabOrder(self.stlb_flu_date_child_twice_led1, self.stlb_flu_age_child_led1)
        QWidget.setTabOrder(self.stlb_flu_age_child_led1, self.stlb_auto_child_flu_lot_cbx)
        QWidget.setTabOrder(self.stlb_auto_child_flu_lot_cbx, self.stlb_flu_age_child_led2)
        QWidget.setTabOrder(self.stlb_flu_age_child_led2, self.stlb_flu_date_child_once_led2)
        QWidget.setTabOrder(self.stlb_flu_date_child_once_led2, self.stlb_flu_date_child_twice_led2)
        QWidget.setTabOrder(self.stlb_flu_date_child_twice_led2, self.stlb_flu_old_end_led)
        QWidget.setTabOrder(self.stlb_flu_old_end_led, self.stlb_flu_age_7074_led1)
        QWidget.setTabOrder(self.stlb_flu_age_7074_led1, self.stlb_flu_age_7074_led2)
        QWidget.setTabOrder(self.stlb_flu_age_7074_led2, self.stlb_flu_age_6569_led1)
        QWidget.setTabOrder(self.stlb_flu_age_6569_led1, self.stlb_flu_age_6569_led2)
        QWidget.setTabOrder(self.stlb_flu_age_6569_led2, self.calendar_opt_write_btn)
        QWidget.setTabOrder(self.calendar_opt_write_btn, self.calendar_yearly_lwg)
        QWidget.setTabOrder(self.calendar_yearly_lwg, self.calendar_yearly_done_btn)
        QWidget.setTabOrder(self.calendar_yearly_done_btn, self.calendar_yearly_next_btn)
        QWidget.setTabOrder(self.calendar_yearly_next_btn, self.calendar_yearly_year_led)
        QWidget.setTabOrder(self.calendar_yearly_year_led, self.calendar_yearly_prev_btn)
        QWidget.setTabOrder(self.calendar_yearly_prev_btn, self.mdoc_edit_btn)
        QWidget.setTabOrder(self.mdoc_edit_btn, self.stlb_reset_btn)
        QWidget.setTabOrder(self.stlb_reset_btn, self.stlb_save_btn)
        QWidget.setTabOrder(self.stlb_save_btn, self.sticky_note_0)
        QWidget.setTabOrder(self.sticky_note_0, self.sticky_note_1)
        QWidget.setTabOrder(self.sticky_note_1, self.sticky_note_2)
        QWidget.setTabOrder(self.sticky_note_2, self.sticky_note_3)
        QWidget.setTabOrder(self.sticky_note_3, self.sticky_note_4)
        QWidget.setTabOrder(self.sticky_note_4, self.sticky_note_5)
        QWidget.setTabOrder(self.sticky_note_5, self.calendar_opt_close_btn)
        QWidget.setTabOrder(self.calendar_opt_close_btn, self.reminders_sublist_close_btn)
        QWidget.setTabOrder(self.reminders_sublist_close_btn, self.reminders_sublist_write_btn)
        QWidget.setTabOrder(self.reminders_sublist_write_btn, self.reminders_sublist_reminder_led)
        QWidget.setTabOrder(self.reminders_sublist_reminder_led, self.reminders_sublist_lwg)
        QWidget.setTabOrder(self.reminders_sublist_lwg, self.lab_reset_btn)
        QWidget.setTabOrder(self.lab_reset_btn, self.bmd_reset_btn)
        QWidget.setTabOrder(self.bmd_reset_btn, self.macros_prev_pt_btn)
        QWidget.setTabOrder(self.macros_prev_pt_btn, self.alz_reset_btn)
        QWidget.setTabOrder(self.alz_reset_btn, self.macros_templates_btn)
        QWidget.setTabOrder(self.macros_templates_btn, self.ipss_reset_btn)
        QWidget.setTabOrder(self.ipss_reset_btn, self.lblr_flu_date_checker_old)
        QWidget.setTabOrder(self.lblr_flu_date_checker_old, self.lblr_flu_date_checker_child)

        self.retranslateUi(Main)

        self.calendar_stack.setCurrentIndex(0)
        self.reminders_stack.setCurrentIndex(1)
        self.apps_stack.setCurrentIndex(3)
        self.studies_stack.setCurrentIndex(3)
        self.settings_stack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"MainWindow", None))
        self.today_gbx.setTitle("")
        self.calendar_day_year_lbl.setText(QCoreApplication.translate("Main", u"2023", None))
        self.calendar_next_month_btn.setText(QCoreApplication.translate("Main", u">>", None))
        self.calendar_yearly_btn.setText(QCoreApplication.translate("Main", u"Yearly", None))
        self.calendar_day_options_btn.setText(QCoreApplication.translate("Main", u"Options", None))
        self.calendar_day_month_lbl.setText(QCoreApplication.translate("Main", u"May", None))
        self.calendar_day_name_lbl.setText(QCoreApplication.translate("Main", u"Wednesday", None))
        self.calendar_prev_month_btn.setText(QCoreApplication.translate("Main", u"<<", None))
        self.calendar_today_btn.setText(QCoreApplication.translate("Main", u"Today", None))
        self.calendar_day_info_led.setText("")
        self.calendar_day_date_lbl.setText(QCoreApplication.translate("Main", u"29", None))
        self.calednar_day_mont_year_lbl.setText(QCoreApplication.translate("Main", u"December, 2023", None))
        self.calendar_opt_title.setText(QCoreApplication.translate("Main", u"Events Add or Edit", None))
        self.calendar_opt_prev_month_btn.setText(QCoreApplication.translate("Main", u"<<", None))
        self.calendar_opt_month_year_lbl.setText(QCoreApplication.translate("Main", u"2024.01", None))
        self.calendar_opt_today_btn.setText(QCoreApplication.translate("Main", u"Today", None))
        self.calendar_opt_next_month_btn.setText(QCoreApplication.translate("Main", u">>", None))
        self.calendar_opt_event_led.setInputMask("")
        self.calendar_opt_event_led.setText("")
        self.calendar_event_date_title.setText(QCoreApplication.translate("Main", u"Event Date", None))
        self.calendar_event_date_dte.setDisplayFormat(QCoreApplication.translate("Main", u"yyyy-MM-dd (ddd)", None))
        self.calendar_multi_day_cbx.setText(QCoreApplication.translate("Main", u"Multi-day Event", None))
        self.calendar_select_end_date_btn.setText(QCoreApplication.translate("Main", u"Select End Date", None))
        self.calendar_start_date_lbl.setText(QCoreApplication.translate("Main", u"2024.01.31 (Wed)", None))
        self.calendar_from_to_lbl.setText(QCoreApplication.translate("Main", u"~", None))
        self.calendar_end_date_lbl.setText(QCoreApplication.translate("Main", u"2024.02.01 (Thu)", None))
        self.calendar_opt_write_btn.setText(QCoreApplication.translate("Main", u"Write", None))
        self.calendar_opt_close_btn.setText(QCoreApplication.translate("Main", u"Close", None))
        self.calendar_not_open_cbx.setText(QCoreApplication.translate("Main", u"NOT OPEN", None))
        self.calendar_event_delete_btn.setText(QCoreApplication.translate("Main", u"DELETE Event", None))
        self.calendar_yearly_done_btn.setText(QCoreApplication.translate("Main", u"DONE", None))
        self.calendar_yearly_year.setText(QCoreApplication.translate("Main", u"Year", None))
        self.calendar_yearly_next_btn.setText(QCoreApplication.translate("Main", u">>", None))
        self.calendar_yearly_year_led.setText(QCoreApplication.translate("Main", u"2023", None))
        self.calendar_yearly_prev_btn.setText(QCoreApplication.translate("Main", u"<<", None))
        self.calendar_yearly_title.setText(QCoreApplication.translate("Main", u"Yearly View", None))
        self.clock_led.setText(QCoreApplication.translate("Main", u"12:55", None))
        self.reminders_gbx.setTitle("")
        self.reminders_title_lbl.setText(QCoreApplication.translate("Main", u"Reminders", None))

        __sortingEnabled = self.reminders_lwg.isSortingEnabled()
        self.reminders_lwg.setSortingEnabled(False)
        ___qlistwidgetitem = self.reminders_lwg.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Main", u"[/] \ud558\uace0\uc788\uc2b4", None));
        ___qlistwidgetitem1 = self.reminders_lwg.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Main", u"[*] \uc911\uc694\ud574", None));
        ___qlistwidgetitem2 = self.reminders_lwg.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Main", u"[!] \ube68\ub9ac\ud574", None));
        ___qlistwidgetitem3 = self.reminders_lwg.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Main", u"[-] \ucde8\uc18c\ub418\uc538", None));
        ___qlistwidgetitem4 = self.reminders_lwg.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Main", u"[x] \ud588\uc5b4", None));
        ___qlistwidgetitem5 = self.reminders_lwg.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("Main", u"[v] \ud588\uc2ec", None));
        ___qlistwidgetitem6 = self.reminders_lwg.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("Main", u"[ ] \uc548\ub155\ud558\uc138\uc694 \uc774\uac83\uc800\uac83 \ud558\uc148 \\n    ::DUE 2023.03.02", None));
        ___qlistwidgetitem7 = self.reminders_lwg.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem8 = self.reminders_lwg.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem9 = self.reminders_lwg.item(9)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem10 = self.reminders_lwg.item(10)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem11 = self.reminders_lwg.item(11)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem12 = self.reminders_lwg.item(12)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem13 = self.reminders_lwg.item(13)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem14 = self.reminders_lwg.item(14)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem15 = self.reminders_lwg.item(15)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        self.reminders_lwg.setSortingEnabled(__sortingEnabled)

        self.reminders_archive_btn.setText(QCoreApplication.translate("Main", u"Archive", None))
        self.reminders_new_led.setText("")
        self.reminders_new_led.setPlaceholderText("")
        self.reminders_clear_btn.setText(QCoreApplication.translate("Main", u"Clear", None))
        self.reminders_star_btn.setText(QCoreApplication.translate("Main", u"*", None))
        self.reminders_ugnt_btn.setText(QCoreApplication.translate("Main", u"!", None))
        self.reminders_prgs_btn.setText(QCoreApplication.translate("Main", u"/", None))
        self.reminders_dlyd_btn.setText(QCoreApplication.translate("Main", u"?", None))
        self.reminders_todo_btn.setText("")
        self.reminders_status_lbl.setText(QCoreApplication.translate("Main", u"[ ]", None))
        self.reminders_done_btn.setText(QCoreApplication.translate("Main", u"x", None))
        self.reminders_canc_btn.setText(QCoreApplication.translate("Main", u"-", None))

        __sortingEnabled1 = self.reminders_sublist_lwg.isSortingEnabled()
        self.reminders_sublist_lwg.setSortingEnabled(False)
        ___qlistwidgetitem16 = self.reminders_sublist_lwg.item(0)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem17 = self.reminders_sublist_lwg.item(1)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem18 = self.reminders_sublist_lwg.item(2)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        self.reminders_sublist_lwg.setSortingEnabled(__sortingEnabled1)

        self.reminders_sublist_item_led.setText("")
        self.reminders_sublist_item_led.setPlaceholderText("")
        self.reminders_sublist_clear_btn.setText(QCoreApplication.translate("Main", u"Clear", None))
        self.reminders_sublist_delete_btn.setText(QCoreApplication.translate("Main", u"Delete", None))
        self.reminders_sublist_write_btn.setText(QCoreApplication.translate("Main", u"Write", None))
        self.reminders_sublist_close_btn.setText(QCoreApplication.translate("Main", u"Close", None))
        self.reminders_sublist_reminder_led.setText(QCoreApplication.translate("Main", u"\ud560\uc77c\ud588\uc18c\ub9cc...TO ME\ud5e4\ud5e4\ud5e4", None))
        self.reminders_sublist_due_cbx.setText(QCoreApplication.translate("Main", u"Due Date", None))
        self.reminders_sublist_due_dte.setDisplayFormat(QCoreApplication.translate("Main", u"yyyy-MM-dd(ddd)", None))
        self.reminders_sublist_todo_btn.setText("")
        self.reminders_sublist_prgs_btn.setText(QCoreApplication.translate("Main", u"/", None))
        self.reminders_sublist_ugnt_btn.setText(QCoreApplication.translate("Main", u"!", None))
        self.reminders_sublist_star_btn.setText(QCoreApplication.translate("Main", u"*", None))
        self.reminders_sublist_dlyd_btn.setText(QCoreApplication.translate("Main", u"?", None))
        self.reminders_sublist_reminder_delete_btn.setText(QCoreApplication.translate("Main", u"DELETE Reminder", None))
        self.reminders_sublist_rem_status_btn.setText(QCoreApplication.translate("Main", u"[ ]", None))
        self.reminders_sublist_done_btn.setText(QCoreApplication.translate("Main", u"x", None))
        self.reminders_sublist_canc_btn.setText(QCoreApplication.translate("Main", u"-", None))
        self.reminders_sublist_status_lbl.setText(QCoreApplication.translate("Main", u"[ ]", None))
        self.reminders_sublist_done_canc_dte.setDisplayFormat(QCoreApplication.translate("Main", u"yyyy-MM-dd(ddd)", None))
        self.reminders_sublist_done_canc_lbl.setText(QCoreApplication.translate("Main", u"CANCELLED", None))
        self.reminders_archive_done_btn.setText(QCoreApplication.translate("Main", u"DONE", None))
        self.reminders_archive_title.setText(QCoreApplication.translate("Main", u"Archives", None))
        self.reminders_archive_limit_cmb.setItemText(0, QCoreApplication.translate("Main", u"Select", None))
        self.reminders_archive_limit_cmb.setItemText(1, QCoreApplication.translate("Main", u"10", None))
        self.reminders_archive_limit_cmb.setItemText(2, QCoreApplication.translate("Main", u"25", None))
        self.reminders_archive_limit_cmb.setItemText(3, QCoreApplication.translate("Main", u"50", None))
        self.reminders_archive_limit_cmb.setItemText(4, QCoreApplication.translate("Main", u"100", None))

        self.reminders_archive_limit_lbl.setText(QCoreApplication.translate("Main", u"Recently DONE or CANCELLED Reminders", None))
        self.reminders_history_btn.setText(QCoreApplication.translate("Main", u"History", None))
        self.macros_gbx.setTitle("")
        self.macros_title_btn.setText(QCoreApplication.translate("Main", u"Macros", None))
        self.macros_prev_pt_btn.setText(QCoreApplication.translate("Main", u"\uc9c1\uc804\ud658\uc790", None))
        self.macros_check_ins_btn.setText(QCoreApplication.translate("Main", u"\uc790\uaca9\uc870\ud68c", None))
        self.macros_no_ins_btn.setText(QCoreApplication.translate("Main", u"\ube44\ubcf4\ud5d8", None))
        self.macros_next_pt_btn.setText(QCoreApplication.translate("Main", u"\ub2e4\uc74c\ud658\uc790", None))
        self.macros_phytx_btn.setText(QCoreApplication.translate("Main", u"\ubb3c\ub9ac\uce58\ub8cc", None))
        self.macros_fluid_btn.setText(QCoreApplication.translate("Main", u"\uc218\uc561\uce58\ub8cc", None))
        self.macros_chr_btn.setText(QCoreApplication.translate("Main", u"\ub9cc\uc131\uc9c8\ud658 \uad00\ub9ac", None))
        self.macros_chr_etc_btn.setText(QCoreApplication.translate("Main", u"\ub9cc\uc131\uc9c8\ud658 \uae30\ud0c0", None))
        self.macros_lab_studies_btn.setText(QCoreApplication.translate("Main", u"\ud608\uc561\uac80\uc0ac \uad00\ub828", None))
        self.macros_other_studies_btn.setText(QCoreApplication.translate("Main", u"\uae30\ud0c0\uac80\uc0ac \uad00\ub828", None))
        self.macros_templates_btn.setText(QCoreApplication.translate("Main", u"\ucc28\ud305 Templates", None))
        self.macros_other_comments_btn.setText(QCoreApplication.translate("Main", u"\uae30\ud0c0 \ucf54\uba58\ud2b8\ub4e4 \ubaa8\uc74c", None))
        self.macros_vac_autostart_btn.setText(QCoreApplication.translate("Main", u"\uc811\uc885\uc2dc\uc2a4\ud15c \uc2dc\uc791", None))
        self.macros_labeler_btn.setText(QCoreApplication.translate("Main", u"Labeler \uc785\ub825", None))
        self.macros_vac_input_btn.setText(QCoreApplication.translate("Main", u"\uc811\uc885\uc2dc\uc2a4\ud15c \uc785\ub825", None))
        self.macros_practive_title_lbl.setText(QCoreApplication.translate("Main", u"\uc9c4\ub8cc \uad00\ub828", None))
        self.macros_comments_title_lbl.setText(QCoreApplication.translate("Main", u"\ucf54\uba58\ud2b8 \ubaa8\uc74c", None))
        self.macros_vac_title_lbl.setText(QCoreApplication.translate("Main", u"\uc608\ubc29\uc811\uc885 \uad00\ub828", None))
        self.macros_reserve_2_btn.setText("")
        self.macros_flu_btn.setText(QCoreApplication.translate("Main", u"\uc778\ud50c\ub8e8\uc5d4\uc790", None))
        self.macros_reserve_3_btn.setText("")
        self.macros_reserve_1_btn.setText(QCoreApplication.translate("Main", u"Covid-19", None))
        self.macros_others_title_lbl.setText(QCoreApplication.translate("Main", u"\uae30\ud0c0 Macros", None))
        self.macros_obsv_btn.setText(QCoreApplication.translate("Main", u"\ub9ac\ud53c\ud2b8 \ucc98\ubc29 \ubc0f \uacbd\uacfc\uad00\ucc30", None))
        self.macros_vac_log_btn.setText(QCoreApplication.translate("Main", u"\ub85c\uadf8\uc544\uc6c3 \uc5f0\uc7a5", None))
        self.info_gbx.setTitle("")
        self.info_zinsss_lbl.setText(QCoreApplication.translate("Main", u"by zinsss @ \uc601\ud574 \uc120\ud55c \uac00\uc815\uc758\ud559\uacfc\uc758\uc6d0", None))
        self.info_not_for_sale_lbl.setText(QCoreApplication.translate("Main", u" eGhis Assistant is Not For Sale nor Distribution", None))
        self.info_title_lbl.setText(QCoreApplication.translate("Main", u"Information", None))
        self.info_yhshfm_address_lbl.setText(QCoreApplication.translate("Main", u"\uacbd\ubd81 \uc601\ub355\uad70 \uc601\ud574\uba74 \uc608\uc8fc\uc2dc\uc7a5\uae38 43-1 1\uce35", None))
        self.apps_gbx.setTitle("")
        self.apps_med_docs_btn.setText(QCoreApplication.translate("Main", u"Med. Docs", None))
        self.apps_quick_saves_btn.setText(QCoreApplication.translate("Main", u"Quick Saves", None))
        self.apps_sticky_btn.setText(QCoreApplication.translate("Main", u"Sticky Notes", None))
        self.apps_labeler_btn.setText(QCoreApplication.translate("Main", u"Labeler", None))
        self.apps_settings_btn.setText(QCoreApplication.translate("Main", u"Settings", None))
        self.apps_studies_btn.setText(QCoreApplication.translate("Main", u"Studies", None))
        self.apps_covid_btn.setText(QCoreApplication.translate("Main", u"Covid-19", None))
        self.sticky_note_0.setText(QCoreApplication.translate("Main", u"# \uacbd\ubd81\uc57d\uad6d\n"
"\n"
"\ud2b8\ub77c\ub9c8\ub864\uc138\ubbf8\uc11c\ubc29\uc815\n"
"\ud2b8\ub77c\ub9c8\ub864\uc11c\ubc29\uc815\n"
"\n"
"\ud0c0\ubbf8\ud50c\ub8e8 >> \ud0c0\ubbf8\ube44\uc5b4", None))
        self.sticky_note_3.setText("")
        self.sticky_note_2.setText("")
        self.sticky_note_1.setText("")
        self.sticky_note_4.setText("")
        self.sticky_note_5.setText("")

        __sortingEnabled2 = self.qsv_lwg.isSortingEnabled()
        self.qsv_lwg.setSortingEnabled(False)
        ___qlistwidgetitem19 = self.qsv_lwg.item(0)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem20 = self.qsv_lwg.item(1)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem21 = self.qsv_lwg.item(2)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem22 = self.qsv_lwg.item(3)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem23 = self.qsv_lwg.item(4)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem24 = self.qsv_lwg.item(5)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        self.qsv_lwg.setSortingEnabled(__sortingEnabled2)

        self.qsv_copypaste_btn.setText(QCoreApplication.translate("Main", u"Copy to Clipboard", None))
        self.qsv_delete_btn.setText(QCoreApplication.translate("Main", u"Delete", None))
        self.qsv_new_btn.setText(QCoreApplication.translate("Main", u"New", None))
        self.mdoc_contents_pte.setPlainText(QCoreApplication.translate("Main", u"\uc0c1\uae30\ub3c4\uac10\uc5fc\uc99d\uc138\ub97c\uc8fc\uc18c\ub85c\ub0b4\uc6d0\ud55c\ubc14\ubcf4\uac19\uc740\ub4f1\uc2e0\ud658\uc790\uc785\ub2c8\ub2e4\ub561\ub561\uc774\uac00\uc758\uc2ec\ub418\uc624\ub2c8\uc870\uce58\uac00", None))
        self.mdoc_new_btn.setText(QCoreApplication.translate("Main", u"New", None))
        self.mdoc_save_btn.setText(QCoreApplication.translate("Main", u"Save", None))
        self.mdoc_copy_btn.setText(QCoreApplication.translate("Main", u"Copy to Clipboard", None))
        self.mdoc_delete_btn.setText(QCoreApplication.translate("Main", u"Delete", None))

        __sortingEnabled3 = self.mdoc_lwg.isSortingEnabled()
        self.mdoc_lwg.setSortingEnabled(False)
        ___qlistwidgetitem25 = self.mdoc_lwg.item(0)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem26 = self.mdoc_lwg.item(1)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem27 = self.mdoc_lwg.item(2)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem28 = self.mdoc_lwg.item(3)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem29 = self.mdoc_lwg.item(4)
        ___qlistwidgetitem29.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem30 = self.mdoc_lwg.item(5)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem31 = self.mdoc_lwg.item(6)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem32 = self.mdoc_lwg.item(7)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem33 = self.mdoc_lwg.item(8)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem34 = self.mdoc_lwg.item(9)
        ___qlistwidgetitem34.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem35 = self.mdoc_lwg.item(10)
        ___qlistwidgetitem35.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem36 = self.mdoc_lwg.item(11)
        ___qlistwidgetitem36.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem37 = self.mdoc_lwg.item(12)
        ___qlistwidgetitem37.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        ___qlistwidgetitem38 = self.mdoc_lwg.item(13)
        ___qlistwidgetitem38.setText(QCoreApplication.translate("Main", u"\uc0c8 \ud56d\ubaa9", None));
        self.mdoc_lwg.setSortingEnabled(__sortingEnabled3)

        self.mdoc_edit_btn.setText(QCoreApplication.translate("Main", u"Edit", None))
        self.mdoc_title_led.setText(QCoreApplication.translate("Main", u"[\ud559\uc0dd] \uc0c1\uae30\ub3c4 \uac10\uc5fc", None))
        self.mdoc_title_led.setPlaceholderText("")
        self.studies_bmd_btn.setText(QCoreApplication.translate("Main", u"BMD", None))
        self.studies_ipss_btn.setText(QCoreApplication.translate("Main", u"IPSS", None))
        self.studies_alz_btn.setText(QCoreApplication.translate("Main", u"Dementia", None))
        self.studies_lab_btn.setText(QCoreApplication.translate("Main", u"Lab Results", None))
        self.lab_hct_lbl.setText(QCoreApplication.translate("Main", u"Hct", None))
        self.lab_hb_lbl.setText(QCoreApplication.translate("Main", u"Hb", None))
        self.lab_hct_led.setText(QCoreApplication.translate("Main", u"45", None))
        self.lab_cbc_title_lbl.setText(QCoreApplication.translate("Main", u"CBC", None))
        self.lab_wbc_lbl.setText(QCoreApplication.translate("Main", u"WBC", None))
        self.lab_plt_lbl.setText(QCoreApplication.translate("Main", u"Plt", None))
        self.lab_hb_led.setText(QCoreApplication.translate("Main", u"14.5", None))
        self.lab_rbc_lbl.setText(QCoreApplication.translate("Main", u"RBC", None))
        self.lab_tsh_lbl.setText(QCoreApplication.translate("Main", u"TSH", None))
        self.lab_ft4_lbl.setText(QCoreApplication.translate("Main", u"fT4", None))
        self.lab_dm_studies_title_lbl.setText(QCoreApplication.translate("Main", u"DM", None))
        self.lab_a1c_lbl.setText(QCoreApplication.translate("Main", u"A1c", None))
        self.lab_t3_lbl.setText(QCoreApplication.translate("Main", u"T3", None))
        self.lab_fbs_lbl.setText(QCoreApplication.translate("Main", u"FBS", None))
        self.lab_tft_title_lbl.setText(QCoreApplication.translate("Main", u"TFT", None))
        self.lab_renal_title_lbl.setText(QCoreApplication.translate("Main", u"Renal.F", None))
        self.lab_cr_lbl.setText(QCoreApplication.translate("Main", u"Cr", None))
        self.lab_bun_lbl.setText(QCoreApplication.translate("Main", u"BUN", None))
        self.lab_psa_lbl.setText(QCoreApplication.translate("Main", u"PSA", None))
        self.lab_hdl_lbl.setText(QCoreApplication.translate("Main", u"HDL", None))
        self.lab_alt_lbl.setText(QCoreApplication.translate("Main", u"ALT", None))
        self.lab_lft_title_lbl.setText(QCoreApplication.translate("Main", u"LFT", None))
        self.lab_tpr_lbl.setText(QCoreApplication.translate("Main", u"t.Pr", None))
        self.lab_gtp_lbl.setText(QCoreApplication.translate("Main", u"GTP", None))
        self.lab_tbil_lbl.setText(QCoreApplication.translate("Main", u"T.bil", None))
        self.lab_tc_lbl.setText(QCoreApplication.translate("Main", u"T.C", None))
        self.lab_vitd_lbl.setText(QCoreApplication.translate("Main", u"VitD", None))
        self.lab_alb_lbl.setText(QCoreApplication.translate("Main", u"Alb", None))
        self.lab_crp_lbl.setText(QCoreApplication.translate("Main", u"CRP", None))
        self.lab_esr_lbl.setText(QCoreApplication.translate("Main", u"ESR", None))
        self.lab_tg_lbl.setText(QCoreApplication.translate("Main", u"TG", None))
        self.lab_ast_lbl.setText(QCoreApplication.translate("Main", u"AST", None))
        self.lab_lipids_title_lbl.setText(QCoreApplication.translate("Main", u"Lipids", None))
        self.lab_ldl_lbl.setText(QCoreApplication.translate("Main", u"LDL", None))
        self.lab_etc_title_lbl.setText(QCoreApplication.translate("Main", u"ETC", None))
        self.lab_inflm_title_lbl.setText(QCoreApplication.translate("Main", u"Inflm.M.", None))
        self.lab_others_title_lbl.setText(QCoreApplication.translate("Main", u"Other Studies", None))
        self.lab_others_pte.setPlainText("")
        self.lab_inst_lbl.setText(QCoreApplication.translate("Main", u"\uae30\uad00", None))
        self.lab_date_lbl.setText(QCoreApplication.translate("Main", u"\ub0a0\uc9dc", None))
        self.lab_date_led.setText(QCoreApplication.translate("Main", u"20221010", None))
        self.lab_inst_led.setText(QCoreApplication.translate("Main", u"\uc601\ub355\uc544\uc0b0\ubcd1\uc6d0", None))
        self.lab_title_lbl.setText(QCoreApplication.translate("Main", u"Lab Results", None))
        self.lab_copy_btn.setText(QCoreApplication.translate("Main", u"Copy to Clipboard", None))
        self.lab_reset_btn.setText(QCoreApplication.translate("Main", u"Reset", None))
        self.bmd_lspine_tscore_led.setText("")
        self.bmd_inst_lbl.setText(QCoreApplication.translate("Main", u"\uae30\uad00", None))
        self.bmd_inst_led.setText(QCoreApplication.translate("Main", u"\uc601\ub355\uc544\uc0b0\ubcd1\uc6d0", None))
        self.bmd_dexxa_title_lbl.setText(QCoreApplication.translate("Main", u"Central DEXXA", None))
        self.bmd_femur_tscore_led.setText("")
        self.bmd_date_led.setText(QCoreApplication.translate("Main", u"20221010", None))
        self.bmd_others_title_lbl.setText(QCoreApplication.translate("Main", u"Comments or Other Modalities", None))
        self.bmd_femur_cmb.setItemText(0, QCoreApplication.translate("Main", u"Lt. Femur", None))
        self.bmd_femur_cmb.setItemText(1, QCoreApplication.translate("Main", u"Rt. Femur", None))

        self.bmd_date_lbl.setText(QCoreApplication.translate("Main", u"\ub0a0\uc9dc", None))
        self.bmd_lspine_lbl.setText(QCoreApplication.translate("Main", u"L-Spine", None))
        self.bmd_others_pte.setPlainText("")
        self.bmd_box_lbl.setText("")
        self.bmd_title_lbl.setText(QCoreApplication.translate("Main", u"Bone Marrow Density", None))
        self.bmd_copy_btn.setText(QCoreApplication.translate("Main", u"Copy to Clipboard", None))
        self.bmd_reset_btn.setText(QCoreApplication.translate("Main", u"Reset", None))
        self.alz_inst_led.setText(QCoreApplication.translate("Main", u"\uc601\ub355\uc544\uc0b0\ubcd1\uc6d0", None))
        self.alz_mmse_led.setText("")
        self.alz_fx_studies_title_lbl.setText(QCoreApplication.translate("Main", u"Functional Studies", None))
        self.alz_cdr_lbl.setText(QCoreApplication.translate("Main", u"CDR:", None))
        self.alz_date_led.setText(QCoreApplication.translate("Main", u"20221010", None))
        self.alz_cdr_led.setText("")
        self.alz_comm_title_lbl.setText(QCoreApplication.translate("Main", u"Comments or Other Modalities", None))
        self.alz_date_lbl.setText(QCoreApplication.translate("Main", u"\ub0a0\uc9dc", None))
        self.alz_box_lbl.setText("")
        self.alz_inst_lbl.setText(QCoreApplication.translate("Main", u"\uae30\uad00", None))
        self.alz_mmse_lbl.setText(QCoreApplication.translate("Main", u"MMSE:", None))
        self.alz_comm_pte.setPlainText("")
        self.alz_gds_led.setText("")
        self.alz_gds_lbl.setText(QCoreApplication.translate("Main", u"GDS:", None))
        self.alz_title_lbl.setText(QCoreApplication.translate("Main", u"Alzheimer and Other Dementia", None))
        self.alz_reset_btn.setText(QCoreApplication.translate("Main", u"Reset", None))
        self.alz_copy_btn.setText(QCoreApplication.translate("Main", u"Copy to Clipboard", None))
        self.ipss_scr_2_5i.setText(QCoreApplication.translate("Main", u">5", None))
        self.ipss_scr_2_2i.setText(QCoreApplication.translate("Main", u"2\ubc88", None))
        self.ipss_scr_2_5.setText(QCoreApplication.translate("Main", u"5", None))
        self.ipss_scr_2_3i.setText(QCoreApplication.translate("Main", u"3\ubc88", None))
        self.ipss_scr_2_1.setText(QCoreApplication.translate("Main", u"1", None))
        self.ipss_scr_2_0i.setText(QCoreApplication.translate("Main", u"\uc5c6\uc74c", None))
        self.ipss_scr_2_2.setText(QCoreApplication.translate("Main", u"2", None))
        self.ipss_scr_2_1i.setText(QCoreApplication.translate("Main", u"1\ubc88", None))
        self.ipss_scr_2_3.setText(QCoreApplication.translate("Main", u"3", None))
        self.ipss_scr_2_0.setText(QCoreApplication.translate("Main", u"0", None))
        self.ipss_scr_2_4i.setText(QCoreApplication.translate("Main", u"4\ubc88", None))
        self.ipss_scr_2_4.setText(QCoreApplication.translate("Main", u"4", None))
        self.ipss_date_lbl.setText(QCoreApplication.translate("Main", u"\ub0a0\uc9dc", None))
        self.ipss_1_cmb.setItemText(0, "")
        self.ipss_1_cmb.setItemText(1, QCoreApplication.translate("Main", u"0", None))
        self.ipss_1_cmb.setItemText(2, QCoreApplication.translate("Main", u"1", None))
        self.ipss_1_cmb.setItemText(3, QCoreApplication.translate("Main", u"2", None))
        self.ipss_1_cmb.setItemText(4, QCoreApplication.translate("Main", u"3", None))
        self.ipss_1_cmb.setItemText(5, QCoreApplication.translate("Main", u"4", None))
        self.ipss_1_cmb.setItemText(6, QCoreApplication.translate("Main", u"5", None))

        self.ipss_inst_led.setText(QCoreApplication.translate("Main", u"\uc601\ub355\uc544\uc0b0\ubcd1\uc6d0", None))
        self.ipss_3_cmb.setItemText(0, "")
        self.ipss_3_cmb.setItemText(1, QCoreApplication.translate("Main", u"0", None))
        self.ipss_3_cmb.setItemText(2, QCoreApplication.translate("Main", u"1", None))
        self.ipss_3_cmb.setItemText(3, QCoreApplication.translate("Main", u"2", None))
        self.ipss_3_cmb.setItemText(4, QCoreApplication.translate("Main", u"3", None))
        self.ipss_3_cmb.setItemText(5, QCoreApplication.translate("Main", u"4", None))
        self.ipss_3_cmb.setItemText(6, QCoreApplication.translate("Main", u"5", None))

        self.ipss_6_lbl.setText(QCoreApplication.translate("Main", u"6. \ud3c9\uc18c \uc18c\ubcc0\uc774 \uae08\ubc29 \ub098\uc624\uc9c0 \uc54a\uc544 \ubc30\uc5d0 \ud798\uc744 \uc8fc\uc5b4\uc57c \ud558\ub294 \uacbd\uc6b0\uac00 \uc788\uc2b5\ub2c8\uae4c?", None))
        self.ipss_2_cmb.setItemText(0, "")
        self.ipss_2_cmb.setItemText(1, QCoreApplication.translate("Main", u"0", None))
        self.ipss_2_cmb.setItemText(2, QCoreApplication.translate("Main", u"1", None))
        self.ipss_2_cmb.setItemText(3, QCoreApplication.translate("Main", u"2", None))
        self.ipss_2_cmb.setItemText(4, QCoreApplication.translate("Main", u"3", None))
        self.ipss_2_cmb.setItemText(5, QCoreApplication.translate("Main", u"4", None))
        self.ipss_2_cmb.setItemText(6, QCoreApplication.translate("Main", u"5", None))

        self.ipss_7_lbl.setText(QCoreApplication.translate("Main", u"7. \ud3c9\uade0\uc801\uc73c\ub85c \uc790\ub2e4 \uc77c\uc5b4\ub098\uc11c \uc18c\ubcc0\uc744 \ubcf4\ub294\uacbd\uc6b0\uac00 \uba87\ubc88\uc785\ub2c8\uae4c?", None))
        self.ipss_3_lbl.setText(QCoreApplication.translate("Main", u"3. \ud3c9\uc18c \uc18c\ubcc0\uc744 \ubcf4\ub294 \ub3c4\uc911\uc5d0 \uc18c\ubcc0\uc904\uae30\uac00 \ub04a\uc5b4\uc9c0\ub294 \uacbd\uc6b0\uac00 \uc788\uc2b5\ub2c8\uae4c?", None))
        self.ipss_4_cmb.setItemText(0, "")
        self.ipss_4_cmb.setItemText(1, QCoreApplication.translate("Main", u"0", None))
        self.ipss_4_cmb.setItemText(2, QCoreApplication.translate("Main", u"1", None))
        self.ipss_4_cmb.setItemText(3, QCoreApplication.translate("Main", u"2", None))
        self.ipss_4_cmb.setItemText(4, QCoreApplication.translate("Main", u"3", None))
        self.ipss_4_cmb.setItemText(5, QCoreApplication.translate("Main", u"4", None))
        self.ipss_4_cmb.setItemText(6, QCoreApplication.translate("Main", u"5", None))

        self.ipss_5_cmb.setItemText(0, "")
        self.ipss_5_cmb.setItemText(1, QCoreApplication.translate("Main", u"0", None))
        self.ipss_5_cmb.setItemText(2, QCoreApplication.translate("Main", u"1", None))
        self.ipss_5_cmb.setItemText(3, QCoreApplication.translate("Main", u"2", None))
        self.ipss_5_cmb.setItemText(4, QCoreApplication.translate("Main", u"3", None))
        self.ipss_5_cmb.setItemText(5, QCoreApplication.translate("Main", u"4", None))
        self.ipss_5_cmb.setItemText(6, QCoreApplication.translate("Main", u"5", None))

        self.ipss_7_cmb.setItemText(0, "")
        self.ipss_7_cmb.setItemText(1, QCoreApplication.translate("Main", u"0", None))
        self.ipss_7_cmb.setItemText(2, QCoreApplication.translate("Main", u"1", None))
        self.ipss_7_cmb.setItemText(3, QCoreApplication.translate("Main", u"2", None))
        self.ipss_7_cmb.setItemText(4, QCoreApplication.translate("Main", u"3", None))
        self.ipss_7_cmb.setItemText(5, QCoreApplication.translate("Main", u"4", None))
        self.ipss_7_cmb.setItemText(6, QCoreApplication.translate("Main", u"5", None))

        self.ipss_inst_lbl.setText(QCoreApplication.translate("Main", u"\uae30\uad00", None))
        self.ipss_5_lbl.setText(QCoreApplication.translate("Main", u"5. \ud3c9\uc18c \uc18c\ubcc0 \uc904\uae30\uac00 \uc57d\ud558\uac70\ub098 \uc57d\ud558\ub2e4\uace0 \ub290\ub080 \uacbd\uc6b0\uac00 \uc788\uc2b5\ub2c8\uae4c?", None))
        self.ipss_date_led.setText(QCoreApplication.translate("Main", u"20221010", None))
        self.ipss_6_cmb.setItemText(0, "")
        self.ipss_6_cmb.setItemText(1, QCoreApplication.translate("Main", u"0", None))
        self.ipss_6_cmb.setItemText(2, QCoreApplication.translate("Main", u"1", None))
        self.ipss_6_cmb.setItemText(3, QCoreApplication.translate("Main", u"2", None))
        self.ipss_6_cmb.setItemText(4, QCoreApplication.translate("Main", u"3", None))
        self.ipss_6_cmb.setItemText(5, QCoreApplication.translate("Main", u"4", None))
        self.ipss_6_cmb.setItemText(6, QCoreApplication.translate("Main", u"5", None))

        self.ipss_2_lbl.setText(QCoreApplication.translate("Main", u"2. \ud3c9\uc18c \uc18c\ubcc0\uc744 \ubcf4\uace0 2\uc2dc\uac04 \uc774\ub0b4 \ub2e4\uc2dc \ubcf4\ub294 \uacbd\uc6b0\uac00 \uc788\uc2b5\ub2c8\uae4c?", None))
        self.ipss_1_lbl.setText(QCoreApplication.translate("Main", u"1. \ud3c9\uc18c \uc18c\ubcc0\uc744 \ubcf4\uace0\ub3c4 \ub0a8\uc544\uc788\ub294\uac83 \uac19\uc740 \ub290\ub08c\uc744 \ub290\ub07c\ub294 \uacbd\uc6b0\uac00 \uc788\uc2b5\ub2c8\uae4c?", None))
        self.ipss_4_lbl.setText(QCoreApplication.translate("Main", u"4. \ud3c9\uc18c\uc5d0 \uc18c\ubcc0\uc744 \ucc38\uae30 \uc5b4\ub824\uc6b4 \uacbd\uc6b0\uac00 \uc788\uc2b5\ub2c8\uae4c?", None))
        self.ipss_scr_1_2i.setText(QCoreApplication.translate("Main", u"1~2/5", None))
        self.ipss_scr_1_1.setText(QCoreApplication.translate("Main", u"1", None))
        self.ipss_scr_1_2.setText(QCoreApplication.translate("Main", u"2", None))
        self.ipss_scr_1_0.setText(QCoreApplication.translate("Main", u"0", None))
        self.ipss_scr_1_5.setText(QCoreApplication.translate("Main", u"5", None))
        self.ipss_scr_1_0i.setText(QCoreApplication.translate("Main", u"\uc5c6\uc74c", None))
        self.ipss_scr_1_4i.setText(QCoreApplication.translate("Main", u"3~4/5", None))
        self.ipss_scr_1_5i.setText(QCoreApplication.translate("Main", u"\ud56d\uc0c1", None))
        self.ipss_scr_1_3i.setText(QCoreApplication.translate("Main", u"2~3/5", None))
        self.ipss_scr_1_3.setText(QCoreApplication.translate("Main", u"3", None))
        self.ipss_scr_1_1i.setText(QCoreApplication.translate("Main", u"~1/5", None))
        self.ipss_scr_1_4.setText(QCoreApplication.translate("Main", u"4", None))
        self.ipss_title_lbl.setText(QCoreApplication.translate("Main", u"IPSS Survey", None))
        self.ipss_reset_btn.setText(QCoreApplication.translate("Main", u"Reset", None))
        self.ipss_copy_btn.setText(QCoreApplication.translate("Main", u"Copy to Clipboard", None))
        self.lblr_count_gbx.setTitle("")
        self.lblr_count_old_flu_ex_led.setText("")
        self.lblr_count_total_covid_lbl.setText(QCoreApplication.translate("Main", u"\ucd1d \ucf54\ub85c\ub098", None))
        self.lblr_count_child_flu_lbl.setText(QCoreApplication.translate("Main", u"\uc18c\uc544\ub3c5\uac10", None))
        self.lblr_count_old_flu_lbl.setText(QCoreApplication.translate("Main", u"\ub178\uc778\ub3c5\uac10", None))
        self.lblr_count_old_flu_ex_lbl.setText(QCoreApplication.translate("Main", u"\ub178\uc778.\uc608\uc678", None))
        self.lblr_count_pf_lbl.setText(QCoreApplication.translate("Main", u"\ud654\uc774\uc790XBB1.5", None))
        self.lblr_count_total_flu_lbl.setText(QCoreApplication.translate("Main", u"\ucd1d \ub3c5\uac10", None))
        self.lblr_count_md_lbl.setText(QCoreApplication.translate("Main", u"\ubaa8\ub354\ub098XBB1.5", None))
        self.lblr_count_edit_btn.setText(QCoreApplication.translate("Main", u"Edit", None))
        self.lblr_count_title_lbl.setText(QCoreApplication.translate("Main", u"\ubc31\uc2e0 \uce74\uc6b4\ud130", None))
        self.lblr_info_lbl.setHtml(QCoreApplication.translate("Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\uc11c\uc6b8\ud55c\uac15 \uc7a5\uccb4 M'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#798aaa;\">### Labeler \uc548\ub0b4 ###</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#64728c;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#64728c;\">\uac1c\uc778\uc815\ubcf4 \ubcf4\ud638 \ubc95\ub960\uacfc \uad00\ub828"
                        "\ud558\uc5ec eA Labeler\ub294 eGhis \uc804\uc790\ucc28\ud2b8\ub85c \ubd80\ud130 \ud658\uc790\uc815\ubcf4\ub97c </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#64728c;\">\uc790\ub3d9\uc73c\ub85c \ubcf5\uc0ac\ud574\uc624\uc9c0\ub9cc, \ud658\uc790\uc640 \uad00\ub828\ud55c \uc5b4\ub5a0\ud55c \uc815\ubcf4\ub3c4 \uc790\uccb4\uc801\uc73c\ub85c \uc800\uc7a5\ud558\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4. </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#64728c;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#64728c;\">\uc989, \uce74\uc6b4\ud130 \uc218\uc815\uc774 \ud544\uc694\ud55c \uacbd\uc6b0 \ub610\ub294 \ub2e4\uc2dc \ud504\ub9b0\ud2b8\ub97c"
                        " \ud574\uc57c\ud558\ub294 \uacbd\uc6b0\uc5d0\ub294 </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#64728c;\">\uce74\uc6b4\ud130\ub97c \uc9c1\uc811 \uc218\uc815\ud574\uc57c\ub418\uba70, \uae30\uc874 \ud504\ub9b0\ud2b8 \ub41c \ub77c\ubca8\ub4e4\uc740 \uc218\uae30\ub85c \uc218\uc815\uc774 \ud544\uc694\ud569\ub2c8\ub2e4. </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#6e7d9a;\">\ub2e8, \uce74\uc6b4\ud130 \uc815\ubcf4(\ub0a0\uc9dc \ubc0f \ubc31\uc2e0\ubcc4 \uce74\uc6b4\ud2b8)\ub294 DB\uc5d0 \uc800\uc7a5\ub429\ub2c8\ub2e4. </span></p></body></html>", None))
        self.lblr_main_gbx.setTitle("")
        self.lblr_step3_lbl.setText(QCoreApplication.translate("Main", u"3. \ubbf8\ub9ac\ubcf4\uae30\ub97c \ud655\uc778 \ud6c4, \ud504\ub9b0\ud2b8\ub97c \ud569\ub2c8\ub2e4.", None))
        self.lblr_print_btn.setText(QCoreApplication.translate("Main", u"Print", None))
        self.lblr_preview_count_vac_lbl.setText("")
        self.lblr_preview_ptphone_lbl.setText("")
        self.lblr_preview_ptjmno_lbl.setText("")
        self.lblr_preview_date_lbl.setText(QCoreApplication.translate("Main", u"22-12-25(Mon)", None))
        self.lblr_preview_ptname_lbl.setText("")
        self.lblr_preview_lot_lbl.setText("")
        self.lblr_preview_counter_lbl.setText("")
        self.lblr_preview_nocount_vac_lbl.setText("")
        self.lblr_get_data_btn.setText(QCoreApplication.translate("Main", u">> from eGhis", None))
        self.lblr_step2_lbl.setText(QCoreApplication.translate("Main", u"2. \uc811\uc885\ud560 \ubc31\uc2e0\uc744 \uc120\ud0dd\ud569\ub2c8\ub2e4.", None))
        self.lblr_step1_lbl.setText(QCoreApplication.translate("Main", u"1. \ud658\uc790 \uc815\ubcf4\ub97c \ucc28\ud2b8\uc5d0\uc11c \uac00\uc838\uc635\ub2c8\ub2e4.", None))
        self.lblr_reset_btn.setText(QCoreApplication.translate("Main", u"Reset", None))
        self.lblr_flu_date_ckecker_gbx.setTitle("")
        self.lblr_flu_date_checker_title.setText(QCoreApplication.translate("Main", u"\uc778\ud50c\ub8e8\uc5d4\uc790 \uc811\uc885", None))
        self.lblr_flu_date_checker_old_lbl.setText(QCoreApplication.translate("Main", u"\ub178\uc778 \ub3c5\uac10", None))
        self.lblr_flu_date_checker_old.setText(QCoreApplication.translate("Main", u"X", None))
        self.lblr_flu_date_checker_chile_lbl.setText(QCoreApplication.translate("Main", u"\uc18c\uc544 \ub3c5\uac10", None))
        self.lblr_flu_date_checker_child.setText(QCoreApplication.translate("Main", u"X", None))
        self.c19r_address1_lbl.setText(QCoreApplication.translate("Main", u"\ub3c4\ub85c\uba85 \uc8fc\uc18c", None))
        self.c19r_sxsince_led.setText(QCoreApplication.translate("Main", u"20221203", None))
        self.c19r_underaged_cbx.setText(QCoreApplication.translate("Main", u"\ubbf8\uc131\ub144\uc790 \uc5ec\ubd80 (\uc790\ub3d9\uccb4\ud06c)", None))
        self.c19r_ptphone_led.setText("")
        self.c19r_address1_led.setText("")
        self.c19r_ptjmno_led.setText("")
        self.c19r_ptphone_lbl.setText(QCoreApplication.translate("Main", u"\uc804\ud654\ubc88\ud638", None))
        self.c19r_sxsince_lbl.setText(QCoreApplication.translate("Main", u"\ubc1c\ubcd1\uc77c", None))
        self.c19r_notes_pte.setPlainText(QCoreApplication.translate("Main", u"\uc804\ubb38\uac00\uc6a9 RAT \uc591\uc131\n"
"", None))
        self.c19r_dx_date_lbl.setText(QCoreApplication.translate("Main", u"\uc9c4\ub2e8\uc77c", None))
        self.c19r_address2_led.setText("")
        self.c19r_doctor_led.setText(QCoreApplication.translate("Main", u"\uc774\uc9c4\uc131", None))
        self.c19r_symp_lbl.setText(QCoreApplication.translate("Main", u"\uc99d\uc0c1", None))
        self.c19r_subtitle2_lbl.setText(QCoreApplication.translate("Main", u"\uae30\ud0c0 \uc785\ub825 \uc0ac\ud56d\ub4e4..", None))
        self.c19r_notes_lbl.setText(QCoreApplication.translate("Main", u"\ud2b9\uc774\uc0ac\ud56d", None))
        self.c19r_ptname_lbl.setText(QCoreApplication.translate("Main", u"\ud658\uc790\uc774\ub984", None))
        self.c19r_symp_pte.setPlainText("")
        self.c19r_subtitle1_lbl.setText(QCoreApplication.translate("Main", u"\ud658\uc790 \uc815\ubcf4", None))
        self.c19r_ptname_led.setText("")
        self.c19r_dx_date_led.setText(QCoreApplication.translate("Main", u"20221203", None))
        self.c19r_adult_name_lbl.setText(QCoreApplication.translate("Main", u"\ubcf4\ud638\uc790 \uc774\ub984", None))
        self.c19r_address2_lbl.setText(QCoreApplication.translate("Main", u"\uc0c1\uc138\uc8fc\uc18c", None))
        self.c19r_ptjmno_lbl.setText(QCoreApplication.translate("Main", u"\uc8fc\ubbfc\ubc88\ud638", None))
        self.c19r_doctor_lbl.setText(QCoreApplication.translate("Main", u"\uc2e0\uace0\uc758\uc0ac", None))
        self.c19r_adult_name_led.setText("")
        self.c19r_report_btn.setText(QCoreApplication.translate("Main", u"Report", None))
        self.c19r_system_login_btn.setText(QCoreApplication.translate("Main", u"Log-in", None))
        self.c19r_title_lbl.setText(QCoreApplication.translate("Main", u"Covid-19 Report", None))
        self.c19r_warning_lbl.setText(QCoreApplication.translate("Main", u"Covid-19 \ud655\uc9c4\uc790\uc5d0 \ub300\ud55c \uc2e0\uace0\uc758\ubb34 2023.08.31 \uc0ad\uc81c !!!\n"
"\n"
"\ud604\ud589: (\uac10\uc2dc)\uc9c0\uc815\uae30\uad00\uc5d0 \ud55c\ud558\uc5ec \uc2e0\uace0.", None))
        self.c19r_reset_btn.setText(QCoreApplication.translate("Main", u"Reset", None))
        self.settings_reserve_2_btn.setText("")
        self.settings_reserve_1_btn.setText("")
        self.settings_gen_btn.setText(QCoreApplication.translate("Main", u"General", None))
        self.settings_lblr_btn.setText(QCoreApplication.translate("Main", u"Labeler", None))
        self.stgn_auto_backup_btn.setText(QCoreApplication.translate("Main", u"- eGhis auto Backup", None))
        self.stgn_messenger_btn.setText(QCoreApplication.translate("Main", u"- Discord Bot", None))
        self.stgn_auto_shutdown_btn.setText(QCoreApplication.translate("Main", u"- auto Shutdown", None))
        self.stgn_auto_stats_btn.setText(QCoreApplication.translate("Main", u"- LPDOM auto Stats", None))
        self.stgn_cloud_sync_btn.setText(QCoreApplication.translate("Main", u"- eGhis Backup Sync", None))
        self.stgn_vac_sys_log_btn.setText(QCoreApplication.translate("Main", u"- Vac. anti log-out", None))
        self.stgn_auto_backup_lbl.setText(QCoreApplication.translate("Main", u"\uc9c0\uc815\ub41c \uc2dc\uac04\uc5d0 eGhis\ub97c \uc885\ub8cc, \ubc31\uc5c5 \uc2dc\ud589    @", None))
        self.stgn_auto_shutdown_lbl.setText(QCoreApplication.translate("Main", u"eGhis \ubc31\uc5c5 \uc2dc '\ubc31\uc5c5 \ud6c4 \uc885\ub8cc' \ub20c\ub7ec \ucef4\ud4e8\ud130 \ub044\uae30", None))
        self.stgn_auto_stats_1_lbl.setText(QCoreApplication.translate("Main", u"\uccad\uad6c\uc77c\uc5d0\ub294 auto Backup/Shutdown \ubb34\uc2dc.", None))
        self.stgn_auto_stats_2_lbl.setText(QCoreApplication.translate("Main", u"\uc9c0\uc815\ub41c \uc2dc\uac04\uc5d0 \uc790\ub3d9\uc73c\ub85c \uccad\uad6c\uc9d1\uacc4 \ubc0f \ub300\uae30    @", None))
        self.stgn_cloud_sync_lbl.setText(QCoreApplication.translate("Main", u"\uc9c0\uc815\ub41c \uc2dc\uac04\uc5d0 eGhis \ubc31\uc5c5 \ud3f4\ub354\ub97c Dropbox\ub85c \ubcf5\uc0ac    @", None))
        self.stgn_messenger_1_lbl.setText(QCoreApplication.translate("Main", u"\uac01\uc885 \uba54\uc138\uc9c0\ub97c \ub514\uc2a4\ucf54\ub4dc\ub85c \ubc1b\uae30.", None))
        self.stgn_messenger_2_lbl.setText(QCoreApplication.translate("Main", u"- \uc2dc\uc2a4\ud15c \uc885\ub8cc \uc804 \uc54c\ub9bc", None))
        self.stgn_messenger_3_lbl.setText(QCoreApplication.translate("Main", u"- auto Stats \uc2dc\uc791 \ubc0f \ub300\uae30 \uc911 \uc54c\ub9bc", None))
        self.stgn_auto_backup_led.setText(QCoreApplication.translate("Main", u"21:00", None))
        self.stgn_auto_stats_led.setText(QCoreApplication.translate("Main", u"18:30", None))
        self.stgn_cloud_sync_led.setText(QCoreApplication.translate("Main", u"13:10", None))
        self.stgn_vac_sys_log_lbl.setText(QCoreApplication.translate("Main", u"\ub9e4\uc2dc\uac04 \uc815\uac01\uc5d0 (\uc624\ud6c4 5\uc2dc \uc774\ud6c4\uc5d4 \uc911\uc9c0) \uc2e4\ud589 \uc911\uc778 \uc811\uc885\uc2dc\uc2a4\ud15c\ub4e4 \ub85c\uadf8\uc544\uc6c3 \uc5f0\uc7a5", None))
        self.stgn_messenger_server_pte.setPlainText("")
        self.stgn_messenger_server_lbl.setText(QCoreApplication.translate("Main", u"- \uc11c\ubc84", None))
        self.stgn_title_lbl.setText(QCoreApplication.translate("Main", u"General Settings", None))
        self.stgn_info_lbl.setText(QCoreApplication.translate("Main", u"\uc6d0\ud558\ub294 \uae30\ub2a5\uc758 \uc81c\ubaa9\uc744 \ub20c\ub7ec\uc8fc\uc138\uc694. \uc0c9\uc774 \uc5c6\uc5b4\uc9c0\uba74 \ud574\uc81c.", None))
        self.stgn_save_btn.setText(QCoreApplication.translate("Main", u"Save Settings", None))
        self.stgn_reset_btn.setText(QCoreApplication.translate("Main", u"Reload", None))
        self.stlb_flu_age_75over_lbl1.setText(QCoreApplication.translate("Main", u"\uc774\uc804", None))
        self.stlb_flu_old_over75_start_lbl.setText(QCoreApplication.translate("Main", u"75\uc138 \uc774\uc0c1", None))
        self.stlb_flu_old_over75_start_led.setText("")
        self.stlb_flu_age_child_lbl.setText(QCoreApplication.translate("Main", u"\ub300\uc0c1 \uc5f0\ub839", None))
        self.stlb_flu_allow_ex_cbx.setText(QCoreApplication.translate("Main", u"\uc608\uc678 \ub4f1\ub85d\ud558\uae30 (\uc8fc\uc18c\uc9c0\ub294 \uc790\ub3d9\ud655\uc778 \uc548\ub428)", None))
        self.stlb_flu_auto_sort_cbx.setText(QCoreApplication.translate("Main", u"\uad6d\uac00 \ub3c5\uac10. \ub0a0\uc9dc/\uc5f0\ub839/\uc608\uc678 \ucc98\ub9ac\ud558\uae30", None))
        self.stlb_flu_age_7074_lbl.setText(QCoreApplication.translate("Main", u"70~74\uc138", None))
        self.stlb_flu_old_7074_start_led.setText("")
        self.stlb_flu_old_6569_start_led.setText("")
        self.stlb_flu_old_7074_start_lbl.setText(QCoreApplication.translate("Main", u"70~74\uc138", None))
        self.stlb_child_flu_lot_led.setText("")
        self.stlb_flu_old_6569_start_lbl.setText(QCoreApplication.translate("Main", u"65~69\uc138", None))
        self.stlb_subtitle_flu_old_age_lbl.setText(QCoreApplication.translate("Main", u"\ub178\uc778\ub3c5\uac10 \uc0ac\uc5c5 \ub300\uc0c1\uc790 \uc5f0\ub839(\uc0dd\uc77c)", None))
        self.stlb_flu_age_6569_lbl.setText(QCoreApplication.translate("Main", u"65~69\uc138", None))
        self.stlb_flu_old_over75_start_lbl1.setText(QCoreApplication.translate("Main", u"\ubd80\ud130", None))
        self.stlb_flu_date_child_once_led1.setText("")
        self.stlb_subtitle_flu_old_date_lbl.setText(QCoreApplication.translate("Main", u"\ub178\uc778\ub3c5\uac10 \uc811\uc885 \uc77c\uc815", None))
        self.stlb_flu_age_75over_led.setText("")
        self.stlb_child_flu_lot_lbl.setText(QCoreApplication.translate("Main", u"LOT", None))
        self.stlb_auto_input_cbx.setText(QCoreApplication.translate("Main", u"\uc811\uc885 \uc120\ud0dd \uc2dc \uac01 \uc2dc\uc2a4\ud15c\ubcc4 \ud658\uc790\uc815\ubcf4 \uc790\ub3d9\uc785\ub825", None))
        self.stlb_flu_date_child_twice_led1.setText("")
        self.stlb_flu_old_6569_start_lbl1.setText(QCoreApplication.translate("Main", u"\ubd80\ud130", None))
        self.stlb_flu_date_child_twice_lbl.setText(QCoreApplication.translate("Main", u"2\ud68c \uc811\uc885\uc790", None))
        self.stlb_flu_age_child_led1.setText("")
        self.stlb_flu_age_75over_lbl.setText(QCoreApplication.translate("Main", u"75\uc138 \uc774\uc0c1", None))
        self.stlb_auto_child_flu_lot_cbx.setText(QCoreApplication.translate("Main", u"\uc18c\uc544\ub3c5\uac10(nip) \uc811\uc885\uc2dc LOT\ubc88\ud638 \ubc14\uafb8\uae30", None))
        self.stlb_flu_old_7074_start_lbl1.setText(QCoreApplication.translate("Main", u"\ubd80\ud130", None))
        self.stlb_flu_age_child_led2.setText("")
        self.stlb_flu_date_child_once_lbl1.setText(QCoreApplication.translate("Main", u"\ubd80\ud130", None))
        self.stlb_subtitle_flu_child_lbl.setText(QCoreApplication.translate("Main", u"\uc18c\uc544\ub3c5\uac10 \uc77c\uc815 \ubc0f \uc5f0\ub839(\uc0dd\uc77c)", None))
        self.stlb_flu_date_child_twice_lbl1.setText(QCoreApplication.translate("Main", u"\ubd80\ud130", None))
        self.stlb_flu_date_child_once_lbl.setText(QCoreApplication.translate("Main", u"1\ud68c \uc811\uc885\uc790", None))
        self.stlb_flu_date_child_once_led2.setText("")
        self.stlb_flu_date_child_once_lbl2.setText(QCoreApplication.translate("Main", u"\uae4c\uc9c0", None))
        self.stlb_flu_date_child_twice_lbl2.setText(QCoreApplication.translate("Main", u"\uae4c\uc9c0", None))
        self.stlb_flu_date_child_twice_led2.setText("")
        self.stlb_flu_old_end_lbl.setText(QCoreApplication.translate("Main", u"\uc0ac\uc5c5\uae30\uac04", None))
        self.stlb_flu_old_end_lbl1.setText(QCoreApplication.translate("Main", u"\uae4c\uc9c0", None))
        self.stlb_flu_old_end_led.setText("")
        self.stlb_title_lbl.setText(QCoreApplication.translate("Main", u"Labeler Settings", None))
        self.stlb_flu_age_child_lbl1.setText(QCoreApplication.translate("Main", u"\ubd80\ud130", None))
        self.stlb_flu_age_child_lbl2.setText(QCoreApplication.translate("Main", u"\uae4c\uc9c0", None))
        self.stlb_flu_age_7074_lbl2.setText(QCoreApplication.translate("Main", u"\uae4c\uc9c0", None))
        self.stlb_flu_age_7074_lbl1.setText(QCoreApplication.translate("Main", u"\ubd80\ud130", None))
        self.stlb_flu_age_7074_led1.setText("")
        self.stlb_flu_age_7074_led2.setText("")
        self.stlb_flu_age_6569_lbl2.setText(QCoreApplication.translate("Main", u"\uae4c\uc9c0", None))
        self.stlb_flu_age_6569_lbl1.setText(QCoreApplication.translate("Main", u"\ubd80\ud130", None))
        self.stlb_flu_age_6569_led1.setText("")
        self.stlb_flu_age_6569_led2.setText("")
        self.stlb_save_btn.setText(QCoreApplication.translate("Main", u"Save Settings", None))
        self.stlb_reset_btn.setText(QCoreApplication.translate("Main", u"Reload", None))
        self.about_te.setHtml(QCoreApplication.translate("Main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\uc11c\uc6b8\ub0a8\uc0b0 \uc7a5\uccb4 B'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; color:#c8af7d;\">eGhis Assistant\ub294...</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e9e9f4;\">\uc9c0\uadf9\ud788 \uac1c\uc778\uc801\uc778 \ubaa9\uc801\uc73c\ub85c"
                        " \uc9c0\uadf9\ud788 \uac1c\uc778\uc801\uc778 \uc0ac\uc6a9\uc744 \uc704\ud574 \uac1c\ubc1c\ub41c,</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#e9e9f4;\">\ubcd1\uc758\uc6d0 \uc6a9 \uc804\uc790\ucc28\ud2b8 \ud504\ub85c\uadf8\ub7a8\uc778, \uc774\uc9c0\uc2a4 \uc804\uc790\ucc28\ud2b8 \uc6a9 \ub9e4\ud06c\ub85c \ud504\ub85c\uadf8\ub7a8\uc785\ub2c8\ub2e4.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#e9e9f4;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#b45050;\">\ud504\ub85c\uadf8\ub798\ubc0d\uc744 \uc804\ubb38\uc801\uc73c\ub85c \uad50\uc721 \ubc1b\uc544\ubcf8 \uc801 \uc5c6\ub294 \uc774\uc758</span></p>\n"
"<p align=\"center\" "
                        "style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#b45050;\">\ucde8\ubbf8\uc0dd\ud65c\ub85c \uc2dc\uc791\ud558\uc5ec, \uac1c\ubc1c\uc790 \ubcf8\uc778\uc870\ucc28\ub3c4 \ub2f9\uc7a5 \uc778\uc9c0\ud558\uace0 \uc788\uc9c0 \ubabb\ud558\uac70\ub098</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#b45050;\">\ub9c8\ub545\ud788 \ud574\uacb0\ud560 \ubc29\ubc95\ub3c4 \uc5c6\ub294 \uc7a0\uc7ac\uc801\uc774\uace0 \ubcf5\uad6c \ubd88\uac00\ub2a5\ud55c</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#b45050;\">\uc624\ub958 \ubc1c\uc0dd \uac00\ub2a5\uc131\uc774 \uc788\uc74c\uc744 \uba3c\uc800 \uacbd\uace0\ud569\ub2c8\ub2e4.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty;"
                        " margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#b45050;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\ubc30\ud3ec \ub610\ub294 \ud310\ub9e4 \ubaa9\uc801\uc73c\ub85c \uac1c\ubc1c\ub41c \uac83\uc740 \uc544\ub2c8\uae30\uc5d0 \ubcf8 \ud504\ub85c\uadf8\ub7a8\uc744 \uc5b4\ub5a0\ud55c \ubc29\ubc95\uc73c\ub85c\ub4e0 </p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\ucde8\ub4dd/\uc0ac\uc6a9 \uc911\uc774\uc2dc\ub77c\uba74, \uac1c\ubc1c\uc790\ub294 \ubcf8 \ud504\ub85c\uadf8\ub7a8\uc744 \uc0ac\uc6a9\uc911 \ubc1c\uc0dd\ud558\ub294 (\uc7a0\uc7ac\uc801)</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#b491af;\">\uc624\ub958, \uc190\uc0c1 "
                        "\uadf8\ub9ac\uace0 \ub2e4\ub978 \uc5b4\ub5a0\ud55c \uacbd\uc6b0\uc5d0 \uc788\uc5b4\uc11c\ub3c4 \uc808\ub300 \ucc45\uc784 \uc9c0\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\uc778\ud130\ub137\uc5d0 \uacf5\uac1c\ub418\uc5b4\uc788\ub294 \uc790\ub8cc\ub4e4\uc744 \ud1a0\ub300\ub85c \uac1c\ubc1c\ud558\uc600\uae30 \ub54c\ubb38\uc5d0,</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\uc18c\uc2a4\ucf54\ub4dc\ub97c \ucc38\uace0\ud558\uc2dc\uace0 \ucc9c\ucc9c\ud788 \uc77d\uc5b4\ubcf4\uba74 \uba87\uac00\uc9c0 \ub2e8\uc21c\ud55c \ucf54\ub529\uc758 \ubc18\ubcf5\uc785\ub2c8\ub2e4.</p>\n"
"<p align=\"center\" style=\""
                        " margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#a3be8c;\">\ubc30\ud3ec \ub610\ub294 \ud310\ub9e4 \ubaa9\uc801\uc774 \uc544\ub2c8\ub77c\uba74, \uc790\uc720\ub86d\uac8c \uc218\uc815/\ubcc0\uacbd \ud558\uc5ec \uc0ac\uc6a9\ud558\uc154\ub3c4 \ub429\ub2c8\ub2e4.</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#f5c891;\">Python 3.7\uc5d0\uc11c \ubd80\ud130 \uc870\uae08\uc529 \uc218\uc815\uc744 \uac70\uccd0\uac00\uba74\uc11c \uac1c\ubc1c\ub418\uc5c8\uc73c\uba70</"
                        "span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#dedee9;\">--------------------------------------------------</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#dedee9;\">PySide 6</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#dedee9;\">PyWinAuto</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#dedee9;\"> Selenium for Python</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#dedee9;\">----------"
                        "----------------------------------------</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#f5c891;\">\ub4f1\uc744 \ud65c\uc6a9\ud569\ub2c8\ub2e4. </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#f5c891;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#787878;\">by ZiNSSS</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#787878;\">\uc601\ud574\uc120\ud55c\uac00\uc815\uc758\ud559\uacfc, \uacbd\ubd81 \uc601\ub355\uad70 \uc601\ud574\uba74 \uc608\uc8fc\uc2dc\uc7a5\uae38 43-1 1\uce35</span></p>"
                        "\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#787878;\">053-733-7766</span></p></body></html>", None))
        self.apps_about_btn.setText(QCoreApplication.translate("Main", u"About", None))
    # retranslateUi

