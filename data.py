import requests
import xml.etree.ElementTree as ET
import tkinter

#병원정보 서비스 예제
url = 'http://apis.data.go.kr/B552657/HsptlAsembySearchService/getHsptlMdcncListInfoInqire?'
# 공공데이터포털에서 발급받은 디코딩되지 않은 인증키 입력
service_key = "%p0G8yABKFtyj10jCeKUNMg2z57VzwUivtRjuOXFSab4sBeGoiFChJUStZNBvWySow%2BI%2BpEPnyeU%2BHxMqM5Z3OA%3D%3D"
queryParams = {'serviceKey': service_key, 'pageNo': '1', 'numOfRows': '10'}

response = requests.get(url, params=queryParams)
print(response.text)
root = ET.fromstring(response.text)

window = tkinter.Tk()
window.title("병원정보")

frame = tkinter.Frame(window)
frame.pack()

header = ["Name", "Addr", "Tel", "Url"]

for i, col_name in enumerate(header):
    label = tkinter.Label(frame, text=col_name, font=("Helvetica", 14, "bold"))
    label.grid(row=0, column=i)

row_count = 1
for item in root.iter("item"):
    yadmNm = item.findtext("dutyName")
    print(yadmNm)
    addr = item.findtext("dutyAddr")
    telno = item.findtext("dutyTel1")
    hospUrl = item.findtext("hospUrl")

    data = [yadmNm, addr, telno, hospUrl]
    for i, value in enumerate(data):
        label = tkinter.Label(frame, text=value, font=("Helvetica", 12))
        label.grid(row=row_count, column=i)

    row_count += 1

window.mainloop()