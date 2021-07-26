from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

# Create your views here.
class ProfileCreationView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    # 완성되었을 때 향할 곳
    success_url = reverse_lazy("accountapp:hello_world")
    # 프로필을 만들 때 어떤 페이지를 기준으로 렌더링 할지
    template_name = "profileapp/create.html"
