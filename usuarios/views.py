from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout


class Login(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    def get_success_url(self):
        self.request.session['cuantos'] = 0
        self.request.session['total'] = 0.0
        self.request.session['articulos'] = {}

        return super().get_success_url()

def logout(request):
    logout(request)
    return redirect('principal:principal')