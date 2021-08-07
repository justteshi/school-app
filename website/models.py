from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class HomePageMessages(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=4096)
    created_at = models.DateTimeField(auto_now_add=True)
    important = models.BooleanField(null=True, blank=True)
    def __str__(self):
        return self.title

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    portfolio = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    #TODO create custom method to rename the photo and folder location
    photo = models.ImageField(upload_to='teachers', null=True, blank=True)

    def __str__(self):
        return self.name


class Publication(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=1024)
    
    def __str__(self):
        return self.title


class Budget(models.Model):
    YEAR_CHOICES = (
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
        ('2022', '2022'),
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
        ('2027', '2027'),
        ('2028', '2028'),
        ('2029', '2029'),
        ('2030', '2030'),
    )
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=6, choices=YEAR_CHOICES)
    link = CharField(max_length=500)
    def __str__(self):
        return self.title
