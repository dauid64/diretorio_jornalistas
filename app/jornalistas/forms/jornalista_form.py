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
                    'class': 'form-control'
                }
            ),
            'nome_de_guerra': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nome de Guerra'
                }
            ),
            'cpf': forms.TextInput(
                attrs={
                    'class': 'form-control mask-cpf',
                    'placeholder': 'CPF',
                    'required': 'True'
                }
            ),
            'telefone': forms.TextInput(
                attrs={
                    'class': 'form-control mask-phone',
                    'placeholder': 'Telefone'
                }
            ),
            'data_de_nascimento': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                },
                format='%d/%m/%Y'
            ),
            'genero': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado_civil': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'registro': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Registro'
                }
            ),
            'diploma': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
