# Generated by Django 3.2.5 on 2021-08-15 08:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0004_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment_reply',
            fields=[
                ('rply_id', models.AutoField(primary_key=True, serialize=False)),
                ('rply', models.TextField()),
                ('timestamp', models.DateField(default=django.utils.timezone.now)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.comment')),
                ('rply_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
