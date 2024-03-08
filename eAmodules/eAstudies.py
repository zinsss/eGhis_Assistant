import main
from eAmodules import eApopup, eAinput

LAB_TARGETS = [
    "lab_date_led", "lab_inst_led",
    "lab_hb_led", "lab_hct_led", "lab_wbc_led", "lab_rbc_led", "lab_plt_led",
    "lab_crp_led", "lab_esr_led",
    "lab_bun_led", "lab_cr_led",
    "lab_alb_led", "lab_tpr_led", "lab_ast_led", "lab_alt_led", "lab_gtp_led", "lab_tbil_led",
    "lab_fbs_led", "lab_a1c_led",
    "lab_tc_led", "lab_hdl_led", "lab_ldl_led", "lab_tg_led",
    "lab_tsh_led", "lab_ft4_led", "lab_t3_led",
    "lab_vitd_led", "lab_psa_led",
    "lab_others_pte",
]

BMD_TARGETS = [
    "bmd_date_led", "bmd_inst_led",
    "bmd_lspine_tscore_led",  "bmd_femur_cmb",  "bmd_femur_tscore_led",
    "bmd_others_pte",
]

ALZ_TARGETS = [
    "alz_date_led", "alz_inst_led",
    "alz_mmse_led", "alz_cdr_led", "alz_gds_led",
    "alz_comm_pte",    
]

IPSS_TARGETS = [
    "ipss_date_led", "ipss_inst_led",
    "ipss_1_cmb", "ipss_2_cmb", "ipss_3_cmb", "ipss_4_cmb", "ipss_5_cmb", "ipss_6_cmb", "ipss_7_cmb",
]


def reset(self, target_widgets:list):
    for target_widget in target_widgets:
        target = getattr(self, target_widget)
        if target_widget.endswith("led"):
            target.setText("")
        elif target_widget.endswith("pte"):
            target.setPlainText("")
        elif target_widget.endswith("cmb"):
            target.setCurrentIndex(0)


