from django import forms
from obras.models import Publicao
from obras.models import ObraJornalistica


class PublicacaoForm(forms.ModelForm):
    titulo = forms.CharField(
        max_length=254,
        widget=forms.TextInput(
            attrs={
                "class": "form-control2",
                "placeholder": "Titulo"
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
            "titulo",
            "veiculo_de_comunicacao",
            "link",
            "anexo",
            "data",
            "tipo",
            "descricao",
        ]
        widgets = {
            "veiculo_de_comunicacao": forms.Select(
                attrs={
                    "class": "form-control2",
                }
            ),
            "link": forms.URLInput(
                attrs={
                    "class": "form-control2",
                    "placeholder": "Link"
                }
            ),
            "anexo": forms.FileInput(
                attrs={
                    "class": "form-control2",
                    "placeholder": "Anexo"
                }
            ),
            "data": forms.DateInput(
                attrs={
                    "class": "form-control2",
                    "type": "date"
                },
                format='%d/%m/%Y'
            ),
            "tipo": forms.Select(
                attrs={
                    "class": "form-control2",
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