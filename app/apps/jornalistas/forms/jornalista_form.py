from django import forms
from apps.jornalistas.models import Jornalista
from django.core.exceptions import ValidationError


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
            'ddi',
            'telefone',
            'cpf',
            'estado_civil',
            'associacoes',
            'registro',
            'show_nome_de_guerra',
            'show_nome',
            'show_sobrenome',
            'show_associacoes',
            'show_cpf',
            'show_data_de_nascimento',
            'show_ddi',
            'show_telefone',
            'show_genero',
            'show_estado_civil',
            'show_registro'
        ]

        labels = {
            'registro': 'MTb',
            'associacoes': 'Associações',
            'ddi': 'DDI',
        }

        help_texts = {
            'registro': '''
            Se tem o registro profissional, insira aqui
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
                    'class': 'form-control',
                    'required': 'True'
                }
            ),
            'ddi': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'telefone': forms.TextInput(
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
            ),
            'show_nome_de_guerra': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
            'show_nome': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
            'show_sobrenome': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
            'show_associacoes': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
            'show_cpf': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
            'show_data_de_nascimento': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
            'show_ddi': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
            'show_telefone': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
            'show_genero': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
            'show_estado_civil': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
            'show_registro': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
        }

    def clean_telefone(self):
        data = self.cleaned_data['telefone']

        if not data.isdigit():
            raise ValidationError(
                "Digite apenas números"
            )

        return data

    def clean_cpf(self):
        data = self.cleaned_data['cpf']

        if not data.isdigit():
            raise ValidationError(
                "Digite apenas números"
            )
        
        return data

    def clean_ddi(self):
        data = self.cleaned_data['ddi']

        if not data.isdigit():
            raise ValidationError(
                "Digite apenas números"
            )

        return data
