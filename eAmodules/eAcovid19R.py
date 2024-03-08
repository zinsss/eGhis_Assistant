from PySide6.QtCore import QDate

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import main
from eAmodules import eAwinauto, eAutils, eApopup


def reset(self):
    self.c19r_ptname_led.setText("")
    self.c19r_ptjmno_led.setText("")
    self.c19r_ptphone_led.setText("")
    self.c19r_pttel_led.setText("")
    self.c19r_address1_led.setText("")
    self.c19r_address2_led.setText("")
    self.c19r_sxsince_led.setText("")
    self.c19r_dx_date_led.setText(main.Infos.date_today.toString("yyyyMMdd"))
    self.c19r_symp_pte.setPlainText("")
    self.c19r_notes_pte.setPlainText("전문가용 RAT 양성")
    self.c19r_doctor_led.setText("이진성")
    self.c19r_underaged_cbx.setChecked(False)
    self.c19r_adult_name_led.setEnabled(False)
    self.c19r_adult_name_led.setText("")
    

def covid_19_get_ptinfo(self):
    # # 병명코드 입력
    # eAinput.icd_input(self, 'u071')
    # eAinput.press_key('enter')
    # # 원스톱진료기관통합진료료(의원) 입력
    # eAinput.rx_input('ah045')

    ptinfo = eAwinauto.current_ptinfo_window()
    self.c19r_ptname_led.setText(ptinfo['ptname'])
    self.c19r_ptjmno_led.setText(ptinfo['ptjmno'])
    self.c19r_ptphone_led.setText(ptinfo['ptphone'])
    self.c19r_pttel_led.setText(ptinfo['pttel'])
    self.c19r_address1_led.setText(ptinfo['ptaddress1'])
    self.c19r_address2_led.setText(ptinfo['ptaddress2'])
    self.c19r_sxsince_led.setText("")
    self.c19r_dx_date_led.setText(main.Infos.date_today.toString("yyyyMMdd"))
    self.c19r_symp_pte.setPlainText("")
    self.c19r_notes_pte.setPlainText("전문가용 RAT 양성")
    self.c19r_doctor_led.setText("이진성")
    print(ptinfo['ptage'])
    print(type(ptinfo['ptage']))
    if int(ptinfo['ptage']) <= 18:
        print("underaged!")
        self.c19r_underaged_cbx.setChecked(True)
        self.c19r_adult_name_led.setEnabled(True)
        self.c19r_adult_name_led.setText("")
    else: 
        self.c19r_underaged_cbx.setChecked(False)
        self.c19r_adult_name_led.setEnabled(False)
        self.c19r_adult_name_led.setText("")
        
        
def data_isValid(self):
    # 환자 이름은 입력했는지..
    if self.c19r_ptname_led.text() == "":
        eApopup.warning(text = "환자 이름을 입력하세요.")
        return False
    # 주민등록번호가 틀리진 않았는지..
    elif eAutils.jmno_isValid(self.c19r_ptjmno_led.text()) == False:
        ok = eApipup.warning(text = "주민등록번호 확인이 필요합니다.\n그래도 진행할까요?\n(외국인의 경우 예외도 있음.)", yes_no = True)
        if not ok: return False
    # 처음 입력시 확인하지만, 주민등록번호를 이용한 미성년자 확인으로 다시 한번 확인해보고..
    elif eAutils.check_underaged(self.parent, self.c19r_ptjmno_led.text()) == True and self.c19r_underaged_cbx.isChecked() == False:
        eApopup.warning(text = "오류, 미성년자로 체크가 안됬습니다.")
        return False
    # 미성년자라면 보호자 이름은 입력했는지..
    elif self.c19r_underaged_cbx.isChecked() and self.c19r_adult_name_led.text() == "":
        eApopup.warning(text = "미성년자입니다.\n보호자 이름을 입력하세요.")
        return False
    # 휴대폰, 전화번호 중 하나는 입력이 되있어야 하고..
    elif self.c19r_ptphone_led.text() == "" and self.c19r_pttel_led.text() == "":
        eApopup.warning(text = "휴대폰 및 전화번호 모두 공란입니다.\n둘 중 하나는 입력하세요.")
        return False
    # 주소가 입력이 되있는지.. (상세주소는 없을수도 있으니 패스)
    # 올바른 도로명주소인지는 확인불가능 함 ㅠㅠ
    elif self.c19r_address1_led.text() == "":
        eApopup.warning(text = "주소를 입력하세요.")
        return False
    # 발병일이 공란은 아닌지..
    elif self.c19r_sxsince_led.text() == "":
        eApopup.warning(text = "발병일을 입력해주세요.")
        return False
    # 발병일이 날짜형식은 바르게 입력됬는지..
    elif QDate.fromString(self.c19r_sxsince_led.text(), "yyyyMMdd").isValid() == False:
        eApopup.warning(text = "발병일 날짜를 확인해주세요.")
        return False
    # 진단일이 공란은 아닌지..
    elif self.c19r_dx_date_led.text() == "":
        eApopup.warning(text = "진단일을 입력해주세요.")
        return False
    # 진단일이 날짜 형식에 맞게 입력됬는지..
    elif QDate.fromString(self.c19r_dx_date_led.text(), "yyyyMMdd").isValid() == False:
        eApopup.warning(text = "진단일 날짜를 확인해주세요.")
        return False
    # 증상이 공란은 아닌지..
    elif self.c19r_symp_pte.toPlainText() == "":
        eApopup.warning(text = "증상을 입력해주세요.")
        return False
    # 특이사항이 공란은 아닌지..
    elif self.c19r_notes_pte.toPlainText() == "":
        eApopup.warning(text = "특이사항이 공란입니다.")
        return False
    # 특이사항에 "전문가용 RAT 양성"은 입력이 되있는지..
    elif "전문가용 RAT 양성" not in self.c19r_notes_pte.toPlainText():
        eApopup.warning(text = "특이사항에 '전문가용 RAT 양성'을 입력하세요.")
        return False
    # 의사 이름이 이진성은 맞는지..
    elif self.c19r_doctor_led.text() != "이진성":
        eApopup.warning(text = "진단 의사 이름을 확인해보세요.")
        return False
    else: return True
        
