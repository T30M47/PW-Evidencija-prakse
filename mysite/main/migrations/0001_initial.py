# Generated by Django 4.0.6 on 2022-12-09 13:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fakultet',
            fields=[
                ('fakultet_OIB', models.CharField(max_length=11, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(11)])),
                ('fakultet_naziv', models.CharField(max_length=100)),
                ('fakultet_email', models.EmailField(max_length=254)),
                ('fakultet_adresa', models.CharField(max_length=50)),
                ('fakultet_grad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Kompanija',
            fields=[
                ('kompanija_OIB', models.CharField(max_length=11, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(11)])),
                ('kompanija_naziv', models.CharField(max_length=50)),
                ('kompanija_email', models.EmailField(max_length=254)),
                ('kompanija_adresa', models.CharField(max_length=50)),
                ('kompanija_grad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('mentor_OIB', models.CharField(max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(10)])),
                ('mentor_ime', models.CharField(max_length=50)),
                ('mentor_prezime', models.CharField(max_length=50)),
                ('mentor_email', models.EmailField(max_length=254)),
                ('mentor_radnoMjesto', models.CharField(max_length=30)),
                ('mentor_kompanija', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.kompanija')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_JMBAG', models.CharField(max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(10)])),
                ('student_ime', models.CharField(max_length=50)),
                ('student_prezime', models.CharField(max_length=50)),
                ('student_email', models.EmailField(max_length=254)),
                ('student_fakultet', models.ManyToManyField(to='main.fakultet')),
            ],
        ),
        migrations.CreateModel(
            name='Praksa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_preddiplomski', models.BooleanField(default=True)),
                ('datum_pocetka', models.DateField()),
                ('datum_zavrsetka', models.DateField(blank=True)),
                ('radno_mjesto', models.CharField(max_length=50)),
                ('napomena', models.TextField(blank=True)),
                ('fakultet_praksa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.fakultet')),
                ('praksa_kompanija', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.kompanija')),
                ('praksa_mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.mentor')),
                ('student_praksa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
        ),
        migrations.CreateModel(
            name='DnevnikStudenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ukupni_sati_rada', models.CharField(max_length=30)),
                ('broj_radnih_mjesta', models.IntegerField()),
                ('broj_kompanija', models.IntegerField()),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
        ),
    ]