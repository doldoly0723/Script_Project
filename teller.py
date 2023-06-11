# 텔레그렘
"""import telepot
import noti"""


import telepot


import noti



def telSearch(user, sido, sidogun, Hpname):
    search_data = noti.getSearchData(sido, sidogun, Hpname)
    msg=''
    msg = search_data["HpName"] + "\n" + \
          "주소: " + search_data["HpAddr"] + '\n' + \
          "전화번호: " + search_data["Hptelno"] + '\n' + \
          "운영시간: " + search_data["HPworkTime"] + '\n' + \
          "진료과목: " + search_data["HpSubject"]
    noti.sendMessage(user, msg)

def telHpcnt(user, sido, sidogun):
    Hpcnt_data = noti.getHpcntDate(sido,sidogun)
    msg = ''
    msg = "해당 도시의 병원 분류명 개수" + '\n'
    for key in Hpcnt_data:
        msg += key + ": " + str(Hpcnt_data[key]) + '개\n'

    noti.sendMessage(user, msg)

def telHpSubject(user, sido, sidogun, Hpsubject):
    noti.getHpSubject_data(user, sido, sidogun, Hpsubject)


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')

    # 물어볼 정보
    # 병원 이름 검색 시 출력
    # 검색 서울시 종로구 서울대학교병원
    if text.startswith('검색') and len(args) >= 4:
        telSearch(chat_id, args[1], args[2], args[3])

    # 현황
    # 현황 서울시 종로구
    elif text.startswith('병원현황') and len(args)>=3:
        telHpcnt(chat_id, args[1], args[2])

    # 진료과 서울시 종로구 내과
    elif text.startswith('진료과검색') and len(args) >= 4:
        telHpSubject(chat_id, args[1], args[2], args[3])

    else:
        noti.sendMessage(chat_id, '모르는 명령어입니다.\n검색 시구 시군구 병원이름\n병원현황 시구 시군구\n진료과검색 시구 시군구 진료과\n으로 검색해주세요')


