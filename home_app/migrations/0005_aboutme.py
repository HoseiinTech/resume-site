# Generated by Django 4.1 on 2022-08-14 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0004_statistics'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('body', models.TextField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
