from website.models import HomePageArticle
from django.contrib import admin
from .models import *

# Register your models here.

@admin.action(description='Dublicate article')
def duplicate_article(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()
duplicate_article.short_description = "Duplicate selected record"


@admin.register(HomePageArticle)
class HomePageArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'subject')

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    actions = [duplicate_article]