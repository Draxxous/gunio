# Generated by Django 3.0.5 on 2020-04-23 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200423_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendship',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined')], default='pending', max_length=8),
        ),
    ]