# Generated by Django 4.1.4 on 2023-05-16 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_myorder_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='myorder',
            name='is_order',
            field=models.BooleanField(default=True),
        ),
    ]
