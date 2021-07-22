from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

# custom decorator
def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        # User를 계속 target_user라고 사용했으므로 target_user를 변수명으로 사용
        # all로 가져오는 것이 아니라 필요한 객체만 가져온다.
        # 단일 객체를 가져올 때에는 고유값 pk가 필요하다. (primary_key)
        # pk는 kwargs['pk']에 있으므로 조건으로 넘긴다.
        target_user = User.objects.get(pk=kwargs["pk"])
        if target_user == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    return decorated  # 호출하는것이 아니므로 () 사용 X, 함수 자체를 되돌려 준다.
