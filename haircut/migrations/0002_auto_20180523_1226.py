# Generated by Django 2.0.1 on 2018-05-23 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('haircut', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='customer_name',
            new_name='customers_name',
        ),
    ]