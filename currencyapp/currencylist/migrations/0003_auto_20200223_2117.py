# Generated by Django 3.0.3 on 2020-02-23 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencylist', '0002_auto_20200223_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangerate',
            name='end_date',
            field=models.DateField(blank=True, default=None, editable=False, null=True),
        ),
    ]
