# Generated by Django 4.0.6 on 2022-12-13 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_ukupan_broj_sati_rada_studentdnevnik_ukupan_broj_sati'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdnevnik',
            name='ukupan_broj_sati',
        ),
    ]
