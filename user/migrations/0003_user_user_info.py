# Generated by Django 3.1.7 on 2021-03-16 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210315_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_info',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
    ]