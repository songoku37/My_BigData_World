# 본 프로그램은 동적인 웹페이지를 크롤링하는 프로그램입니다.
# 작성 시작일자 2021. 04. 16
# 작성자 이성재
# Selenium.py
# 셀레니움을 사용하여 구글 이미지 검색을 시작합니다.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys

# 크롬 열고 검색하기
path = "chromedriver/chromedriver.exe" # 웹 드라이버가 있는 경로
driver = webdriver.Chrome(path)
driver.get("https://www.google.co.kr/imghp?hl=ko") # 구글 이미지 메인 페이지
elem = driver.find_element_by_name("q") # 검색 부분에 name이 q이다
elem.send_keys("배우") # 검색하고자 하는 것
elem.send_keys(Keys.RETURN) # 엔터값 전송 크롤링이라는 글자를 입력하고 엔터를 누르는 과정


# 페이지 끝까지 스크롤 내리기
SCROLL_PAUSE_TIME = 1 # 대기시간을 1초로 셋팅

# 스크롤 깊이 측정하기 자바스크립트문을 실행시킴
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # 스크롤 끝까지 내리기
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 페이지 로딩 기다리기
    time.sleep(SCROLL_PAUSE_TIME)

    # 더 보기 요소가 있을 경우 클릭하기
    new_height = driver.execute_script("return document.body.scrollHeight")


    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click() # 더 보기에 css name이 mye4qd이다
        except:
            break
    last_height = new_height

# 이미지를 찾고 , 다운받기
image_path = "c:/actor/" # 이미지 저장될 경로 설정
images_list = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
# class 명이 rg_i Q4LuWd 이지만 .으로 구분하고 css가 2개 적용된 거임
# images_list는 배열이다 즉 여러개 이미지의 정보를 넣는다

count = 1
for image in images_list:
    try :

        image.click() # 크롬 브라우저에서 작은 이미지를 클릭하는 효과와 동일
        time.sleep(2)  # 2초 기다린다.
        # f12을 사용하여 개발자모드에서 검사-> copy -> Copy Xpath를 해서 경로를 가지고 온다
        try :
            imgUrl = driver.find_element_by_xpath("//*[@id=\"Sva75c\"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img").get_attribute("src")
        except Exception as e :
            print(e)
        # "" 안에 " 기호를 쓰기위해 \ 로 감싸준다
        print("imgUrl : ", imgUrl)
        # 이미지를 urllib.request를 사용하여 저장
        # xpath 값 ,  저장될 공간 + 크롤링(이름)
        urllib.request.urlretrieve(imgUrl, image_path+"actor" + str(count) + ".jpg")

        count = count + 1

    except:
        print("이미지를 저장할 수 없습니다.")
        pass # 에러 발생시 무시하고 계속 진행

# 프로그램 종료
driver.close()