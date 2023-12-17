# Generated by Django 5.0 on 2023-12-07 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_cards_size_warning_alter_gallery_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='i_agree',
            field=models.BooleanField(default=False, verbose_name='Большой размер'),
        ),
        migrations.AlterField(
            model_name='cards',
            name='size_warning',
            field=models.TextField(blank=True, default='Внимание! Если размер файла привышает 500кб, то загрузка сайта будет снижена!', null=True, verbose_name='Большие данные'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Картинка'),
        ),
    ]
