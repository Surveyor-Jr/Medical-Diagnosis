# Generated by Django 4.0.1 on 2022-01-23 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billinginformation',
            name='price',
            field=models.IntegerField(default=1),
        ),
    ]
