# Generated by Django 3.0 on 2023-03-04 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0002_remove_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, max_length=264),
        ),
    ]