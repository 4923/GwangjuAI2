# key (Encoding, 21-05-03 only) => 한두시간 후에나 사용 가능하다는데 어느 세월에 기다리냐
# e2Z9t4eATx2wlQuWKatDsSLF%2FpWhq%2FlDiDhgE3CfTeWDIQK26jm0jA3UvNy%2FdHCi2QOKFHd1rASdJmTnB%2BbA4w%3D%3D

import requests, json

"""
2) [초단기예보조회] 상세기능명세
초단기예보정보를 조회하기 위해 발표일자, 발표시각, 예보지점 X 좌표, 예보지점 Y 좌표의 조회 조건으로 자료구분코드, 예보값, 발표일자, 발표시각, 예보지점 X 좌표, 예보지점 Y 좌표의 정보를 조회하는 기능

http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtFcst
?serviceKey=인증키&numOfRows=10&pageNo=1
&base_date=20151201&base_time=0630&nx=55&ny=127

"""
URL = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtFcst?serviceKey=e2Z9t4eATx2wlQuWKatDsSLF%2FpWhq%2FlDiDhgE3CfTeWDIQK26jm0jA3UvNy%2FdHCi2QOKFHd1rASdJmTnB%2BbA4w%3D%3D&numOfRows=10&pageNo=1&base_date=20210503&base_time=0630&nx=55&ny=127"
# 최근 1일 간의 자료만 제공

request = requests.get(URL)  # json
text = request.text
# print(text)
# print('--------------------------')
weather = json.dumps(text, indent=4, sort_keys=True)
print(weather)

# 뭐가 나오긴 하는데 분류가 안됨
