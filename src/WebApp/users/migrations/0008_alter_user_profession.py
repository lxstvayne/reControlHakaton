# Generated by Django 4.1.7 on 2023-02-18 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profession_alter_user_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profession',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profession'),
        ),
    ]
