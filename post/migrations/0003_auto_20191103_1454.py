# Generated by Django 2.2.6 on 2019-11-03 22:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0002_post_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='slug',
            new_name='slug_post',
        ),
        migrations.RenameField(
            model_name='postcategory',
            old_name='slug',
            new_name='slug_category',
        ),
        migrations.RenameField(
            model_name='postseries',
            old_name='slug',
            new_name='slug_series',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
    ]