# Generated by Django 5.1.1 on 2024-09-21 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FooterText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.CharField(blank=True, max_length=255, null=True)),
                ('text2', models.CharField(blank=True, max_length=255, null=True)),
                ('text3', models.CharField(blank=True, max_length=255, null=True)),
                ('link_url', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Footer Text',
                'verbose_name_plural': 'Footer Text',
            },
        ),
        migrations.CreateModel(
            name='HeaderText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('quastion', models.CharField(max_length=255)),
                ('url_name', models.CharField(max_length=255)),
                ('html_class', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Header Text',
                'verbose_name_plural': 'Header Texts',
            },
        ),
    ]