# Generated by Django 2.1.3 on 2019-03-12 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mijngemeente', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notification',
            new_name='UserNotification',
        ),
    ]
