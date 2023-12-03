from django import forms
from apps.opcoes.models import RedesSociais


class RedesSociaisForm(forms.ModelForm):
    class Meta:
        model = RedesSociais
        fields = '__all__'

        widgets = {
            'tipo_de_rede_social': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'link': forms.URLInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }