# Generated by Django 3.2.4 on 2021-07-05 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('keiba_forecasts', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='keiba_forecasts.blog'),
        ),
    ]
