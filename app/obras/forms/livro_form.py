from django import forms
from obras.models import Livro


class LivroForm(forms.ModelForm):
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
                "rows": 5,
                "class": "form-control2 span",
                "placeholder": "Descrição"
            }
        )
    )

    class Meta:
        model = Livro
        fields = [
            "titulo",
            "paginas",
            "ano_publicacao",
            "cidade",
            "estado",
            "isbn13",
            "isbn10",
            "descricao",
        ]
        widgets = {
            "paginas": forms.TextInput(
                attrs={
                    "class": "form-control2",
                    "placeholder": "Páginas"
                }
            ),
            "ano_publicacao": forms.TextInput(
                attrs={
                    "class": "form-control2",
                    "placeholder": "Data"
                }
            ),
            "cidade": forms.TextInput(
                attrs={
                    "class": "form-control2",
                    "placeholder": "Cidade"
                }
            ),
            "estado": forms.TextInput(
                attrs={
                    "class": "form-control2",
                    "placeholder": "Estado"
                }
            ),
            "isbn13": forms.TextInput(
                attrs={
                    "class": "form-control2",
                    "placeholder": "ISBN13"
                }
            ),
            "isbn10": forms.TextInput(
                attrs={
                    "class": "form-control2",
                    "placeholder": "ISBN10"
                }
            ),
        }