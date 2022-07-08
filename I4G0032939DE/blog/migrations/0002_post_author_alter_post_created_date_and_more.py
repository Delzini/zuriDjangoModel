# Generated by Django 4.0.5 on 2022-06-21 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='Created_date',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='post',
            name='Published_date',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='post',
            name='Text',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='post',
            name='Title',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
