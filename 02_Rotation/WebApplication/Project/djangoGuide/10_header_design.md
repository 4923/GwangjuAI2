# 헤더의 na 버튼을 만들기

헤더의 버튼은 어디에 만들어뒀었지?
- templates/header.html에 만들어뒀었다. (accountapp의 templates 아님)

1. login signup 버튼 만들기
2. login한 사용자에게 login 버튼 아닌 logout버튼 보여주기 
    - django template language if문 사용
    - django template 에서 user라는 객체에 접근하여 user인지 아닌지 확인 할 수 있다. 
        - login 했는지 안했는지 확인할 수 있는 메서드 사용 : `user.is_authenticated` 
    - template language로 상황별 노출 버튼 설정


# 디자인
> 뭔가 디자인을 적용하기 signup 페이지에서 input tag를 다 설정하기 어려우니까 
django bootstrap4 를 쓴다 : 외부라이브러리 이름
1. install
    - `pip install django-bootstrap4`
2. settings.py의 INSTALLED_APPS에 bootstrap4를 추가 
3. Quickstart : load bootstrap4 
    - `{% load bootstrap4 %}`
    - 위치 : create.html의 extends base.html 아래
4. Quickstart : bootstrap_form
    - `{% bootstrap_form form %}`
    - quickstart에 적힌것 처럼 csrf token 밑에 추가 

- 층이 깔끔하게 나누어졌고 bootstrap form 디자인이 추가되었다.
- 통일성이 없으니 디자인은 이후에 정리  (너비)
5. static의 base.css에 디자인 요소 모아두었으니 확인 
    - 최대 너비를 지정한다는 의미에서 mw-500 으로 class name 설정 
    - 내부 여백인 padding도 추가
    - 중앙정렬도 해야지 : `m-auto` 에서 m는 margin이고 margin auto는 margin을 자동으로 중앙에 맞게 설정한다.

    - 이게 바로적용이 되는 사람도 있고 아닌 사람도 있음. 
    - 웹 디자인은 잘 변형되지 않기 때문에 css를 밀받고 이걸 계속 재활용 한다. (in browser)
    - 새 클래스가 반영되지 않으므로 수동으로 갱신해야 한다.
6. 수동 갱신 : f12로 개발자모드의 네번째 탭인 Network에서 disable cache 기능으로 cache 제거
    - f12를 켜고 새로고침해야 disable cache가 적용된다 (!!!)
    - 마우스오버하면 while Dev Tools is open 이라는 알림이 뜨는 것 확인

**로그인도 똑같이 적용**
1. login.html에서 load bootstrap
2. 단순출력 form 제거하고 bootstrap_form form 으로 적용
3. 최대너비 설정을 위해 최상위 div tag에서 mw-500으로 추가 
    - 이미 static에 mw-500이 있으므로 또 만들 필요 X
4. 중앙정렬을 위해 4와 같은 위치에 m-auto 설정

**폰트 적용**
1. `.otf` 파일 등을 다운받아 `mainapp/static/fonts`에 저장한다.
    - font는 일반적으로 mainapp의 static에서 관리한다.
2. 외부 statics를 불러오는 파일인 `head.html`의 style 요소로 font를 추가한다.
    ```html
    <!-- head.html -->
    <style>
        @font-face {
            font-family: 'NanumSquareR';
            src: local('NanumSquareR'),
            url("{% static 'fonts/NanumSquareR.otf' %}") format("opentype");
        }
        @font-face {
            font-family: 'NanumSquareEB';
            src: local('NanumSquareEB'),
            url("{% static 'fonts/NanumSquareEB.otf' %}") format("opentype");
        }
        @font-face {
            font-family: 'NanumSquareB';
            src: local('NanumSquareB'),
            url("{% static 'fonts/NanumSquareB.otf' %}") format("opentype");
        }
        @font-face {
            font-family: 'NanumSquareL';
            src: local('NanumSquareL'),
            url("{% static 'fonts/NanumSquareL.otf' %}") format("opentype");
        }
    </style>
    ```
3. font를 불러올 준비가 완료되었으니 필요한 위치에서 font를 불러온다.
    ```html
    <!-- base.html -->
    <body style="font-family: 'NanumSquareR'">
    ```

- issue:
    - Invalid block tag on line 22: 'static'. Did you forget to register or load this tag?
    - 이런 에러가 발생한다면 `{% load static %}` 으로 static 불러왔는지 확인 할 것