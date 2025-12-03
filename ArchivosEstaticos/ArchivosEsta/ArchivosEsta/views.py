from django.shortcuts import render #render nos ayuda a poder cargar plantillas


def estaticos(request):
    return render(request, 'estaticos.html',)#renderiza la plantilla estaticos.html