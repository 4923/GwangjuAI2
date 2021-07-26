from django.forms import ModelForm
from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        # models안에 적은 속성객체는 네개다.
        # 근데 왜... 세개만 받을까?
        # 서버는 클라이언트를 믿으면 안되기 때문 : user는 제외한다. (내것만 만들도록 설정)
        # 서버 내에서 직접 요청을 보내는 사람이 누구인지 확인하고 그 유저 객체의 프로필을 서버가 배정하도록 함.

        fields = ["image", "nickname", "message"]
