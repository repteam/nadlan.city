# Generated by Django 5.0 on 2023-12-04 14:00

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('desc', models.CharField(max_length=500, verbose_name='Краткое описание')),
                ('desc_main', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
