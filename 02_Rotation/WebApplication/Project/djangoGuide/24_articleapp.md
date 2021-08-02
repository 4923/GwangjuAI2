# acticleapp

1. python manage.py startapp articleapp
2. projectapp/urls.py 에 path 추가
3. projectapp/settings.py 에 INSTALLED_APPS에 앱 추가
4. articleapp/urls.py 에서 template 추가
    ```py
    app_name = "articleapp"

    urlpatterns = [
        path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name="list"),
    ]
    ```
    - TemplateView : import
    - name = 'list' : route name
    - app_name = 'articleapp' 을 위에 적어주어야 template_name에서 articleapp/list.html을 불러올 수 있다. 슬래쉬 (/) 앞의 articleapp이 app_name이기 때문

5. 이 상태에서 runserver 했을 때 base.html만 정상적으로 보여야 한다.

6. 레이아웃 생성
magic grid[github](https://github.com/e-oj/Magic-Grid) 에서 [on JSFIDDLE](https://jsfiddle.net/eolaojo/4pov0rdf/)로 이동 (live coding)
- HTML, CSS, JS 전부 복사 후 붙여넣기
    - HTML, CSS는 html 안에 입력
    - JS : 컨테이너는 만들어졌는데 레이아웃 구성이 안된다? : js를 가져오지 않았기 때문
        - 근데 페이지의 js는 구동부다. (only 함수 호출)
        - $\therefore$ 함수 선언부를 다시 가져와야 한다.
            - github repo의 dist에서 magic grid 관련 js를 가져올 수 있다. (버전이 여러가지 있으므로 cjs 가져온다.)
            - 전부 긁어서 가져오는데
                - html 안에 `<script></script>` 로 가져올 수 있지만 외부에서 가져오는 방식을 쓴다. $\because$ html이 너무 길어지므로
                - static dir 안에 넣어주자.
                    - 혼선을 방지하기 위해 `static/js`를 만들어 그 안에 추가한다. (파일명 : `magicgrid.js`)
                    - 마지막에 `module.export`가 있는데 이 부분은 제거 : django가 아니라 다른 웹 프레임 워크에서 사용하는 부분이기 때문
                    - JSFIDDLE의 구동부는 `magicgrid.js`의 마지막에 추가한다.

        - 완성한 js를 `list.html`을 긁어온다.
            - `<script src="{% static 'js/magicgrid.js' %}"></script>`
                - static을 사용하는 방법 : `{% static '' %}` 을 열고
                - 따옴표 안에 static 폴더 안의 경로를 입력 : `js.magicgrid.js`
                - static을 사용하려면 html 상단에 `{% load static %}` 부분을 추가해야 한다.


7. random한 이미지 불러와서 레이아웃(갤러리)에 추가
    - https://picsum.photos/200/300
        - 여기서 200/300 은 이미지 크기이며 이미지 크기만 제대로 지정하면 랜덤하게 이미지를 전송하게 된다.
    - list.html을   - div class = "item1" 에 img 태그 추가
        - <img src="https://picsum.photos/200/300">

8. 사진 크기에 맞춰 외부 컨테이너의 크기를 변경
    1. 높이
        - css에서 높이와 너비를 수동으로 지정하고 있는데 (높이가 달라도 자ㅔ동으로 맞춰진다는 것을 시연하기 위함이었으므로) 이 부분 제거
        - .container의 div에서 기본 높이가 지정되므로 그 부분도 제거
        - => 이렇게 되면 이미지가 있는 컨테이너는 자동으로 높이가 조절 된다.
    2. 너비
        - container의 class 안의 img태그를 생성한다
            ```css
            .container img {
                width: 100%;
            }
            <!-- 꽉찬 너비로 가져가라 -->
            ```
        - 이렇게 하면 뒷부분의 컨테이너 색이 보이지 않는다. 

    3. 둥글게 변경
        - 카드형이었으므로 `border-radius: 1rem;` 으로 추가
        ```css
        .container img{
            width: 100%;
            border-radius: 1rem;    /* 추가 */
        }
        ```
        또, 뒷부분 배경도 변경해야 하므로
        ```css
        .container div {
            /* 생략 */
            border-radius: 1rem;
        }
        ```
        border-radius 추가

    4. 적용
        - 멀티커서 이용하여 같은 형식 추가

    5. container의 여백 추가
        - `<div class="container my-4>`


9. 세부 디자인

10. 처음 로딩할 때 배치가 제대로 안되는 문제 해결
    - 개발자모드의 waterfall : 이 페이지를 구성하기 위해 가져오는 리소스들이 언제 요청되고 완료되었는지 타임라인으로 보여진다.
    - 이미지의 사이즈와 용량이 다 다르기 때문에 로딩 될 때마다 레이아웃 재배치 하도록 변경 : js로 작성

    - magicgrid.js에서 진행
        ```js
        /* 
        비대칭 블럭/벽돌형 구조를 masonrys라고 한다. 
        list.html 전체를 documents라고 한다. 
        이미지 태그 전체를 찾는다.
        */
        var masonrys = document.getElementsByTagName("img")

        for (let i=0; i < masonrys.length; i++)
        {   
            /*
            어떤 이벤트가 발생했는지 감시하는 장치를 부착
            ('load') : 이미지가 load 되었을 때 할 일 지정
            function(){magicGrid} 안의 positionItems를 재배치 해라.
            */
            masonrys[i].addEventListener('load', function(){
                magicGrid.positionItems();
                False
            })
        }
        ```

11. logic
    - articleapp/models.py에서
    ```py
    # related_name : 뭐였더라
    class Profile(models.Model):
        # 작성자 정보
        writer = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='article', null=True)  

        # 게시글에 포함할 정보
        title = models.CharField(max_length=200, null=True)     # 사진만 올릴수도 있으므로 title null=True

        # 사진
        # upload_to : article/ 이라는 위치에 업로드 할 것 => 전체 프로젝트 폴더의 media dir안의 article에 이미지들 저장한다.
        image = models.ImageField(upload_to="article/", null=True)

        # 본문
        content = models.TextField(null=True)
    
        # 시간 정보
        # 사용자가 작성하는게 아니고, DB에서 자동으로 작성하도록 auto_now_add를 True로 설정
        created_at = models.DateField(auto_now_add=True, null=True)
    ```

    - 이후 migration
    - `related_name`
        - profileapp의 model에서 작성한 부분 : user랑 연결한 후 related_name을 profile로 지정했었는데
        - User라는 객체가 있다고 하면 그거에 연결된 profile에 접근할 때 User.profile로 접근할 수 있다.
            - related_name을 prof 라고 했다면 접근할 때 User.prof로 접근할 수 있다.
        - detail.html에서 target_user.profile로 접근하면 된다.
        - related_name을 설정하는건 : models.py에서 설정한 class에 접근하기 위함
        - DB로 이해하면 된다.
            - 1번 profile에서 보면 유저 객체의 번호는 4번임
            - 역으로 4번 유저의 객체를 찾을 때 : (auth_user db에서는 profile 정보는 알 수 없다) profile이라는 related_name으로 접근해서 profile을 찾게 된다.

12. form
    - articleapp/forms.py에서 ArticleCreateForm(ModelForm) 생성
    ```py
    from django.forms import ModelForm
    from articleapp.models import Article

    class ArticleCreateForm(ModelForm):
        class Meta:
            model = Article
            fields = ['title', 'image', 'content']
    ```