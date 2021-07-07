import requests as req 

res = req.get('https://www.google.com/')
# 이상 없으면 200 응답
# 없는 주소라면 400
# 500은 서버 문제

# 가지고 올 내용은 `.text에 존재`
res.text

url = 'http://naver.com'
res = req.get(url)
res


# req는 주소만 가져올 수 있고, 검색창을 사용하려면 selenium을 사용해야 한다.
# 대신 주소로 검색을 할 수 있는데, 이 때 사용하는 것이 쿼리스트링
url = 'https://search.naver.com/search.naver'
res = req.get(url, params={ 'query' : '정보처리기사'})    # requests의 params(parameters) 속성을 사용하면 웹에서 쓸 수 있는 이름으로 바꿔서 가져온다.
# --------------------------------

# 프로그램을 요청하면 안되게끔 막아둔 곳이 있음
# ex) 다나와

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'referer':'https://nid.naver.com/login/sso/finalize.nhn?url=https%3A%2F%2Fwww.naver.com&sid=KBwWbyEJdJL521l3&svctype=1'}

url2 = 'http://prod.danawa.com/list/?cate=11229515&logger_kw=ca_main_more'
res = req.get(url)  #  2000 포트가 나오긴 함
res.text    # error가 정상적으로 [2000] 출력됨

# 이런거 검사할 때 보통 브라우저에서 접근했는지 확인하는데
# 이걸 해결하는 방법 : headers를 추가해줘야 한다.
res = req.get(url, headers=headers)     # 이렇게 하면 정상 값이 출력된다.
res.text