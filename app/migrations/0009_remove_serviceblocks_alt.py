# Generated by Django 5.1.1 on 2024-09-23 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_serviceblocks_alt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceblocks',
            name='alt',
        ),
    ]
