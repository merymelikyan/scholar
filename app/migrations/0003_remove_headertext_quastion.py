# Generated by Django 5.1.1 on 2024-09-21 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_headertext_html_class_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headertext',
            name='quastion',
        ),
    ]
