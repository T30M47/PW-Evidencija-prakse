from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from main.models import *

## Create your views here.
def homepage(request):
    return render(request, 'base_generic.html')
    
class StudentList(ListView):
    model=Student

class FakultetList(ListView):
    model=Fakultet

class StudentDnevnikList(ListView):
    model=StudentDnevnik

class KompanijaList(ListView):
    model=Kompanija

class MentorList(ListView):
    model=Mentor

class PraksaList(ListView):
    model=Praksa