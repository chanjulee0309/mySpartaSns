# Generated by Django 4.2 on 2023-04-17 04:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_usermodel_managers_remove_usermodel_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='follow',
            field=models.ManyToManyField(related_name='followee', to=settings.AUTH_USER_MODEL),
        ),
    ]
