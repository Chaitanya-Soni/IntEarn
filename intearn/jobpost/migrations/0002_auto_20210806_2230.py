# Generated by Django 3.1 on 2021-08-06 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobpost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyjobpost',
            name='dateCreated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
