from django import forms
from jornalistas.models import Jornalista
from associacoes.models import Associacao


class JornalistaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JornalistaForm, self).__init__(*args, **kwargs)
        self.fields['estado'].widget.attrs = {
            'class': 'form-control estado-select2'
        }
        self.fields['cidade'].widget.attrs = {
            'class': 'form-control cidade-select2'
        }

    class Meta:
        model = Jornalista
        fields = [
            'associacao',
            'nome_de_guerra',
            'nome',
            'sobrenome',
            'cpf',
            'telefone',
            'estado',
            'cidade',
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
            'telefone': forms.TextInput(
                attrs={
                    'class': 'form-control mask-phone-international',
                    'type': 'tel',
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
