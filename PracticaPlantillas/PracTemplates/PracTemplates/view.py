from django.shortcuts import render #render nos ayuda a poder cargar plantillas

def index(request):
    return render(request, 'index.html',{})#renderiza la plantilla index.html

def porfolio(request):
    return render(request, 'porfolio.html',{})#renderiza la plantilla index.html

