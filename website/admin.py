from website.models import HomePageArticle
from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(HomePageArticle)
class HomePageArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

@admin.register(SchoolEmployee)
class SchoolEmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'subject')