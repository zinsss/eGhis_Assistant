## Archives of Commonly Used Strings For Better Management and More Readability of Main Code.

## MACROS
# = 진료관련

# = 코멘트모음
FLUID_LST = ["수액;", "수액;;", "수액;;;"]
PT_LST = ["물치;", "물치;;", "물치;;;", "물치;;;;", "물치;;;;;", "물치;;;;;;"]
CHRMAN_LST = ["만성;", "만성;;", "만성;;;", "만성;;;;", "만성;;;;;", "만성;;;;;;"]
REPEATS_LST = ["# 리피트", "# 기존약 유지", "# 리피트 처방"]
NIC_LST = ["nic;", "nic;;", "nic;;;", "nic;;;;"]
OBSV_LST = ["경과;", "경과;;"]
LAB_PLAN_LST = ["다음랩;", "다음랩;;", "다음랩;;;", "다음랩;;;;"]
LAB_MUST_LST = [
    "# 다음 내원 시 혈액검사 희망\n  주기적 혈액검사 확인 필요성 강조함.",
    "# 혈액검사 필요성 설명하였으나\n  다음 처방일로 연기 희망하심.",
    "# 환자 요청으로 다음 내원일로 혈액검사 연기",
    "# 혈액검사 연기 희망\n  다음 처방 시에는 검사 필요함을 설명함."
]
BMD_PLAN = "# 다음 처방 전 BMD 추적검사 필요함을 설명."
MMSE_PLAN = "# 다음 처방 전 MMSE, CDR 등 치매척도관련 검사 필요함을 설명."
XRAY_PLAN = ">> 증상 호전/악화/지속 여부에 따라 추후 엑스선 촬영 여부 결정."
XRAY_REFUSE = "# 엑스선 촬영 권유하였으나,\n  보존적 치료 우선 시행 후\n  증상 호전여부에 따라\n  엑스선 촬영 여부 결정 원하심."
HOME_MON = "# 가정에서도 주기적으로 혈압/혈당 확인해보세요.\n  >> 가능하면 결과 적어오세요."
REC_HOME_MON_BST = "# 주기적으로 집에서도 식전 및/또는 식후(2시간)\n  혈당 확인 후 다음 내원 시 적어 오시도록 권유함."
REC_HOME_MON_BP = "# 주기적으로 집에서도 혈압 측정 후\n  다음 내원시 적어 오시도록 권유함."

# = 예방접종 관련

# = 코로나19 관련
RAT_NEGA = "\n# 본원 확인 한 RAT상 음성."
RAT_POSI = """\n# 본원 확인 한 RAT상 양성. 주의사항 및 안내사항 설명함.
 - 자가격리의 의무사항은 없어지고, 5일간의 격리 권고.
 - 가능한 사람 많은 곳을 외출 삼가하시도록 안내.
 - 외출 시 가능한 마스크 착용할것을 설명함.
 - 증상 지속/악화 시 재 방문하도록 설명함."""
RAT_FU_REC = "\n# 증상호전 없이 지속/악화되는 경우에는\n RAT 또는 자가진단키트 반복검사의 고려 필요성을 설명함."

# = 인플루엔자관련
FLU_NEGA = "\n# 본원에서 확인한 FLU 키트검사 상 음성."
FLU_A = "\n# 본원에서 확인한 FLU 키트검사 상 A형 인플루엔자 확인."
FLU_B = "\n# 본원에서 확인한 FLU 키트검사 상 B형 인플루엔자 확인."
TAMIFLU_INFO = "\n# 타미플루 처방. 관련 부작용 및 안내사항 설명함."


## Quick Saves
VACCINATION = "\n접종관련 부작용 과거력: 없음\n상기도감염증세: 없음\n발열여부: 없음"
LIMAPROST = "양측 SLR 40도 내외.\n간헐성 파행, 10m 내외."
CHOLINE_ALFO = "최근 기억력 저하, 특히 short term memory.\n돈계산 등 집중력 저하는 미미."
MONTELUKAST = "항히스타민제제 단독투여(타기관 처방 포함)에도\n호전보이지 않는 비폐색 및 비염증세."
ESTROGEN = "주기적(년1회) 여성암(자궁경부암, 유방암) 검진 받도록 설명 및 과거 검진력 확인."
X_OS_NS = "엑스선 촬영 상 no prominent fracture line noted.\n증상의 지속/악화여부에 따라 microfracture등 확인 위해 7일뒤 재방문 설명함."
X_PA_NS = "흉부엑스선 촬영 상 no abnormal findings noted."
