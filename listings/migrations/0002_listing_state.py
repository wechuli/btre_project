# Generated by Django 2.1.2 on 2018-12-04 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='state',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
