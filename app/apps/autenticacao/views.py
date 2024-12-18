import random
import smtplib
from django.conf import settings
from email.mime.text import MIMEText
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from apps.autenticacao.forms import RegisterUserForm, LoginForm, RecuperarSenhaForm
from django.contrib import messages
from django.core.mail import send_mail
from apps.jornalistas.models import Jornalista


class RecuperarSenha(View):
    def get(self, request):
        form = RecuperarSenhaForm()

        return render(
            request,
            'autenticacao/pages/recuperar_senha.html',
            context = {
                'form': form
            }
        );

    def post(self, request):


        form = RecuperarSenhaForm(request.POST)

        email = request.POST['email']

        jornalistas = Jornalista.objects.all()
        users = [jornalista.usuario for jornalista in jornalistas]

        found = False
        username = ''
        target_user =None

        for user in users:
            if user.email == email:
                found = True 
                username = user.username
                target_user = user


        new_password = int(random.random()*10**6)

        if form.is_valid() and found:
            target_user.set_password(str(new_password));
            target_user.save();

            cd = form.cleaned_data
            subject: str = "Nova Senha da APJOR"
            message: str = f"Olá usuário {username}, sua nova senha é {new_password}"
            #sender="diretorio@profissaojornalista.com.br" #"diretorio@profissaojornalista.com.br"
            #list_of_targets = [email]


            #send_mail(subject,message,sender,list_of_targets)

            user = settings.SMTP_USER
            password = settings.SMTP_PASSWORD
            sender = settings.SMTP_SENDER
            recipients = email

            msg = MIMEText(message)

            msg['Subject'] = subject
            msg['From'] = sender
            msg['To'] = recipients

            s = smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT)
            s.set_debuglevel(int(settings.DEBUG))
            s.login(user, password)
            s.sendmail(sender, recipients, msg.as_string())
            s.quit()        

            print("form sended!")

        return render(
            request,
            "autenticacao/pages/recuperar_senha.html",
            context = {
                'form': form,
                'found': found
            }
        );

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
                    reverse('core:home')
                )
            else:
                messages.warning(request, 'Credênciais inválidas')
        else:
            messages.warning(request, 'E-mail ou senha inválido')

        return redirect(
            reverse('autenticacao:login')
        )


@method_decorator(
    login_required(login_url='autenticacao:login', redirect_field_name='next'),
    name="dispatch"
)
class LogoutUserView(View):
    def get(self, request):
        logout(request)
        return redirect(
            reverse(
                "core:home"
            )
        )
