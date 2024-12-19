# Generated by Django 5.1.4 on 2024-12-18 10:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0003_builtcountry_rename_color_name_productcolor_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='built_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.builtcountry', verbose_name='کشور سازنده'),
        ),
    ]
