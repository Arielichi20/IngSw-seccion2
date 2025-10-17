from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('admin-drf/')),
    path('admin-drf/', admin.site.urls),

    path('api/usuarios/', include('ModuloUsuarios.urls')),
    path('api/cursos/', include('ModuloCursos.urls')),
    path('api/pagos/', include('ModuloPagos.urls')),
    path('api/archivos/', include('ModuloArchivos.urls')),
    path('api/mantenedores/', include('ModuloMantenedores.urls')),

    # ruta dinámica global
    path('api/core/', include('ApiCore.urls')),
]
