import requests
import xml.etree.ElementTree as ET
from tkinter import*
from tkinter import font
from PIL import Image, ImageTk

class MainGUI:
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

    def create_nameSearch_frame(self):
        self.NameSearchFrame = Frame(self.SearchWindow, width=1200, height=700)
        self.NameSearchFrame.place(x=0, y=100)
        self.Searchframe_left = Frame(self.NameSearchFrame, width=600, height=700,  relief='solid', borderwidth=2)
        self.Searchframe_left.place(x=0, y=0)
        frame_right = Frame(self.NameSearchFrame, width=600, height=700, relief='solid', borderwidth=2)
        frame_right.place(x=600, y=0)


        label = Label(self.Searchframe_left, text="검색어:", font=self.TempFont)
        label.place(x=0,y=10)

        self.nameSearch_entry = Entry(self.Searchframe_left, relief='solid',font=self.TempFont, width=27)
        self.nameSearch_entry.place(x=80, y=10)

        button = Button(self.Searchframe_left, text='병원 이름 검색', font=self.TempFont, command=self.nameSearch)
        button.place(x=425, y=1)

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
        """
        getHsptlMdcncListInfoInqire
        getHsptlMdcncLcinfoInqire
        getHsptlBassInfoInqire
        getBabyListInfoInqire
        getBabyLcinfoInqire
        getHsptlMdcncFullDown
        """
        url = 'http://apis.data.go.kr/B552657/HsptlAsembySearchService/getHsptlMdcncListInfoInqire'
        # 공공데이터포털에서 발급받은 디코딩되지 않은 인증키 입력
        service_key = "%2Bnq6kOXB0yaZ9BZzYUlRNHDMMcE81wG%2BuSs7gw7I2EBE8aQwTtxTssfXO3g4RPat2f3jmxy7Nht1ya3rpysfPw%3D%3D"

        queryParams = {'serviceKey': service_key, "QN": self.nameSearch_entry.get(), "numOfRows": 100}
        response = requests.get(url, params=queryParams)
        root = ET.fromstring(response.text)

        for item in root.iter("item"):
            if item.findtext("dutyName") == self.nameSearch_entry.get():
                print(item.findtext("dutyName"))
                print(item.findtext("hpid"))
                Url = 'http://apis.data.go.kr/B552657/HsptlAsembySearchService/getHsptlBassInfoInqire'
                Params = {'serviceKey': service_key, "HPID": item.findtext("hpid"), "numOfRows": 10}
                Response = requests.get(Url, params=Params)
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
                    subjectList = HpSubject.split(',')

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
                    xpos = 0
                    cnt = 0
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