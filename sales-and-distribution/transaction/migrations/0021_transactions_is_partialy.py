# Generated by Django 2.2 on 2020-01-20 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0020_transactions_detail_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='is_partialy',
            field=models.BooleanField(default=False),
        ),
    ]
