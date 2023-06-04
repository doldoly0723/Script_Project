import requests
import xml.etree.ElementTree as ET
from tkinter import*
from tkinter import font
from tkinter.ttk import Combobox
from PIL import Image, ImageTk


class MainGUI:
    Si_Do_list = ["","서울특별시", "부산광역시", "대구광역시", "인천광역시", "광주광역시", "대전광역시", "울산광역시", "세종특별시",
                  "경기도", "강원도", "충청북도", "충청남도", "전라북도", "전라남도", "경상북도", "경상남도", "제주특별자치도"]
    seoul_list = ["","강남구", "강동구", "강북구", "강서구", "관악구", "광진구", "구로구", "금천구", "노원구", "도봉구", "동대문구", "동작구", "마포구",
                  "서대문구", "서초구", "성동구", "성북구", "송파구", "양천구", "영등포구", "용산구", "은평구", "종로구", "중구", "중랑구"]
    busan_list = ["","중구", "서구", "동구", "영도구", "부산진구", "동래구", "남구", "북구", "해운대구", "사하구", "금정구", "강서구", "연제구", "수영구", "사상구",
                  "기장군"]
    daegu_list = ["","중구","동구","서구","남구","북구","수성구","달서구","달성군","군위군"]
    incheon_list =["","중구","동구","미추홀구","연수구","남동구","부평구","계양구","서구","강화군","옹진군"]
    gwangju_list=["","동구","서구","남구","북구","광산구"]
    daejeon_list=["","동구","중구","서구","유성구","대덕구"]
    ulsan_list=["","중구","남구","동구","북구","울주군"]
    sejong_list=["","조치원읍","금남면","부강면","소정면","연기면","연동면","연서면","장군면","전동면","전의면",
                 "고운동","나성동","다정동","대평동","도담동","반곡동","보람동","소담동","새롬동","아름동","어진동","종촌동","한솔동","해밀동"]
    gyeonggi_do_list=["","수원시","성남시","의정부시","안양시","부천시","광명시","평택시","동두천시","안산시","고양시","과천시","의왕시","구리시","남양주시","오산시","시흥시","군포시",
                      "하남시","용인시","파주시","이천시","안성시","김포시","화성시","광주시","양주시","포천시","여주시","연천군","가평군","양평군"]
    gangwon_do_list=["","춘천시","원주시","강릉시","동해시","태백시","속초시","삼척시","홍천군","횡성군","영월군","평창군","정선군","철원군","화천군","양구군","인제군","고성군","양양군"]
    chung_cheong_bukdo = ["","청주시","충주시","제천시","보은군","옥천군","영동군","증평군","진천군","괴산군","음성군","단양군"]
    chung_cheong_namdo = ["","천안시","공주시","보령시","아산시","서산시","논산시","계룡시","당진시","금산군","부여군","서천군","청양군","홍성군","예산군","태안군"]
    jeolla_bukdo = ["","전주시","군산시","익산시","정읍시","남원시","김제시","완주군","진안군","무주군","장수군","임실군","순창군","고창군","부안군"]
    jeolla_namdo = ["","목포시","여수시","순천시","나주시","광양시","담양군","곡성군","구례군","고흥군","보성군",
                    "화순군","장흥군","강진군","해남군","영암군","무안군","함평군","영광군","장성군","완도군","진도군","신안군"]
    gyeongsang_bukdo=["","포항시","경주시","김천시","안동시","구미시","영주시","영천시","상주시","문경시","경산시","군위군","의성군",
                      "청송군","영양군","영덕군","청도군","고령군","성주군","칠곡군","예천군","봉화군","울진군","울릉군"]
    gyeongsang_namdo=["","창원시","진주시","통영시","사천시","김해시","밀양시","거제시","양산시","의령군","함안군","창녕군","고성군","남해군","하동군","산청군","함양군","거창군","합천군"]
    jeju_do=["","제주시","서귀포시"]

    HpSubject_list=["","내과", "소아청소년과", "신경과", "정신건강의학과", "피부과", "외과", "흉부외과", "정형외과", "신경외과", "성형외과",
               "산부인과", "안과", "이비인후과", "비뇨기과", "재활의학과", "마취통증의학과", "영상의학과", "치료방사선과", "임상병리과",
               "해부병리과", "가정의학과", "핵의학과", "응급의학과", "치과", "구강악안면외과"]
    HpSubject_dict={
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
    service_key = "+nq6kOXB0yaZ9BZzYUlRNHDMMcE81wG+uSs7gw7I2EBE8aQwTtxTssfXO3g4RPat2f3jmxy7Nht1ya3rpysfPw=="

    def __init__(self):
        self.InitMain()
    def InitMain(self):
        self.window = Tk()
        self.window.title("우리 동네 병원 찾기")
        self.window.geometry("800x600")
        self.TempFont = font.Font(size=20, weight='bold', family='Consolas')
        self.TempFont2 = font.Font(size=16, weight='bold', family='Consolas')

        # 프레임 구분을 위해 색칠
        frame1 = Frame(self.window, width=800, height=100, bg='#efefef')  # 상단 프레임 생성
        frame1.place(x=0, y=0)  # 상단에 프레임 배치
        label = Label(frame1, text="우리 동네 병원 찾기", font=self.TempFont, bg="#efefef")  # 라벨 생성
        label.place(relx=0.5, rely=0.5, anchor=CENTER)

        frame2 = Frame(self.window, width=400, height=500, bg='white')  # 왼쪽 프레임 생성
        frame2.place(x=0, y=100)  # 왼쪽에 프레임 배치
        # 병원 이미지(로고)
        logo_image = Image.open('image/병원마크.png')
        image_tk = ImageTk.PhotoImage(logo_image)
        image_label = Label(frame2, image=image_tk)
        image_label.place(x=72, y=122)

        frame3 = Frame(self.window, width=400, height=500, bg='#e74b47')  # 오른쪽 프레임 생성
        frame3.place(x=400, y=100)  # 오른쪽에 프레임 배치

        self.SearchButton = Button(frame3, text="검색", font=self.TempFont, width=20,height=3, command=self.InitSearch)
        self.SymptomButton = Button(frame3, text="내 증상", font=self.TempFont, width=20,height=3, command=self.InitSearch)
        self.MapButton = Button(frame3, text="지도", font=self.TempFont, width=20,height=3, command=self.InitSearch)

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

        #시도 콤보박스
        label = Label(self.Searchframe_left, text="시,도 선택", font=self.TempFont)
        label.place(x=0, y=10)


        self.selected_si_gu = StringVar()
        self.selected_si_gu.set("서울특별시")  # 초기값 설정
        #gu_options = set(i for i in Si_Do_list)
        self.si_do_combo = Combobox(self.Searchframe_left, textvariable=self.selected_si_gu, values=self.Si_Do_list)
        self.si_do_combo.place(x=150, y=15)

        #시구군 콤보박스
        self.selected_sigungu = StringVar()
        self.selected_sigungu.set("강남구")
        self.sigungu_combo = Combobox(self.Searchframe_left, textvariable=self.selected_sigungu, values=self.seoul_list)
        self.sigungu_combo.place(x=400, y=15)

        self.si_do_combo.bind("<<ComboboxSelected>>", self.Update_ComboBox)

        label = Label(self.Searchframe_left, text="검색어:", font=self.TempFont)
        label.place(x=0,y=70)

        self.nameSearch_entry = Entry(self.Searchframe_left, relief='solid',font=self.TempFont, width=27)
        self.nameSearch_entry.place(x=80, y=70)

        button = Button(self.Searchframe_left, text='병원 이름 검색', font=self.TempFont, command=self.nameSearch)
        button.place(x=425, y=60)

        self.frame_imformation = Frame(self.Searchframe_left, width=500, height=550, relief='solid', borderwidth=2, bg='red')
        self.frame_imformation.place(x=50, y=100)
        
    def destroy_nameSearch_frame(self):
        if self.NameSearchFrame:
            self.NameSearchFrame.destroy()

    def create_fieldSearch_frame(self):
        self.FieldSearchFrame = Frame(self.SearchWindow, width=1200, height=700, bg='green')
        self.FieldSearchFrame.place(x=0, y=100)
    def destroy_fieldSearch_frame(self):
        if self.FieldSearchFrame:
            self.FieldSearchFrame.destroy()

    def nameSearch(self):
        self.frame_imformation.destroy()
        self.frame_imformation = Frame(self.Searchframe_left, width=500, height=550, relief='solid', borderwidth=2,
                                       bg='red')
        self.frame_imformation.place(x=50, y=100)

        self.Searchframe_right.destroy()
        self.Searchframe_right = Frame(self.NameSearchFrame, width=600, height=700, relief='solid', borderwidth=2)
        self.Searchframe_right.place(x=600, y=0)
        """
        getHsptlMdcncListInfoInqire
        getHsptlMdcncLcinfoInqire
        getHsptlBassInfoInqire
        getBabyListInfoInqire
        getBabyLcinfoInqire
        getHsptlMdcncFullDown
        """

        # 공공데이터포털에서 발급받은 디코딩되지 않은 인증키 입력
        queryParams = {'serviceKey': self.service_key,"Q0": self.si_do_combo.get(),"Q1": self.sigungu_combo.get(), "QN": self.nameSearch_entry.get(), "numOfRows": 100}
        response = requests.get(self.url1, params=queryParams)
        root = ET.fromstring(response.text)

        for item in root.iter("item"):
            if self.nameSearch_entry.get() == item.findtext("dutyName"):
                Params = {'serviceKey': self.service_key, "HPID": item.findtext("hpid"), "numOfRows": 10}
                Response = requests.get(self.url3, params=Params)
                Root = ET.fromstring(Response.text)

                header = ["Name", "Addr", "Tel", "Time"]
                ypos = 0
                for Item in Root.iter('item'):
                    HpName = Item.findtext("dutyName")
                    Hpaddr = Item.findtext("dutyAddr")
                    Hptelno = Item.findtext("dutyTel1")
                    HpworkStart = Item.findtext("dutyTime1s")
                    HpworkEnd = Item.findtext("dutyTime1c")
                    HpSubject = Item.findtext("dgidIdName")
                    HPworkTime = str(HpworkStart) + "~" + str(HpworkEnd)


                    label = Label(self.frame_imformation, text="병원 이름: " + HpName, font=self.TempFont)
                    label.place(x=0, y=ypos)
                    label2 = Label(self.frame_imformation, text="병원 주소: ", font=self.TempFont)
                    label2.place(x=0, y=ypos + 30)
                    label2 = Label(self.frame_imformation, text=Hpaddr, font=self.TempFont)
                    label2.place(x=0, y=ypos + 60)
                    label3 = Label(self.frame_imformation, text="전화번호: " + Hptelno, font=self.TempFont)
                    label3.place(x=0, y=ypos + 90)
                    label4 = Label(self.frame_imformation, text="운영 시간: " + HPworkTime, font=self.TempFont)
                    label4.place(x=0, y=ypos + 120)
                    label5 = Label(self.frame_imformation, text="진료 과목", font=self.TempFont)
                    label5.place(x=0, y=ypos + 150)
                    ypos += 180
                    if HpSubject != None:
                        xpos = 0
                        cnt = 0
                        subjectList = HpSubject.split(',')
                        for sub in subjectList:
                            label5 = Label(self.frame_imformation, text=sub, font=self.TempFont)
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
                    self.DivNam = item.findtext("dutyDivNam")   #분야별 분류를 위한 변수
                    queryParams1 = {'serviceKey': self.service_key, "Q0": self.si_do_combo.get(),
                                    "Q1": self.sigungu_combo.get(), "QZ": self.hospital_types[item.findtext("dutyDivNam")],"pageNo": self.page_cnt, "numOfRows": 20}
                    response1 = requests.get(self.url1, params=queryParams1)
                    root1 = ET.fromstring(response1.text)
                    ypos = 0

                    label = Label(self.Searchframe_right, text="해당 지역 " + item.findtext("dutyDivNam") + " 목록", font=self.TempFont)
                    label.place(x=0, y=ypos)

                    button_back = Button(self.Searchframe_right, text="->", command=self.back_button, font=self.TempFont)
                    button_back.place(x=550, y=650)
                    button_front = Button(self.Searchframe_right, text="<-", command=self.front_button, font=self.TempFont)
                    button_front.place(x=0, y=650)

                    ypos += 30
                    for item1 in root1.iter("item"):
                        hpName = item1.findtext("dutyName")
                        label = Label(self.Searchframe_right, text=hpName, font=self.TempFont)
                        label.place(x=0, y=ypos)
                        ypos+=30

            else:   # 병원 이름이 아닌 치과 이런식으로 병원명 만 적을 때
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

                button_back = Button(self.Searchframe_right, text="->", command=self.front_button,
                                        font=self.TempFont)
                button_back.place(x=550, y=650)
                button_front = Button(self.Searchframe_right, text="<-", command=self.back_button,
                                        font=self.TempFont)
                button_front.place(x=0, y=650)

                ypos += 30
                for item1 in root1.iter("item"):
                    hpName = item1.findtext("dutyName")
                    label = Label(self.Searchframe_right, text=hpName, font=self.TempFont)
                    label.place(x=0, y=ypos)
                    ypos += 30
            break
    def back_button(self):
        if self.page_cnt >=1:
            self.Searchframe_right.destroy()
            self.Searchframe_right = Frame(self.NameSearchFrame, width=600, height=700, relief='solid', borderwidth=2)
            self.Searchframe_right.place(x=600, y=0)
            self.page_cnt += 1
            queryParams1 = {'serviceKey': self.service_key, "Q0": self.si_do_combo.get(),
                            "Q1": self.sigungu_combo.get(), "QZ": self.hospital_types[self.DivNam],
                            "pageNo": self.page_cnt, "numOfRows": 20}
            response1 = requests.get(self.url1, params=queryParams1)
            root1 = ET.fromstring(response1.text)
            ypos = 0

            label = Label(self.Searchframe_right, text="해당 지역 " + self.DivNam + " 목록",
                          font=self.TempFont)
            label.place(x=0, y=ypos)

            button_back = Button(self.Searchframe_right, text="->", command=self.back_button, font=self.TempFont)
            button_back.place(x=550, y=650)
            button_front = Button(self.Searchframe_right, text="<-", command=self.front_button, font=self.TempFont)
            button_front.place(x=0, y=650)

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
            queryParams1 = {'serviceKey': self.service_key, "Q0": self.si_do_combo.get(),
                            "Q1": self.sigungu_combo.get(), "QZ": self.hospital_types[self.DivNam],
                            "pageNo": self.page_cnt, "numOfRows": 20}
            response1 = requests.get(self.url1, params=queryParams1)
            root1 = ET.fromstring(response1.text)
            ypos = 0

            label = Label(self.Searchframe_right, text="해당 지역 " + self.DivNam + " 목록",
                          font=self.TempFont)
            label.place(x=0, y=ypos)

            button_back = Button(self.Searchframe_right, text="->", command=self.back_button, font=self.TempFont)
            button_back.place(x=550, y=650)
            button_front = Button(self.Searchframe_right, text="<-", command=self.front_button, font=self.TempFont)
            button_front.place(x=0, y=650)

            ypos += 30
            for item1 in root1.iter("item"):
                hpName = item1.findtext("dutyName")
                label = Label(self.Searchframe_right, text=hpName, font=self.TempFont)
                label.place(x=0, y=ypos)
                ypos += 30

    def fieldSearch(self):
        pass
    def InitSearch(self):
        self.window.destroy()
        self.SearchWindow = Tk()
        self.SearchWindow.geometry("1200x800")
        self.TempFont = font.Font(size=16, weight='bold', family='Consolas')

        frame1 = Frame(self.SearchWindow, width=1200, height=100, bg="gray")
        frame1.place(x=0, y=0)
        label = Label(frame1, text="병원 검색", font=self.TempFont, bg="gray")  # 라벨 생성
        label.place(relx=0.5, rely=0.5, anchor=CENTER)

        # 홈버튼 추가
        home = Button(self.SearchWindow, width=10, height=5, bg='white', command=self.SearchtoHome)
        home.place(x=5, y=5)

        self.NameSearchVar = IntVar()  # 이름 검색 체크박스 변수
        self.FieldSearchVar = IntVar()
        self.NameSearchCheckbox = Checkbutton(frame1, text="이름 검색",font=self.TempFont, variable=self.NameSearchVar, bg='gray', command=self.check_name_search)
        self.FieldSearchCheckbox = Checkbutton(frame1, text="분야 검색",font=self.TempFont, variable=self.FieldSearchVar, bg='gray', command=self.check_field_search)
        self.NameSearchCheckbox.place(relx=0.7, rely=0.5, anchor=CENTER)
        self.FieldSearchCheckbox.place(relx=0.85, rely=0.5, anchor=CENTER)

        self.NameSearchFrame = None
        self.FieldSearchFrame = None


        self.SearchWindow.mainloop()
    def InitMap(self):
        self.window.destroy()
        self.MapWindow = Tk()
        self.MapWindow.geometry("1200x600")
        self.MapWindow.mainloop()
    def InitSymptom(self):
        self.window.destroy()
        self.SymptomWindow = Tk()
        self.SymptomWindow.geometry("800x600")
        self.SymptomWindow.mainloop()

    # 홈버튼 함수
    def SearchtoHome(self):
        self.SearchWindow.destroy()
        self.InitMain()



MainGUI()