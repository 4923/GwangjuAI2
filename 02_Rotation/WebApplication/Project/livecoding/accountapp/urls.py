from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from accountapp.views import (
    AccountCreateView,
    hello_world,
    AccountDetailView,
    AccountUpdateView,
    AccountDeleteView,
)

app_name = "accountapp"

# 어떤 주소를 적어야 들어갈 수 있는지
urlpatterns = [
    path("hello_world/", hello_world, name="hello_world"),
    path("login/", LoginView.as_view(template_name="accountapp/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("create/", AccountCreateView.as_view(), name="create"),
    # 두번째 인자로 가져와야 할 건 함수 (view) 인데 AccountCreateView는 클래스라 .as_view를 추가해야 한다. 추가하면 view로 가져올 수 있음.
    path("create/", AccountCreateView.as_view(), name="create"),
    path("detail/<int:pk>", AccountDetailView.as_view(), name="detail"),
    path("update/<int:pk>", AccountUpdateView.as_view(), name="update"),  # route 이름이 update
    path("delete/<int:pk>", AccountDeleteView.as_view(), name="delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
