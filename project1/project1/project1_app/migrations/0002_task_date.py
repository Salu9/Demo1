# Generated by Django 3.2.12 on 2022-03-23 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1996-03-28'),
            preserve_default=False,
        ),
    ]
