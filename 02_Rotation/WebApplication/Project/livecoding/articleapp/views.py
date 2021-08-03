from django.urls import reverse_lazy

from django.views.generic import CreateView

from articleapp.forms import ArticleCreateForm
from articleapp.models import Article

# Create your views here.


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreateForm  # model form을 기반으로 만들었다.
    success_url = reverse_lazy("articleapp:list")
    template_name = "articleapp/create.html"

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)
