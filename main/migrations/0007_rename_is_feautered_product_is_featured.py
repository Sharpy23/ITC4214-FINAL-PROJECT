# Generated by Django 5.0.7 on 2024-07-20 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_banner_options_alter_brand_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_feautered',
            new_name='is_featured',
        ),
    ]