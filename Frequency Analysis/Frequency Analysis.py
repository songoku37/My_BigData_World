# 본 프로그램은 텍스트 데이터를 빈도 분석하기 전 기초편입니다.
# 작성자 이성재
# 프로그램 Frequency Analysis.py
# 코엔엘파이 라이브러리는 다른 라이브러리에 비해 설치가 조금 까다로운 편이며
# 설치가 정사적으로 되었으면 형태소 분리를 테스트한다.

from konlpy.tag import Twitter
twitter = Twitter()

sentance = '아버지가 방에 들어 가신다.'
tagging = twitter.pos(sentance)
print(tagging)
'''
출력 : 
[('아버지', 'Noun'), ('가', 'Josa'), ('방', 'Noun'), ('에', 'Josa'), ('들어', 'Verb'), ('가신다', 'Verb'),
 ('.', 'Punctuation')]
'''

# 단어 뭉치가 리스트(배열)로 들어있을 경우
title_list = [
    '인천시 연수구 , 을 강연 ICLC 성공개최..지역 10개 대학 간담회',
    '인천일보 대표 고통안전 챌린지 동참',
    '안산대, 2021년도 인천 경기북부 총장협의회 개최'
]

twitter = Twitter()
sentences_tag = []
# 형태소 분석하여 리스트에 넣기
for sentence in title_list :
    word = twitter.pos(sentence)
    sentences_tag.append(word)
    print(word)
'''
출력 : 
[('인천', 'Noun'), ('시', 'Noun'), ('연수구', 'Noun'), (',', 'Punctuation'), ('을', 'Josa'), ('강연', 'Noun'),
 ('ICLC', 'Alpha'), ('성공', 'Noun'), ('개최', 'Noun'), ('..', 'Punctuation'), ('지역', 'Noun'), ('10', 'Number'),
 ('개', 'Noun'), ('대학', 'Noun'), ('간담', 'Noun'), ('회', 'Noun')]
[('인천', 'Noun'), ('일보', 'Noun'), ('대표', 'Noun'), ('고통', 'Noun'), ('안전', 'Noun'), ('챌', 'Verb'), ('린지', 'Noun'),
 ('동참', 'Noun')]
[('안산대', 'Noun'), (',', 'Punctuation'), ('2021년', 'Number'), ('도', 'Foreign'), ('인천', 'Noun'), ('경기', 'Noun'),
 ('북부', 'Noun'), ('총장', 'Noun'), ('협의', 'Noun'), ('회', 'Noun'), ('개최', 'Noun')]
'''