# Generated by Django 4.2.5 on 2023-09-17 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_order_order_product_payment_delete_customer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='is_ordered',
            new_name='is_orderd',
        ),
    ]
