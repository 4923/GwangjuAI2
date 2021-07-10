# from django.http import HttpResponse, request
from django.shortcuts import render


# Create your views here.
def hello_world(request):  # register -> request
    if request.method == "POST":
        return render(
            request, "accountapp/hello_world.html", context={"text": "POST METHOD!"}
        )
    else:  # GET
        return render(
            request, "accountapp/hello_world.html", context={"text": "GET METHOD!"}
        )
