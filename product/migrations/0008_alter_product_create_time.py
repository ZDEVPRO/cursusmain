# Generated by Django 4.0 on 2021-12-17 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_product_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='create_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
