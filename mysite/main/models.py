from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Fakultet(models.Model):
    fakultet_OIB=models.CharField(max_length=11, primary_key=True, validators=[MinLengthValidator(11)])
    fakultet_naziv=models.CharField(max_length=100)
    fakultet_email=models.EmailField()
    fakultet_adresa=models.CharField(max_length=50)
    fakultet_grad=models.CharField(max_length=50)

    def __str__(self):
        return '{}, OIB: {}'.format(self.fakultet_naziv, self.fakultet_OIB)


class Student(models.Model):
    student_JMBAG=models.CharField(max_length=10, primary_key=True, validators=[MinLengthValidator(10)])
    student_ime=models.CharField(max_length=50)
    student_prezime=models.CharField(max_length=50)
    student_email=models.EmailField()
    student_fakultet=models.ManyToManyField(Fakultet)

    def __str__(self):
        return '{} {}, JMBAG: {}'.format(self.student_ime, self.student_prezime, self.student_JMBAG)



class Kompanija(models.Model):
    kompanija_OIB=models.CharField(max_length=11, primary_key=True, validators=[MinLengthValidator(11)])
    kompanija_naziv=models.CharField(max_length=50)
    kompanija_email=models.EmailField()
    kompanija_adresa=models.CharField(max_length=50)
    kompanija_grad=models.CharField(max_length=50)
    
    def __str__(self):
        return '{}, OIB: {}'.format(self.kompanija_naziv, self.kompanija_OIB)

class Mentor(models.Model):
     mentor_OIB=models.CharField(max_length=10, primary_key=True, validators=[MinLengthValidator(10)])
     mentor_ime=models.CharField(max_length=50)
     mentor_prezime=models.CharField(max_length=50)
     mentor_email=models.EmailField()
     mentor_radnoMjesto=models.CharField(max_length=30)
     mentor_kompanija=models.ForeignKey(Kompanija, on_delete=models.CASCADE)

     def __str__(self):
        return '{} {}, Radno mjesto: {}, Kompanija: {}'.format(self.mentor_ime, self.mentor_prezime, self.mentor_radnoMjesto, self.mentor_kompanija)

class Praksa(models.Model):
    student_praksa=models.ForeignKey(Student, on_delete=models.CASCADE)
    fakultet_praksa=models.ForeignKey(Fakultet, on_delete=models.CASCADE)
    student_preddiplomski=models.BooleanField(default=True)
    datum_pocetka=models.DateField()
    datum_zavrsetka=models.DateField(blank=True, null=True)
    radno_mjesto=models.CharField(max_length=50)
    napomena=models.TextField(blank=True)
    broj_odradenih_sati=models.IntegerField()
    praksa_kompanija=models.ForeignKey(Kompanija, on_delete=models.CASCADE)
    praksa_mentor=models.ForeignKey(Mentor, on_delete=models.CASCADE)
    

    def __str__(self):
        return 'student: {}, Radno mjesto: {}, kompanija: {}'.format(self.student_praksa, self.radno_mjesto, self.praksa_kompanija)


class StudentDnevnik(models.Model):
    student=models.OneToOneField(Student, on_delete=models.CASCADE)
    prakse=models.ManyToManyField(Praksa)

    def __str__(self):
        return 'Dnevnik od studenta: {}'.format(self.student) 