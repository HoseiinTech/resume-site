# Generated by Django 4.1 on 2022-08-15 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0015_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Message',
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name_plural': 'Message'},
        ),
    ]
