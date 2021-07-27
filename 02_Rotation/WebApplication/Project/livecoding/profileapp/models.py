from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    # User
    # account와 일대일 연결되어야 하므로 파라미터로 연결하고자 하는 클래스를 넘긴다 (User, django에서 기본 제공하는 그 유저모델)

    # on_delete = models.CASCADE
    # 속성으로 on_delete를 넣는다.: models에서 CASCADE를 속성값으로 준다.
    # on_delete : 는 삭제되었을 때 라는 뜻
    # 회원탈퇴했을 때 profile 도 연결되었으므로 어떻게 할 지 설정해야 한다.
    # 이 속성의 값을 CASCADE(=종속)으로 하면 account가 사라졌을 때 profile도 사라진다.
    # on_delete=models.SETNULL
    # 회원이 작성했던 게시글은 삭제하지 않고 남길 때 : 글쓴이를 모르는 상태로 하려면
    # on_delete=models.SET_NULL
    # 이 옵션으로 해결 가능

    # related_name = profile
    # 이 뭐였더라

    # image, nickname, message를 만들어야 한다.
    image = models.ImageField(upload_to="profile/", null=True)
    # upload_to
    # 사진을 받았을 때 어디로 저장하나? 원래 MEDIA_ROOT 안에 저장되지만 그 안에서도 profile 폴더를 생성해서 그 안에 프로필 사진들을 넣는다.
    # null
    # 이미지가 없을 때 어떻게 할지? => 상관 X

    nickname = models.CharField(max_length=10, unique=True, null=True)
    # unique값을 True로 함으로써 nickname이 고유한 값을 가지도록 설정한다.
    # 여기선 null을 True로 하지만 나중에 처리할 예정

    messages = models.CharField(max_length=200, null=True)
