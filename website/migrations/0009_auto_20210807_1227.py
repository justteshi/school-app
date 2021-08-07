# Generated by Django 3.2.6 on 2021-08-07 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20210807_0907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.CharField(choices=[('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028'), ('2029', '2029'), ('2030', '2030')], max_length=6)),
                ('link', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='homepagemessages',
            name='important',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
