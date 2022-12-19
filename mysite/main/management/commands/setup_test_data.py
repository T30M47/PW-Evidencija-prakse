import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import *
from main.factory import *

NUM_STUDENTS = 20
NUM_FAKULTETS=20
NUM_STUDENTDNEVNIKS=20
NUM_KOMPANIJAS=20
NUM_MENTORS=20
NUM_PRAKSAS=20


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Student, Fakultet, StudentDnevnik, Kompanija, Mentor, Praksa]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        fakulteti=[]
        prakseList=[]
        for _ in range(NUM_FAKULTETS):
            fakultet = FakultetFactory()
            fakulteti.append(fakultet)
        for _ in range(NUM_STUDENTS):
            student = StudentFactory()
            moguci=[1,2]
            odabir=random.choice(moguci)
            student_fakulteti=random.choices(fakulteti, k=odabir)
            student.student_fakultet.add(*student_fakulteti)
        for _ in range(NUM_KOMPANIJAS):
            kompanija=KompanijaFactory()
        for _ in range(NUM_MENTORS):
            mentor=MentorFactory()
        for _ in range(NUM_PRAKSAS):
            praksa=PraksaFactory()
            prakseList.append(praksa)
        for _ in range(NUM_STUDENTDNEVNIKS):
            studentDnevnik = StudentDnevnikFactory()
            moguci=[1,2,3]
            odabir=random.choice(moguci)
            student_prakse=random.choices(prakseList, k=odabir)
            studentDnevnik.prakse.add(*student_prakse)

