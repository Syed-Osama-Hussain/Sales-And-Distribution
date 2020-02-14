# Generated by Django 2.2 on 2020-02-14 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0021_transactions_is_partialy'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseheader',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
            preserve_default=False,
        ),
    ]
