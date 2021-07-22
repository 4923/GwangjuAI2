
`views.py`

> 장고에서 decorator를 미리 만들어 두었다.  
> decorator도 함수이므로 불러와야 한다. 

## 1. hello_world 함수에서 로그인 했는지 확인하는 항목을 삭제
```py
if request.user.is_authenticated:
    # 중략
    pass
else:
    return HttpResponseRedirect(reverse("accountapp:login"))
```
- 로그인 하지 않은 상태에서 hello_world에 접근해도 login 페이지로 이동한다.

- 로그인 하는 url이 뭔지 알려주지 않았는데 어떻게 자동으로 찾아가나? : default form 있음
    - 현재 로그인 하는 페이지 : /accounts/login 을 로그인 기본 페이지로 설정했었음
    - accountapp/login 처럼 accounts가 아닌 다른 url을 설정했을 경우 page not founc가 뜰 것
        - 해결? : @login_required(login_url = reverse_lazy('accountapp:login')) 으로 url 지정

## 2. decorator 적용

1. **CDV에서도 @login_required도 적용하기**
    def get ~ 위에 decorator를 적으면 될 것 같지만 구동이 되지 않는다.
    - 왜?
    ```py
    class AccountUpdateView:
        def get():
            # 생략
            pass
    ```
    이기 때문에 get()함수는 함수가 아니라 메서드다.

    - 해결?
        - 함수에 사용한 decorator를 메서드에서도 사용할 수 있게 decorator를 변환 -> django에서 구현한 기능 있음 
            - `@method_decorator` : 함수에 사용한 decorator를 메서드에서도 사용할 수 있게 하는 장고의 기본 구현 decorator
            - 그런데 이거만 사용하면 어떤 method에 적용해야 할 지 알 수 없게 되므로 인자값 추가해야한다. `@method_decorator(login_required, 'get')`
            - 두 메서드에 사용하고 싶다면 decorator를 두 번 사용해야 한다.
        ```py
        # 완성된 AccountUpdateView class
        @method_decorator(login_required, "get")
        @method_decorator(login_required, "post")
        class AccountUpdateView(UpdateView):
            model = User
            form_class = AccountCreationForm
            context_object_name = "target_user"
            success_url = reverse_lazy("accountapp:hello_world")
            template_name = "accountapp/update.html"
        # login 인증이 필요한 다른 class(AccountDeleteView)에도 적용한다.
        ```

2. **Custom decorator**
    > target user == request를 보내는 유저?
    request user 와 target user (account user) 가 동일한지를 확인하는 과정을 거치기 위해

    decorator를 커스텀한다.
    1. accountapp에서 decorators.py 생성 
    2. 하단과 같은 코드 작성
    ```py
    # custom decorator
    def account_ownership_required(func):
        def decorated(request, *args, **kwargs):
            # User를 계속 target_user라고 사용했으므로 target_user를 변수명으로 사용
            # all로 가져오는 것이 아니라 필요한 객체만 가져온다.
            # 단일 객체를 가져올 때에는 고유값 pk가 필요하다. (primary_key)
            # pk는 kwargs['pk']에 있으므로 조건으로 넘긴다.
            target_user = User.objects.get(pk=kwargs["pk"])
            if target_user == request.user:
                return func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden()

        return decorated  # 호출하는것이 아니므로 () 사용 X, 함수 자체를 되돌려 준다.
    ```

## 3. **`views.py`에서 적용**
1. 해당 함수 호출하여 `has_ownership` 생성
    - decorator도 함수이기 때문에 호출 가능
    - `has_ownership = [login_required, account_ownership_required]`
2. method_decorator에 인자로 넘겨주었던 login_required 자리에 has_ownership을 넘겨준다.
```py
# 아래와 같이 수정
@method_decorator(has_ownership, "get")
@method_decorator(has_ownership, "post")
```

