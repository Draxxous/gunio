# Generated by Django 3.0.5 on 2020-04-23 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200423_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.FileField(null=True, upload_to='uploads/'),
        ),
    ]
