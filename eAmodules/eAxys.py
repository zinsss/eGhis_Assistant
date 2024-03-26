
## Some Specifications of Locations of Buttons and Input Area that Can Not Be Automated By PyWindAuto.

# TODO Go and Read Through the codes and delete unused.

#= eGhis 전자차트
class eGhis:
    FIND_PT = ()
    MDOC = ()
    MDOC2 = ()
    MENU_CLAIM = (2070, 80)
    CLAIM_START_STAT = (3680, 130)
    SHUTDOWN_AFTER = (1498, 1298)

#= 통합예방접종시스템    
class VacGen:
    TO_MAIN = (1050,2555)
    INPUT_PTJMNO = (1345, 2285)
    DEL_PTJMNO = (1515, 2288)
    CONT_LOGIN = (2700, 2175)

#= 현물공급독감시스템
class VacFlu:
    INPUT_PTJMNO = (1343, 2360)
    DEL_PTJMNO = (1343, 2360)
    # VACCINATE = (2020, 2700)

#= 코로나19접종시스템
class VacCovid19:
    INPUT_PTJMNO = (1166, 2315)
    DEL_PTJMNO = (1365, 2315)
    CONT_LOGIN = (2745, 2185)
    PF_MOD_SEL = (1650, 2365)

#= Find_xy 용 png 파일 경로
class Image:
    CJ_CODE = ""
    JJ_CODE = ""
    RAT = ""

#= Find_xy 용 area
class Area:
    F3_TOPBAR = ()
    F3_CODES = ()
    F3_CODENAMES = ()