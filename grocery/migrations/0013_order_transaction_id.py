# Generated by Django 3.1.6 on 2021-02-04 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0012_order_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
