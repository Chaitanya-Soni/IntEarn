# Generated by Django 3.1 on 2021-08-13 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapplied', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobapplied',
            old_name='save',
            new_name='savePost',
        ),
    ]
