# Generated by Django 5.0.7 on 2024-07-20 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_product_image_productattribute_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattribute',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]