# Generated by Django 4.1 on 2022-08-15 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0013_rename_project_address_project_github_address_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutme',
            options={'verbose_name_plural': 'About Me'},
        ),
        migrations.AlterModelOptions(
            name='home',
            options={'verbose_name_plural': 'Home'},
        ),
        migrations.AlterModelOptions(
            name='statistics',
            options={'verbose_name_plural': 'Statistics'},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='image',
            new_name='profile_photo',
        ),
    ]
