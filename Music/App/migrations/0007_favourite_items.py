# Generated by Django 3.2.9 on 2022-05-03 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_auto_20220430_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourite_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favourite', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.favourite')),
                ('song', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.song')),
            ],
        ),
    ]
