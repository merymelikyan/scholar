# Generated by Django 5.1.1 on 2024-09-23 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_latestcourses_categore1_latestcourses_categore2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='latestcourses',
            old_name='categore1',
            new_name='category1',
        ),
        migrations.RenameField(
            model_name='latestcourses',
            old_name='categore2',
            new_name='category2',
        ),
        migrations.RenameField(
            model_name='latestcourses',
            old_name='categore3',
            new_name='category3',
        ),
    ]
