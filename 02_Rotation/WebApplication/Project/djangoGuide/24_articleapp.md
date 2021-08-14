# articleapp

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
        writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)  

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

    > CRUD 다 쓸 예정

13. CreateView
    1. articleapp/views.py에서 기본 logic 생성
        ```py
        # views.py
        from django.urls import reverse_lazy
        from articleapp.forms import ArticleCreateForm
        from django.views.generic import CreateView
        from articleapp.models import Article
        # Create your views here.


        class ArticleCreateView(CreateView):
            model = Article
            form_class = ArticleCreateForm  # model form을 기반으로 만들었다.
            success_url = reverse_lazy("articleapp:list")
            template_name = "articleapp/create.html"
        ```

        urls.py로 이동해서 create/로 이동할 수 있도록 변경 : URL routing
        ```py
        path("create/", ArticleCreateView.as_view(), name="create"),
        ```

    2. create template 생성 : create.html
        - accountapp의 templates/accountapp/create.html의 틀 복붙
        - 이 때 form action ~ 부분에 `enctype="multipart/form-data"`를 추가해야 이미지 첨부 가능

        => 그런데 이렇게 했을 때 writer_id가 null 처리 된다. 이러면 안되는데?
        - accountapp에서 create.html 할 때 form_valid에서 profile과 account를 1:1 매칭하는 작업을 profileapp/views.py에서 진행했었음
        - $\therefore$ articleapp/views.py 에서 동일한 작업 진행 (overiding)

        ```py
        # ArticleCreateView안에 method 작성
        def form_valid(self, form):
            form.instance.writer = self.request.user
            return super().form_valid(form)
        ```

        - 이 때 로그인 되지 않은 상태에서 게시글 작성하면 simple lazy error 발생 : 유저 객체가 없기 때문에 해당 에러가 발생한다.

        - 로그인창으로 이동하게 하려면 decorator생성해서 유저 객체를 알려줘야 한다. (잠시 보류)

        - IntegrityError at /articleapp/create/
            - UNIQUE constraint failed: articleapp_article.writer_id
            - [해결](https://cw9206.tistory.com/105)

15. DetailView
    1. 기본 logic : views.py
        ```py
        class ArticleDetailView(DetailView):
            model = Article
            context_object_name = 'target_article'      # 객체 지정
            template_name = 'articleapp/detail.html'    # 렌더링 페이지
        ```
    2. urls.py에서 path 지정
        - detail page는 **어떤 게시글을 볼 것인지에 대한 KEY를 넘겨야 한다. : PK**
        - **뭘 대상으로 하는지 RUD는 항상 명시해야 한다.**
        ```py
        path('detail/', ArticleDetailView.as_view(), name="detail", pk = {{target_article}}) # detail : route의 이름
        ```
    
    3. detail page 생성 : html

15. UpdateView
    1. 기본 logic
    ```py
    class ArticleUpdateView(UpdateView):
        model = Article
        form_class = ArticleCreationForm
        context_object_name = 'target_article'
        # success_url = reverse_lazy("articleapp:list")   # 이후 삭제
    ```
        - 수정한 게시글이므로 다른 method를 동적으로 overide한다.
    ```py
    class ArticleUpdateView(UpdateView):
        model = Article
        form_class = ArticleCreationForm
        context_object_name = 'target_article'
        template_name = "articleapp/update.html"
        def get_success_url(self):
            return reverse('articleapp:detail', kwargs={'pk':self.object.writer.pk})
            # self.object == target_article (거의 동일)
            # self.object인 Article는 user를 가지고있지 않고 writer를 가지고있으므로 writer로 지정?
    ```
    2. urls.py에서 routing
    ```py
    path('update/<int:pk>', ArticleUpdateView.as_view(), name="update")
    ```
    3. update page 생성 : html
        - 이전에 사용했었던 articleapp/create.html을 재사용
            - 제목 변경
            - form action 경로 변경 : create가 아닌 update로 이동
            - pk 추가
    4. detail에 링크 추가  
        1. 두번째 div태그 안에 하위 div 태그 생성한다
        2. anchor 태그 생성 : articleapp에서 update로 이동하는 링크 생성 (pk 잊지 말 것)
            - rounded-pill : 알약모양버튼
            - px : 내부여백 (상하좌우)

16. DeleteView 
    1. 삭제 여부만 확인하면 땡이므로 form은 필요 X
        ```py
        class ArticleDeleteView(DeleteView):
            model = Article
            context_object_name = 'target_article'
            success_url = reverse_lazy('articleapp:list')
            template_name = 'articleapp/delete.html'
        ```
    2. urls.py
        ```py
        path('delete/<int:pk>', ArticleDeleteView.as_view(), name="delete"),
        ```
    
    3. template 생성 : html
        - update.html재사용

    4. delete.html에 링크 생성
        - update 버튼 옆 (a 태그 재사용)

17. 권한 확인 : decorator
    - create
        - 로그인만 확인하면 된다.
        - `@method_decorator(login_required, 'get/post')`
            - 왜 login_required?
                - form_valid에서 self.request를 찾아야 하는데 로그인 하지 않으면 이게 안 됨. 따라서 로그인 여부 확인
        - 수정했을 때처럼 게시글 작성 후 작성한 게시글 확인할 수 있게 (get_success_url ...) 해야 한다.
    - update/delete
        - 작성자만 수정/삭제할 수 있어야 하므로 새로운 decorator 생성
        - articleapp/decorators.py 생성 후 decorator 작성
            ```py
            def article_ownership_required(func):
                def decorated(request, *args, **kwargs):    # parameter는 고정
                    target_article = Article.objects.get(pk=kwaargs['pk'])
                    if target_article.writer == request.user:
                        return func(request, *args, **kwargs)
                    else:
                        return HttpResponseForbidden()
                return decorated
            ```
        - 이제 updateview, deleteview 위에 @method_decorator(article_ownership_required, 'get/post') 를 불러준다.

18. design
    1. 중앙정렬
    2. 제목, 본문 등에 여백 넣기
    3. 제목 볼드처리
    4. 내용과 제목 나누는 구분자
        - div태그 두개를 hr로 나눈다
        - 밑의 div에 my-5로 마진 추가한다
    5. 사진과 내용의 층을 나눈다.
        - target article을 위한 div를 생성한다.
        - my-5정도로 마진 추가
    6. 사진을 둥글게 깎고 크기 조절한다. 그림자도 넣자.
        - img 태그를 위한 class 생성 : article_image
        - 이제 article_image라는 class를 static/base.css에 추가.
        ```css
        .article_image{
            width : 60%
            border-radius: 2rem;
            box-shadow: 0 0 1rem grey;
        }
        ```
    7. article_content로 게시글 속성 설정
        ```css
        .article_content{
            text-align: left;
            font-size: 1.5em; /* 1rem이 기본*/
        }
        ```
19. 본인이 아닐 때에는 update나 delete 보이지 않게 하기
     - detail.html에서
    ```html
    {% if target_article.writer == user %}
    <!-- 생략 -->
    {% endif %}
    ```

20. 페이지네이션 : 페이지를 나누는 방식 => list view [docs](https://docs.djangoproject.com/en/3.2/ref/paginator/#page-class)
    - vs 핀터레스트는 페이지가 없고 무한 스크롤 방식이다. 피드가 자동으로 채워진다.
    => JS를 써야 한다.
    ```py
    # list view

    ```
    - article List : context_object_name의 내용
        - 레이아웃 하나하나에 게시글이 들어가야 한다.
        -
    - page obj : 페이지네이션에 필요한 정보를 담고있는 객체. 여기가 몇 페이지인지 알려준다.

    - 10개까지 나오는건 커스터마이징 필요하고 지금은 3개까지만 나온다.
    ```html
    <!-- list.html 의 create article button 위 -->

    <!-- 지금 있는 페이지 -->
    <div class = "text-center">
        {% if page_obj.has_previous %}
            <a href="?page={{page_obj.previous_page_number }}" class="btn btn-secondary rounded-pill">
                {{ page_obj.previous_page_number }}
            </a>
        {% endif %}
        <a href="#" class="btn btn-dark rounded-pill">    
        <!-- 현재 내가 있는 페이지 -->
        <!-- pagenated_by인가 view에서 조정하면 한 페이지에 몇 개의 게시글 노출할지 설정할 수 있다. -->
        {{ page_obj.number }}
        </a>
        <!-- 다음 페이지가 있으면 다음 페이지로 이동하는 anchor 추가 :docs 참고 -->
        {% if page_obj.has_next %}
        <a href="?page={{ page_obj.next_page_number }}" class="btn btn-secondary rounded-pill">
            {{ page_obj.next_page_number }}
        </a>
        {% endif %}
    </div>
    ```
    - secondary는 회색으로 변하고 dark는 짙은색이라 현재 페이지를 구별할 수 있다.

21. 너무 기니까 include를 통해 내용을 빼낸다.
    - snippets : 코드조각들
    ```html
    {% include 'snippets/pagination.html' %}
    ```