# Generated by Django 3.2.9 on 2022-05-06 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_favouriteitems_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favouriteitems',
            name='name',
        ),
    ]