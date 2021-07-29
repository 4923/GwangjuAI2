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

## design
**edit 버튼을 icon으로 변경**
1. material icons 검색
    - [google fonts icons](https://fonts.google.com/icons?selected=Material+Icons:delete)
    - [icons github](https://github.com/google/material-design-icons) -> getting started

2. 복사해서 외부 source를 담는 head.html에 적는다.
```html
<link href="https://fonts.googleapis.com/css2?family=Material+Icons"
      rel="stylesheet">
```

3. class로 적용한다.
```html
<a href="{% url 'profileapp:update' pk=target_user.profile.pk %}" class="material-icons">
edit
</a>
```

이 때 a 태그 안의 텍스트가 icon 이름이 된다. (edit라고 적어두었으니 관련 아이콘이 적용된다.)

**버튼 디자인**
- 버튼 색 변경: color
- 하이퍼링크 밑줄 제거: text-decoration
- 그림자 효과 추가 : box-shadow
    - 그림자의 위치(x,y), 크기, 색깔
        - ex) 0 0 3px black
- 외곽형태 변경: border-radius
- 내부여백 (외부 : margin) : padding

```css
/* static/base.css */
.round_button {
    color: black;
    text-decoration: none;
    box-shadow: 0 0 3px black;
    border-radius: 20rem;
    padding: 0.3rem;
}   
```

**마우스오버시 변경되는 색**
클래스에 작업을 했을 때 변하는 내용이라 별도로 작업
```css
/* static/base.css */
.round_button:hover{
    color: dimgrey;
}
```