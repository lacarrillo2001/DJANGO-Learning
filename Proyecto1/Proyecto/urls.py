from django.contrib import admin
from django.urls import path

from . import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/',views.saludo, name='saludo'),#es una ruta estatica no resive variables
    path('despedida/', views.despedida, name='despedida'),
    path('adulto/<int:edadUser>/',views.adulto,name='adulto')#ruta dinamica que resive una varible de tipo entero
]