## selenium 이용한 실제 코로나 확진자 등록
def covid_report(self):
    ok = eApopup.warning(text = "다시 한번 환자정보를 확인하세요!\n그대로 진행할까요?", yes_no = True)
    if not ok: return    
    
    # 완벽하진 않더라도 제대로 입력되있는지 먼저 확인은 해보고..
    if not data_isValid(self): return
    
    def killpopup():
        wins = drv.window_handles
        for win in range(1,len(wins)):
            drv.switch_to.window(wins[win])
            drv.close()
        drv.switch_to.window(wins[0])

    global drv
    
    drv = webdriver.Chrome()

    url = 'https://covid19.kdca.go.kr/'
    drv.get(url)
    # killpopup()
    action = ActionChains(drv)
    self.delayed_exec(1.5)
    drv.switch_to.frame('base')
    # 병원 공인인증서 눌러주고
    drv.find_element(By.XPATH, '//*[@id="xwup_cert_table"]/table/tbody/tr[3]/td[2]/div').click()
    drv.find_element(By.XPATH, '//*[@id="xwup_certselect_tek_input1"]').send_keys("733-7766fm")
    drv.find_element(By.XPATH, '//*[@id="xwup_certselect_tek_input1"]').send_keys(Keys.ENTER)
    self.delayed_exec(1.7)
    # 팝업창 모두 닫아주고
    # killpopup()
    drv.switch_to.frame('base')
    drv.find_element(By.XPATH, '//*[@id="mCSB_1_container"]/ul/li[1]/a').click()
    self.delayed_exec(0.5)
    drv.find_element(By.XPATH, '//*[@id="mCSB_1_container"]/ul/li[1]/ul/li/a').click()
    self.delayed_exec(0.5)
    drv.find_element(By.XPATH, '//*[@id="mCSB_1_container"]/ul/li[1]/ul/li/ul/li[1]/a').click()
    self.delayed_exec(1)
    # 실제 확진자 등록 ifrm.
    drv.switch_to.frame('ifrm')
    drv.find_element(By.XPATH, '//*[@id="mbtnStatement"]').click()
    self.delayed_exec(0.5)
    # 이름
    drv.find_element(By.XPATH, '//*[@id="ptxtPatntNm"]').send_keys(self.c19r_ptname_led.text())
    # 주민번호
    drv.find_element(By.XPATH, '//*[@id="ptxtPatntIhidnum1"]').send_keys(self.c19r_ptjmno_led.text())
    # 보호자이름
    drv.find_element(By.XPATH, '//*[@id="ptxtPrtctorNm"]').send_keys(self.c19r_adult_name_led.text())
    # 휴대폰번호
    drv.find_element(By.XPATH, '//*[@id="ptxtPatntMbtlnum1"]').send_keys(self.c19r_ptphone_led.text())
    # 주소찾기 버튼
    drv.find_element(By.XPATH, '//*[@id="pbtnSearchRdnmadr"]').click()
    self.delayed_exec(1)
    # 주소입력창으로 옮겨서..
    wins = drv.window_handles
    drv.switch_to.window(wins[1])
    # 주소입력란에 입력하기
    drv.find_element(By.XPATH, '//*[@id="keyword"]').send_keys(self.c19r_address1_led.text())
    drv.find_element(By.XPATH, '//*[@id="keyword"]').send_keys(Keys.ENTER)
    self.delayed_exec(1)
    # 1번 결과물 누르기
    drv.find_element(By.XPATH, '//*[@id="roadAddrDiv1"]').click()    #: (따라서 이지스차트 환자정보에서 정확하게 입력이 되어있어야함!!!)
    self.delayed_exec(0.5)
    # 주소 전송
    drv.find_element(By.XPATH, '//*[@id="resultData"]/div/a').click()
    # 기존창 기존 프레임으로 이동
    drv.switch_to.window(wins[0])
    drv.switch_to.frame('base')
    drv.switch_to.frame('ifrm')
    # 도로명 주소 상세주소는 일단 삭제하고
    drv.find_element(By.XPATH, '//*[@id="ptxtPatntRdnmadrDtl"]').clear()
    # 도로명 세부주소 복붙
    drv.find_element(By.XPATH, '//*[@id="ptxtPatntRdnmadrDtl"]').send_keys(self.c19r_address2_led.text())
    # 증상 및 징후
    drv.find_element(By.XPATH, '//*[@id="ptxtNwkndIcdStarmySymptms"]').send_keys(self.c19r_symp_pte.toPlainText())
    # 발병일
    drv.find_element(By.XPATH, '//*[@id="ptxtAtfssDe1"]').send_keys(self.c19r_sxsince_led.text())
    # 진단일
    drv.find_element(By.XPATH, '//*[@id="ptxtDgnssDe1"]').send_keys(self.c19r_dx_date_led.text())
    # 양성, 환자 라디오버튼 클릭해주고
    drv.find_element(By.XPATH, '//*[@id="prdoDsndgnssInspctResultTyCd1"]').click()
    # 환자 누르고 발생하는 alert 처리
    drv.switch_to.alert.accept()
    drv.find_element(By.XPATH, '//*[@id="prdoPatntClCd1"]').click()
    # 비고 특이사항 입력
    drv.find_element(By.XPATH, '//*[@id="ptxtRmInfo"]').send_keys(self.c19r_notes_pte.toPlainText())
    # 진단의사 성명
    drv.find_element(By.XPATH, '//*[@id="ptxtSttemntDoctrNm"]').send_keys(self.c19r_doctor_led.text())
    # 확인 컨펌 체크박스 누르고.
    drv.find_element(By.XPATH, '//*[@id="pchkNA0012ErrCheck"]').click()
    #- 만약을위해 최종 확진자 신고 버튼은 자동화 안하기!!!!!!!!!!!!!!!
    
    ok = eApopup.confirm(text = "신고가 정상적으로 완료되었나요?\n입력 폼을 초기화 할까요?")
    if not ok: return
    else: reset(self)
    

