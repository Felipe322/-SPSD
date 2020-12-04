from django.urls import path
from  principal.views import principal

app_name = 'principal'

urlpatterns = [
    path('',principal,name='principal'),
]
