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