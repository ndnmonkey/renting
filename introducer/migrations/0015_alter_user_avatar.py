# Generated by Django 3.2.5 on 2021-11-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introducer', '0014_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='media/introducer/profile/', upload_to='media/introducer/profile/'),
        ),
    ]
