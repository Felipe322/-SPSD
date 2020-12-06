from django.urls import path
from usuarios.views import Login

app_name = 'usuarios'

urlpatterns = [
    path('', Login.as_view(), name='login'),
]
