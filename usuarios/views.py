from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, redirect
from presupuestos.models import Presupuesto

class Login(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        self.request.session['anio'] = None
        return super().get_success_url()

def logout_view(request):
    logout(request)
    return redirect('usuarios:login')

