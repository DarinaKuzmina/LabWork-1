# Generated by Django 2.1.2 on 2018-10-13 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nap', '0002_categorie_icon_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='task',
            name='icon',
        ),
        migrations.DeleteModel(
            name='Icon',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
