from profileapp.models import Profile
from django.http import HttpResponseForbidden


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        # request를 보내는 유저와 profile주인을 확보해야 한다.
        # request user : request안에 있다.
        # profile : DB에서 가져온다. how? 해당 Profile class
        # kwargs : dict type 이므로 대괄호로 접근
        target_profile = Profile.objects.get(pk=kwargs["pk"])
        if target_profile.user == request.user:
            return func(request, *args, **kwargs)  # 목표로 하는 함수 실행 (인자도 잊지 말 것)
            # get과 post는 return값이 있으므로 return까지 추가
        else:
            return HttpResponseForbidden()

    return decorated
