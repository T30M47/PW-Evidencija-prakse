# Generated by Django 4.0.6 on 2022-12-12 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_praksa_datum_zavrsetka'),
    ]

    operations = [
        migrations.AddField(
            model_name='praksa',
            name='broj_odradenih_sati',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]