# profile 의 url을 연결한다.

### views.py
1. ProfileCreateView class를 생성한다. 
    ```py
    class ProfileCreateView(CreateView):
        model = Profile
        form_class = ProfileCreateForm
        # 완성되었을 때 향할 곳
        success_url = reverse_lazy("accountapp:hello_world")
        # 프로필을 만들 때 어떤 페이지를 기준으로 렌더링 할지
        template_name = "profileapp/create.html"

        def form_valid(self, form):
            # profile creationf form은 세 값만 받기 때문에 user는 넣을 수 없다.
            # form이 가지고 있는 profile instance에 접근한다. : form user -> form.instance
            form.instance.user = self.request.user
            return super().form_valid(form)

            # db에서 이미지에 들어가는 값은 경로! 다
            # 이미지 하나 올리면 media가 생겼을 것
    ```
    1. CreateView를 상속받는 ProfileCreateView class를 생성한다.
    2. model을 Profile로 설정하고 (form에서처럼)
    3. 완성되었을 때, profile이 성공적으로 생성되거나 업데이트 되었을 때 향할 지점을 설정한다.
        - routing에서 사용하는 함수 : reverse_lazy("appname:page")
    4. profile을 생성할 때 기준이 되는 template를 설정하고
        - profileapp의 create.html을 template으로 사용할 것이다. (아직 구현 X)
    
    5. 올바른 form인지 확인하기 위해 form_valid method를 생성한다.
        - ProfileCreateForm은 user를 제외한 field를 받기 때문에 user값을 직접 넘겨줄 수 없는데 이를 해결하기 위한 method다.
        - form이 가지고 있는 profile instance에 접근하여 user값을 요청을 보내는 사용자 정보를 넘겨준다. (`form.instance.user = self.request.user`)
        - 과정이 완료되었으면 상속받은 `super()` 클래스인 `CreateView`에 form_valid를 넘겨준다.

### urls.py
```py
app_name = "profileapp"

urlpatterns = [
    path("create/", ProfileCreateView.as_view(), name="create"),
    path(
        "update/<int:pk>", ProfileUpdateView.as_view(), name="update"
    ),  # 어떤 객체를 수정 할 것인지 알아야 하므로 pk 추가
]
```
0. app_name을 profileapp으로 설정한다.
2. urlpatterns를 추가한다.
    - create가 오면 프로필을 생성하도록 하고, 해당 과정을 create라고 명명한다.
    - path를 가져올 때 as_view()를 써야 함을 잊지 않는다.

