from django.urls import path
from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = "profileapp"

urlpatterns = [
    path("create/", ProfileCreateView.as_view(), name="create"),
    path(
        "update/<int:pk>", ProfileUpdateView.as_view(), name="update"
    ),  # 어떤 객체를 수정 할 것인지 알아야 하므로 pk 추가
]
