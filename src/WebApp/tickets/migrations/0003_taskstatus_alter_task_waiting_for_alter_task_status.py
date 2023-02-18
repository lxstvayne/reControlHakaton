# Generated by Django 4.1.7 on 2023-02-18 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_alter_ticket_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('name', models.CharField(max_length=48, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='waiting_for',
            field=models.CharField(choices=[('ЭЛЕКТРИК', 'Electrician'), ('БУХГАЛТЕР', 'Accountant')], max_length=128),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.taskstatus'),
        ),
    ]