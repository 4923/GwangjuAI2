# urllib : 이미지를 가져올 때 유용하다. 기능도 많다.
import urllib.request

url = "https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png"

# urlretrieve
urllib.request.urlretrieve(url, "img_name.png")  # 파이썬 파일의 위치에 이미지가 생성된다.

# urlopen
png = urllib.request.urlopen(url).read()  # url을 다 읽어들일 수 있다.
# 나중에 openCV 쓰면 바로 불러오는대로 사용할 수 있지만 우선 png라는 변수에 저장
with open("test2.png", "wb") as f:
    f.write(png)
