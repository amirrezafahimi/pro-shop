# Generated by Django 3.2.6 on 2021-08-12 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_rename_total_price_order_totalprice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='payment_method',
            new_name='paymentMethod',
        ),
    ]
