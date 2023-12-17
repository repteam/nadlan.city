# Generated by Django 5.0 on 2023-12-04 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_cards_options_alter_cards_desc_main_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='images', to='main.cards'),
        ),
    ]
