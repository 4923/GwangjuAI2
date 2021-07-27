from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView

from profileapp.forms import ProfileCreateForm
from profileapp.models import Profile

# Create your views here.
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    # 완성되었을 때 향할 곳
    success_url = reverse_lazy("accountapp:hello_world")
    # 프로필을 만들 때 어떤 페이지를 기준으로 렌더링 할지
    template_name = "profileapp/create.html"

    def form_valid(self, form):
        # profile creationf form은 세 값만 받기 때문에 user는 넣을 수 없다.
        # form이 가지고 있는 profile instance에 접근한다. : form user -> form.instance
        form.instance.user = self.request.user
        return super().form_valid(form)

        # db에서 이미지에 들어가는 값은 경로! 다
        # 이미지 하나 올리면 media가 생겼을 것


class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = "target_profile"
    form_class = ProfileCreateForm
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = "profileapp/update.html"
