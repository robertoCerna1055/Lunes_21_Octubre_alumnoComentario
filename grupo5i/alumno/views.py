from django.shortcuts import render,get_object_or_404
from .models import Alumno

# Create your views here.

def  index_vista(request):
    MisAlumnos = Alumno.objects.all().order_by("id")
    return render(request, 'index.html',{"MisAlumnos":MisAlumnos})

def Alumno_vista(request,id):
    alumno = get_object_or_404(Alumno,id=id)
    return render(request, 'alumno.html',{'objeto':alumno})