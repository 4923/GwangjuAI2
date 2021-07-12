# from django.http import HttpResponse, request
from django.shortcuts import render


# Create your views here.
def hello_world(request):  # register -> request
    if request.method == "POST":
        # temp : user에게 받은 입력을 받았다가 되돌려준다 (return에서)
        temp = request.POST.get("input_text")  # post 방식에서 get을 사용하면 post 안의 데이터를 뽑아낼 수 있다.
        return render(request, "accountapp/hello_world.html", context={"text": temp})
    else:  # GET
        return render(request, "accountapp/hello_world.html", context={"text": "GET METHOD!"})
