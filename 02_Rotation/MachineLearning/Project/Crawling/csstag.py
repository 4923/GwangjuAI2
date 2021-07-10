# css 선택자 사용하기?
# 목표1 : css 선택자를 사용해서 원하는 요소 추출
# 목표2 : h1과 li 태그를 추출

from bs4 import BeautifulSoup
import urllib.request
import requests as req

html = """ 
<html><body>
<div id = 'books'>
    <h1>위키북스 도서</h1>
    <ul class="item">
        <li>게임 입문</li>
        <li>파이썬 입문</li>
        <li>웹 디자인 입문</li>
    </ul>
</div>
<body></html>
"""

soup = BeautifulSoup(html, "html.parser")

# 웹 구조가 복잡할 때 select를 쓰면 세밀하게 가져올 수 있다.
h1 = soup.select_one("div#books > h1")
li_list = soup.select("div#books > ul.item > li")

# 윤동주 시인의 작품 목록 가져오기
# 크롬의 개발자도구 또는 우클릭하고 검색 누르면 바로 개발자 도구가 뜬다.

url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
res = urllib.request.urlopen(url)

# copy -> copy selector : 어느 경로로 들어가면 되는지 알려준다.
# mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > b > a
# mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > ul > li:nth-child(1) > a

# 작품 목록을 가져와보세요
# 위에서 nth-child(6)은 6번째에 있는 요소를 가리킨다
# 이를 기반으로 작품목록을 가져오는 프로그램을 작성하겠다.

# res = req.get(url).text
res = urllib.request.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

poet_list = soup.select(
    "#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > b > a"
)
poet_list = soup.select(
    "#mw-content-text > div.mw-parser-output > ul a"
)  # > 를 쓰면 그 밑에있는것을 지정, 없이 띄어쓰기 기준으로 나열하면 ul 밑에 있는 모든 a

for poet in poet_list:
    print(poet.string)
