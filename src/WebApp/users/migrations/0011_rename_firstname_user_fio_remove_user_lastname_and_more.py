# Generated by Django 4.1.7 on 2023-02-19 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_user_city_user_organization'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='firstname',
            new_name='fio',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='middlename',
        ),
    ]