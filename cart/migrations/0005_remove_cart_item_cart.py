# Generated by Django 5.0.1 on 2024-02-25 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_remove_cart_item_variations_cart_item_variations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_item',
            name='cart',
        ),
    ]