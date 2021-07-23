# 본 프로그램은 텍스트 데이터를 빈도 분석
# 작성자 이성재
# 프로그램명 Frequency Analysis2.py

from bs4 import BeautifulSoup
import requests
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt

# 네이버 뉴스 검색하는 크롤링
def get_titles(search_word, start_num , end_num):
    title_list = []

    # start_num ~ end_num 까지 크롤링
    while 1:
        if start_num > end_num:
            return title_list
            break
        # print(title_list) 한 페이지에 제목을 한바퀴 돌 때 한 페이지 제목이 다 들어가 있음
        # 두번 돌면 .append 되어가지고 두개에 리스트가 아닌 한개의 리스트에 넣어짐

        url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={}&start={}'\
            .format(search_word,start_num) # 줄바꿈할 떈 이렇게 써야한다
        # print(url)

        req = requests.get(url)

        if req.ok : # .ok 참일시 제대로 URL 주소를 가져왔을 때
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')

            # 뉴스제목 뽑아오기
            titles = soup.select('.news_area a[title]') # class는 앞에 .을 붙힘 .news_area 그 안에 a태그 안에[]는 속성값

            # list에 넣어준다
            for title in titles:
                title_list.append(title.text)
                # print(title.text) # [올림픽] 도쿄 밝힌 희망의 성화…하나될 시간, 스포츠의 이름으로 (종합) ...
        start_num += 10

# 문장을 형태소로 분류
def sentence_tag(title_list):
    okt = Okt()
    sentences_tag = []

    # 형태소 분석하여 리스트에 넣기
    for sentence in title_list : # title_list에서 제목을 받아온 걸 sentence에 하나씩 넣는다
        morph = okt.pos(sentence) # 형태소 분석하는 과정 ('나',Noun)...
        sentences_tag.append(morph) # 형태소 분리한 걸 리스트에 넣음
        # print(morph)
    # print ("sentences_tag = ",sentences_tag) append를 했기 때문에 [[...],[...]] 형식으로 나옴
    return sentences_tag


# 단어별 카운트
def word_count(sentences_tag):
    noun_adj_list = []

    # 명사와 형용사만 구분하여 noun_adj_list에 넣기
    for sentence in sentences_tag :
        for word , tag in sentence: # word는 '도쿄' tag는 'Noun'
            print(word + " " + tag)
            if tag in ['Noun' , 'Adjective']:
                noun_adj_list.append(word) # 명사랑 형용사를 넣는 과정

    # 형태소별 count
    counts = Counter(noun_adj_list)
    # print(counts) # Counter({'aa': 2, 'dd': 1, 'cc': 1, 'bb': 1, 'ee': 1}) 이거처럼 개수를 분류해줌
    tags = counts.most_common() # most_common() 배열로 변환하는 함수
    # print(tags)
    return tags

# 단어별로 카운트된 데이터를 이미지화
def wordCloud_Image(word_count_list):

    # wordCloud 생성 (한글 폰트중 일부는 지원 않되는 것이 있음)
    wc = WordCloud(font_path="C:/Winodws/Fonts/batang.ttc", background_color = 'white', width = 800, height = 600)
    # 이미지할 때 필요한 설정 어떤 폰트로 어떤 바탕화면으로 어떤 크기로 할지
    counts = (dict(word_count_list)) # 배열로 만든 걸 사전형으로 변환
    # print(counts)

    cloud = wc.generate_from_frequencies(counts)
    plt.figure(figsize=(10,8))
    plt.axis('off')
    plt.imshow(cloud)
    plt.show()

title_list  = get_titles("올림픽",1, 200)
sentences_tag = sentence_tag(title_list)
word_count_list = word_count(sentences_tag)
wordCloud_Image(word_count_list)