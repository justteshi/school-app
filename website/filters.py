import django_filters
from .models import Teacher
from django_filters import ChoiceFilter


class TeacherFilter(django_filters.FilterSet):
    TEACHER_TYPE = (
        ('Ръководство', 'Ръководство'),
        ('Чужди езици', 'Чужди езици'),
        ('Природни науки', 'Природни науки'),
        ('Обществени науки', 'Обществени науки'),
    )

    type = ChoiceFilter(choices=TEACHER_TYPE)

    class Meta:
        model = Teacher
        fields = ['type']