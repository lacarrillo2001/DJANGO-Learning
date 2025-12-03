from django.shortcuts import render #render nos ayuda a poder cargar plantillas

def index(request):
    return render(request, 'index.html',{})#renderiza la plantilla index.html

def herencia(request):
    return render(request, 'herencia.html',{})#renderiza la plantilla herencia.html

def ejemplo(request):
    return render(request, 'ejemplo.html',{})#renderiza la plantilla ejemplo.html

def otra(request):
    return render(request, 'otra.html',{})#renderiza la plantilla estaticos.html