from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


class Login(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        self.request.session['cuantos'] = 0
        self.request.session['total'] = 0.0
        self.request.session['articulos'] = {}
        return super().get_success_url()
