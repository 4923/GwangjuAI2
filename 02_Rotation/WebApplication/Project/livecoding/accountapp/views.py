from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls.base import reverse_lazy
from accountapp.models import HelloWorld
from django.shortcuts import render
from django.views.generic.edit import CreateView

from django.urls import reverse


def hello_world(request):  # register -> request
    if request.method == "POST":
        # temp : user에게 받은 입력을 받았다가 되돌려준다 (return에서)
        temp = request.POST.get("input_text")  # post 방식에서 get을 사용하면 post 안의 데이터를 뽑아낼 수 있다.

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
    success_url = reverse_lazy("accountapp:hello_world")
    # 위에서처럼 reverse를 그냥 사용하면 안된다.
    # reverse_lazy : reverse와 하는건 똑같다. 인자값을 가지고주소를 역추적 하는건 같은데 함수형에서 reverse해서 추적하는것과 클래스에서 추적하는게 다르기 때문. 나중에 실제 객체가 생성된 후에 필요할때만 불러야 하므로 _lazy를 붙인다.
    # 함수형에선 reverse 클래스에서는 reverse_lazy
    template_name = "accountapp/create.html"
