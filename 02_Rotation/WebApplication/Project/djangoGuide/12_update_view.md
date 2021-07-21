# 회원정보 수정 기능 구현 (crUd)
1. views.py에서 AccountUpdateView(UpdateView)를 생성
    - 주요 파라미터
        1. 어떤 객체를 수정할 것인가? : model = User
        2. 어떤 방식으로 수정할 것인가? (form) : form_class = UserCreationForm
            - CreateView와 동일
        3. 어떤 이름으로 객체에 접근할 것인가? : context_object_name = 'target_user'
        4. 어디로 이동할 것인가? : detail page로 이동하고 싶은데
            - success_url = reverse_lazy('accountapp : detail') 이렇게 하면 안된다.
            - urls.py에서 path를 : "detail/<int:pk>" 으로 적었기 때문 (pk가 없다.)
2. routing
    - urls.py에서 path 지정 
    - `path("update/<int:pk>", AccountUpdateView.as_view(), name="update"),`
    - 이 때 route 이름이 update이다.

3. update.html 생성 
    - action에서 pk도 넣어야 하는데 따옴표 밖에서 pk를 지정한다.
        - action : 어디로 요청을 보낼 것인가?
        - 어떤 pk? : `target_user.pk`
            - 이 때 띄어쓰기 하지 말 것 : TemplateSyntaxError ~ Could not parse the remainder: '=' from '=' error가 발생한다.
                - (O) : pk=target_user.pk
                - (X) : pk = target_user.pk
z
4. detail page에 update로 이동하는 링크 지정 (detail.html에서 링크)

5. id를 변경 제한
    - 현재 상황에서는 변경이 가능한데, 서버 관리자 입장에서는 아이디가 변경되면 곤란해진다.
    - 따라서 user info update form에서 id 칸을 무력화한다. (변경 불가능하게 한다.)
    
    
    - update/views.py에서 어떤 form을 쓰는지 확인하면 `UserCreationForm`을 쓰는것을 확인할 수 있다. 
    1. UserCreationForm 상속받아 커스터마이징 할 수 있다.
        1. accountapp에 forms.py를 생성한다.
        2. 커스터마이징 하기 위해 상속할 class를 생성한다.
            ```python
            from django.contrib.auth.forms import UserCreationForm


            class AccountCreationForm(UserCreationForm):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, **kwargs)
            ```
            - UserCreationForm과 다를게 없는 상태다.
        3. 커스터마이징
            - `self.fields['username']` id를 입력할 수 있는 필드에 `.disabled` 라는 속성을 활성화한다.
    2. AccountUpdateView 에서 이전처럼 그대로 UserCreationForm을 가져오지 않고 forms.py에서 생성한 UserCreationForm을 불러온다.
        - 짙은 회색으로 변경되어 수정할 수 없게 된다.

    - 수정 불가능한 것 처럼 만든거지 소스코드를 만지면 변경할 수 있다. (value를 수정하면 됨.) 하지만 disabled 속성을 추가해씩 때문에 django에서는 변경된 값을 인지하지 않게 된다.
    - 서버를 구축할 때에는 client를 믿으면 안 된다!
