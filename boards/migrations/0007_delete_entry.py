# Generated by Django 2.0.5 on 2018-06-22 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0006_entry'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Entry',
        ),
    ]