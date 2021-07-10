# 파이썬 2를 설치했었다면 pip3 install 을 해야 하는데 (python 2에 설치되기 때문에) 아니라면 그냥 pip install 해도 된다.

from bs4 import BeautifulSoup

html = """
<html><body>
    <h1 id="title"> 파이썬으로 웹 문서 읽기 실습 </h1>
    <p id="p1"> 페이지 분석 기능 </p>
    <p id="p2"> 페이지 정렬 </p>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
h1 = soup.html.body.h1  # 태그를 바로 읽어올 수 있다. (태그까지 함께 읽어온다)
# >> <h1> 파이썬으로 웹 문서 읽기 실습 </h1>
p1 = soup.html.body.p

# 계층 구조이므로 첫 값만 불러오게 된다. (.next_sibling으로 다음 위치를 불러오게 된다.)
p2 = p1.next_sibling.next_sibling  # next_sibling 한번만 하면 줄개행 문자만 나온다.
# >> <p> 페이지 정렬 </p>

# find를 사용하면 id로 가져올 수도 있다. (이 단계에서 html에 아이디 추가했으므로 위 결과에는 id 속성은 포함되지 않음)
# id가 있을때는 id를 사용하고 아니면 다른 방법을 사용 할 것 (실제 html엔 id를 부여할 수 없으므로)
h1_1 = soup.find("h1")  # 이렇게 하면 태그만 가져오고
h1_2 = soup.find(id="title")  # 내용을 가져온다.

print(h1_1)
print(h1_2)

p1 = soup.find(id="p1")
p2 = soup.find(id="p2")
print(p1)
print(p2)

# findall : 전체를 가져올 수 있다.
html = """
<html><body>
  <ul>
    <li><a href='http://www.naver.com'>naver</a></li>
    <li><a href='http://www.daum.net'>daum</a></li>
  </ul>
</body></html>
"""
soup = BeautifulSoup(html, "html.parser")
links = soup.find_all("a")
for a in links:
    href = a.attrs["href"]
    text = a.string
    print(href, text)
