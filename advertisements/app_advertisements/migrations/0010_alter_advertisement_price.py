# Generated by Django 4.2.4 on 2023-08-31 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0009_advertisement_favourites_alter_advertisement_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
    ]
