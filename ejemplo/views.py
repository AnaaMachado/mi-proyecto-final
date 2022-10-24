from django.shortcuts import render
from ejemplo.models import Familiar

def index(request):
    return render(request, "ejemplo/saludar.html",
    {
        "nombre":"German"
    })

def mostrar_familiares(request):
    lista_familiares=Familiar.objects.all()
    return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})
# Create your views here.
