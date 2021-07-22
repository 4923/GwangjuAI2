### 구현할 기능
- 프로필 
- 이미지 
- 닉네임 
- 상태메시지

### 구현하지 않을 기능
- detail page X
- delete X (D)


## Model Form
model은 일단 만들어야 한다.
form을 model에서 자동으로 변환한다.

---
## 새로운 앱을 만든다.
1. 터미널에서 새로운 앱 생성
    - python manage.py startapp profileapp
2. mainapp/settings.py 의 INSTALLED_APPS에 profileapp 추가
3. mainapp/urls.py 의 urlpatterns에 profileapp 추가
    - `path("profileapp/", include("profileapp.urls")),`
    - profileapp 으로 설정하면 주소창에 profileapp이라고 적어야 해당 앱으로 접근 가능하게 된다.
    - personalproject에서는 profiles로 설정
4. profileapp/urls.py에 urlpatterns=[] 만 추가
    - 무엇을 넣을지 고민하고, 내용은 아직 비워둔다.