import urllib.request

# 클라이언트정보를 보여주는 샘플 api 사이트
# header를 쓸 때 상대방 컴퓨터가 나를 어떻게 보는지 알 수 없는데 이를 확인할 때 사용하면 좋다.
url = "http://api.aoikujira.com/ip/ini"

# 기상청 데이터 가져오기
# open api : 미리 가입 후 요청해야 한다.
# 보통 일이주 걸리는데 휴가기간이라 더 걸릴 수도 있다.

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
res = urllib.request.urlopen(url)
data = res.read()

# data 그대로 출력하면 b로 시작되는 문자열을 받기는 하는데, 우리가 사용할 수 있는 형식은 아니다. 따라서 디코딩을 해야하는데 파이썬에선 한글을 utf-8로 받는다.
# b'<?xml version="1.0" encoding="utf-8" ?>\r\n<rss version="2.0">\r\n<channel>\r\n<title>\xea\xb8\xb0\xec\x83\x81\xec\xb2\xad \xec\x9c\xa1\xec\x83\x81 \xec\xa4\x91\xea\xb8\xb0\xec\x98\x88\xeb\xb3\xb4</title>\r\n<link>

text = data.decode('utf-8')
text

print(text)

