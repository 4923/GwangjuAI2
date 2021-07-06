
# Make BASIC view
[commit log](https://github.com/4923/GwangjuAI2/commit/fd6d28b7b5cffa1182268ff616748daf09a0cd57)

1. accountapp 앱의 메인 페이지가 될 html 문서를 생성한다 : `base.html`
    - `base.html` 의 내용은 임의로 작성

2. accountapp/views.py
    - **`render`**함수를 사용하여 특정 주소 (/hello_world)를 입력했을 때 이동할 페이지를 지정한다.
    - ```python
        def hello_world(request):   # register -> request
        return render(request, 'base.html')
        ```
    - hello_world라는 함수의 요청(request)가 왔을 때 request를 base.html로 렌더링 하라는 명령이다.

    - 렌더링이란?
        1. 사전적 정의 : 컴퓨터 그래픽(스)이나 디지털 애니메이션에서 가상으로 완성된 결과를 만들어 내는 과정. 또는 완성된 화면이나 영상.[(link)](https://terms.naver.com/entry.naver?cid=42627&categoryId=42627&docId=1649375)
            - 동영상 작업, 3D처리, 이미지 작업, 웹 개발에서 두루 사용되는데, 모두 컴퓨터 그래픽을 사용하기 때문이다.
        2. HTML에서 : html 파일을 받아 해석하고, 그 결과를 그리는 과정이다. 순서상 html 안의 내용을 먼저 읽고 그 다음으로 외부의 css를 읽어들이므로 inline style이 external style보다 우선적으로 처리된다. (별도 문서로 보충)
            - 참고
                1. 렌더링 : [velog/렌더링이란](https://velog.io/@ru_bryunak/%EB%A0%8C%EB%8D%94%EB%A7%81%EC%9D%B4%EB%9E%80)
                2. 렌더링엔진 :  [Naver D2/브라우저는 어떻게 동작하는가?](https://d2.naver.com/helloworld/59361)

### flow
1. accountapp을 생성하고 mainapp/settings.py에서 accountapp을 추가했음을 알린다
   ```python
    INSTALLED_APPS = [
        # 생략
        "accountapp",   # 추가
    ]
   ```
2. mainapp/urls.py에서 accountapp으로 분기하는 urlpatterns를 생성하여 페이지 경로 주소에 accountapp을 입력할 시 accountapp.urls로 이동하도록 설정했다.
    ```python
    urlpatterns = [
        #path("admin/", admin.site.urls)
        path("accountapp/", include("accountapp.urls")),    # accountapp이라는 주소가 들어오면 accountapp이라는 앱의 urls.py로 이동한다.
    ]
    ``` 
    - `path("페이지 경로 주소/", include("accountapp.urls")),` 이므로 accountapp이 아닌 다른 주소명을 적어도 무관하다. personalproject에서는 accounts로 설정했다.
3. accountapp/ulrs.py에서 반환할 html 문서를 지정한다. 해당 앱의 메인 페이지를 설정하기 위해 html 문서(`hello_world.html`)를 생성해서 path에 추가했다.
    ```python
    urlpatterns = [
    # path(route, 실행할 view 함수 -> HttpResoponse, 페이지 주소)
    path("hello_world/", hello_world, name="hello_world"),
    ]
    ```
    - 이 또한 분기점이므로 현재까지의 상태에서 `python manage.py runserver`를 돌렸을 때 hello_world.html문서로 이동하려면 `로컬서버주소/accountapp/hello_world`라고 적어야한다. accountapp까지만 적었을 시 주소를 찾지 못한다는 에러페이지를 만나게 된다.

4. 이제 accountapp/views.py에서 3번의 요청에 응답할 view 함수 hello_world를 생성한다.
    ```python
    def hello_world(request):   # register -> request
        return render(request, 'base.html')
    ```
5. 4번의 `base.html`이 종착지이며, 해당 html문서를 가지고 지금까지의 과정을 거슬러 올라가 사용자에게 `base.html`을 렌더링한 화면을 보여준다.
