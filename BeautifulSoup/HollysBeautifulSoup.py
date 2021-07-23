# 본프로그램은 정적인 웹페이지를 크롤링 하는 프로그램입니다.
# 작성 시작일자 2021. 03. 19
# 작성자 이성재
# 할리스매장 클롤링연습01
# 프로그램명 HollysBeautifulSoup.py
# 첫페이지만 크롤링하는 예제
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

html = requests.get('http://web.codetector.co.kr:8080/kmview/bigdata01.do')
soup = bs(html.text,'html.parser')

# 크롤링 할 영역을 찾는다
tbody_tag = soup.find('tbody') # tobdy태그에 들어감
print(tbody_tag) # 출력 : <tbody id="data_uniq1"> <tr class="t....

# 반복되는 영역을 찾는다 (findAll로 찾으면 데이터가 배열형태로 저장된다)
tr_tag_list = tbody_tag.findAll('tr') # tr을 전부 찾아서 list에 넣는다
print(tr_tag_list) # 출력 : [<tr class="tr_...   tr_tag값 확인해보기
print(len(tr_tag_list)) # 출력 : 10   tr_tag_list 속에 몇개 인지

# 크롤링한 결과가 최종적으로 저장되는 변수배열
result = []

for tr_tag in tr_tag_list: # tr_tag_list에서 하나씩 순차적으로 값을 꺼내온다.

    # td 태그중에 각각의 영역에 해당하는 데이터를 저장한다.
    zone    = tr_tag.find('td',{'class':'text-center zone'}).text # 지역
    store   = tr_tag.find('td',{'class':'text-center store'}).text # 매장명
    open    = tr_tag.find('td',{'class':'text-center open'}).text # 현황
    address = tr_tag.find('td',{'class':'text-center address'}).text # 주소
    tel     = tr_tag.find('td',{'class':'text-center tel'}).text # 전화번호

    # 각각의 변수에 잘 저장되어 있는지 확인을 해본다
    # print(zone + "," + store + "," + open + "," + address + "," + tel)

    # 변수배열에 순차적으로 저장한다.
    result.append([zone, store , open , address, tel])



# pandas 라이브러리를 이용해 csv파일로 저장
print(result[0]) # 출력: ['서울 서대문구', '신촌점', '영업중', '서울특별시 서대문구 연세로 34 (창천동 31-12)  할리스', '02-393-2004']
# result값이 배열이므로 배열값중 하나(첫번째)를 화면에 표시해본다.
bigdata_table = pd.DataFrame(result, columns=('zone','store','open','address','tel'))
bigdata_table.to_csv("HollysCSV.csv", encoding="utf-8", mode ='w' ,index = True) # ./ 자기 밑에