# Generated by Django 3.2.6 on 2021-08-08 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20210807_1521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total_price',
            new_name='totalPrice',
        ),
    ]
