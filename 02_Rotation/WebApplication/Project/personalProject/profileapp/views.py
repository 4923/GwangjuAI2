from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreationView(CreateView):
    model = Profile
    form_class = ProfileCreationForm  # form에서 import
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = "profileapp/create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = "target_profile"
    form_class = ProfileCreationForm
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = "profileapp/update.html"
