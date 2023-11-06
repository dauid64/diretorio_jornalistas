from django import forms
from jornalistas.models import Jornalista


class JornalistaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JornalistaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Jornalista
        fields = [
            'nome_de_guerra',
            'nome',
            'sobrenome',
            'data_de_nascimento',
            'genero',
            'telefone',
            'cpf',
            'estado_civil',
            'associacoes',
            'registro'
        ]

        labels = {
            'registro': 'MTb',
            'associacoes': 'Associações'
        }

        help_texts = {
            'registro': '''
            Insira no campo acima, se obtiver, sua Emissão de Registro Profissional
            '''
        }

        widgets = {
            'associacoes': forms.SelectMultiple(
                attrs={
                    'class': 'select2 form-control'
                }
            ),
            'nome_de_guerra': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Carlos Neto'
                }
            ),
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Carlos David'
                }
            ),
            'sobrenome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Castro de Souza Neto'
                }
            ),
            'cpf': forms.TextInput(
                attrs={
                    'class': 'form-control mask-cpf',
                    'placeholder': '123.456.789-00',
                    'required': 'True'
                }
            ),
            'telefone': forms.HiddenInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'data_de_nascimento': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                },
                format='%Y-%m-%d'
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
                }
            )
        }
