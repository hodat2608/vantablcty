# Generated by Django 4.2.1 on 2023-07-28 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vantablack', '0009_alter_share_post_share_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentviews',
            name='share_post_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vantablack.share_post'),
        ),
    ]
