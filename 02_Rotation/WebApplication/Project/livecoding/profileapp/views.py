from django.contrib.auth.decorators import login_required
from django.urls.base import reverse
from profileapp.decorators import profile_ownership_required
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView

from profileapp.forms import ProfileCreateForm
from profileapp.models import Profile

from django.utils.decorators import method_decorator

# Create your views here.
# login_required 는 왜 has_ownership에서 했던 것 처럼 리스트를 만들지 않나? (accountapp/views.py)
# login 되지 않은 유저가 profile을 가질 리가 없기 때문
@method_decorator(login_required, "get")
@method_decorator(login_required, "post")
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    # 프로필을 만들 때 어떤 페이지를 기준으로 렌더링 할지
    template_name = "profileapp/create.html"

    def form_valid(self, form):
        # profile creationf form은 세 값만 받기 때문에 user는 넣을 수 없다.
        # form이 가지고 있는 profile instance에 접근한다. : form user -> form.instance
        form.instance.user = self.request.user
        return super().form_valid(form)

        # db에서 이미지에 들어가는 값은 경로! 다
        # 이미지 하나 올리면 media가 생겼을 것

    # 완성되었을 때 향할 곳
    def get_success_url(self):
        return reverse("accountapp:detail", kwargs={"pk": self.object.user.pk})     # profile의 pk


@method_decorator(profile_ownership_required, "get")
@method_decorator(profile_ownership_required, "post")
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = "target_profile"
    form_class = ProfileCreateForm
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = "profileapp/update.html"

    # override
    def get_success_url(self):
        # 받는게 self뿐이기 때문에 pk를 self에서 뽑아오는데 object로 불러온다.
        # 결과적으로 self.object.user.pk와 context_object_name = 'target_profile' 같다.
        return reverse("accountapp:detail", kwargs={"pk": self.object.user.pk})     # profile의 pk
