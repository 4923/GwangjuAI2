from articleapp.views import ArticleCreateView
from django.views.generic import TemplateView
from django.urls import path

app_name = "articleapp"

urlpatterns = [
    path("list/", TemplateView.as_view(template_name="articleapp/list.html"), name="list"),
    path("create/", ArticleCreateView.as_view(), name="create"),
]
