# Generated by Django 3.1 on 2021-08-13 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobpost', '0002_auto_20210806_2230'),
        ('student', '0002_award_certification_education_skills_workexperince_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='jobApplied',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateApplied', models.DateTimeField(auto_now=True)),
                ('save', models.BooleanField(default=False, null=True)),
                ('apply', models.BooleanField(default=False, null=True)),
                ('JobPosted', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobpost.companyjobpost')),
                ('studentApplied', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
            options={
                'order_with_respect_to': 'dateApplied',
            },
        ),
    ]
