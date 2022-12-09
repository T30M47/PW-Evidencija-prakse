from django.urls import path
from . import views
from main.views import *

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('studenti', StudentList.as_view()),
    path('fakulteti', FakultetList.as_view()),
    path('dnevnici', StudentDnevnikList.as_view()),
    path('kompanije', KompanijaList.as_view()),
    path('mentori', MentorList.as_view()),
    path('prakse', PraksaList.as_view()),
]
