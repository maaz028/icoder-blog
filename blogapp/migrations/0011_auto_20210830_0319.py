# Generated by Django 3.2.5 on 2021-08-30 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0010_auto_20210816_1051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='h1content',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='h1heading',
        ),
        migrations.RemoveField(
            model_name='post',
            name='h2content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='h2heading',
        ),
    ]
