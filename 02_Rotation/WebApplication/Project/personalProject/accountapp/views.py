from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls.base import reverse_lazy
from accountapp.models import HelloWorld
from django.shortcuts import render
from django.views.generic.edit import CreateView

from django.urls import reverse

# Create your views here.
def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get("input_text")

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse("accountapp:hello_world"))

    else:
        hello_world_list = HelloWorld.objects.all()
        return render(
            request, "accountapp/hello_world.html", context={"hello_world_list": hello_world_list}
        )


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("accoutapp:hello_world")
    template_name = "accountapp/create.html"
