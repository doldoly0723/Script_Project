# 텔레그렘 데이터 읽어오기
import requests
import xml.etree.ElementTree as ET
import telepot
import traceback
import sys


url1 = 'http://apis.data.go.kr/B552657/HsptlAsembySearchService/getHsptlMdcncListInfoInqire'
url3 = 'http://apis.data.go.kr/B552657/HsptlAsembySearchService/getHsptlBassInfoInqire'
service_key = "+nq6kOXB0yaZ9BZzYUlRNHDMMcE81wG+uSs7gw7I2EBE8aQwTtxTssfXO3g4RPat2f3jmxy7Nht1ya3rpysfPw=="
TOKEN = '6085039623:AAHl5X6rFLIiK5pCoSBpB7ykqVCjuSlg-jE'
bot = telepot.Bot(TOKEN)


def getSearchData(sido, sidogun, Hpname):
    queryParams = {'serviceKey': service_key, "Q0": sido, "Q1": sidogun,
                   "QN": Hpname, "numOfRows": 100}
    response = requests.get(url1, params=queryParams)
    root = ET.fromstring(response.text)

    data_dict={}
    # 여기서부터 실행이 안된다.
    for item in root.iter("item"):
        if Hpname == item.findtext('dutyName'):
            Params = {'serviceKey': service_key, "HPID": item.findtext("hpid"), "numOfRows": 10}
            Response = requests.get(url3, params=Params)
            Root = ET.fromstring(Response.text)
            for Item in Root.iter('item'):
                data_dict["HpName"] = Item.findtext("dutyName")
                data_dict["HpAddr"] = Item.findtext("dutyAddr")
                data_dict["Hptelno"] = Item.findtext("dutyTel1")
                HpworkStart = Item.findtext("dutyTime1s")
                HpworkEnd = Item.findtext("dutyTime1c")
                data_dict["HpSubject"] = Item.findtext("dgidIdName")
                data_dict["HPworkTime"] = str(HpworkStart) + "~" + str(HpworkEnd)
                return data_dict

def getHpcntDate(sido, sidogun):
    queryParams = {'serviceKey': service_key, "Q0": sido, "Q1": sidogun,
                   "numOfRows": 100000}
    response = requests.get(url1, params=queryParams)
    root = ET.fromstring(response.text)
    Hpcnt = {}
    for item in root.iter("item"):
        HpDivNam = item.findtext("dutyDivNam")
        if HpDivNam in Hpcnt:
            Hpcnt[HpDivNam] += 1
        else:
            Hpcnt[HpDivNam] = 1
    return Hpcnt
def getHpSubject_data(user, sido, sidogun, HpSymptom):
    queryParams = {'serviceKey': service_key, "Q0": sido, "Q1": sidogun,
                   "numOfRows": 50000}
    response = requests.get(url1, params=queryParams)
    root = ET.fromstring(response.text)
    Hpid_list = []
    for item in root.iter("item"):
        Hpid_list.append(item.findtext("hpid"))

    HpSymptom_list=[]

    for hpid in Hpid_list:
        Params = {'serviceKey': service_key, "HPID": hpid, "numOfRows": 10}
        Response = requests.get(url3, params=Params)
        Root = ET.fromstring(Response.text)
        for item in Root.iter("item"):
            HpSubject = item.findtext("dgidIdName")
            if HpSubject:
                HpSubject = HpSubject.split(',')
            else:
                HpSubject = []
            if HpSymptom in HpSubject:
                # 병원 이름, 진료과 출력
                HpName = item.findtext("dutyName")
                Hpaddr = item.findtext("dutyAddr")
                Hptelno = item.findtext("dutyTel1")
                msg = HpName + '\n' + Hpaddr + '\n' + Hptelno + '\n' + str(HpSubject) + '\n'
                sendMessage(user, msg)

def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except:
        traceback.print_exc(file=sys.stdout)