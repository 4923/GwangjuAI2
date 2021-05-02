# Python 2강 : open API, JSON

공공 데이터에 대한 수요와 공급이 증가하고 있다.  
공공 데이터는 open API로 자료를 제공하므로, 공공 데이터의 활용을 위해서는 open API를 알아야 한다.

### 미리 알아두기
dictionary  
- key와 value의 대응 관계를 가진 자료형.  
- 순서가 없으므로 key로 value값에 접근할 수 있다.

### JSON
`J`ava`S`cript `O`bject `N`otation
- 개요
    1. JS에 기반하고 있다.
    2. 데이터를 효율적으로 저장하고 교환하는데 사용하는 **텍스트 데이터 형식**이다.
    3. 장점
        - 사람이 읽고 쓰기 쉽다.
        - 컴퓨터가 파싱하고 생성하기 쉽다.
    4. 구조
        1. 이름과 값의 집합
        2. 정렬된 값의 리스트
        +) 파이썬의 리스트와 튜플이 JSON으로 변환되면 각 자료형은 array가 되며, JSON이 파이썬으로 변환되면 array는 리스트가 된다.

### 파이썬에서 JSON다루기

1. JSON -> Python
    ```python
    import json
    with open('student_file.json') as json_file:
        json_data = json.load(json_file)
    json_data
    ```
    1. JSON 형식의 데이터를 열어 파이썬 객체로 읽어온다.  
        `with` 문과 함께 `open` 함수를 사용한다. 이 때 `as`는 별칭을 짓는데 사용하는 함수.
    2. 불러온 데이터를 `json`모듈의 `load`함수에 통과시켜 파이썬 객체로 저장한다.  
        앞에서 다룬 바와 같이, json이 파이썬으로 변환될 때 json의 array는 파이썬의 리스트가 된다.

2. Python -> JSON
    ```python
    import json
    months = {1: 'january', 2: 'february', 3: 'march'}
    months_json = json.dumps(months, indent = 4)
    ```
    파이썬 객체를 `json` 모듈의 `dumps`함수에 통과시켜 `json 문자열`로 변환한다.
    - 옵션
        1. `indent` : 이 때 가독성이 떨어지는 문제가 발생하므로, `dump`함수의 `indent` 옵션을 통해 들여쓰기를 설정한다.
        2. `sort_keys` : `sort_keys` 속성에 `True`값을 주면 key값으로 정렬된다.


### Open API
`Open` `A`pplication `P`rogramming `I`nterface
> 인터넷 이용자가 웹 검색 결과 및 사용자 인터페이스 등을 수동적으로 제공받는데 그치지 않고 직접 응용 프로그램과 서비스를 개발할 수 있도록 공개된 API

> => 인터넷 이용자가 웹 검색 결과 (데이터) 를 지정한 조건에 맞게끔 가져올 수 있게 하는 도구

### 실습 : 영화진흥위원회
- 준비 : key
    + 공급자가 제공하는 key가 필요하다. (대부분. 모두는 아니다.)
    + key : API 제공자가 사용자들의 API 사용을 통제하기 위한 도구
    + why? 특정 사용자의 과다 사용을 막기 위해, 모든 사람이 안정적으로 API를 사용할 수 있게 하기 위해.

- key는 발급받았는데 어떻게 데이터를 끌고 오지?   
    50ee936c7380f8675b6bb4de9a74212e
    => 제공자가 대부분 가이드라인을 제시해 둔다.
    1. 필요한 데이터 확인
    2. 데이터 공급형태 확인  
        어떠한 데이터를 어떻게 공급하는지 -> 활용할 방법을 생각하기 위해
    3. 데이터 정제
    4. URL에 python을 통해 접근한다.  
        응답예시를 살펴보고, url의 `key=`에 내 key값을 넣고 `targetDt=`에 원하는 날짜를 입력한다.
    ```python
    import requests  # requests.get()
    url = "http://www.~/~openapi/~/~key=50ee936c7380f8675b6bb4de9a74212e&targetDt=2020051"
    # url을 통해 정보를 요청 (request)
    res = requests.get(url)  
    # 정보를 우리가 이해할 수 있게 text로 변환
    text = res.text  
    # json형식으로 변환
    MD_json = json.load(text)  # MD : Movie Data
    ```

- 받은 데이터 확인  
    ```python
    # dumps로 python변환, 가독성 향상을 위해 속성값 조절 (indent, sort_keys)
    print(json.dumps(MD_json, indent = 4, sort_keys=True))
    ```
    이제 이 key값이 구체적으로 뭘 하는지 확인하기 위해서는 API 가이드라인을 살펴봐야한다.

- 데이터 활용
    ```python
    print(MD_josn.keys())  # dict의 key값만 추출하는 함수
    print(MD_json['boxOfficeResult'].keys())

    # 출력
    for i in MD_json['boxOfficeResut']['dailyBoxOfficeList']:
        # i['응답필드']
        print(i['rank'], i['rankOldAndNew'], i['movieCd'], i['movieNm'], i'salesAmt']) 

    # pandas 자료형으로 저장
    import pandas as pd
    movie = []
    for i in MD_json['boxOfficeResut']['dailyBoxOfficeList']:
        # i['응답필드']
        movie.append(i['rank'], i['rankOldAndNew'], i['movieCd'], i['movieNm'], i'salesAmt']) 
    data = pd.DataFrame(movie)  # list를 pd의 DataFrame 형식으로 변환        
    ```
### 실습 : 공공데이터 / 동네예보 조회서비스
Open API : https://data.go.kr/data/15057682/openapi.do
서비스URL http://apis.data.go.kr/1360000/VilageFcstInfoService
실습파일 : open_API/weather_api_2018.py
