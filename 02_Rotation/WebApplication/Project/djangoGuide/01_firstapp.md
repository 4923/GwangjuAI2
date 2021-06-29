## Guide
2021.06.29 | 간단한 view 실습

1. `startapp` 으로 앱 생성
python manage.py startapp accountapp
: python의 manage.py에서 accountapp을 startapp하라
이걸 했다고 끝나는게 아니라 사용할 수 있게 명시해야한다.

2. `project/settings.py`의 INSTALLED_APPS에 앱 등록하기
프로젝트 이름과 동일한 앱이 메인 앱이며, 해당 앱 폴더에 `settings.py`가 있다.
`settings.py`의 `INSTALLED_APPS`에서 새로 만든 앱이름을 추가한다.
    - 이 때 project는 프로젝트명으로 메인 앱을 의미한다.

3. [VIEW] `project/views.py`에서 함수형태로 view 작성
이후 views.py로 이동해서 기능을 함수형태로 작성한다.
    ```python
    def hello_world(register):
        return HttpResponse('Hello World!')
    ```
이 HttpResponse만 기억하면 pycharm에서는 바로 불러올 수 있다.

* Pytharm : alt enter로 문맥상 문제되는 부분 고침. 모듈 이름만 기억하면 알아서 가져온다.

4. `projectapp/urls.py`에서 accountapp으로 연결
    ```
    path("accounts/", include("accountapp.urls"))
    ```

5. `accountapp/urls.py` 생성
    

6. `accountapp/urls.py` 에서 Routing
    1. urlpatters에 하단 코드 추가
        - accountapp에서 다시 하위분기를 하라는 명령어
    2. 생성한 앱 이름을 작성

        ```
        from django.urls import path

        from accountapp.views import hello_world    # 추가

        app_name = "accountapp"

        urlpatterns = [
            path("hello_world/", hello_world, name="hello_world"),
        ]       # 이부분이 view에 해당하는 내용

        ```
    - hello_world는 작성한 view고 name에는 라우트의 이름을 적는다. 이 때 hello_world는 views에서 추가해와야 한다.

7. `python manage.py runserver` or Pycharm에서 run server