## 홈페이지 로그인만.     
def covid_sys_login(self):
    ok = eApopup.warning(text = "다시 한번 환자정보를 확인하세요!\n그대로 진행할까요?", yes_no = True)
    if not ok: return    
    # 셀레늄 기본설정, 홈페이지 오픈
    global drv    
    drv = webdriver.Chrome()
    url = 'https://covid19.kdca.go.kr/'
    drv.get(url)
    self.delayed_exec(1.5)
    # 병원 공인인증서 눌러주고
    drv.switch_to.frame('base')
    drv.find_element(By.XPATH, '//*[@id="xwup_cert_table"]/table/tbody/tr[3]/td[2]/div').click()
    drv.find_element(By.XPATH, '//*[@id="xwup_certselect_tek_input1"]').send_keys("733-7766fm")
    drv.find_element(By.XPATH, '//*[@id="xwup_certselect_tek_input1"]').send_keys(Keys.ENTER)
    self.delayed_exec(1.7)
    drv.switch_to.frame('base')
    drv.find_element(By.XPATH, '//*[@id="mCSB_1_container"]/ul/li[1]/a').click()
    self.delayed_exec(0.5)
    drv.find_element(By.XPATH, '//*[@id="mCSB_1_container"]/ul/li[1]/ul/li/a').click()
    self.delayed_exec(0.5)
    drv.find_element(By.XPATH, '//*[@id="mCSB_1_container"]/ul/li[1]/ul/li/ul/li[1]/a').click()
