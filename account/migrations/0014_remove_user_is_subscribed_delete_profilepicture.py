# Generated by Django 4.2.1 on 2023-05-11 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_user_is_subscribed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_subscribed',
        ),
        migrations.DeleteModel(
            name='ProfilePicture',
        ),
    ]
