from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from eAmodules import eAwinauto

# Vaccine System들은 pywinauto로 자동화가 안됨.
# 마우스 클릭좌표를 이용한 자동화 말고는 다른 방법은 없어,
# 항상 지정된 자리, 지정된 창크기로 사용할 수 밖에..
# FancyZones를 이용하며, 다행히 시스템의 위치,크기는 저장되는듯.

# 크롬드라이버 설치된 위치.
# C:\Users\leejs\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe


# 질병청 예방접종 시스템들 자동실행
def iskdca_login(self, options: int):
    '''Options (as integer, as in index of below list.)
    ['통합예방접종시스템(V)', '현물독감접종시스템(F)', '코로나19접종시스템(C)',
    'V + F', 'V + C', 'F + C', 'V + F + C', '홈페이지 로그인']
    '''

    # selenium, kill popup windows
    def killpopup():
        wins = drv.window_handles
        for win in range(1, len(wins)):
            drv.switch_to.window(wins[win])
            drv.close()
        drv.switch_to.window(wins[0])

    # 원래 창으로 복귀
    def backtomain():
        wins = drv.window_handles
        drv.switch_to.window(wins[0])

    # global 선언으로 함수 종료 이후에도 chrome창이 종료되지 않음.
    global drv
    drv = webdriver.Chrome()
    url = 'https://is.kdca.go.kr'
    drv.get(url)
    killpopup()
    drv.switch_to.frame('base')
    # 공인인증서 로그인 버튼 눌러주고
    drv.find_element(By.XPATH, '//*[@id="contents"]/div/article[1]/a[1]').click()
    self.delayed_exec(2)
    print("del")
    # 병원 공인인증서 눌러주고
    drv.find_element(By.XPATH, '//*[@id="xwup_cert_table"]/table/tbody/tr[3]/td[2]/div').click()
    drv.find_element(By.XPATH, '//*[@id="xwup_certselect_tek_input1"]').send_keys("733-7766fm")
    drv.find_element(By.XPATH, '//*[@id="xwup_certselect_tek_input1"]').send_keys(Keys.ENTER)
    self.delayed_exec(1)
    # 팝업창 모두 닫아주고
    killpopup()

    # 접종시스템 시작, fancy zones 나열, 접종화면으로 이동
    def vac_start():
        drv.switch_to.frame('base')
        # 선택 combobox
        drv.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div[2]/div/a').click()
        self.delayed_exec(0.5)
        # 예방접종통합관리시스템 (combobox)
        drv.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div[2]/div/ul/li[3]/a').click()
        self.delayed_exec(1)
        # chrome dev tool에서 프레임 확인!
        drv.switch_to.frame('ifrm')
        # 예방접종통합관리시스템 링크(그림)
        drv.find_element(By.XPATH, '//*[@id="ocs_button1"]').click()
        self.delayed_exec(6)
        eAwinauto.gen_sys_prepare(self)

        # vac_sys_pos = [vac_sys.left+20, vac_sys.top+10]
        # pag.moveTo(vac_sys_pos)
        # pag.keyDown('shifleft')
        # pag.keyDown('shiftright')
        # # fancy zones area
        # pag.dragTo(3282, 108, 0.75, button='left')
        # pag.keyUp('shiftright')
        # pag.keyUp('shiftleft')
        # # 접종화면 클릭
        # pag.click(2800, 400)
        # self.logcont_vac_cb.setChecked(True)
        # backtomain()

    # 현물공급 플루 시스템 시작, fancy zones 나열
    def fluold_start():
        drv.switch_to.frame('base')
        # 홈페이지 로고 (처음 창으로)
        drv.find_element(By.XPATH, '//*[@id="logo"]/a/img').click()
        self.delayed_exec(1)
        killpopup()
        drv.switch_to.frame('base')
        # 선택 combobox
        drv.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div[2]/div/a').click()
        self.delayed_exec(0.5)
        # 예방접종관리(콤보박스내)
        drv.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div[2]/div/ul/li[3]/a').click()
        self.delayed_exec(1)

        # drv.switch_to.frame('ifrm')
        # # 현물공급 인플루엔자등록시스템 링크(그림)
        # drv.find_element(By.XPATH, '//*[@id="inf_button1"]').click()

        drv.find_element(By.XPATH, '//*[@id="197625"]/a[1]').click()
        self.delayed_exec(0.5)
        drv.find_element(By.XPATH, '//*[@id="197625"]/ul[1]/li/a[1]').click()
        self.delayed_exec(0.5)
        drv.find_element(By.XPATH, '//*[@id="197625"]/ul[1]/li/ul[1]/li/a[3]').click()
        self.delayed_exec(6)

        # fluold_sys_pos = [fluold_sys.left+20, fluold_sys.top+10]
        # pag.moveTo(fluold_sys_pos)
        # pag.keyDown('shifleft')
        # pag.keyDown('shiftright')
        # # fancy zones area
        # pag.dragTo(3282, 108, 0.75, button='left')
        # pag.keyUp('shiftright')
        # pag.keyUp('shiftleft')
        # self.logcont_fluold_cb.setChecked(True)
        # backtomain()

    # 코로나 시스템 시작, fancy zones 나열
    def corona_start():
        drv.switch_to.frame('base')
        # 홈페이지 로고(처음 창으로)
        drv.find_element(By.XPATH, '//*[@id="logo"]/a/img').click()
        self.delayed_exec(1)
        killpopup()
        drv.switch_to.frame('base')
        # 선택 combobox
        drv.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div[2]/div/a').click()
        self.delayed_exec(0.5)
        # 코로나 접종시스템 (combobox)
        drv.find_element(By.XPATH, '//*[@id="contents"]/div[1]/div[2]/div/ul/li[1]/a').click()
        self.delayed_exec(1)
        drv.find_element(By.XPATH, '//*[@id="203443"]/a[1]').click()
        self.delayed_exec(0.5)
        drv.find_element(By.XPATH, '//*[@id="203443"]/ul[1]/li/a').click()
        self.delayed_exec(6)
        eAwinauto.vaccine_focus(2)

        # corona_sys_pos = [corona_sys.left+20, corona_sys.top+10]
        # pag.moveTo(corona_sys_pos)
        # pag.keyDown('shifleft')
        # pag.keyDown('shiftright')
        # pag.dragTo(3282, 108, 0.75, button='left')
        # pag.keyUp('shiftright')
        # pag.keyUp('shiftleft')
        # self.logcont_corona_cb.setChecked(True)

    if options == 0:
        vac_start()
    elif options == 1:
        fluold_start()
    elif options == 2:
        corona_start()
    elif options == 3:
        vac_start()
        backtomain()
        fluold_start()
    elif options == 4:
        vac_start()
        backtomain()
        corona_start()
    elif options == 5:
        fluold_start()
        backtomain()
        corona_start()
    elif options == 6:
        vac_start()
        backtomain()
        fluold_start()
        backtomain()
        corona_start()
    elif options == 7:
        return
