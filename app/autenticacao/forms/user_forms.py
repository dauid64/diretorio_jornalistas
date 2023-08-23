from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
        labels = {
            'username': 'Usuário',
            'email': 'Email',
            'password': 'Senha'
        }

        widgets = {
            'username': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Usuário"
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email"
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Senha"
                }
            )
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        exist_username = User.objects.exists(username=username)
        if exist_username:
            raise ValidationError(
                'Já existe um usuário com este username!'
            )
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        exist_email = User.objects.exists(email=email)
        if exist_email:
            raise ValidationError(
                'Já existe um usuário com este email!'
            )
        return email
    

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'caixa-login',
                'class': 'form-control',
                'placeholder': 'Usuário'
            }
        )
    )
    password = forms.CharField(
        max_length=32,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Senha'
            }
        ),
        required=True
    )