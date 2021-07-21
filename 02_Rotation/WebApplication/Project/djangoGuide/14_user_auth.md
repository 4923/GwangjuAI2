# 회원 검증

> user == target_user ?

문제 : 로그인 하지 않은 상황 또는 다른 유저로 로그인 한 상황에서 detail/pk 로 접근해도 다른 유저의 페이지가 보인다.
해결 : 상세정보와 탈퇴 버튼이 분기문 없이 노출되므로 detail.html에서  user(client) 와 account 객체가 동일할 때에만 delete 하도록 설정한다.

1. 로그인한 유저에게만 `hello_world` 보여주기
    - accountapp/views.py 에서 진행
    - templates/hello_world의 요청 관련된 인자가 request에 들어가 있다. (`request.user : request.user`)
    1. user에 user.is_authenticated 가 있으므로 : '로그인 되어있다면' -> hello_world 안의 내용 전부 실행
    2. 아니라면 -> 로그인 창으로 redirect

    ```py
        if request.user.is_authenticated:
            if request.method == "POST":
                # 중략
        else:
            return HttpResponseRedirect(reverse("accountapp:login"))
    ```

2. 로그인한 유저에게만 `update` 보여주기
    - 1과 같은 방식으로 진행
    - `get` 방식과 `post` 방식 모두 사용해야 하므로 아래와 같이 `class AccountUpdateView`에 함수를 추가한다
    ```py
    class AccountUpdateView(UpdateView):
    # 생략

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse("account:login"))

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse("account:login"))
    ```

3. 로그인한 유저에게만 `delete` 보여주기
    - 2와 동일
    - 같은 코드를 복사 붙여넣기 한다.'

> 이렇게 반복되는 코드는 decorator로 정리할 수 있다.

4. 로그인 상태에서 다른 사람의 update, delete page에 접근할 수 없게 하기
    - detail.html 에서 user == target_user 임을 확인했을 때 정보를 제공한다.
    
