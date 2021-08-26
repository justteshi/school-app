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
    TEACHER_TYPE = (
        ('Ръководство', 'Ръководство'),
        ('Чужди езици', 'Чужди езици'),
        ('Природни науки', 'Природни науки'),
        ('Обществени науки', 'Обществени науки'),
    )

    name = models.CharField(max_length=50)
    portfolio = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    type = models.CharField(max_length=256, choices=TEACHER_TYPE, null=True, blank=True)
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


class ClassTest(models.Model):
    SUBJECT_CHOICES = (
        ('Математика', 'Математика'),
        ('Български език и литература', 'Български език и литература'),
        ('Английски език', 'Английски език'),
        ('Немски език', 'Немски език'),
        ('Испански език', 'Испански език'),
        ('Руски език', 'Руски език')
    )
    SROK_CHOICES = (
        ('I срок', 'I срок'),
        ('II срок', 'II срок')
    )
    KLAS_CHOICES = (
        ('8','8'),
        ('9','9'),
        ('10','10'),
        ('11','11'),
        ('12','12'),
    )
    PARALELKA_CHOICES = (
        ('А', 'А'),
        ('Б', 'Б'),
        ('В', 'В'),
        ('Г', 'Г'),
    )

    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    date = models.DateField()
    srok = models.CharField(max_length=10, choices=SROK_CHOICES)
    klas = models.CharField(max_length=50, choices=KLAS_CHOICES)
    paralelka = models.CharField(max_length=10, choices=PARALELKA_CHOICES)

    def __Str__(self):
        return self.subject + self.klas + self.paralelka