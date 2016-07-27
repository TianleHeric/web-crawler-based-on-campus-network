from wtforms import Form, SelectField, SubmitField
import bs4
import requests

class serarchForm(Form):
    area=SelectField(label='教学区',choices=[('3','主校区')])
    building=SelectField(label='教学楼',choices=[('80','综合楼'),('1021','科研楼'),('10','19楼'),('164','教一楼'),('126','教五楼')])
    weekTime=SelectField(label='周次',choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),('18','18'),('19','19')])
    dayTime=SelectField(label='日期',choices=[('1','周一'),('2','周二'),('3','周三'),('4','周四'),('5','周五'),('6','周六'),('7','周日')])
    submit=SubmitField('submit')

def getHtml(buildInfor,weekInfor,dayinfor,cook):
    datas={'aid':'3','buildingid':buildInfor,'room':'-1','whichweek':weekInfor,'week':dayinfor,'Submit':'确定'}
    url="http://202.204.105.22/academic/teacher/teachresource/roomschedule_week.jsdo"
    response=requests.post(url,data=datas,cookies=cook)
    htmlForSchedule=str(response.text)
    print(datas,cook)
    return htmlForSchedule

def getTableZonghelou(html):
    mainSoup=bs4.BeautifulSoup(html,'html.parser')
    s=mainSoup.find('body').find_all('table')[1].contents
    script1=[]
    script2=[]
    script3=[]
    script4=[]
    script5=[]
    table=[script1,script2,script3,script4,script5]
    tagRoomList=[]

    for tagRoom in s:
        if str(type(tagRoom))=="<class 'bs4.element.Tag'>":
            if tagRoom.name=='tr':
                tagRoomList.append(tagRoom)
    tableIterator=0
    roomNumber=1
    scriptNumber=1
    while scriptNumber<10:
        while roomNumber<34:
            if tagRoomList[roomNumber].contents[13].contents[0].contents[3].contents[scriptNumber].contents==['\xa0']:
                table[tableIterator].append(tagRoomList[roomNumber].contents[1].contents[0])
            roomNumber+=1
        tableIterator+=1
        scriptNumber+=2
        roomNumber=1
    return table

def getTableKeyanlou(html):
    mainSoup=bs4.BeautifulSoup(html,'html.parser')
    s=mainSoup.find('body').find_all('table')[1].contents
    script1=[]
    script2=[]
    script3=[]
    script4=[]
    script5=[]
    table=[script1,script2,script3,script4,script5]
    tagRoomList=[]
    for tagRoom in s:
        if str(type(tagRoom))=="<class 'bs4.element.Tag'>":
            if tagRoom.name=='tr':
                tagRoomList.append(tagRoom)
    tableIterator=0
    roomNumber=1
    scriptNumber=1
    while scriptNumber<10:
        while roomNumber<30:
            if tagRoomList[roomNumber].contents[13].contents[0].contents[3].contents[scriptNumber].contents==['\xa0']:
                table[tableIterator].append(tagRoomList[roomNumber].contents[1].contents[0])
            roomNumber+=1
        tableIterator+=1
        scriptNumber+=2
        roomNumber=1
    return table



def getTableJiaoyilou(html):
    mainSoup=bs4.BeautifulSoup(html,'html.parser')
    s=mainSoup.find('body').find_all('table')[1].contents
    script1=[]
    script2=[]
    script3=[]
    script4=[]
    script5=[]
    table=[script1,script2,script3,script4,script5]
    tagRoomList=[]
    for tagRoom in s:
        if str(type(tagRoom))=="<class 'bs4.element.Tag'>":
            if tagRoom.name=='tr':
                tagRoomList.append(tagRoom)
    tableIterator=0
    roomNumber=1
    scriptNumber=1
    while scriptNumber<10:
        while roomNumber<11:
            if tagRoomList[roomNumber].contents[13].contents[0].contents[3].contents[scriptNumber].contents==['\xa0']:
                table[tableIterator].append(tagRoomList[roomNumber].contents[1].contents[0])
            roomNumber+=1
        tableIterator+=1
        scriptNumber+=2
        roomNumber=1
    return table


    pass

def getTableShijiulou(html):
    mainSoup=bs4.BeautifulSoup(html,'html.parser')
    s=mainSoup.find('body').find_all('table')[1].contents
    script1=[]
    script2=[]
    script3=[]
    script4=[]
    script5=[]
    table=[script1,script2,script3,script4,script5]
    tagRoomList=[]
    for tagRoom in s:
        if str(type(tagRoom))=="<class 'bs4.element.Tag'>":
            if tagRoom.name=='tr':
                tagRoomList.append(tagRoom)
    tableIterator=0
    roomNumber=1
    scriptNumber=1
    while scriptNumber<10:
        while roomNumber<18:
            if tagRoomList[roomNumber].contents[13].contents[0].contents[3].contents[scriptNumber].contents==['\xa0']:
                table[tableIterator].append(tagRoomList[roomNumber].contents[1].contents[0])
            roomNumber+=1
        tableIterator+=1
        scriptNumber+=2
        roomNumber=1
    return table

def getTableJiaowulou(html):
    mainSoup=bs4.BeautifulSoup(html,'html.parser')
    s=mainSoup.find('body').find_all('table')[1].contents
    script1=[]
    script2=[]
    script3=[]
    script4=[]
    script5=[]
    table=[script1,script2,script3,script4,script5]
    tagRoomList=[]
    for tagRoom in s:
        if str(type(tagRoom))=="<class 'bs4.element.Tag'>":
            if tagRoom.name=='tr':
                tagRoomList.append(tagRoom)
    tableIterator=0
    roomNumber=1
    scriptNumber=1
    while scriptNumber<10:
        while roomNumber<17:
            if tagRoomList[roomNumber].contents[13].contents[0].contents[3].contents[scriptNumber].contents==['\xa0']:
                table[tableIterator].append(tagRoomList[roomNumber].contents[1].contents[0])
            roomNumber+=1
        tableIterator+=1
        scriptNumber+=2
        roomNumber=1
    return table


