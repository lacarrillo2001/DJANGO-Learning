from django.shortcuts import render  # se utiliza para la función render que permite renderizar el contenido


def simple(request):
    return render(request, 'simple.html', {})

def dinamico(request, name):
    categories = ['Tech', 'Health', 'Sports', 'Education', 'Entertainment']
    context = {'name': name, 'categories': categories }
    return render(request,'dinamico.html',context)