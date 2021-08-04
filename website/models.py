from django.db import models

# Create your models here.

class HomePageArticle(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=4096)
    created_at = models.DateTimeField(auto_now_add=True)