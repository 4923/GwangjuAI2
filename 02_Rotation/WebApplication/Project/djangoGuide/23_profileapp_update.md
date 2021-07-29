# 생성한 프로필을 업데이트 하는 기능

## 프로필 수정
```py
# profileapp/views.py
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = "target_profile"
    form_class = ProfileCreateForm
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = "profileapp/update.html"
```

1. model을 Profile로 지정한다.
2. 업데이트하려면 사용자의 pk를 알아야 하므로 accountapp의 views.py에서 한 것 처럼 `context_object_name`을 생성한다.
    - 이 때 `target_user`가 아닌 `target_profile`이라고 설정해야한다. 유의 할 것
3. form_class를 위에서 생성한 ProfileCreateView로 설정한다.

## 로그인한 유저에게만 edit 버튼 노출
- 참고 : accountapp/details.html, decorator
html에서도

로직에서도 막아야 한다. (인증)
views.py 

- 로그인 되어있지 않으면 프로필을 만들 수 없음 => 로그인이 필요하다고 표시할 것
    - @method_decorator
        - import도 필요

    - 커스텀 decorator 만들고  (profile_ownership_required)
        - updateview, createview에 모두 decorator적용
    
## get_success_url : 수정 성공했을때 detail page로 이동하도록 함.
```py
# profileapp/views.py ProfileUpdateView
# profileapp/views.py ProfileCreateView
def get_success_url(self):
    return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})
```
- 받는게 self뿐이기 때문에 pk를 self에서 뽑아오는데 object로 불러온다. : profile의 pk (Profile의 View이므로)
- 결과적으로 `self.object.user.pk`와 `context_object_name` = 'target_profile' 같다.


**하는김에 accountapp의 get_success_url도 변경**
```py
# accountapp/views.py AccountUpdateView
def get_success_url(self):
    return reverse('accountapp:detail', kwargs={'pk': self.object.pk})   # user의 pk (AccountUpdateView이므로)
```
- updateview에서는 self.object : target_user
- pk 헷갈릴 땐 클래스 이름 잘 살펴볼 것 (Account인지 Profile인지)