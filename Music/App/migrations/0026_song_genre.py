# Generated by Django 3.2.9 on 2022-05-11 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0025_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.CharField(choices=[('0', '-'), ('1', 'Pop'), ('2', 'Hip-Hop'), ('3', 'Rock'), ('4', 'Jazz'), ('5', 'Indian'), ('6', 'Dance/Electronic'), ('7', 'Country'), ('8', 'Metal'), ('9', 'K-Pop'), ('10', 'Acoustic')], default=0, max_length=30),
        ),
    ]
