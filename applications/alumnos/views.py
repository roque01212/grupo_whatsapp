from django.shortcuts import render
from django.views.generic import Listview
from .models import Alumno
# Create your views here.



class AlumnoListView(ListView):
    model = Alumno
    template_name = "alumno/lista.html"

