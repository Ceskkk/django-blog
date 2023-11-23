from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic.edit import FormView
from .models import User
from .forms import (
    UserRegisterForm,
    LoginForm,
    UpdatePasswordForm,
)


class UserRegisterView(FormView):
    # TODO: No funciona el register pero cuando ponemos {{form.password}} en vez de {{form.password1}} si que va
    template_name = 'pages/user/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users_app:login')

    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            name=form.cleaned_data['name'],
            job=form.cleaned_data['job'],
            gender=form.cleaned_data['gender'],
            birthdate=form.cleaned_data['birthdate'],
        )
        return super(UserRegisterView, self).form_valid(form)


class LoginUser(FormView):
    template_name = 'pages/user/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:home-user')

    def form_valid(self, form):
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class LogoutView(View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )


class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = 'pages/user/update.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users_app:user-login')
    login_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            email=usuario.email,
            password=form.cleaned_data['password1']
        )

        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()

        logout(self.request)
        return super(UpdatePasswordView, self).form_valid(form)
