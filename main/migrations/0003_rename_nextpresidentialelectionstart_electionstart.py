# Generated by Django 4.2.1 on 2023-05-12 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_nextpresidentialelectionstart'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NextPresidentialElectionStart',
            new_name='ElectionStart',
        ),
    ]
