# AttributeError: partially initialized module 'requests' has no attribute 'get' (most likely due to a circular import)
# 파이썬 이름과 파일 이름이 같으면 발생하는 오류 [link](https://brunch.co.kr/@princox/209)


import requests as req
import json
from pandas.io.json import json_normalize  # json을 변환시키는 라이브러리

# 예전 실검 구조
url = "http://rank.search.naver.com/rank.js"

# object로 구성되어있다.
# key와 value으로 나누어져 있다.: rank, keyword
# object 안에 object가 들어올 수도 있고 list가 들어올 수도 있다.

# data 안의 rank list를 가져오자.
# pandas로 바로 변환
res = req.get(url)
j = json.loads(res.text)
json_normalize(j, ["data", "data"])
