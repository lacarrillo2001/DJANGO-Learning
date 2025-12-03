
from django.contrib import admin
from django.urls import path
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('herencia/', view.herencia,name='herencia'),
    path('ejemplo/', view.ejemplo,name='ejemplo'),
    path('otra/', view.otra,name='otra'),
    path('', view.index,name='index'),
]
