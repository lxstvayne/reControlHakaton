# Generated by Django 4.1.7 on 2023-02-18 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_alter_task_waiting_for'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='address',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
