from django.urls import path
from usuarios.views import Login, logout_view

app_name = 'usuarios'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/',logout_view,name='logout'),
]
