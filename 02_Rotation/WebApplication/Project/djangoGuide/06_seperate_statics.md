

> 일반적으로 html에는 구조만 담고 디자인적 요소는 css에 담는다. css으로 디자인 요소를 옮겨보자.

1. 최상위 폴더에 `static` 폴더를 생성
2. `static/`에 `base.css`를 생성한다.
3. `base.css`에 클래스를 설정한다
    - 클래스는 `.`으로 시작
    - header의 div 안에 적어두었던 style태그 안의 내용을 클래스 안으로 옮긴다.
    ```css
    // 예시
    .blog_header_logo {
    margin-top: 3rem;
    font-family: 'Merienda', cursive;
    }
    ```
4. `header.html` (옮겨온 style이 있던 자리) 에 class를 적용시킨다.
    ```django
    <div class = "class name"></div>
    ```
5. `base.css`를 `head`로 가져온다.
    - 단, 내부 소스이므로 템플릿 언어로 `{% load static %}` 으로 static 파일을 불러온다.
        ```django
        {% load static %}
        <!-- 중략 -->
        {% comment %} STATIC FILES LINK {% endcomment %}
        <link rel="stylesheet" type="text/css" href="{% static 'base.css' %}">
        ```
    - django는 static을 사용하지 않는다고 전제하므로 static이 어디에 있는지 알려줘야 한다.
        - 검색어 : django static [document](https://docs.djangoproject.com/en/3.2/howto/static-files/)
        - 프로젝트 내 앱에 연결되지 않은 static files를 관리하는 방법
            ```python
            # in `settings.py`
            STATICFILES_DIRS = [
                BASE_DIR / "static",
                # '/var/www/static/',     # 필요 없는 부분이므로 이부분은 삭제 -->
            ]
            ```