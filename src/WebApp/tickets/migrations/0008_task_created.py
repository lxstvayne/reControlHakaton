# Generated by Django 4.1.7 on 2023-02-18 20:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_task_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
