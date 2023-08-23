from django import forms
from obras.models import Publicao


class PublicacaoForm(forms.ModelForm):
    titulo = forms.CharField(
        max_length=254,
        widget=forms.TextInput(
            attrs={
                "class": "form-control2",
                "placeholder": "Descrição"
            }
        )
    )
    descricao = forms.CharField(
        max_length=254,
        widget=forms.Textarea(
            attrs={
                "rows": 8,
                "class": "form-control2 span",
                "placeholder": "Descrição"
            }
        )
    )

    class Meta:
        model = Publicao
        fields = [
            "veiculo_de_comunicacao",
            "titulo",
            "link",
            "anexo",
            "data",
            "descricao"
        ]
        widgets = {
            "veiculo_de_comunicacao": forms.TextInput(
                attrs={
                    "class": "form-control2",
                    "placeholder": "Veiculo Jornalístico"
                }
            ),
            "link": forms.TextInput(
                attrs={
                    "class": "form-control2",
                    "placeholder": "Link"
                }
            ),
            "anexo": forms.TextInput(
                attrs={
                    "class": "form-control2",
                    "placeholder": "Anexo"
                }
            ),
            "data": forms.TextInput(
                attrs={
                    "class": "form-control2",
                    "placeholder": "Data"
                }
            ),
        }
