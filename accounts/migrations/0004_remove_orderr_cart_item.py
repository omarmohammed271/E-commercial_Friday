# Generated by Django 5.0.1 on 2024-03-05 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_orderr_orderproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderr',
            name='cart_item',
        ),
    ]
