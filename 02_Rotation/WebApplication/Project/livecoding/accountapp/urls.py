from django.urls import path

from accountapp.views import AccountCreateView, hello_world

app_name = "accountapp"

# 어떤 주소를 적어야 들어갈 수 있는지
urlpatterns = [
    path("hello_world/", hello_world, name="hello_world"),
    path("create/", AccountCreateView.as_view, name="create"),
    # 두번째 인자로 가져와야 할 건 함수 (view) 인데 AccountCreateView는 클래스라 .as_view를 추가해야 한다. 추가하면 view로 가져올 수 있음.
]