#: Lab Studies
def lab_results_copy(self, close_window:bool = True):
    #1 우선 빈 리스트를 하나 만들고,
    results = []
    #2-1 주어진 결과값을 하나하나 복사를 하는데, 결과값의 위젯 종류에 따라
    #2-2 lineEdit(led)이면 text()값을, plainTextEdit(pte)면 toPlainText()값을
    #2-3 그리고 combobox(cmb)이면 currentText()값을
    #2-4 순서대로 위 리스트에 append한다.
    for lab_target in LAB_TARGETS:
        target = getattr(self, lab_target)
        if lab_target.endswith("led"):
            results.append(target.text())
        elif lab_target.endswith("pte"):
            results.append(target.toPlainText())
        elif lab_target.endswith("cmb"):
            results.append(target.currentText())
    #3 해당 값에 대한 검사명/부위등을 순서에 맞게 새로운 리스트로 만들어놓고
    #3* 사실 GUI에서 해당 값의 label(lbl)의 값을 같이 불러와서 lbl:lab_target값의 형태로 dictionary가 편했을듯.        
    RESULT_NAMES = [
        "검사일", '기관', #0-1
        'Hb', 'Hct', 'WBC', 'RBC', 'Plt', #2-6
        'CRP', 'ESR', #7-8
        'BUN', 'Cr', #9-10
        'Alb', 't.Protein', 'AST', 'ALT', 'GTP', 't.Bil', #11-16
        'FBS', 'A1c', #17-18
        't.Chol', 'HDL', 'LDL', 'TG', #19-22
        'TSH', 'fT4', 'T3', #23-25
        'Vit.D', 'PSA', 'Others' #26-28
    ]
    #4 처음 작성 해 놓은 리스트에서 값이 있는 것들의 리스트 내 인덱스 번호만 따와서 새로 리스트를 만들고,    
    givenResults = [i for i in range(len(results)) if results[i] != ""]
    #4* 단, 인덱스 0과 1은 검사 시행기관 및 검사날짜 이기 때문에 새 리스트에서 해당 인덱스번호가 없다면, 진행불가처리.
    if 0 not in givenResults or 1 not in givenResults:
        eApopup.warning(text = "시행일 및 기관을 확인해주세요.")
        return   
    #5 텍스트 스트링으로 제목만 우선 작성해놓고,
    LAB_RESULT_FORM = f'\n### 타기관 혈액검사 결과'
    #6 제목에 추가로 동일 라인넘버에 시행일과 시행기관을 작성해주고 
    LAB_RESULT_FORM = LAB_RESULT_FORM + f':  시행일: {results[0]}  기관: {results[1]} ###'
    #7-1 코드가 길어지더라도, Lab 항목별로 보기 쉽게 줄단위로 정리할수 있도록 RESULT_NAMES와 같이 인덱스 번호들을 이용하여,
    #7-2 givenResult 리스트와 range(2,7)_(즉 2,3,4,5,6)의 리스트간의 intersection이 있다면,
    if bool(set(givenResults).intersection(list(range(2,7)))):
        #7-3 새줄에 # CBCs를 입력한 다음, 그 다음줄 부터
        LAB_RESULT_FORM = LAB_RESULT_FORM + f'\n# CBCs\n'
        #7-4 range(2,7)의 리스트 중 givenResult에 있는 값을 인덱스 번호로 활용하여
        #7-5 RESULT_NAMES와 results리스트의 항목을 불러와 추가해준다.
        for i in range(2,7):
            if i in givenResults:
                LAB_RESULT_FORM = LAB_RESULT_FORM + f'{RESULT_NAMES[i]}:{results[i]}  '
    #7의 반복                
    if bool(set(givenResults).intersection(list(range(7, 9)))):
        LAB_RESULT_FORM = LAB_RESULT_FORM + f'\n# Inflamatory Markers\n'
        for i in range(7,9):
            if i in givenResults:
                LAB_RESULT_FORM = LAB_RESULT_FORM + f'{RESULT_NAMES[i]}:{results[i]}  '
    #7의 반복
    if bool(set(givenResults).intersection(list(range(9,11)))):
        LAB_RESULT_FORM = LAB_RESULT_FORM + f'\n# Renal Function Tests\n'
        for i in range(9,11):
            if i in givenResults:
                LAB_RESULT_FORM = LAB_RESULT_FORM + f'{RESULT_NAMES[i]}:{results[i]}  '
    #7의 반복
    if bool(set(givenResults).intersection(list(range(11,17)))):
        LAB_RESULT_FORM = LAB_RESULT_FORM + f'\n# Liver Function Tests\n'
        for i in range(11,17):
            if i in givenResults:
                LAB_RESULT_FORM = LAB_RESULT_FORM + f'{RESULT_NAMES[i]}:{results[i]}  '
    #7의 반복
    if bool(set(givenResults).intersection(list(range(17,19)))):
        LAB_RESULT_FORM = LAB_RESULT_FORM + f'\n# Diabetes Melitus Related\n'
        for i in range(17,19):
            if i in givenResults:
                LAB_RESULT_FORM = LAB_RESULT_FORM + f'{RESULT_NAMES[i]}:{results[i]}  '
    #7의 반복
    if bool(set(givenResults).intersection(list(range(19,23)))):
        LAB_RESULT_FORM = LAB_RESULT_FORM + f'\n# Lipid Profile\n'
        for i in range(19,23):
            if i in givenResults:
                LAB_RESULT_FORM = LAB_RESULT_FORM + f'{RESULT_NAMES[i]}:{results[i]}  '
    #7의 반복
    if bool(set(givenResults).intersection(list(range(23,26)))):
        LAB_RESULT_FORM = LAB_RESULT_FORM + f'\n# Thyroid Function Tests\n'
        for i in range(23,26):
            if i in givenResults:
                LAB_RESULT_FORM = LAB_RESULT_FORM + f'{RESULT_NAMES[i]}:{results[i]}  '
    #7의 반복
    if bool(set(givenResults).intersection(list(range(26,29)))):
        LAB_RESULT_FORM = LAB_RESULT_FORM + f'\n# ETC\n'
        for i in range(26,29):
            if i in givenResults:
                LAB_RESULT_FORM = LAB_RESULT_FORM + f'{RESULT_NAMES[i]}:{results[i]}  '
    
    # 실수로 창을 닫거나 중간에 잘못 눌렀을수도 있으니, 복사버튼을 눌렀을때 먼저 확인 후 리셋하는걸로...
    done = eApopup.confirm(text= "결과 복사 후 입력 결과를 초기화할까요?")
    if not done: return
    else:
        eAinput.copy_it(LAB_RESULT_FORM)
        reset(self, LAB_TARGETS)
        self.hide()
     
     
