from django.http import HttpResponse 

def saludo(request):
    return HttpResponse("Hola, bienvenido a mi sitio web!")


def despedida(request):
    return HttpResponse("¡Adiós, gracias por visitar de mi sitio web!")

def adulto(request, edadUser):
    if edadUser >= 18:
        return HttpResponse("Eres mayor de edad.")
    else:
        return HttpResponse("Eres menor de edad.")