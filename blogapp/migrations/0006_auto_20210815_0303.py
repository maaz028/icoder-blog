# Generated by Django 3.2.6 on 2021-08-15 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_comment_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment_parent',
            fields=[
                ('parent_id', models.AutoField(primary_key=True, serialize=False)),
                ('parent_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.comment')),
            ],
        ),
        migrations.DeleteModel(
            name='comment_reply',
        ),
    ]