#: BMD
def bmd_results_copy(self, close_window:bool = True):
    results = []
    for bmd_target in BMD_TARGETS:
        target = getattr(self, bmd_target)
        if bmd_target.endswith("led"):
            results.append(target.text())
        elif bmd_target.endswith("pte"):
            results.append(target.toPlainText())
        elif bmd_target.endswith("cmb"):
            results.append(target.currentText())
            
    BMD_RESULT_FORM = f'\n### 타기관 골밀도 검사 결과'
    
    if results[0] == "" or results[1] == "":
        eApopup.warning(text = "시행일 및 기관을 확인해주세요.")
        return
    BMD_RESULT_FORM = BMD_RESULT_FORM + f':  시행일: {results[0]}  기관: {results[1]} ###'
    
    BMD_RESULT_FORM = BMD_RESULT_FORM + f'\n# L-Spine:{results[2]}   {results[3]}:{results[4]}'
    
    if results[5] != "":
        BMD_RESULT_FORM = BMD_RESULT_FORM + f'\n# Other Comments\n{results[5]}'
    
    done = eApopup.confirm(text= "결과 복사 후 입력 결과를 초기화할까요?")
    if not done: return
    else:
        eAinput.copy_it(BMD_RESULT_FORM)
        reset(self, BMD_TARGETS)
        self.hide()
        

#: Dementia
def alz_results_copy(self, close_window:bool = True):
    results = []
    for alz_target in ALZ_TARGETS:
        target = getattr(self, alz_target)
        if alz_target.endswith("led"):
            results.append(target.text())
        elif alz_target.endswith("pte"):
            results.append(target.toPlainText())
        elif alz_target.endswith("cmb"):
            results.append(target.currentText())
            
    ALZ_RESULT_FORM = f'\n### 타기관 치매관련 검사'
    
    if results[0] == "" or results[1] == "":
        eApopup.warning(text = "시행일 및 기관을 확인해주세요.")
        return
    ALZ_RESULT_FORM = ALZ_RESULT_FORM + f':  시행일: {results[0]}  기관: {results[1]} ###'
    
    if results[2] != "":
        ALZ_RESULT_FORM = ALZ_RESULT_FORM + f'\n# MMSE:{results[2]}  '
    if results[3] != "":
        ALZ_RESULT_FORM = ALZ_RESULT_FORM + f'CDR:{results[3]}  '
    if results[4] != "":
        ALZ_RESULT_FORM = ALZ_RESULT_FORM + f'GDS:{results[4]}  '
    
    if results[5] != "":
        ALZ_RESULT_FORM = ALZ_RESULT_FORM + f'\n# Other Comments\n{results[5]}'
        
    done = eApopup.confirm(text= "결과 복사 후 입력 결과를 초기화할까요?")
    if not done: return
    else:
        eAinput.copy_it(ALZ_RESULT_FORM)
        reset(self, ALZ_TARGETS)
        self.hide()
        
        
#: IPSS
def ipss_results_copy(self, close_window:bool = True):
    results = []
    for ipss_target in IPSS_TARGETS:
        target = getattr(self, ipss_target)
        if ipss_target.endswith("led"):
            results.append(target.text())
        elif ipss_target.endswith("pte"):
            results.append(target.toPlainText())
        elif ipss_target.endswith("cmb"):
            results.append(target.currentText())
            
    IPSS_RESULT_FORM = f'\n### IPSS 검사'
    
    if results[0] == "" and results[1] != "":
        yes = eApopup.confirm(text = "날짜가 입력되지 않았습니다.\n금일로 입력할까요?")
        if not yes: return
        results[0] = main.Infos.date_today.toString("yyyyMMdd")
    elif results[0] != "" and results[1] == "":
        yes = eApopup.confirm(text = "기관이 입력되지 않았습니다.\n본원으로 입력할까요?")
        if not yes: return
        results[1] = "본원"
    elif results[0] == "" and results[1] == "":
        yes = eApopup.confirm(text = "날짜/기관이 입력되지 않았습니다.\n금일/본원으로 입력할까요?")
        if not yes: return
        results[0] = main.Infos.date_today.toString("yyyyMMdd")
        results[1] = "본원"
        
    IPSS_RESULT_FORM = IPSS_RESULT_FORM + f':  시행일: {results[0]}  기관: {results[1]} ###'
    
    IPSS_RESULT_FORM = IPSS_RESULT_FORM + f'\n[1] {results[2]}  [2] {results[3]}  [3] {results[4]}  [4] {results[5]}  [5] {results[6]}  [6] {results[7]}  [7] {results[8]}'
    total_score = int(results[2]) + int(results[3]) +int(results[4]) + int(results[5]) + int(results[6]) + int(results[7]) + int(results[8])
    IPSS_RESULT_FORM = IPSS_RESULT_FORM + f'\nTotal Score: {total_score}'
    
    done = eApopup.confirm(text= "결과 복사 후 입력 결과를 초기화할까요?")
    if not done: return
    else:
        eAinput.copy_it(IPSS_RESULT_FORM)
        reset(self, IPSS_TARGETS)
        self.hide()