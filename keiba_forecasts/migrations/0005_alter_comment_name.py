# Generated by Django 3.2.4 on 2021-07-09 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keiba_forecasts', '0004_auto_20210709_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=200, verbose_name='名前'),
        ),
    ]
