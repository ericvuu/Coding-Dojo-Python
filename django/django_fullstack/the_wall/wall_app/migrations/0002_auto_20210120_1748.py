# Generated by Django 2.2.4 on 2021-01-21 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wall_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='context',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='message',
            new_name='context',
        ),
    ]
