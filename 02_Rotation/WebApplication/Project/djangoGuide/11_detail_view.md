> 유저를 식별하여 개인 페이지 (templates/accountapp/detail.html) 를 만든다.
> 유저를 식별했음을 확인하기 위해 개인페이지에 로그인한 유저의 아이디를 노출한다.

1. views.py 에서 class AccountDetailView() 를 생성 
    - 상속은 DetailView를 받는다.
    - import도 잊지 말 것 
    ```py
    class AccountDetailView(DetailView):
        # user 객체를 어떻게 뽑아낼 것인가
        model = User
        context_object_name = "target_user"  # 이 이름을 통해 html에서 account 객체에 접근하게 된다 (!!)
        template_name = "accountapp/detail.html"
    ```
    - DetailView와 User는 models.py에 이미 선언된 객체
    - detatil.html에서 target_user인 로그인상태의 유저를 부르는 이름을 context_object_name으로 설정한다.

2. MyPage (`detatil.html`) 생성
    1. `accountapp/templates/accountapp`에서 `detail.html`을 생성한다.
    2. `{% extends 'base.html' %}` 에서 본문 내용만 작성한다
    3. template language로 변수를 선언하여 `target_user` 객체를 호출한다.
        - `.username` : 로그인한 유저의 이름
        - `.date_joined` : 가입일자
    4. 중앙정렬 (`<div class="text-center mw-500 m-auto">`)

3. MyPage와 연결되는 url을 `urls.py`에서 생성한다
    - url을 관리하는 urlpatterns에서 pk를 기준으로 detail 페이지에 접근할 수 있는 url을 생성한다
    - ```py
        urlpatterns = [
            path("detail/<int:pk>", AccountDetailView.as_view(), name="detail"),
        ] 
        ```

4. 이 때 유저별 pk를 식별할 수 있는것은 template을 불러온 위치인 `header.html`에서 `pk=user.pk` 라고 설정해두었기 때문이다.
    ```html
    <a href="{% url 'accountapp:detail' pk=user.pk %}">MyPage</a>
    ```

