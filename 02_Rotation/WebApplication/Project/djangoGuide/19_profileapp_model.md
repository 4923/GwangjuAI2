# profile model 생성

## accountapp
accountapp을 만들 때에는 Django에서 제공하는 UserCreationForm 을 사용했다.
- 왜? 웹사이트에서 계정은 필수 요소이기 때문.
- Update에서 id를 비활성화 하기 위해 약간의 커스터마이징을 하기는 했지만, 일단 기본제공폼이 있었기에 가능했다.

## profileapp
그러나 profile은 부가요소로, 웹사이트 구성의 필수 요소가 아니다.   
$\therefore$ form을 처음부터 만들어야 한다.

### 개발방법
1. model 선언
2. 해당 app이 필요로 하는 기능을 form의 필드로 구현한다.

문제! 그런데 이 필드의 개수가 많아지면 관리가 어려워진다.


django의 기본 model form (UserCreationForm과는 다른 form) 을 상속받아 **어떤 client로부터 값을 입력받을것인지 설정한다.**

### 과정
**모델 생성**

1. 장고에서 제공하는 model을 상속받는다.
    ```py
    # profileapp/models.py
    class Profile(models.Model):
    ```
2. account와 일대일(`OneToOneField`)로 연결이 되어야 하는 기능 (profile) 이므로 파라미터로 연결되고자 하는 클래스를 넘긴다.
    ```py
        user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    ```
    - 이 때 User는 django에서 제공하는 기본 사용자 모델이다. (import 필요)
    - `on_delete` : 삭제되었을 때 수행할 명령
        - `CASCADE` : 회원이 탈퇴했을 때 account에 연결된 profile도 사라지게 된다. (cascade : 종속)
        - `SET_NULL` : 회원이 작성했던 게시글은 글쓴이를 모르게 한 상태로 남긴다.
    - related_name : 이 뭐였더라?

3. 일반적으로 profile에 포함되는 profile image, nickname, profile message 필드도 만들어야 한다.
    - 각 속성에 맞는 Field를 생성하고 속성값을 설정한다.
    ```py
        image = models.ImageField(upload_to="profile/", null=True)
        nickname = models.CharField(max_length=10, null=True, unique=True)
        message = models.CharField(max_length=200, null=True)
    ```
    - image
        - upload_to : 사진을 받았을 때 저장할 위치를 지정한다. 원래는 MEDIA_ROOT 안에 저장되지만 사진들이 많아져 혼동될 경우를 대비하여 MEDIA_ROOT/profile 를 생성한다. 
        - null : 이미지가 없을 때에도 프로필은 생성 또는 업데이트 되어야 하므로 True로 설정한다.
    
    - nickname
        - unique : 값을 True로 설정함으로써 nickname이 고유한 값을 가지도록 설정한다.
        - null : 닉네임이 없으면 안되지만 우선 True로 설정한다. 이 부분은 이후에 처리한다.
        


**makemigrations, migrate**
4. model을 작성했으니 터미널에서 migrations를 만든다.
    - 이 때 이미지 프로세싱하는 라이브러리인 pillow를 설치하지 않았다면 에러가 발생한다.
        - `pip install pillow`
5. migrate를 통해 생성된 변경사항 파일을 DB에 반영한다.


### 이제 profileapp/forms.py를 작성한다.