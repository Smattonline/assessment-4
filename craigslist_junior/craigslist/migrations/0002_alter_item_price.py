# Generated by Django 3.2.5 on 2021-07-17 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craigslist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
    ]
