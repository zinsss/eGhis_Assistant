
## Qt Stylesheets Archive. Also For Better Managements and Readability of Codes.

# TODO Go through Each Stylesheets for Unused and Delete it.

## MainWindow Alert Styles, ON and OFF
ALERT_OFF = "color: rgb(70, 80, 100);"
PT_ALERT_ON = """
color: rgb(225, 75, 75);
background-color: rgb(252, 227, 246);
border-radius:8px;
border:1px solid rgb(225, 75, 75);
"""
CLAIM_ALERT_ON = "color: rgb(225, 125, 50);"
EVENTS_ALERT_ON = "color: rgb(75, 150, 250);"
REMINDERS_ALERT_ON_TODAY = "color: rgb(125, 200, 150);"
REMINDERS_ALERT_ON_7DAYS = "color: rgb(122, 155, 111);"
REMINDERS_ALERT_ON_OVERDUE = "color: rgb(225, 75, 75);"

## CalRemAdit MenuButtons
CALREM_ADIT_ON_PAGE = """
QPushButton {	
	color: rgb(143, 188, 187);
	border:none;
}
"""
CALREM_ADIT_TO_PAGE = """
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

## Alert Notification for Allergies and Contra-Indications
ALERT_ALLERGIES_OFF = """
background-color: transparent;
color: transparent;
border-radius: 15px;
border:2px solid transparent;
"""
ALERT_ALLERGIES_ON = """
background-color: rgb(255, 244, 233);
color: rgb(200, 75, 75);
border-radius: 15px;
border:2px solid rgb(250, 150, 150);
"""
## APP Buttons
REMINDERS_NEW_SYMBOL = """
background-color:rgb(42,48,58);
border:none;
border:1px solid rgb(50,55,70);
border-bottom-left-radius:10px;
border-right:none;
"""
REMINDERS_NEW_LED = '''
background-color:rgb(42,48,58);
border:none;
border:1px solid rgb(50,55,70);
border-right:none;
border-left:none;
'''

APPS_GBX_DEFAULT = """
QPushButton {
	font: bold italic 12pt "Lucida Sans";
	color: rgb(150, 155, 175);
	border:none;
}
QPushButton:hover {    
	color:rgb(145,170,170);
}
QPushButton:pressed {
	color:rgb(75,75,90);
}
"""
APPS_GBX_SELECTED = """
QPushButton {
	font: bold italic 14pt "Lucida Sans";
	color: rgb(143, 188, 187);
    border:none;
}
"""

## QMessageBoxes
WARNBOX = """
QMessageBox {
    font: 14pt "나눔바른고딕";
    background-color: rgb(250, 200, 180);
    border: 3px solid rgb(190, 95, 105);
}
QLabel {
    min-width:333px;
    padding-top:10px;
    color: rgb(150, 85, 100);
}
QPushButton {
    min-width:100px;
    min-height:29px;
    font: bold italic 12pt "Lucida Sans";
    color: rgb(233, 222, 233);
    background-color: rgb(190, 95, 105);
    border-radius:14%;
    border:1px solid rgb(190, 75, 105);
}
QPushButton:hover {    
    color:rgb(255,244,255);
}
QPushButton:pressed {
    background-color:rgb(180, 85, 95);
}
QPushButton[text="YES"] {
    min-width:100px;
    min-height:29px;
    font:bold italic 12pt "Lucida Sans";
    color: rgb(233, 222, 233);	
    background-color: rgb(150, 125, 175);
    border-radius:14%;
    border:1px solid rgb(125, 100, 150);
}
QPushButton[text="YES"]:hover {    
    color: rgb(255, 244, 255);
}
QPushButton[text="YES"]:pressed {
    background-color:rgb(140,110,165);
}
"""

MSGBOX = """
QMessageBox {
    font: 14pt "나눔바른고딕";
    background-color: rgb(170, 180, 225);
    border: 3px solid rgb(100, 120, 175);
}
QLabel {
    min-width:300px;
    padding-top:10px;
    color: rgb(100, 85, 130);
}
QPushButton {
    min-width:100px;
    min-height:29px;
    font: bold italic 12pt "Lucida Sans";
    color: rgb(233, 222, 233);
    background-color: rgb(200, 125, 175);
    border-radius:14%;
    border:1px solid rgb(166, 111, 133);
}
QPushButton:hover {    
    color:rgb(255,244,255);
}
QPushButton:pressed {
    background-color:rgb(190,110,150);
}
"""

NOTIBOX = """
QMessageBox {
    font: 14pt "나눔바른고딕";
    background-color: rgb(170, 180, 225);
    border: 3px solid rgb(100, 120, 175);
}
QLabel {
    min-width:300px;
    padding-top:10px;
    color: rgb(100, 85, 130);
}
QPushButton {
    min-width:100px;
    min-height:29px;
    font: bold italic 12pt "Lucida Sans";
    color: rgb(233, 222, 233);
    background-color: rgb(200, 125, 175);
    border-radius:14%;
    border:1px solid rgb(166, 111, 133);
}
QPushButton:hover {    
    color:rgb(255,244,255);
}
QPushButton:pressed {
    background-color:rgb(190,110,150);
}
"""

MENUBOX = """
QMessageBox {
    font:16pt "서울남산 장체 EB";
    background-color: rgb(180, 200, 225);
    border: 3px solid rgb(81, 112, 149);
}
QLabel {
    padding-top:10px;
    color: rgb(66, 99, 144);
    min-height:45px;
    min-width:20px;
}
QPushButton {
    min-width:225px;
    min-height:29px;
    font: bold 12pt "나눔바른고딕";
    color: rgb(233, 222, 233);
    background-color: rgb(100, 120, 160);
    border-radius:14%;
    border:1px solid rgb(77, 99, 122);
}
QPushButton:hover {
    color:rgb(255,244,255);
}
QPushButton:pressed {
    background-color:rgb(110,130,175);
}
QPushButton[text="CLOSE"] {
    min-width:100px;
    min-height:29px;
    font: bold italic 12pt "Lucida Sans";
    color: rgb(233, 222, 233);	
    background-color: rgb(190, 125, 175);
    border-radius:14%;
    border:1px solid rgb(155, 111, 133);
}
QPushButton[text="CLOSE"]:hover {    
    color:rgb(255,244,255);
}
QPushButton[text="CLOSE"]:pressed {
    background-color:rgb(180,110,150);
}
"""

REMINDERS_MENU = """
QMessageBox {
    font: bold italic 16pt "Lucida Sans";
    background-color: rgb(50,55,65);
    border: 3px solid rgb(40,45,50);
}
QLabel {
    padding-top:10px;
    color: rgb(180,185,195);
    min-height:45px;
    min-width:20px;
}
QPushButton {
    min-width:225px;
    min-height:29px;
    font: italic 12pt "Lucida Sans";
    color: rgb(177, 188, 211);
    background-color: rgb(45,50,60);
    border-radius:14%;
    border:1px solid rgb(40,45,50);
}
QPushButton[text="In-Progress"] {
    color: rgb(100,150,200);
}
QPushButton[text="Forwarded"] {
    color: rgb(155,190,185);
}
QPushButton[text="Urgent"] {
    color: rgb(200,125,100);
}
QPushButton[text="Starred"] {
    color: rgb(200,175,125);
}
QPushButton[text="Maybe/Uncertain"] {
    color: rgb(175,125,180);
}
QPushButton[text="Done"] {
    color: rgb(133,188,122);
    background-color: rgb(40,50,35);
}
QPushButton[text="Cancelled"] {
    color: rgb(233,211,211);
    background-color: rgb(70,40,40);
}
QPushButton[text="DELETE"] {
    color: rgb(233, 200, 222);	
    background-color: rgb(60, 40, 50);
}
QPushButton[text="EDIT"] {
    color: rgb(233, 200, 222);	
    background-color: rgb(50, 40, 60);
}
QPushButton:hover {
    font: bold italic 12pt "Lucida Sans";
}
QPushButton:pressed {
    font: bold italic 11pt "Lucida Sans";
}
QPushButton[text="CLOSE"] {
    min-width:100px;
    min-height:29px;
    color: rgb(233, 222, 233);	
    background-color: rgb(190, 125, 175);
    font: bold italic 12pt "Lucida Sans";
    border-radius:14%;
    border:1px solid rgb(40,45,50);
}
QPushButton[text="CLOSE"]:hover {    
    color:rgb(255,244,255);
}
QPushButton[text="CLOSE"]:pressed {
    background-color:rgb(180,110,150);
}
"""

CONFBOX = """
QMessageBox {
    font:14pt "나눔바른고딕";
    background-color: rgb(180, 200, 225);
    border: 3px solid rgb(81, 112, 149);
}
QLabel {
    min-width:300px;
    padding-top:10px;
    color: rgb(81, 112, 149);
}
QPushButton {
    min-width:125px;
    min-height:29px;
    font: bold italic 12pt "Lucida Sans";
    color: rgb(233, 222, 233);	
    background-color: rgb(100, 120, 160);
    border-radius:14%;
    border:1px solid rgb(77, 99, 122);
}
QPushButton:hover {    
    color:rgb(255,244,255);
}
QPushButton:pressed {
    background-color:rgb(110,130,175);
}
QPushButton[text="NO"] {
    min-width:100px;
    min-height:29px;
    font: bold italic 12pt "Lucida Sans";
    color: rgb(233, 222, 233);	
    background-color: rgb(180, 133, 190);
    border-radius:14%;
    border:1px solid rgb(144, 122, 155);
}
QPushButton[text="NO"]:hover {    
    color:rgb(255,244,255);
}
QPushButton[text="NO"]:pressed {
    background-color:rgb(170,120,180);
}
"""

CONFBOX_BIG = """
QMessageBox {
    font:14pt "나눔바른고딕";
    background-color: rgb(180, 200, 225);
    border: 3px solid rgb(81, 112, 149);
}
QLabel {
    min-width:660px;
    padding-top:10px;
    color: rgb(81, 112, 149);
}
QPushButton {
    min-width:125px;
    min-height:29px;
    font: bold italic 12pt "Lucida Sans";
    color: rgb(233, 222, 233);	
    background-color: rgb(100, 120, 160);
    border-radius:14%;
    border:1px solid rgb(77, 99, 122);
}
QPushButton:hover {    
    color:rgb(255,244,255);
}
QPushButton:pressed {
    background-color:rgb(110,130,175);
}
QPushButton[text="NO"] {
    min-width:100px;
    min-height:29px;
    font: bold italic 12pt "Lucida Sans";
    color: rgb(233, 222, 233);	
    background-color: rgb(180, 133, 190);
    border-radius:14%;
    border:1px solid rgb(144, 122, 155);
}
QPushButton[text="NO"]:hover {    
    color:rgb(255,244,255);
}
QPushButton[text="NO"]:pressed {
    background-color:rgb(170,120,180);
}
"""
 
INPUTBOX = """
QInputDialog {
    font:12pt "D2Coding";
    background-color: rgb(180, 200, 225);
    border: 3px solid rgb(81, 112, 149);
}
QLineEdit {
    min-height:30px;
    font:12pt "D2Coding";
    color:rgb(80, 100, 125);
    padding-left:10px;
    background-color: rgb(220,240,255);
    border:1px solid rgb(150, 170, 200);
    border-radius:15%;
}
QSpinBox {
    min-height:30px;
    font:12pt "D2Coding";
    color:rgb(80, 100, 125);
    padding-left:10px;
    background-color: rgb(220,240,255);
    border:1px solid rgb(150, 170, 200);
    border-radius:15%;
}
QSpinBox::up-button {
    subcontrol-position: top right; /* position at the top right corner */
    width: 20px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */
    background-color: rgb(190, 125, 175);
    border-left:1px solid rgb(150, 170, 200);
    border-top-right-radius: 13px;
}
QSpinBox::down-button {
    subcontrol-position: bottom right; /* position at bottom right corner */
    width: 20px;
    border-width: 1px;
    border-left:1px solid rgb(150, 170, 200);
    background-color: rgb(125, 150, 220);
    border-bottom-right-radius: 13px;
}
QLabel {
    min-width:200px;
    font:14pt "D2Coding";
    padding-top:10px;
    color: rgb(80, 110, 150);
}
QPushButton {
    min-width:125px;
    min-height:29px;
    font:12pt "D2Coding";
    color: rgb(233, 222, 233);	
    background-color: rgb(100, 120, 160);
    border-radius:14%;
    border:1px solid rgb(77, 99, 122);
}
QPushButton:hover {    
    color:rgb(255,244,255);
}
QPushButton:pressed {
    background-color:rgb(110,130,175);
}
"""

MULTILINEBOX = """
QInputDialog {
    font:12pt "D2Coding";
    border: 3px solid rgb(81, 112, 149);
    background-color: rgb(180, 200, 225);
}
QPlainTextEdit {
    min-height:250px;
    min-width:525;
    max-width:525;
    font:12pt "D2Coding";
    color:rgb(80, 100, 125);
    padding:5px;
    background-color: rgb(220,240,255);
    border:1px solid rgb(150, 170, 200);
    border-radius:15%;
}
QLabel {
    font:bold 14pt "D2Coding";
    padding-top:10px;
    color: rgb(80, 110, 150);
}
QPushButton {
    min-width:125px;
    min-height:29px;
    font:12pt "D2Coding";
    color: rgb(233, 222, 233);
    background-color: rgb(100, 120, 160);
    border-radius:14%;
    border:1px solid rgb(77, 99, 122);
}
QPushButton:hover {    
    color:rgb(255,244,255);
}
QPushButton:pressed {
    background-color:rgb(110,130,175);
}
"""