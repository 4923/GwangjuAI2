from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import HelloWorld


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
