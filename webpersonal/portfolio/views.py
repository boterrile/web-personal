from django.shortcuts import render

#importamos modelos porque vamos a ir a la BBDD a buscar los proyectos que teniamos creados
from .models import Project

# Create your views here.

def portfolio(request):
    services = Service.objects.all() # Nos devuevle todos objetos del modelo que tiene Services a la lista services 


     #creamos un nuevo directorio en portfolio => templates/portfolio y nos lo traemos de core/templates/core/portfolio.html
    return render(request,"portfolio/portfolio.html", {'projects': projects})