# Generated by Django 5.1.1 on 2024-09-21 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_headertext_quastion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='headertext',
            old_name='html_icon',
            new_name='quastion',
        ),
        migrations.RenameField(
            model_name='headertext',
            old_name='html_main',
            new_name='request',
        ),
        migrations.RemoveField(
            model_name='headertext',
            name='url_icon',
        ),
        migrations.RemoveField(
            model_name='headertext',
            name='url_main',
        ),
    ]