# Generated by Django 4.1.7 on 2023-02-18 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_firstname_user_lastname_user_middlename_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(max_length=255, null=True, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profession',
            field=models.CharField(choices=[('ЭЛЕКТРИК', 'Electrician'), ('БУХГАЛТЕР', 'Accountant')], max_length=128, null=True),
        ),
    ]