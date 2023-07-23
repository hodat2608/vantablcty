# Generated by Django 4.2.1 on 2023-07-23 07:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vantablack', '0008_share_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='share_post',
            name='share_post_likes',
            field=models.ManyToManyField(blank=True, related_name='share_post_like', to=settings.AUTH_USER_MODEL),
        ),
    ]