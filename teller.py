# 텔레그렘
"""import telepot
import noti"""

import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
import re
from datetime import date, datetime, timedelta
import traceback

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
    pass

def telHpSubject(user, sido, sidogun, Hpsubject):
    pass

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
    elif text.startswith('진료과') and len(args) >= 4:
        telHpSubject(chat_id, args[1], args[2], args[3])

    else:
        noti.sendMessage(chat_id, '모르는 명령어입니다.')


today = date.today()
current_month = today.strftime('%Y%m')

print( '[',today,']received token :', noti.TOKEN )

bot = telepot.Bot(noti.TOKEN)
pprint( bot.getMe() )

bot.message_loop(handle)

print('Listening...')

while 1:
  time.sleep(10)