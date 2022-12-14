# Generated by Django 4.1 on 2022-09-27 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_todolist_is_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='title',
            field=models.TextField(null=True),
        ),
    ]
