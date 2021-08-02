from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    writer = models.OneToOneField(User, related_name="article", on_delete=models.CASCADE, null=True)

    title = models.CharField(max_length=200, null=True)

    image = models.ImageField(upload_to="article/", null=True)

    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)
