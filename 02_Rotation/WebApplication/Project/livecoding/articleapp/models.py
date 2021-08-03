from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Article(models.Model):
    # 작성자 정보
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="article", null=True)

    # 게시글에 포함할 정보
    title = models.CharField(max_length=200, null=True)  # 사진만 올릴수도 있으므로 title null=True

    # 사진
    # upload_to : article/ 이라는 위치에 업로드 할 것 => 전체 프로젝트 폴더의 media dir안의 article에 이미지들 저장한다.
    image = models.ImageField(upload_to="article/", null=True)

    # 본문
    content = models.TextField(null=True)

    # 시간 정보
    created_at = models.DateField(auto_now_add=True, null=True)
