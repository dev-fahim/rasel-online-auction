# Generated by Django 3.2.4 on 2022-06-18 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0014_rename_user_id_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_rejected',
            field=models.BooleanField(default=False),
        ),
    ]
