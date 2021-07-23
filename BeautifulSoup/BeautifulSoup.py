
import requests
from bs4 import BeautifulSoup as bs

html = requests.get('https://search.naver.com/search.naver?'
                    'sm=tab_hty.top&where=nexearch&query=%EB%82%A0%EC%94%A8&oquery=%EB%'
                    '82%A0%EC%94%A8&tqi=hZrKcsprvOsssQswMTwssssssUh-229279') # 주소를 받는다
soup = bs(html.text,'html.parser') # HTML 소스코드 가져옴

data1 = soup.find('div',{'class':'detail_box'}) # soup의 div라는 태그를 찾고 그 중에서 detai1_box라는 태그를 가져온다
print(data1) # 출력 : <div class="detail_box"> <dl class="indicator"> <dt>....

data2 = data1.findAll('dd') # 가져온 것중에서 dd태그를 다 가져온다 (리스트로 담김)
print(data2) # 출력 : [<dd class="lv2"><span class="num">48㎍/㎥</span>보통<span class="ico"></span></dd>, <dd cla

dust01 = data2[0].find('span',{'class':'num'}).text # dd태그 중에서 span이란 태그를 찾고 그 중에서 num이라는 클래스 선언한 거 찾기
print(dust01) # 출력 : 48㎍/㎥

dust02 = data2[1].find('span',{'class':'num'}).text # 초미세먼지
print(dust02) # 출력 : 32㎍/㎥

O3 = data2[2].find('span',{'class':'num'}).text # 오존
print(O3) # 출력 : 0.092ppm

data3 = soup.find('div',{'class':'main_info'}) # main_info 클래스 안에 있는 거 다 보여줌
print(data3) # 출력 : <div class="main_info"> <span class..

degree = data3.find('span',{'class':'todaytemp'}).text # text 안 붙히면 <span class="todaytemp">13</span>가 출력 됨
print(degree) # 출력 : 31
