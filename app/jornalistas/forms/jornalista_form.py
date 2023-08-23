from django import forms
from jornalistas.models import Jornalista


class JornalistaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JornalistaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Jornalista
        fields = [
            'associacao',
            'nome_de_guerra',
            'cpf',
            'telefone',
            'data_de_nascimento',
            'genero',
            'estado_civil',
            'registro',
            'diploma',
        ]

        widgets = {
            'associacao': forms.Select(
                attrs={
                    'class': 'form-control2'
                }
            ),
            'nome_de_guerra': forms.TextInput(
                attrs={
                    'class': 'form-control2',
                    'placeholder': 'Nome de Gerra'
                }
            ),
            'cpf': forms.TextInput(
                attrs={
                    'class': 'form-control2',
                    'placeholder': 'CPF',
                    'required': 'True'
                }
            ),
            'telefone': forms.TextInput(
                attrs={
                    'class': 'form-control2',
                    'placeholder': 'Telefone'
                }
            ),
            'data_de_nascimento': forms.DateInput(
                attrs={
                    'class': 'form-control2',
                    'placeholder': 'Data de nascimento'
                }
            ),
            'genero': forms.Select(
                attrs={
                    'class': 'form-control2'
                }
            ),
            'estado_civil': forms.Select(
                attrs={
                    'class': 'form-control2',
                }
            ),
            'registro': forms.TextInput(
                attrs={
                    'class': 'form-control2',
                    'placeholder': 'Registro'
                }
            ),
            'diploma': forms.FileInput(
                attrs={
                    'class': 'form-control2'
                }
            ),
        }