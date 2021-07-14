# View : Django View pattern

지금까지 hello world라는 함수를 열심히 만들었다. 장고의 패턴을 이해하고 사용하기 위함.

form에서 input text를 받고 hello world라는 함수를 통해 데이터베이스에 저장하고 그게 html로 내보내진다. 이 때 django template lang의 for문을 사용해 데이터베이스의 모든 데이터를 내보냈었다.

hello world는 function, 다시 말해 로직인데 현재는 아무나 hello world를 통해 데이터를 db에 저장할 수 있다. 근데 아무나 쓸 수 있게 하면 서비스에 문제가 생긴다.

이 때 추가하는 과정이 authentication 인증과정이다 : 접근제어

인증과정을 만들자
뭐가 필요하냐? : 계정 앱이다

그래서 우리가 hello world를 만들기 전에 account app을 만든거다.

account app도 자원인데 account app을 만들기 위해 필요한 건
1. sign up : 회원가입
2. view info : 본인 페이지 열람
3. change info : 개인정보 변경
4. quit : 탈퇴

이렇게 네가지다. (기본 요구사항)

특이한건 계정은 특수한 권한이므로 로그인 과정도 추가해야 한다.
이상의 과정을 구현해보자.

## logic 설정 : views.py에서
```py

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("accoutapp:hello_world")  # 그냥 사용하면 안된다.
    # reverse_lazy : reverse와 하는건 똑같다. 인자값을 가지고주소를 역추적 하는건 같은데 함수형에서 reverse해서 추적하는것과 클래스에서 추적하는게 다르기 때문. 나중에 실제 객체가 생성된 후에 필요할때만 불러야 하므로 _lazy를 붙인다.
    # 함수형에선 reverse 클래스에서는 reverse_lazy
    template_name = "accountapp/create.html"
```


## routing : urls.py 에서

```py

urlpatterns = [
    # 생략
    # 어떤 주소를 적어야 들어갈 수 있는지
    path(
        "create/", AccountCreateView.as_view(), name="create"
    ),  # 두번째 인자로 가져와야 할 건 함수 (view) 인데 AccountCreateView는 클래스라 .as_view를 추가해야 한다. 추가하면 view로 가져올 수 있음.
]

```

- 여기까지 해서 서버 돌리면 template이 없다고 뜨니까 template 만들어야 한다.

## create.html
회원가입 페이지 생성
- class center로 중앙정렬 가능
- base.html에서 content가 아닌 contents로 변수명을 지정했기 때문에 contents로 써야 함.

## login logout?
- 기본적으로 장고가 함
- 패스워드 가져와서 해시 비교하고 어쩌구 저쩌구 할 필요 없다.

1. urls.py에서 주소 정함
```py
path("login/", LoginView.as_view(templatename="accountapp/login.html"), name="login"),
path('logout/', LogoutView.as_view(), name="logout"),
```
2. login.html 작성

- 아니 주소에 만든 적 없는 profile로 redirect가 되는데 왜그런걸까?
- login view, logout view
    - get에서 post로 데이터 (로그인) 정보를 넘긴다.
    1. next값이 들어갔으면 재연결
    2. 없으면 LOGIN_REDIRECT_URL 에 지정된 주소로 redirect
    3. 2가 없으면 장고 자체적으로 default로 넘어간다 : account/profile
        - 기본 django의 default redirect url : account/profile
        - 이게 싫으면 2번을 고쳐야 함
        - how?
            - main app의 settings.py 맨 밑에
                ```py
                LOGIN_REDIRECT_URL = reverse_lazy('accountapp:hello_world')
                ```
                - login 했을 때 어디로 가긴 가야하는데 일단 만들어둔게 hello_world만 있으므로 hello_world로 redirect 하도록 지시
            - logout도 같은 방식으로 진행한다. LOGIN_REDIRECT_URL 밑에 이어서 적는다.
                ```py
                # LOGIN_REDIRECT_URL ~ 생략
                LOGOUT_REDIRECT_URL = reverse_lazy('accountapp:login')
                ```