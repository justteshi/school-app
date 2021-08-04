from django.db import models

# Create your models here.

class HomePageArticle(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=4096)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class SchoolEmployee(models.Model):
    name = models.CharField(max_length=50)
    portfolio = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    #TODO create custom method to rename the photo and folder location
    photo = models.ImageField(upload_to='teachers', null=True, blank=True)

    def __str__(self):
        return self.name

