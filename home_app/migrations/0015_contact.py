# Generated by Django 4.1 on 2022-08-15 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0014_alter_aboutme_options_alter_home_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('body', models.TextField()),
            ],
        ),
    ]