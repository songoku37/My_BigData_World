# 본 프로그램은 공공데이터를 이용하여 지하철 승차인원수 구하기
# 작성 시작일자 2021. 06. 04
# 작성자 : 이성재
# 프로그램명 : openAPI



# url 변수에 최종 완성본 url을 넣자
import json
import urllib.request
import pandas as pd

url = "http://openapi.seoul.go.kr:8088/나의 인증키/json/CardSubwayStatsNew/1/5/20210603"

# url을 불러오고 이것을 인코딩을 utf-8로 전환하여 결과를 받자.
response = urllib.request.urlopen(url)
json_str = response.read().decode("utf-8")

# 받은 데이터가 문자열이라서 이를 json으로 변환한다.
json_object = json.loads(json_str)



# ['CardSubwayStatsNew']['row']를 데이터 프레임 df 불러오는 것은 아래와 같다.
df = pd.json_normalize(json_object['CardSubwayStatsNew']['row'])

print(df)