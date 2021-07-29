# profile forms.py 생성
> form을 model에서 자동으로 변환한다. 

```py
class ProfileCreateForm(ModelForm):
    class Meta:
        model = Profile
        # models안에 적은 속성객체는 네개다.
        # 근데 왜... 세개만 받을까?
        # 서버는 클라이언트를 믿으면 안되기 때문 : user는 제외한다. (내것만 만들도록 설정)
        # 서버 내에서 직접 요청을 보내는 사람이 누구인지 확인하고 그 유저 객체의 프로필을 서버가 배정하도록 함.

        fields = ["image", "nickname", "messages"]
```

1. ProfileCreateForm class 생성
    profileapp에서의 naming convention도 camelCase로 유지하고 class를 생성한다.
    - django에서 기본으로 제공하는 ModelForm을 상속받는다.
2. Meta
    - 내부에 meta라는 class를 또 생성하며 이는 django 구문이다.
    - 이 때 Meta는 메타 정보를 담는 클래스다.
    ```py
    class ProfileCreateForm(ModelForm):
        class Meta:
    ```
    - 메타정보란? : 실제 데이터는 아니지만 관계있는 데이터 외적인 정보들
        - 이미지의 예
            - 이미지는 pixel 정보다.
            - 이미지의 메타 데이터는 이미지 외적인 요소들이다. (언제, 어떤 카메라로, 어디에서 찍었는지)
            - 그런 정보들은 이미지 정보에 메타정보라는 이름으로 포함된다. 
    
3. Form의 명세서 작성
    ```py
    model : Profile
    fields = ["image", "nickname", "messages"]
    ```
    - 어떤 모델을 쓸 것인가? : model = Profile
    - 받아올 필드는 무엇인가? : models.py에서 생성한 필드 목록
        - **이 때 user는 제외한다.**, 왜?
            - 서버는 클라이언트에서 보내는 정보를 믿을 수 없기 때문이다.
            - user까지 받아버리면 다른 사용자의 profile에까지 접근할 수 있게 된다.
            - $\therefore$ 서버 내에서 직접 요청을 보내는 사람이 누구인지 확인하고 그 유저 객체의 프로필을 서버가 배정하도록 한다.

### 이제 urls.py에서 url을 연결한다.