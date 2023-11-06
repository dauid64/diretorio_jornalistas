from django import forms
from jornalistas.models import Diploma


class DiplomaForm(forms.ModelForm):
    class Meta:
        model = Diploma
        fields = ['arquivo', 'descricao']
        labels = {
            'arquivo': 'Diploma',
            'descricao': 'Descrição'
        }
        widgets = {
            'arquivo': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'descricao': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
