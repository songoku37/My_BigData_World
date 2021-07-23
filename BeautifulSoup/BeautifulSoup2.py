import requests
from bs4 import BeautifulSoup as bs

tag = "<p class='big_data01' id='uniq01'> Hello World </p>"
soup = bs(tag,'html.parser')

# 태그 이름으로 특정
data01 = soup.find('p')
print(data01) # 출력 : <p class="big_data01" id="uniq01"> Hello World </p>

data01_text = soup.find('p').text # Hello World
print(data01_text) # 출력 :

# 클래스 이름으로 특정
data03 = soup.find(class_='big_data01')
print(data03) # 출력 : <p class="big_data01" id="uniq01"> Hello World </p>

data03_text = soup.find(class_='big_data01').text
print(data03_text) # 출력 : Hello World
