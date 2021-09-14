# Generated by Django 3.2.6 on 2021-09-01 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_budget_classtest_homepagemessages_publication_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassOfStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('klas', models.CharField(choices=[('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=50)),
                ('paralelka', models.CharField(choices=[('А', 'А'), ('Б', 'Б'), ('В', 'В'), ('Г', 'Г')], max_length=10)),
            ],
        ),
    ]