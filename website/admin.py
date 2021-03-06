from website.models import HomePageMessages
from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin



# Register your models here.

@admin.action(description='Dublicate article')
def duplicate_article(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()
duplicate_article.short_description = "Duplicate selected record"


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User role',
            {
                'fields':(
                    'is_student',
                    'is_teacher'
                )
            }
        )
    )


@admin.register(HomePageMessages)
class HomePageMessagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    actions = [duplicate_article]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'subject', 'type')
    actions = [duplicate_article]


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    actions = [duplicate_article]

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('title', 'year')


@admin.register(ClassTest)
class ClassTestAdmin(admin.ModelAdmin):
    list_display = ('subject', 'klas', 'paralelka', 'srok', 'date')


@admin.register(ClassOfStudents)
class ClassOfStudentsAdmin(admin.ModelAdmin):
    pass