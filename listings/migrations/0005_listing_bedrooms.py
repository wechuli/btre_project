# Generated by Django 2.1.2 on 2018-12-04 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_listing_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bedrooms',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
