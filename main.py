import requests
import xml.etree.ElementTree as ET
from tkinter import*
from tkinter import font
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import tkinter.messagebox
from tkintermapview import TkinterMapView
import telepot
import teller
import noti
from pprint import pprint
from urllib.request import urlopen
import re
from datetime import date, datetime, timedelta
import traceback
import sys
import time
import sqlite3
import spam

class MainGUI:
    # 지역 정보
    Si_Do_list = ["", "서울특별시", "부산광역시", "대구광역시", "인천광역시", "광주광역시", "대전광역시", "울산광역시",
                  "세종특별시", "경기도", "강원도", "충청북도", "충청남도", "전라북도", "전라남도", "경상북도", "경상남도",
                  "제주특별자치도"]
    seoul_list = ["", "강남구", "강동구", "강북구", "강서구", "관악구", "광진구", "구로구", "금천구", "노원구", "도봉구",
                  "동대문구", "동작구", "마포구", "서대문구", "서초구", "성동구", "성북구", "송파구", "양천구", "영등포구",
                  "용산구", "은평구", "종로구", "중구", "중랑구"]
    busan_list = ["", "중구", "서구", "동구", "영도구", "부산진구", "동래구", "남구", "북구", "해운대구", "사하구", "금정구",
                  "강서구", "연제구", "수영구", "사상구", "기장군"]
    daegu_list = ["", "중구", "동구", "서구", "남구", "북구", "수성구", "달서구", "달성군", "군위군"]
    incheon_list = ["", "중구", "동구", "미추홀구", "연수구", "남동구", "부평구", "계양구", "서구", "강화군", "옹진군"]
    gwangju_list = ["", "동구", "서구", "남구", "북구", "광산구"]
    daejeon_list = ["", "동구", "중구", "서구", "유성구", "대덕구"]
    ulsan_list = ["", "중구", "남구", "동구", "북구", "울주군"]
    sejong_list = ["", "조치원읍", "금남면", "부강면", "소정면", "연기면", "연동면", "연서면", "장군면", "전동면", "전의면",
                   "고운동", "나성동", "다정동", "대평동", "도담동", "반곡동", "보람동", "소담동", "새롬동", "아름동", "어진동",
                   "종촌동", "한솔동", "해밀동"]
    gyeonggi_do_list = ["", "수원시", "성남시", "의정부시", "안양시", "부천시", "광명시", "평택시", "동두천시", "안산시",
                        "고양시", "과천시", "의왕시", "구리시", "남양주시", "오산시", "시흥시", "군포시", "하남시", "용인시",
                        "파주시", "이천시", "안성시", "김포시", "화성시", "광주시", "양주시", "포천시", "여주시", "연천군",
                        "가평군", "양평군"]
    gangwon_do_list = ["", " 춘천시", "원주시", "강릉시", "동해시", "태백시", "속초시", "삼척시", "홍천군", "횡성군", "영월군",
                       "평창군", "정선군", "철원군", "화천군", "양구군", "인제군", "고성군", "양양군"]
    chung_cheong_bukdo = ["", "청주시", "충주시", "제천시", "보은군", "옥천군", "영동군", "증평군", "진천군", "괴산군",
                          "음성군", "단양군"]
    chung_cheong_namdo = ["", "천안시", "공주시", "보령시", "아산시", "서산시", "논산시", "계룡시", "당진시", "금산군",
                          "부여군", "서천군", "청양군", "홍성군", "예산군", "태안군"]
    jeolla_bukdo = ["", "전주시", "군산시", "익산시", "정읍시", "남원시", "김제시", "완주군", "진안군", "무주군", "장수군",
                    "임실군", "순창군", "고창군", "부안군"]
    jeolla_namdo = ["", "목포시", "여수시", "순천시", "나주시", "광양시", "담양군", "곡성군", "구례군", "고흥군", "보성군",
                    "화순군", "장흥군", "강진군", "해남군", "영암군", "무안군", "함평군", "영광군", "장성군", "완도군", "진도군",
                    "신안군"]
    gyeongsang_bukdo = ["", "포항시", "경주시", "김천시", "안동시", "구미시", "영주시", "영천시", "상주시", "문경시", "경산시",
                        "군위군", "의성군", "청송군", "영양군", "영덕군", "청도군", "고령군", "성주군", "칠곡군", "예천군",
                        "봉화군", "울진군", "울릉군"]
    gyeongsang_namdo = ["", "창원시", "진주시", "통영시", "사천시", "김해시", "밀양시", "거제시", "양산시", "의령군", "함안군",
                        "창녕군", "고성군", "남해군", "하동군", "산청군", "함양군", "거창군", "합천군"]
    jeju_do = ["", "제주시", "서귀포시"]

    # 병원 정보
    HpSubject_list = ["", "내과", "소아청소년과", "신경과", "정신건강의학과", "피부과", "외과", "흉부외과", "정형외과",
                      "신경외과", "성형외과", "산부인과", "안과", "이비인후과", "비뇨기과", "재활의학과", "마취통증의학과",
                      "영상의학과", "치료방사선과", "임상병리과", "해부병리과", "가정의학과", "핵의학과", "응급의학과",
                      "치과", "구강악안면외과"]
    HpSubject_dict = {
        "내과": "D001",
        "소아청소년과": "D002",
        "신경과": "D003",
        "정신건강의학과": "D004",
        "피부과": "D005",
        "외과": "D006",
        "흉부외과": "D007",
        "정형외과": "D008",
        "신경외과": "D009",
        "성형외과": "D010",
        "산부인과": "D011",
        "안과": "D012",
        "이비인후과": "D013",
        "비뇨기과": "D014",
        "재활의학과": "D016",
        "마취통증의학과": "D017",
        "영상의학과": "D018",
        "치료방사선과": "D019",
        "임상병리과": "D020",
        "해부병리과": "D021",
        "가정의학과": "D022",
        "핵의학과": "D023",
        "응급의학과": "D024",
        "치과": "D026",
        "구강악안면외과": "D034"
    }

    hospital_types = {
        "종합병원": "A",
        "병원": "B",
        "의원": "C",
        "요양병원": "D",
        "한방병원": "E",
        "한의원": "G",
        "기타": "I",
        "치과의원": "N",
        "치과병원": "M",
        "보건소": "R",
        "기타(구급차)": "W"
    }

    url1 = 'http://apis.data.go.kr/B552657/HsptlAsembySearchService/getHsptlMdcncListInfoInqire'
    url3 = 'http://apis.data.go.kr/B552657/HsptlAsembySearchService/getHsptlBassInfoInqire'
    service_key = spam.spam_key()

    # 텔레그램 연동을 위한 코드
    today = date.today()
    current_month = today.strftime('%Y%m')

    print('[', today, ']received token :', noti.TOKEN)

    bot = telepot.Bot(noti.TOKEN)
    pprint(bot.getMe())

    bot.message_loop(teller.handle)

    print('Listening...')

    def __init__(self):
        self.InitMain()

    def InitMain(self):
        self.window = Tk()
        self.window.title("우리 동네 병원 찾기")
        self.window.geometry("800x600")
        self.TempFont = font.Font(size=20, weight='bold', family='맑은 고딕')
        self.TempFont2 = font.Font(size=16, weight='bold', family='맑은 고딕')
        self.mainscreenfont = font.Font(size=24, weight='bold', family='맑은 고딕')

        # 프레임 구분을 위해 색칠
        frame1 = Frame(self.window, width=800, height=100, bg='#efefef')  # 상단 프레임 생성
        frame1.place(x=0, y=0)  # 상단에 프레임 배치
        label = Label(frame1, text="우리 동네 병원 찾기", font=self.TempFont, bg="#efefef")  # 라벨 생성
        label.place(relx=0.5, rely=0.5, anchor=CENTER)

        frame2 = Frame(self.window, width=400, height=500, bg='white')  # 왼쪽 프레임 생성
        frame2.place(x=0, y=100)  # 왼쪽에 프레임 배치

        # 병원 이미지(로고)
        logo_image = Image.open('image/Cross.png').resize((200, 200))
        logo_image_tk = ImageTk.PhotoImage(logo_image)
        image_label = Label(frame2, image=logo_image_tk, bg='white')
        image_label.place(x=100, y=150)

        frame3 = Frame(self.window, width=400, height=500, bg='#ed5151')  # 오른쪽 프레임 생성
        frame3.place(x=400, y=100)  # 오른쪽에 프레임 배치

        # 버튼 이미지
        search_image = Image.open('image/Search.png').resize((40, 40))
        search_image_tk = ImageTk.PhotoImage(search_image)

        symptom_image = Image.open('image/Symptom.png').resize((40, 40))
        symptom_image_tk = ImageTk.PhotoImage(symptom_image)

        map_image = Image.open('image/Map.png').resize((40, 40))
        map_image_tk = ImageTk.PhotoImage(map_image)

        self.SearchButton = Button(frame3, text="검색", image=search_image_tk, compound='left', font=self.mainscreenfont,
                                   width=300, height=100, command=self.InitSearch)
        self.SymptomButton = Button(frame3, text="증상", image=symptom_image_tk, compound='left',
                                    font=self.mainscreenfont, width=300, height=100, command=self.InitSymptom)
        self.MapButton = Button(frame3, text="지도", image=map_image_tk, compound='left', font=self.mainscreenfont,
                                width=300, height=100, command=self.InitMap)

        self.SearchButton.place(relx=0.5, rely=0.2, anchor=CENTER)  # 버튼을 프레임에 배치 (위에서 아래로 순서대로)
        self.SymptomButton.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.MapButton.place(relx=0.5, rely=0.8, anchor=CENTER)

        self.window.mainloop()

    # 둘 중 하나의 체크 박스만 선택할 수 있도록 수정
    def check_name_search(self):
        if self.NameSearchVar.get() == 1:
            self.create_nameSearch_frame()
            self.destroy_fieldSearch_frame()
            self.FieldSearchVar.set(0)
        else:
            self.destroy_nameSearch_frame()

    def check_field_search(self):
        if self.FieldSearchVar.get() == 1:
            self.create_fieldSearch_frame()
            self.destroy_nameSearch_frame()
            self.NameSearchVar.set(0)
        else:
            self.destroy_fieldSearch_frame()

    # 콤보박스 업데이트
    def Update_ComboBox(self, event):
        if self.si_do_combo.get() == "서울특별시":
            self.selected_sigungu.set(self.seoul_list[0])
            self.sigungu_combo['values'] = self.seoul_list
        elif self.si_do_combo.get() == "부산광역시":
            self.selected_sigungu.set(self.busan_list[0])
            self.sigungu_combo['values'] = self.busan_list
        elif self.si_do_combo.get() == "대구광역시":
            self.selected_sigungu.set(self.daegu_list[0])
            self.sigungu_combo['values'] = self.daegu_list
        elif self.si_do_combo.get() == "인천광역시":
            self.selected_sigungu.set(self.incheon_list[0])
            self.sigungu_combo['values'] = self.incheon_list
        elif self.si_do_combo.get() == "광주광역시":
            self.selected_sigungu.set(self.gwangju_list[0])
            self.sigungu_combo['values'] = self.gwangju_list
        elif self.si_do_combo.get() == "대전광역시":
            self.selected_sigungu.set(self.daejeon_list[0])
            self.sigungu_combo['values'] = self.daejeon_list
        elif self.si_do_combo.get() == "울산광역시":
            self.selected_sigungu.set(self.ulsan_list[0])
            self.sigungu_combo['values'] = self.ulsan_list
        elif self.si_do_combo.get() == "세종특별시":
            self.selected_sigungu.set(self.sejong_list[0])
            self.sigungu_combo['values'] = self.sejong_list
        elif self.si_do_combo.get() == "경기도":
            self.selected_sigungu.set(self.gyeonggi_do_list[0])
            self.sigungu_combo['values'] = self.gyeonggi_do_list
        elif self.si_do_combo.get() == "강원도":
            self.selected_sigungu.set(self.gangwon_do_list[0])
            self.sigungu_combo['values'] = self.gangwon_do_list
        elif self.si_do_combo.get() == "충청북도":
            self.selected_sigungu.set(self.chung_cheong_bukdo[0])
            self.sigungu_combo['values'] = self.chung_cheong_bukdo
        elif self.si_do_combo.get() == "충청남도":
            self.selected_sigungu.set(self.chung_cheong_namdo[0])
            self.sigungu_combo['values'] = self.chung_cheong_namdo
        elif self.si_do_combo.get() == "전라북도":
            self.selected_sigungu.set(self.jeolla_bukdo[0])
            self.sigungu_combo['values'] = self.jeolla_bukdo
        elif self.si_do_combo.get() == "전라남도":
            self.selected_sigungu.set(self.jeolla_namdo[0])
            self.sigungu_combo['values'] = self.jeolla_namdo
        elif self.si_do_combo.get() == "경상북도":
            self.selected_sigungu.set(self.gyeongsang_bukdo[0])
            self.sigungu_combo['values'] = self.gyeongsang_bukdo
        elif self.si_do_combo.get() == "경상남도":
            self.selected_sigungu.set(self.gyeongsang_namdo[0])
            self.sigungu_combo['values'] = self.gyeongsang_namdo
        elif self.si_do_combo.get() == "제주특별자치도":
            self.selected_sigungu.set(self.jeju_do[0])
            self.sigungu_combo['values'] = self.jeju_do

    def create_nameSearch_frame(self):
        self.NameSearchFrame = Frame(self.SearchWindow, width=1200, height=700)
        self.NameSearchFrame.place(x=0, y=100)
        self.Searchframe_left = Frame(self.NameSearchFrame, width=600, height=700,  relief='solid', borderwidth=2)
        self.Searchframe_left.place(x=0, y=0)
        self.Searchframe_right = Frame(self.NameSearchFrame, width=600, height=700, relief='solid', borderwidth=2)
        self.Searchframe_right.place(x=600, y=0)

        # 시도 콤보박스
        label = Label(self.Searchframe_left, text="시,도 선택", font=self.TempFont)
        label.place(x=0, y=10)

        self.selected_si_gu = StringVar()
        self.selected_si_gu.set("서울특별시")  # 초기값 설정

        self.si_do_combo = Combobox(self.Searchframe_left, textvariable=self.selected_si_gu, values=self.Si_Do_list)
        self.si_do_combo.place(x=150, y=15)

        # 시구군 콤보박스
        self.selected_sigungu = StringVar()
        self.selected_sigungu.set("강남구")
        self.sigungu_combo = Combobox(self.Searchframe_left, textvariable=self.selected_sigungu, values=self.seoul_list)
        self.sigungu_combo.place(x=400, y=15)

        self.si_do_combo.bind("<<ComboboxSelected>>", self.Update_ComboBox)

        label = Label(self.Searchframe_left, text="검색어:", font=self.TempFont)
        label.place(x=0, y=70)

        self.nameSearch_entry = Entry(self.Searchframe_left, relief='solid', font=self.TempFont, width=27)
        self.nameSearch_entry.place(x=80, y=70)

        button = Button(self.Searchframe_left, text='병원 이름 검색', font=self.TempFont, command=self.nameSearch)
        button.place(x=425, y=60)

        self.frame_imformation = Frame(self.Searchframe_left, width=500, height=550, relief='solid', borderwidth=2,
                                       bg='#f3a8a8')
        self.frame_imformation.place(x=50, y=100)
        
    def destroy_nameSearch_frame(self):
        if self.NameSearchFrame:
            self.NameSearchFrame.destroy()

    def create_fieldSearch_frame(self):
        self.FieldSearchFrame = Frame(self.SearchWindow, width=1200, height=700, bg='#f3a8a8')
        self.FieldSearchFrame.place(x=0, y=100)

        # 시도 콤보박스
        label = Label(self.FieldSearchFrame, text="시,도 선택", font=self.TempFont)
        label.place(x=5, y=13)

        self.selected_si_gu = StringVar()
        self.selected_si_gu.set("서울특별시")  # 초기값 설정
        # gu_options = set(i for i in Si_Do_list)
        self.si_do_combo = Combobox(self.FieldSearchFrame, textvariable=self.selected_si_gu, values=self.Si_Do_list,
                                    font=self.TempFont)
        self.si_do_combo.place(x=150, y=13)

        label = Label(self.FieldSearchFrame, text="시,군,구 선택", font=self.TempFont)
        label.place(x=600, y=13)

        # 시구군 콤보박스
        self.selected_sigungu = StringVar()
        self.selected_sigungu.set("강남구")
        self.sigungu_combo = Combobox(self.FieldSearchFrame, textvariable=self.selected_sigungu,
                                      values=self.seoul_list, font=self.TempFont)
        self.sigungu_combo.place(x=770, y=13)

        self.si_do_combo.bind("<<ComboboxSelected>>", self.Update_ComboBox)

        button = Button(self.FieldSearchFrame, text='검색', font=self.TempFont, command=self.fieldSearch, width=8)
        button.place(x=1100, y=7)

        self.fieldBarChart = Frame(self.FieldSearchFrame, width=1200, height=650, bg='white')
        self.fieldBarChart.place(x=0, y=50)

    def destroy_fieldSearch_frame(self):
        if self.FieldSearchFrame:
            self.FieldSearchFrame.destroy()

    def nameSearch(self):
        self.frame_imformation.destroy()
        self.frame_imformation = Frame(self.Searchframe_left, width=500, height=550, relief='solid', borderwidth=2,
                                       bg='#f3a8a8')
        self.frame_imformation.place(x=50, y=100)

        self.Searchframe_right.destroy()
        self.Searchframe_right = Frame(self.NameSearchFrame, width=600, height=700, relief='solid', borderwidth=2)
        self.Searchframe_right.place(x=600, y=0)

        # index label
        self.page_cnt = 1
        self.index_label = Label(self.SearchWindow, text=self.page_cnt, bg='white', font=self.TempFont2, width=2)
        self.index_label.place(x=900, y=752)

        # 공공데이터포털에서 발급받은 디코딩되지 않은 인증키 입력
        queryParams = {'serviceKey': self.service_key, "Q0": self.si_do_combo.get(), "Q1": self.sigungu_combo.get(),
                       "QN": self.nameSearch_entry.get(), "numOfRows": 100}
        response = requests.get(self.url1, params=queryParams)
        root = ET.fromstring(response.text)

        for item in root.iter("item"):
            if self.nameSearch_entry.get() == item.findtext("dutyName"):
                Params = {'serviceKey': self.service_key, "HPID": item.findtext("hpid"), "numOfRows": 10}
                Response = requests.get(self.url3, params=Params)
                Root = ET.fromstring(Response.text)

                ypos = 0
                for Item in Root.iter('item'):
                    HpName = Item.findtext("dutyName")
                    Hpaddr = Item.findtext("dutyAddr")
                    Hptelno = Item.findtext("dutyTel1")
                    HpworkStart = Item.findtext("dutyTime1s")
                    HpworkEnd = Item.findtext("dutyTime1c")
                    HpSubject = Item.findtext("dgidIdName")
                    HPworkTime = str(HpworkStart) + "~" + str(HpworkEnd)

                    label = Label(self.frame_imformation, text="병원 이름: " + HpName, font=self.TempFont, bg='#f3a8a8')
                    label.place(x=0, y=ypos)
                    label2 = Label(self.frame_imformation, text="병원 주소: ", font=self.TempFont, bg='#f3a8a8')
                    label2.place(x=0, y=ypos + 30)
                    label2 = Label(self.frame_imformation, text=Hpaddr, font=self.TempFont, bg='#f3a8a8')
                    label2.place(x=0, y=ypos + 60)
                    label3 = Label(self.frame_imformation, text="전화번호: " + Hptelno, font=self.TempFont, bg='#f3a8a8')
                    label3.place(x=0, y=ypos + 90)
                    label4 = Label(self.frame_imformation, text="운영 시간: " + HPworkTime, font=self.TempFont,
                                   bg='#f3a8a8')
                    label4.place(x=0, y=ypos + 120)
                    label5 = Label(self.frame_imformation, text="진료 과목", font=self.TempFont, bg='#f3a8a8')
                    label5.place(x=0, y=ypos + 150)
                    ypos += 180

                    if HpSubject is not None:
                        xpos = 0
                        cnt = 0
                        subjectList = HpSubject.split(',')
                        for sub in subjectList:
                            label5 = Label(self.frame_imformation, text=sub, font=self.TempFont, bg='#f3a8a8')
                            label5.place(x=xpos, y=ypos)
                            if len(sub) > 7:
                                xpos += 340
                                cnt += 2
                            else:
                                xpos += 170
                                cnt += 1
                            if cnt >= 3:
                                xpos = 0
                                ypos += 30
                                cnt = 0

                    # 오른쪽에 비슷한 과 출력
                    # 진료과가 여러개일 경우:
                    # 의원일 경우 과를 비교 , 아닐 경우 병원 분류명으로 분류
                    self.page_cnt = 1
                    self.DivNam = item.findtext("dutyDivNam")   # 분야별 분류를 위한 변수
                    queryParams1 = {'serviceKey': self.service_key, "Q0": self.si_do_combo.get(),
                                    "Q1": self.sigungu_combo.get(),
                                    "QZ": self.hospital_types[item.findtext("dutyDivNam")],
                                    "pageNo": self.page_cnt, "numOfRows": 20}
                    response1 = requests.get(self.url1, params=queryParams1)
                    root1 = ET.fromstring(response1.text)
                    ypos = 0

                    label = Label(self.Searchframe_right, text="해당 지역 " + item.findtext("dutyDivNam") + " 목록",
                                  font=self.TempFont)
                    label.place(x=0, y=ypos)

                    button_back = Button(self.Searchframe_right, text="->", command=self.back_button,
                                         font=self.TempFont, bg='white')
                    button_back.place(x=550, y=650)
                    button_front = Button(self.Searchframe_right, text="<-", command=self.front_button,
                                          font=self.TempFont, bg='white')
                    button_front.place(x=10, y=650)

                    ypos += 30
                    for item1 in root1.iter("item"):
                        hpName = item1.findtext("dutyName")
                        label = Label(self.Searchframe_right, text=hpName, font=self.TempFont)
                        label.place(x=0, y=ypos)
                        ypos += 30

            else:   # 병원 이름이 아닌 '치과' 같은 병원명 만 적었을 경우
                self.page_cnt = 1
                self.DivNam = item.findtext("dutyDivNam")
                queryParams1 = {'serviceKey': self.service_key, "Q0": self.si_do_combo.get(),
                                "Q1": self.sigungu_combo.get(),
                                "QZ": self.hospital_types[item.findtext("dutyDivNam")], "pageNo": self.page_cnt,
                                "numOfRows": 20}
                response1 = requests.get(self.url1, params=queryParams1)
                root1 = ET.fromstring(response1.text)
                ypos = 0

                label = Label(self.Searchframe_right, text="해당 지역 " + item.findtext("dutyDivNam") + " 목록",
                              font=self.TempFont)
                label.place(x=0, y=ypos)

                button_back = Button(self.Searchframe_right, text="->", command=self.back_button,
                                     font=self.TempFont, bg='white')
                button_back.place(x=550, y=650)
                button_front = Button(self.Searchframe_right, text="<-", command=self.front_button,
                                      font=self.TempFont, bg='white')
                button_front.place(x=10, y=650)

                ypos += 30
                for item1 in root1.iter("item"):
                    hpName = item1.findtext("dutyName")
                    label = Label(self.Searchframe_right, text=hpName, font=self.TempFont)
                    label.place(x=0, y=ypos)
                    ypos += 30
            break

    def fieldSearch(self):
        self.fieldBarChart.destroy()
        self.fieldBarChart = Frame(self.FieldSearchFrame, width=1200, height=650, bg='gray')
        self.fieldBarChart.place(x=0, y=50)

        queryParams = {'serviceKey': self.service_key, "Q0": self.si_do_combo.get(), "Q1": self.sigungu_combo.get(),
                       "numOfRows": 100000}
        response = requests.get(self.url1, params=queryParams)
        root = ET.fromstring(response.text)
        Hpcnt = {}
        for item in root.iter("item"):
            HpDivNam = item.findtext("dutyDivNam")
            if HpDivNam in Hpcnt:
                Hpcnt[HpDivNam] += 1
            else:
                Hpcnt[HpDivNam] = 1
        # 딕셔너리 생성 완료

        c_width = 1200
        c_height = 650
        c = Canvas(self.fieldBarChart, width=c_width, height=c_height, bg='white')
        c.pack()

        max_value = max(Hpcnt.values())
        y_stretch = 400 / max_value  # 비율로 막대 높이 조정
        y_gap = 20
        x_width = 40
        x_gap = 70

        x = x_gap
        for label, value in Hpcnt.items():
            # calculate rectangle coordinates
            x0 = x
            y0 = c_height - (value * y_stretch + y_gap)
            x1 = x + x_width
            y1 = c_height - y_gap

            # draw the bar
            c.create_rectangle(x0, y0, x1, y1, fill="red")
            c.create_text(x0 + 2, y0, anchor=SW, text=str(value))

            # draw the label
            c.create_text(x0 + x_width // 2, c_height - 5, anchor=S, text=label)

            x += x_width + x_gap

    # 병원 검색을 위한 앞뒤 버튼
    # 다른 검색과는 호환이 안됨
    def back_button(self):
        if self.page_cnt >= 1:
            self.Searchframe_right.destroy()
            self.Searchframe_right = Frame(self.NameSearchFrame, width=600, height=700, relief='solid', borderwidth=2)
            self.Searchframe_right.place(x=600, y=0)
            self.page_cnt += 1
            self.index_label.configure(text=self.page_cnt)

            queryParams1 = {'serviceKey': self.service_key, "Q0": self.si_do_combo.get(),
                            "Q1": self.sigungu_combo.get(), "QZ": self.hospital_types[self.DivNam],
                            "pageNo": self.page_cnt, "numOfRows": 20}
            response1 = requests.get(self.url1, params=queryParams1)
            root1 = ET.fromstring(response1.text)
            ypos = 0

            label = Label(self.Searchframe_right, text="해당 지역 " + self.DivNam + " 목록",
                          font=self.TempFont)
            label.place(x=0, y=ypos)

            button_back = Button(self.Searchframe_right, text="->", command=self.back_button, font=self.TempFont,
                                 bg='white')
            button_back.place(x=550, y=650)
            button_front = Button(self.Searchframe_right, text="<-", command=self.front_button, font=self.TempFont,
                                  bg='white')
            button_front.place(x=10, y=650)

            ypos += 30
            for item1 in root1.iter("item"):
                hpName = item1.findtext("dutyName")
                label = Label(self.Searchframe_right, text=hpName, font=self.TempFont)
                label.place(x=0, y=ypos)
                ypos += 30

    def front_button(self):
        if self.page_cnt > 1:
            self.Searchframe_right.destroy()
            self.Searchframe_right = Frame(self.NameSearchFrame, width=600, height=700, relief='solid', borderwidth=2)
            self.Searchframe_right.place(x=600, y=0)
            self.page_cnt -= 1
            self.index_label.configure(text=self.page_cnt)

            queryParams1 = {'serviceKey': self.service_key, "Q0": self.si_do_combo.get(),
                            "Q1": self.sigungu_combo.get(), "QZ": self.hospital_types[self.DivNam],
                            "pageNo": self.page_cnt, "numOfRows": 20}
            response1 = requests.get(self.url1, params=queryParams1)
            root1 = ET.fromstring(response1.text)
            ypos = 0

            label = Label(self.Searchframe_right, text="해당 지역 " + self.DivNam + " 목록",
                          font=self.TempFont)
            label.place(x=0, y=ypos)

            button_back = Button(self.Searchframe_right, text="->", command=self.back_button, font=self.TempFont,
                                 bg='white')
            button_back.place(x=550, y=650)
            button_front = Button(self.Searchframe_right, text="<-", command=self.front_button, font=self.TempFont,
                                  bg='white')
            button_front.place(x=10, y=650)

            ypos += 30
            for item1 in root1.iter("item"):
                hpName = item1.findtext("dutyName")
                label = Label(self.Searchframe_right, text=hpName, font=self.TempFont)
                label.place(x=0, y=ypos)
                ypos += 30

    def InitSearch(self):
        self.window.destroy()
        self.SearchWindow = Tk()
        self.SearchWindow.geometry("1200x800")

        # 폰트
        self.TempFont = font.Font(size=12, weight='bold', family='맑은 고딕')
        self.TempFont2 = font.Font(size=16, weight='bold', family='맑은 고딕')
        self.mainscreenfont = font.Font(size=24, weight='bold', family='맑은 고딕')

        # 버튼 이미지
        self.home_image = Image.open('image/Home.png').resize((40, 40))
        self.home_image_tk = ImageTk.PhotoImage(self.home_image)

        frame1 = Frame(self.SearchWindow, width=1200, height=100, bg="#ed5151")
        frame1.place(x=0, y=0)
        label = Label(frame1, text="병원 검색", font=self.mainscreenfont, bg="#ed5151")  # 라벨 생성
        label.place(relx=0.5, rely=0.5, anchor=CENTER)

        # 홈버튼 추가
        home = Button(self.SearchWindow, width=85, height=85, image=self.home_image_tk, bg='white',
                      command=self.SearchtoHome)
        home.place(x=5, y=5)

        self.NameSearchVar = IntVar()  # 이름 검색 체크박스 변수
        self.FieldSearchVar = IntVar()
        self.NameSearchCheckbox = Checkbutton(frame1, text="이름 검색", font=self.TempFont2,
                                              variable=self.NameSearchVar, bg='#ed5151', command=self.check_name_search)
        self.FieldSearchCheckbox = Checkbutton(frame1, text="분야 검색", font=self.TempFont2,
                                               variable=self.FieldSearchVar, bg='#ed5151',
                                               command=self.check_field_search)
        self.NameSearchCheckbox.place(relx=0.7, rely=0.5, anchor=CENTER)
        self.FieldSearchCheckbox.place(relx=0.85, rely=0.5, anchor=CENTER)

        self.NameSearchFrame = None
        self.FieldSearchFrame = None

        self.SearchWindow.mainloop()

    def InitMap(self):
        WIDTH = 1200
        HEIGHT = 800

        # 폰트
        MapFont = font.Font(size=12, weight='bold', family='맑은 고딕')

        self.window.destroy()
        self.mapwindow = Tk()

        self.mapwindow.title("지도")
        self.mapwindow.geometry(f"{WIDTH}x{HEIGHT}")

        # 상단 프레임
        frame1 = Frame(self.mapwindow, width=1200, height=100, bg="#ed5151")
        frame1.place(x=0, y=0)

        # 지도 프레임
        frame2 = Frame(self.mapwindow, width=1200, height=700, bg="#f3a8a8")
        frame2.place(x=0, y=100)

        # 버튼 이미지
        home_image = Image.open('image/Home.png').resize((40, 40))
        home_image_tk = ImageTk.PhotoImage(home_image)

        # 홈버튼
        home = Button(self.mapwindow, width=85, height=85, image=home_image_tk, bg='white',
                      command=self.MaptoHome)
        home.place(x=5, y=5)

        # frame1 텍스트 라벨
        label = Label(frame1, text='병원 이름 검색', font=MapFont, fg='black', bg='#ed5151')
        label.place(x=200, y=40)

        # 검색창
        self.search_bar = Entry(frame1, width=80)
        self.search_bar.place(x=350, y=40)
        self.search_bar.focus()

        # 검색 버튼
        self.search_bar_button = Button(master=frame1, width=10, text="Search", command=self.search, bg='white')
        self.search_bar_button.place(x=1000, y=36)

        # 검색 초기화 버튼
        self.search_bar_clear = Button(master=frame1, width=10, text="Clear", command=self.clear, bg='white')
        self.search_bar_clear.place(x=1100, y=36)

        # 지도
        self.map_widget = TkinterMapView(width=WIDTH-20, height=700-20)
        self.map_widget.place(x=10, y=110)

        # 초기 화면
        self.map_widget.set_address('seoul')

        self.mapwindow.mainloop()

    def search(self):
        if self.search_bar.get() == '':
            pass
        else:
            # 마커 초기화
            self.map_widget.delete_all_marker()

            # 데이터 불러오기 (수정)
            queryParams = {'serviceKey': self.service_key, "QN": self.search_bar.get(), "numOfRows": 10000}
            response = requests.get(self.url1, params=queryParams)
            root = ET.fromstring(response.text)
            marker_dict = {}
            for item in root.iter("item"):
                HpName = item.findtext('dutyName')
                HpLongitude = str(round(float(item.findtext('wgs84Lon')), 4))
                HpLatitude = str(round(float(item.findtext('wgs84Lat')), 4))
                if HpLatitude+' '+HpLongitude not in marker_dict:
                    marker_dict[HpLatitude+' '+HpLongitude] = [HpName]
                else:
                    marker_dict[HpLatitude + ' ' + HpLongitude][0] += ', '+HpName

            for k, v in marker_dict.items():
                lat, long = k.split()
                self.map_widget.set_marker(float(lat), float(long), text=v[0])

    def clear(self):
        self.search_bar.delete(0, last=tkinter.END)

    def Symptom_next(self):
        self.index_value += 1

        self.frame_detail.destroy()
        self.frame_detail = Frame(self.SymptomWindow, width=1200, height=650)
        self.frame_detail.place(x=0, y=150)
        self.Symptom_nextButton = Button(self.frame_detail, text="->", font=self.TempFont, command=self.Symptom_next,
                                         bg='white')
        self.Symptom_nextButton.place(x=1170, y=620)
        self.Symptom_backButton = Button(self.frame_detail, text='<-', font=self.TempFont, command=self.Symptom_back,
                                         bg='white')
        self.Symptom_backButton.place(x=10, y=620)
        cnt = 0
        ypos = 0

        for i in range(self.index_list[self.index_value], len(self.Hpid_list)-1):
            Params = {'serviceKey': self.service_key, "HPID": self.Hpid_list[i], "numOfRows": 10}
            Response = requests.get(self.url3, params=Params)
            Root = ET.fromstring(Response.text)

            for item in Root.iter("item"):
                HpSubject = item.findtext("dgidIdName")
                if HpSubject:
                    HpSubject = HpSubject.split(',')
                else:
                    HpSubject = []
                if self.selected_Symptom.get() in HpSubject:
                    # 병원 이름, 진료과 출력
                    HpName = item.findtext("dutyName")
                    Hpaddr = item.findtext("dutyAddr")
                    Hptelno = item.findtext("dutyTel1")
                    label = Label(self.frame_detail, text=HpName + "  " + Hpaddr + "  " + Hptelno + " ",
                                  font=self.TempFont)
                    label.place(x=0, y=ypos)
                    ypos += 20
                    label_text = ', '.join(HpSubject)

                    label = Label(self.frame_detail, text="진료과" + "  " + label_text)
                    label.place(x=0, y=ypos)
                    ypos += 50
                    cnt += 1
            if cnt == 9:
                self.index_list.append(self.Hpid_list.index(self.Hpid_list[i]) + 1)
                break

    def Symptom_back(self):
        if self.index_value != 0:
            self.index_value -= 1

            self.frame_detail.destroy()
            self.frame_detail = Frame(self.SymptomWindow, width=1200, height=650)
            self.frame_detail.place(x=0, y=150)
            self.Symptom_nextButton = Button(self.frame_detail, text="->", font=self.TempFont,
                                             command=self.Symptom_next, bg='white')
            self.Symptom_nextButton.place(x=1170, y=620)
            self.Symptom_backButton = Button(self.frame_detail, text='<-', font=self.TempFont,
                                             command=self.Symptom_back, bg='white')
            self.Symptom_backButton.place(x=10, y=620)

            cnt = 0
            ypos = 0

            for i in range(self.index_list[self.index_value], len(self.Hpid_list) - 1):
                Params = {'serviceKey': self.service_key, "HPID": self.Hpid_list[i], "numOfRows": 10}
                Response = requests.get(self.url3, params=Params)
                Root = ET.fromstring(Response.text)

                for item in Root.iter("item"):
                    HpSubject = item.findtext("dgidIdName")
                    if HpSubject:
                        HpSubject = HpSubject.split(',')
                    else:
                        HpSubject = []
                    if self.selected_Symptom.get() in HpSubject:
                        # 병원 이름, 진료과 출력
                        HpName = item.findtext("dutyName")
                        Hpaddr = item.findtext("dutyAddr")
                        Hptelno = item.findtext("dutyTel1")
                        label = Label(self.frame_detail, text=HpName + "  " + Hpaddr + "  " + Hptelno + " ",
                                      font=self.TempFont)
                        label.place(x=0, y=ypos)
                        ypos += 20
                        label_text = ', '.join(HpSubject)

                        label = Label(self.frame_detail, text="진료과" + "  " + label_text)
                        label.place(x=0, y=ypos)
                        ypos += 50
                        cnt += 1
                if cnt == 9:
                    self.index_list.pop()
                    break

    def SearchSymptom(self):
        # 증상 초기화
        for i in range(25):
            self.info_label[i].destroy()

        queryParams = {'serviceKey': self.service_key, "Q0": self.si_do_combo.get(), "Q1": self.sigungu_combo.get(),
                       "numOfRows": 50000}
        response = requests.get(self.url1, params=queryParams)
        root = ET.fromstring(response.text)
        self.Hpid_list = []
        for item in root.iter("item"):
            self.Hpid_list.append(item.findtext("hpid"))
        self.Symptom_nextButton = Button(self.frame_detail, text="->", font=self.TempFont, command=self.Symptom_next,
                                         bg='white')
        self.Symptom_nextButton.place(x=1170, y=620)
        self.Symptom_backButton = Button(self.frame_detail, text='<-', font=self.TempFont, command=self.Symptom_back,
                                         bg='white')
        self.Symptom_backButton.place(x=10, y=620)

        cnt = 0
        ypos = 0
        self.index_list = [0]
        self.index_value = 0

        for hpid in self.Hpid_list:
            Params = {'serviceKey': self.service_key, "HPID": hpid, "numOfRows": 10}
            Response = requests.get(self.url3, params=Params)
            Root = ET.fromstring(Response.text)

            for item in Root.iter("item"):
                HpSubject = item.findtext("dgidIdName")
                if HpSubject:
                    HpSubject = HpSubject.split(',')
                else:
                    HpSubject = []
                if self.selected_Symptom.get() in HpSubject:
                    # 병원 이름, 진료과 출력
                    HpName = item.findtext("dutyName")
                    Hpaddr = item.findtext("dutyAddr")
                    Hptelno = item.findtext("dutyTel1")

                    label = Label(self.frame_detail, text=HpName + "  " + Hpaddr + "  " + Hptelno + " ",
                                  font=self.TempFont)
                    label.place(x=0, y=ypos)
                    ypos += 20
                    label_text = ', '.join(HpSubject)

                    label = Label(self.frame_detail, text="진료과" + "  " + label_text)
                    label.place(x=0, y=ypos)
                    ypos += 50
                    cnt += 1
            if cnt == 9:
                self.index_list.append(self.Hpid_list.index(hpid) + 1)
                break

    def symptomInfo(self):
        info = [
            '내과 - 복통, 속쓰림, 소화불량, 오심, 구토, 설사, 변비, 토혈, 혈변, 흑변, 체중감소',
            '소아청소년과 - 신생아질환, 소아 호흡기질환, 소아 소화기질환, 내분비질환, 혈액질환, 소아 감염성 질환, 소아 응급진료',
            '신경과 - 두통 및 어지럼증, 실신, 의식소실, 뇌졸중, 뇌막염 및 뇌염, 간질, 수면장애, 치매, 운동장애',
            '정신건강의학과 - 조현병, 기분장애, 불안장애, 치매 등의 주요 정신질환',
            '피부과 - 아토피피부염, 건선, 접촉피부염, 여드름 등의 피지선 관련 질환, 모발 및 손발톱질환, 하지의 염증성 결절, 수포성 및 결체조직질환, 피부암',
            '외과 - 신경외과, 흉부외과, 정형외과, 성형외과, 산부인과, 비뇨기과, 이비인후과, 안과, 소아외과 등의 전문분야로 독립한 분야를 제외한 나머지 모든 분야',
            '흉부외과 - 심장, 폐 및 식도질환과 혈관질환',
            '정형외과 - 수부, 견주관절, 족관절, 무릎, 고관절, 척추, 소아, 종양',
            '신경외과 - 뇌종양, 뇌혈관, 척추, 외상, 그리고 정위기능',
            '성형외과 - 선천기형, 구순구개열, 안면 외상, 사지 재건, 유방 재건, 흉터 성형술등의 재건 수술과 안검 성형 및 코 성형, 유방 성형, 지방이식술',
            '산부인과 - 고위험임신, 태아치료, 부인과 양성 및 악성 종양의 진단 및 치료, 난임 및 가임력 보존 치료, 미성년 여성질환의 치료 및 폐경 관리, 요실금 및 골반장기탈출증 진단 및 치료',
            '안과 - 각막 / 굴절이상질환, 백내장, 녹내장, 망막유리체질환, 포도막질환, 안운동이상(사시), 시신경질환, 선천유전질환, 희귀질환 관련 안과 이상',
            '이비인후과 - 중이염, 귀울림, 어지러움증과 비염, 소음성 난청, 알레르기성 비염, 축농증, 코 버섯, 편도염, 후두염, 음성질환, 두경부 암, 양성종양, 악성종양',
            '비뇨기과 - 콩팥(신장), 요관, 방광, 요도 등 요로계 장기들과 음경, 고환, 정관 및 전립선',
            '재활의학과 - 스포츠 손상, 척추손상 및 척수질환, 소아발달장애, 뇌성마비, 뇌졸증, 외상 후 뇌손상, 인지 재활',
            '마취통증의학과 - 마취, 수술 후 통증관리, 만성통증 치료',
            '영상의학과 - X - 선검사, 초음파검사, CT검사, MRI검사, 골밀도검사, 유방촬영',
            '치료방사선과 - 유방암, 두경부암, 폐암, 소화기암 등 각종 암에 대해 최적의 방사선 치료',
            '임상병리과 - 혈액, 소변, 대변, 체액, 조직 등 인체로부터 채취 되는 각종 검체에서 분자 및 세포 성분을 검사함으로써 질병의 선별, 조기 발견, 진단, 경과 관찰, 치료, 예후를 판정',
            '해부병리과',
            '가정의학과 - 성인병 및 만성질환, 피로, 기운 없음, 부종, 두통, 복통, 가슴 통증, 소화불량, 속쓰림, 기침, 가래, 관절통, 요통, 체중감소, 식욕감소 등의 증상에 대하여 종합적으로 접근하고 진단',
            '핵의학과 - 뇌신경질환, 심장질환, 악성종양 그리고 갑상선 질환 등 신체의 대부분 기관의 질환에 대하여 진단과 치료',
            '응급의학과 - 심폐소생, 쇼크, 중독 분야',
            '치과 - 신경치료, 충치치료, 치아미백, 임플란트, 잇몸염증, 발치, 교정치교, 틀니',
            '구강악안명외과 - 입(구강), 턱(악), 얼굴(안면)부위와 관련된 다양한 질환, 외상 및 재건, 그리고 선천적 또는 후천적 기형에 대한 전문적인 진단과 진료',
        ]

        self.frame_detail.destroy()

        self.frame_detail = Frame(self.SymptomWindow, width=1200, height=650)
        self.frame_detail.place(x=0, y=150)

        ypos = 0
        self.info_label = [Label(self.frame_detail, text='', font=self.TempFont) for _ in range(25)]
        for i in range(25):
            self.info_label[i].configure(text=info[i])
            self.info_label[i].place(x=0, y=ypos + i*25)

    def InitSymptom(self):
        self.window.destroy()
        self.SymptomWindow = Tk()
        self.SymptomWindow.geometry("1200x800")

        self.TempFont = font.Font(size=10, weight='bold', family='맑은 고딕')
        self.TempFont2 = font.Font(size=20, weight='bold', family='맑은 고딕')

        # 상단 프레임과 라벨
        frame1 = Frame(self.SymptomWindow, width=1200, height=100, bg="#ed5151")
        frame1.place(x=0, y=0)

        label = Label(frame1, text="현재 내 증상", font=self.TempFont2, bg="#ed5151")  # 라벨 생성
        label.place(relx=0.5, rely=0.5, anchor=CENTER)

        # 증상 설명 버튼
        symptomButton = Button(self.SymptomWindow, width=20, height=2, text='진료과 증상 설명', font=self.TempFont,
                               command=self.symptomInfo)
        symptomButton.place(x=1000, y=25)

        # 버튼 이미지
        home_image = Image.open('image/Home.png').resize((40, 40))
        home_image_tk = ImageTk.PhotoImage(home_image)

        # 홈버튼
        home = Button(self.SymptomWindow, width=85, height=85, image=home_image_tk, bg='white',
                      command=self.SymptomtoHome)
        home.place(x=5, y=5)

        # 콤보박스 만들기 지역, 구, 과
        # 지역, 구를 고르고 url1에서 해당 병원들 코드 가져와서
        # url3에서 가져온 코드로 검색하여 과가 해당 과에 존재시 출력?
        frame_main = Frame(self.SymptomWindow, width=1200, height=50, bg='#f3a8a8')
        frame_main.place(x=0, y=100)

        # 시도 콤보박스
        label = Label(frame_main, text="지역 선택", font=self.TempFont, bg='#f3a8a8')
        label.place(x=10, y=15)

        self.selected_si_gu = StringVar()
        self.selected_si_gu.set("서울특별시")  # 초기값 설정

        self.si_do_combo = Combobox(frame_main, textvariable=self.selected_si_gu, values=self.Si_Do_list, width=30)
        self.si_do_combo.place(x=120, y=15)


        # 시구군 콤보박스
        self.selected_sigungu = StringVar()
        self.selected_sigungu.set("강남구")

        self.sigungu_combo = Combobox(frame_main, textvariable=self.selected_sigungu, values=self.seoul_list, width=30)
        self.sigungu_combo.place(x=420, y=15)

        self.si_do_combo.bind("<<ComboboxSelected>>", self.Update_ComboBox)

        # 진료과 label
        label = Label(frame_main, text="진료과 선택", font=self.TempFont, bg='#f3a8a8')
        label.place(x=700, y=15)

        # 진료과 콤보박스
        self.selected_Symptom = StringVar()
        self.selected_Symptom.set("내과")
        self.Hpsubject_combo = Combobox(frame_main, textvariable=self.selected_Symptom, values=self.HpSubject_list,
                                        width=30)
        self.Hpsubject_combo.place(x=800, y=15)

        button = Button(frame_main, text='검색', font=self.TempFont, command=self.SearchSymptom, width=10)
        button.place(x=1100, y=10)

        self.frame_detail = Frame(self.SymptomWindow, width=1200, height=650)
        self.frame_detail.place(x=0, y=150)

        self.info_label = [Label(self.frame_detail, text='', font=self.TempFont) for _ in range(25)]

        self.SymptomWindow.mainloop()

    # 홈버튼 함수
    def SearchtoHome(self):
        self.SearchWindow.destroy()
        self.InitMain()

    def SymptomtoHome(self):
        self.SymptomWindow.destroy()
        self.InitMain()

    def MaptoHome(self):
        self.mapwindow.quit()
        self.mapwindow.destroy()
        self.InitMain()



MainGUI()