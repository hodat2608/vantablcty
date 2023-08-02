# Generated by Django 4.2.1 on 2023-08-02 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vantablack', '0010_commentviews_share_post_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentviews',
            name='post_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vantablack.postviews'),
        ),
        migrations.AlterField(
            model_name='commentviews',
            name='share_post_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vantablack.share_post'),
        ),
    ]
