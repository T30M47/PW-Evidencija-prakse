# Generated by Django 4.0.6 on 2022-12-09 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_dnevnikstudenta_studentdnevnik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='praksa',
            name='datum_zavrsetka',
            field=models.DateField(blank=True, default=False),
        ),
    ]