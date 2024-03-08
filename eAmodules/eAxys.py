
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
    TO_MAIN = (2600, 1500)
    INPUT_PTJMNO = (455, 540)
    DEL_PTJMNO = (600, 540)
    CONT_LOGIN = (1070, 430)

#= 현물공급독감시스템
class VacFlu:
    INPUT_PTJMNO = (205, 580)
    DEL_PTJMNO = (555, 575)
    CONT_LOGIN = (1075, 435)
    INPUT_LOT = (235, 880)
    AS_EX = (3085, 1020)

#= 코로나19접종시스템
class VacCovid19:
    INPUT_PTJMNO = (270, 575)
    DEL_PTJMNO = (450, 575)
    CONT_LOGIN = (1100, 440)

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
    CALENDAR = ()