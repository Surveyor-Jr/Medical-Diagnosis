# Generated by Django 4.0.1 on 2022-01-23 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(help_text='(e.g. 0776887606', max_length=10)),
                ('paid_on', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField(default=1, editable=False)),
                ('expire_date', models.DateField()),
                ('reference_code', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Billing Information',
            },
        ),
    ]
