# DOM 요소 파악하기
from bs4 import BeautifulSoup 
import urllib.request

# Document Object Model: XML이나 HTML 요소에 접근하는 구조를 나타낸다
# DOM 요소의 속성이란 태그 뒤에 나오는 속성을 말한다 태그의 속성은 href이다

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
res = urllib.request.urlopen(url)

soup = BeautifulSoup(res, 'html.parser')
title = soup.find('title').string
wf  = soup.find('wf').string

print(title)
print('-' * 20)
print(wf)