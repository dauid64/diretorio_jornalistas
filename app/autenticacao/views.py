from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import RegisterUserForm, LoginForm
from django.contrib import messages


class RegisterUserView(View):
    def get(self, request):
        register_form_data = request.session.get('register_form_data', None)
        register_form = RegisterUserForm(register_form_data)

        return render(
            request,
            'autenticacao/pages/registrar.html',
            context={
                'form': register_form
            }
        )

    def post(self, request):
        POST = request.POST
        request.session['register_form_data'] = POST
        register_form = RegisterUserForm(POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            del (request.session['register_form_data'])
            return redirect(
                reverse('jornalistas:cadastrar')
            )

        return redirect(
            reverse('autenticacao:registrar')
        )


class LoginUserView(View):
    def get(self, request):
        form = LoginForm()
        return render(
            request,
            'autenticacao/pages/login.html',
            context={
                'form': form
            }
        )
    
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            authenticated_user = authenticate(
                username=login_form.cleaned_data.get('username', ''),
                password=login_form.cleaned_data.get('password', '')
            )

            if authenticated_user is not None:
                login(request, authenticated_user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect(
                    reverse('jornalistas:home')
                )
            else:
                messages.warning(request, 'Credênciais inválidas')
        else:
            messages.warning(request, 'E-mail ou senha inválido')

        return redirect(
            reverse('autenticacao:login')
        )


class LogoutUserView(View):
    def get(self, request):
        logout(request)
        return redirect(
            reverse(
                "jornalistas:home"
            )
        )