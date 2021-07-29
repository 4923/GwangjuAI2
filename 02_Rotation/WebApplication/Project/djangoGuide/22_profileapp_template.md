# template 생성

1. profileapp의 template를 모아두는 templates 디렉토리를 생성하고, 그 안에 혼선을 방지하기 위해 다시 profileapp 디렉토리를 생성한다.
2. 프로필을 생성할 때 필요한 기능은 accountapp의 create.html와 유사하니 폼을 그대로 가져온다.
    - 수정이 필요한 사항
        1. 페이지 제목
        2. form 요청을 보낼 때 action에서 어디로 post 요청을 보내는지 지정하는데, accountapp으로 보낼것이 아니기 때문에 profileapp으로 변경한다
3. 이미지를 인식할 수 있도록 `enctype`을 추가한다.
    - enctype : **enc**oding **type**
    - `<form action="{% url 'profileapp:create' %}" enctype="multipart/form-data" method="post">`
    - 기본적으로 text로 인식하기 때문에 이 정보가 이미지라는 것을 알리기 위해 속성값을 지정한다.
    - enctype을 추가해도 NOT NULL constraint failed: profileapp_profile.user_id 에러가 발생한다면 이는 **views에서 user, image, nickname, message를 받는데 user를 지정하지 않았기 때문**이다.
        - views.py에서 지정해주자 : `ProfileCreateView/form_valid`