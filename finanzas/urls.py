"""finanzas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('capitulos/',include('partidas.urls_capitulos')),
    path('partidas/',include('partidas.urls_partidas')),
    path('presupuestos/',include('presupuestos.urls_presupuestos')),
    path('actividades/',include('presupuestos.urls_actividades')),
    path('gastos/',include('gastos.urls_gastos')),
    path('principal/',include('principal.urls')),
    path('login/',include('usuarios.urls')),
    
]


admin.site.site_header = 'Administración Finanzas'