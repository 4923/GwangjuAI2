from django.contrib.auth.decorators import login_required
from articleapp.decorators import article_ownership_required
from django.urls import reverse_lazy, reverse

from django.views.generic import CreateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView

from articleapp.forms import ArticleCreateForm
from articleapp.models import Article

from django.utils.decorators import method_decorator

# Create your views here.


@method_decorator(login_required, "get")
@method_decorator(login_required, "post")
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreateForm  # model form을 기반으로 만들었다.
    success_url = reverse_lazy("articleapp:list")
    template_name = "articleapp/create.html"

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = "target_article"  # 객체 지정
    template_name = "articleapp/detail.html"  # 렌더링 페이지


@method_decorator(article_ownership_required, "get")
@method_decorator(article_ownership_required, "post")
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreateForm
    context_object_name = "target_article"
    template_name = "articleapp/update.html"

    def get_success_url(self):
        return reverse("articleapp:detail", kwargs={"pk": self.object.pk})
        # self.object == target_article (거의 동일)
        # Article은 user를 가지고있지 않으니 self.object.user.pk는 불가 / 대신 self.object.writer.pk는 가능
        # 식별하기 번거로우므로 self.object.pk로 지정


@method_decorator(article_ownership_required, "get")
@method_decorator(article_ownership_required, "post")
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = "target_article"
    success_url = reverse_lazy("articleapp:list")
    template_name = "articleapp/delete.html"


class ArticleListView(ListView):
    model = Article
    context_object_name = "article_list"
    template_name = "articleapp/list.html"
    paginate_by = 20
