from django import forms
from apps.associacoes.models import Associacao


class AssociacaoForm(forms.ModelForm):
    class Meta:
        model = Associacao
        fields = [
            'nome_fantasia',
            'razao_social',
            'cnpj',
            'telefone',
            'email',
            'presidente',
        ]
        labels = {
            'nome_fantasia': 'Nome fantasia',
            'razao_social': 'Razão Social',
            'cnpj': 'CNPJ',
            'telefone': 'telefone',
            'email': 'e-mail',
            'presidente': 'presidente'
        }
        widgets = {
            'nome_fantasia': forms.TextInput(
                attrs={
                    'class': 'form-control2',
                    'placeholder': 'Nome fantasia'
                }
            ),
            'razao_social': forms.TextInput(
                attrs={
                    'class': 'form-control2',
                    'placeholder': 'Razão social'
                }
            ),
            'cnpj': forms.TextInput(
                attrs={
                    'class': 'form-control2 mask-cnpj',
                    'placeholder': 'CNPJ'
                }
            ),
            'ddd_telefone': forms.TextInput(
                attrs={
                    'class': 'form-control2 mask-ddd',
                    'placeholder': 'DDD'
                }
            ),
            'telefone': forms.TextInput(
                attrs={
                    'class': 'form-control2',
                    'placeholder': 'Telefone'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control2',
                    'placeholder': 'E-mail'
                }
            ),
            'presidente': forms.TextInput(
                attrs={
                    'class': 'form-control2',
                    'placeholder': 'Presidente'
                }
            )
        }