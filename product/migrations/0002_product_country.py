# Generated by Django 4.0 on 2021-11-28 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='country',
            field=models.CharField(choices=[('Uzbekistan', 'Uzbekistan'), ('Russia', 'Russia')], default='Russia', max_length=50),
            preserve_default=False,
        ),
    ]
