from django.contrib import admin
from main.models import *
# Register your models here.
modeli=[Student, Kompanija, Praksa, Fakultet, Mentor, StudentDnevnik]
admin.site.register(modeli)