from django import forms
from obras.models import Livro
from obras.models import ObraJornalistica


class LivroForm(forms.ModelForm):
    titulo = forms.CharField(
        max_length=254,
        widget=forms.TextInput(
            attrs={
                "class": "form-control2",
                "placeholder": "Título"
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
            "cidade": forms.Select(
                attrs={
                    "class": "form-control2"
                }
            ),
            "estado": forms.Select(
                attrs={
                    "class": "form-control2"
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
    
    def save(self, commit=True):
        instance = super().save(commit)
        if commit:
            instance.save()
        obra_jornalistica = ObraJornalistica.objects.create(
            titulo=self.cleaned_data['titulo'],
            descricao=self.cleaned_data['descricao']
        )
        instance.obra_jornalistica = obra_jornalistica
        return instance
