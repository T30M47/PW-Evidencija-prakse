## factories.py
import factory 
from factory.django import DjangoModelFactory
import factory.fuzzy
from main.models import *
## Defining a factory
class StudentFactory(DjangoModelFactory):
    class Meta:
        model = Student

    student_JMBAG=factory.fuzzy.FuzzyInteger(1000000000, 9999999999)
    student_ime=factory.Faker('first_name')
    student_prezime=factory.Faker('last_name')
    student_email=factory.Faker('free_email')
    @factory.post_generation
    def fakultets(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for fakultet in extracted:
                self.fakultets.add(fakultet)

class FakultetFactory(DjangoModelFactory):
    class Meta:
        model=Fakultet
     
    fakultet_OIB=factory.fuzzy.FuzzyInteger(10000000000, 99999999999)
    fakultet_naziv=factory.Faker('company')
    fakultet_email=factory.Faker('free_email')
    fakultet_adresa=factory.Faker('address')
    fakultet_grad=factory.Faker('city')


class StudentDnevnikFactory(DjangoModelFactory):
    class Meta:
        model=StudentDnevnik

    student=factory.Iterator(Student.objects.all())
    @factory.post_generation
    def prakse(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for praksa in extracted:
                self.prakse.add(praksa)
    ukupni_broj_sati_rada=factory.fuzzy.FuzzyInteger(0, 999)
                
    


class KompanijaFactory(DjangoModelFactory):
    class Meta:
        model=Kompanija
    
    kompanija_OIB=factory.fuzzy.FuzzyInteger(10000000000, 99999999999)
    kompanija_naziv=factory.Faker('company')
    kompanija_email=factory.Faker('free_email')
    kompanija_adresa=factory.Faker('address')
    kompanija_grad=factory.Faker('city')

class MentorFactory(DjangoModelFactory):
    class Meta:
        model=Mentor
    
    mentor_OIB=factory.fuzzy.FuzzyInteger(10000000000, 99999999999)
    mentor_ime=factory.Faker('first_name')
    mentor_prezime=factory.Faker('last_name')
    mentor_email=factory.Faker('free_email')
    mentor_radnoMjesto=factory.Faker('job')
    mentor_kompanija=factory.Iterator(Kompanija.objects.all())


class PraksaFactory(DjangoModelFactory):
    class Meta:
        model=Praksa
    
    student_praksa=factory.Iterator(Student.objects.all())
    fakultet_praksa=factory.Iterator(Fakultet.objects.all())
    student_preddiplomski=factory.fuzzy.FuzzyChoice(choices=[True, False])
    datum_pocetka=factory.Faker('date_time')
    datum_zavrsetka=factory.Faker('date_time')
    radno_mjesto=factory.Faker('job')
    napomena=factory.Faker("sentence", nb_words=10)
    broj_odradenih_sati=factory.fuzzy.FuzzyInteger(0, 999)
    praksa_kompanija=factory.Iterator(Kompanija.objects.all())
    praksa_mentor=factory.Iterator(Mentor.objects.all())
    
