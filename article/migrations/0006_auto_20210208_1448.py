# Generated by Django 3.1.5 on 2021-02-08 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0005_auto_20210208_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Comment'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]