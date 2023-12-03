from django import forms
from apps.historico_profissional.models import Referencia


class ReferenciaForm(forms.ModelForm):
    class Meta:
        model = Referencia
        fields = ['nome', 'contato']

        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nome da refêrencia'
                }
            ),
            'contato': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Forma de localizar a refêrencia'
                }
            )
        }
